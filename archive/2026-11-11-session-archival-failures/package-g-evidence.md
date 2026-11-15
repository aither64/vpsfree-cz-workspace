# G: runtime mechanical refresh review supplement

The conflict-free refresh is committed at
`43085d5d5ac1bfc8dbca48a809c2162acf8e0e74`. All required quick checks passed.
This supplement preserves the original
[review packet](review-packet.md), [R](final-review.md),
[R2](final-review-r2.md) and [old-head CI evidence](verification.md).
Lead owns refreshed independent review, publication and subsequent verification.
No push, long integration, claim, merge, deployment or lifecycle action occurred.

## Scope and revisions

The accepted A6 section of [design.md](design.md) authorizes only refreshing the
original archive/monitor feature onto the current runtime default. No new
behavior or consumer/input change was authored. The original user request,
contracts, trust boundary, non-goals and documentation inventory remain in the
preserved review packet. Any conflict or manual behavior change would have
stopped the package; none occurred.

- Repository: `git@github.com:aither64/dev-workspace.git`; target `master`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-11-session-archival-failures/dev-workspace`.
- Feature: `2026-11-11-session-archival-failures`.
- Reviewed old base: `6587c4c1cedabee95bcc52f4667e7d33e3a82859`.
- Reviewed old head: `79700e46361543dbc399647a218671d7ad4b55e1`.
- Retained old ref: `refs/heads/2026-11-11-session-archival-failures-reviewed-original`.
- New base: `02881b401955ff0db71bb74f6fb84f6e475a7879`, fetched from origin.
- New head: `43085d5d5ac1bfc8dbca48a809c2162acf8e0e74`.

Complete refreshed series, oldest first:

1. `e92f76e65166dad7ac6d43ee0e031cc22b6f35b5` — monitor: reject contradictory new terminal reports.
2. `43085d5d5ac1bfc8dbca48a809c2162acf8e0e74` — session: wait through archive preparation contention.

Final diff command:

```sh
git diff 02881b401955ff0db71bb74f6fb84f6e475a7879..43085d5d5ac1bfc8dbca48a809c2162acf8e0e74
```

It contains the same 13 feature files, +565/-7. The only upstream commit is
`02881b401955ff0db71bb74f6fb84f6e475a7879`, repository comparison metadata
loading. The only shared changed file is `portal/internal/web/static/app.js`;
upstream's repository-review asset URL and the feature's archive presentation
hunks are disjoint. Both changes are retained.

## Complete equivalence evidence

The full command
`git range-diff --no-color 6587c4c1..79700e46 02881b40..43085d5d`
returned only:

```text
1:  3a0af7ad = 1:  e92f76e6 monitor: reject contradictory new terminal reports
2:  79700e46 = 2:  43085d5d session: wait through archive preparation contention
```

Ordered `git patch-id --stable` values:

| Position | Old commit | Refreshed commit | Identical stable patch ID |
| --- | --- | --- | --- |
| 1 | `3a0af7ad6b97ae4a3a7e38921beac8a2cdf9ff54` | `e92f76e65166dad7ac6d43ee0e031cc22b6f35b5` | `ca137f4ee89d4a2ffab49fbd4d44e438e4bfbb99` |
| 2 | `79700e46361543dbc399647a218671d7ad4b55e1` | `43085d5d5ac1bfc8dbca48a809c2162acf8e0e74` | `d1f26b74fb05f532a141ca361d261225f15c9bf5` |

The old-base → new-base diff and old-head → new-head diff also have the same
stable patch ID, `4f705bf6c916230cbd2174ae4793ac9160e3a276`, and identical
changed-path inventories. Thus the refresh retains exactly the upstream delta
alongside the equivalent feature series; no manual patch was introduced.

The following blobs are byte-identical between old and refreshed feature heads.
SHA-256 values name the checked current bytes:

| Input or contract | SHA-256 |
| --- | --- |
| `flake.nix` | `130f7f72f984ec259f4d357a8b7910d0085fef31308852ee9e8d64459bbd0e0d` |
| `flake.lock` | `f5e37857e42a2f975fc4e8da8d64e525c127d38b442ecc60823d36fc5d418079` |
| `portal/go.mod` | `05b6de24e48c05c4139e578286b6a89f9e24e383de69a47add153ddc39edcced` |
| `portal/go.sum` | `9e714fdbd4171c613f91698fb2235b4fbf2b17b4098d6c293925d19f41f9a9a3` |
| `.github/workflows/check.yml` | `a361135ed8d481c9e8edca546d8ded6fab14bb15cad8e5d445cc2ba8036d3018` |
| `nix/workspace-portal.nix` | `27e374b01ffaea01101f281d2f5f5d940d2d2e908599bdec13b5e118039e0585` |
| `nix/tests/session-archive-lifecycle.nix` | `98f63b3909f5212a76518d1fd59d3412a71b0a74aa87c8cd6cb3bcde31614800` |
| `libexec/dev-session` | `6fc68ca90f8916f55ecb0e6d3affb30f4d29d092638050e0ec3fc74755bcf3b5` |
| `portal/internal/monitoroperation/types.go` | `a4f107b0e2d37fd8e65358c7e5abdc1aaefb01cb39a61989edcccaaf9c460041` |
| `portal/internal/monitoroperation/store.go` | `96e07f15d303453367da797b083ea6e556e7cd000e72fcd01b99dff732f7c0e9` |
| `portal/internal/monitoroperation/lifecycle.go` | `4c21a53d358b99c0dfa0084673e2dddd13d6f3fb8decd7dc1d4d13fee2c3509f` |
| `test/archive_lifecycle_browser.cjs` | `7c15b58d85fd6f0a0255b6d75665173b82c74dc609f72df1603160573164c22a` |

The 60-second prearmed real hydration-response assertion is unchanged. No
persisted schema, recovery contract, module/dependency input, workflow selection
or application authority rule changed in this refresh. This is equivalence and
focused-check evidence, not a complete deployed input-graph receipt.

## Quick verification

Lead released the known-quick exception for the retained focused invocations;
no watcher substitution or long test was used.

- `nix develop --command go -C portal test -mod=readonly -count=1
  ./internal/monitoroperation`: passed, package 5.396 seconds, source tool
  session `31851` joined with exit 0.
- `nix develop --command bash -c 'set -e; node --check
  portal/internal/web/static/app.js; node --check
  portal/internal/web/browser_contract_test.cjs; node --check
  test/archive_lifecycle_browser.cjs'`: passed; tool session `68075` joined
  with exit 0.
- `nix develop --command go -C portal test -mod=readonly ./internal/web
  -run 'TestArchivePreparation|TestLifecycleOperationErrorsAreBoundedAndHideCommandInvocation|TestLifecycleSnapshotGETDoesNotWaitForGenerationOrReceiptMutex'
  -count=1`: passed, 39.399 seconds elapsed, package 18.351 seconds; log
  `/tmp/2026-11-11-session-archival-failures-G-archive.log`.
- `nix develop --command bash -c 'cd portal/internal/web;
  node browser_contract_test.cjs --unit http://127.0.0.1
  /home/aither/go/pkg/mod/github.com/aither64/codex-web@v0.0.0-20261108185431-dd90fb4308ba/conversation/assets/conversation.js'`:
  passed, 1.011 seconds elapsed, including 29 preparation cases and composer
  retry contracts; log
  `/tmp/2026-11-11-session-archival-failures-G-browser.log`.
  This and the archive selector ran as one known-quick related batch in tool
  session `91093`, joined with exit 0, below the released 60-second expectation.
- Base-to-head `git diff --check` passed; worktree and index are clean.

The parallel Nix evaluation emitted an ignored busy eval-cache diagnostic; both
completed quick commands returned success. No environment modification or retry
was needed. The repository still declares no hook framework or configured
hook path; the rebase used ordinary Git behavior, with no hook bypass.

## History, migrations, documentation and next dependency

The final range contains exactly the two original logical features in order.
No superseded feature/fixup approach, repeated pin stream or transitional path
was introduced. No migrations, including persisted-format migrations; no
migration merge/release/deployment/external-consumption lineage exists to alter.
Original reviewed refs/reports and old-head CI provenance remain preserved.
No claim is made that the nonancestor old head was literally merged.

Product documentation, monitor instructions and archive recovery guidance are
unchanged feature patches, retaining the routing and fidelity conclusions in R
and R2. Upstream documentation changes describe its comparison metadata feature.
No new prose or documentation move was authored. This supplement records the
individual refresh and its evidence in session tracking, outside product docs.

G's runtime index/rebase/commit window is released. All three source handles
listed above are joined; no G command or tool session remains running.

Next: lead accepts the quick/equivalence evidence and selects the independent
final review plan, including whole-branch history/no-migrations conclusions.
Publication remains held until that release. F must wait for the reviewed and
published exact runtime head before pin generation. Fresh fast/archive/creation
CI is still required; old-head CI is not a new-head result. No optional test or
refactor is proposed.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-session-archival-failures/).

## G2 refresh onto the settled counts baseline

This section records G2 separately from the accepted G record above. A8 of
[design.md](design.md#a8-sufficient-g2f2-implementation-brief) and the current
A8 section of [rollout.md](rollout.md) are its sufficient accepted brief.
Fresh SSH fetch confirmed the exact settled runtime default before mutation.
Identity and the saved same-session implementer1 roster settings were verified;
both session environment variables were absent and the trusted binding matched.

G2 rebased the same two commits without conflict or manual source changes:

- Old base: `02881b401955ff0db71bb74f6fb84f6e475a7879`.
- Old reviewed head: `43085d5d5ac1bfc8dbca48a809c2162acf8e0e74`.
- New base: `db4b0fa62633b925e1917ec880737e1776f82cc8`.
- New head: `e1c67dbee3188df9dc7c37fa1d1e724515530fea`.
- Retained G ref:
  `refs/heads/2026-11-11-session-archival-failures-reviewed-g-43085d5d`.
- Original retained ref remains
  `refs/heads/2026-11-11-session-archival-failures-reviewed-original` at
  `79700e46361543dbc399647a218671d7ad4b55e1`.

Complete G2 series, oldest first:

1. `f124fd4e4fa34b20aef5063247a3ae8cb57a6d48` — monitor: reject contradictory new terminal reports.
2. `e1c67dbee3188df9dc7c37fa1d1e724515530fea` — session: wait through archive preparation contention.

The exact old/new range comparison is:

```sh
git range-diff --no-color 02881b401955ff0db71bb74f6fb84f6e475a7879..43085d5d5ac1bfc8dbca48a809c2162acf8e0e74 db4b0fa62633b925e1917ec880737e1776f82cc8..e1c67dbee3188df9dc7c37fa1d1e724515530fea
```

Its complete output is:

```text
1:  e92f76e6 = 1:  f124fd4e monitor: reject contradictory new terminal reports
2:  43085d5d = 2:  e1c67dbe session: wait through archive preparation contention
```

Ordered stable patch IDs remain
`ca137f4ee89d4a2ffab49fbd4d44e438e4bfbb99` and
`d1f26b74fb05f532a141ca361d261225f15c9bf5`, respectively, matching G and the
original two-commit feature. The final feature diff is
`git diff db4b0fa62633b925e1917ec880737e1776f82cc8..e1c67dbee3188df9dc7c37fa1d1e724515530fea`.

### G2 independent tree, delta and input proof

Two fresh temporary Git indexes independently reconstructed the complete tree:

1. Read new base `db4b0fa6`, apply the original G commits' binary patches in
   order with `git apply --cached`, then `git write-tree`.
2. Read old G head `43085d5d`, apply the complete upstream binary delta
   `02881b4..db4b0fa6`, then `git write-tree`.

Both returned `f77d3ee6b0d0726f72d70c1a52881fe90c0ee53f`, exactly the new
HEAD tree. These checks used separate temporary index paths, without changing
the real index or worktree. They independently verify the rebase's complete
tree, rather than relying only on commit labels or patch IDs. Independent final
review remains lead-owned.

Upstream `02881b4..db4b0fa6` and refresh `43085d5d..e1c67dbe` deltas both have
stable patch ID `8f8c4abb5c98138c7b738f37d27bd66cc79ff1df` and the exact same
16 changed paths. Twelve of the thirteen feature files are byte-identical to
G; only `static/app.js` also carries the upstream repository asset version
change. The automatic counts behavior and `--full-index` immutable-blob diff
remain in the composed result. No upstream behavior was removed.

All twelve input/contract hashes in the G table above were checked again
against old G and new G2 heads and are identical, including the full runtime
lock, Go modules, workflow, package definition, archive VM, CLI, monitor
types/store/lifecycle and archive browser harness. The reviewed prearmed real
60-second hydration gate is byte-identical. Raw structured proofs are retained
at `/tmp/2026-11-11-session-archival-failures-G2-proofs.json`; the exact identities
and conclusions are preserved here independently of that disposable artifact.

No migrations, new schema, changed recovery/authority contract or dependency
input was authored. Final history remains two ordered logical features with no
obsolete fixup/history stream or repeated pin update. Original and G reviews,
old-head CI and old candidate build/copy receipts remain unchanged evidence for
their exact revisions. Nonancestor old heads are not claimed literally merged.

### G2 verification and review boundary

One fresh native Luna/low utility was launched for the related focused batch at
exact G2 head. Its current selected package was independently confirmed by ordinary
`workspace-host status` as
`/nix/store/s0g8bym5k588czihviybr5822xr4xr0x-dev-workspace-0.2.0`.
That package's schema-6 catalog digest is
`f2d5a8909570f32bf65098940649922528d081974eefdb3bf678fb38e4ad568d`; utility
`dw_e792014d07f1ab00a4e052aeb6fbc575674f9dbc9073f569` selects
`gpt-6-luna`/`low`, package execution `full_access`, native
`danger-full-access` and approval `never`. The trusted native executor policy
agrees. The utility is outside the retained team roster and was launched with
fresh context; no other operation or watcher was reused.

The first utility turn attempted an unavailable policy-introspection command
and did not launch any check. One same-operation clarification identified the
trusted developer/executor permissions and installed TOML as authoritative;
there is no extra introspection requirement. That utility then ran the batch
from the session records directory instead of its assigned worktree. It exited
1 after 75 seconds at `go: chdir portal: no such file or directory`, before any
test ran. Its source shell `11187` and every owned tool/cell were joined;
failure log `/tmp/2026-11-11-session-archival-failures-G2-focused.log` is retained.
No source defect or failed test result is inferred from this setup failure.

The authorized visible parent fallback runs the original exact batch from an
explicit canonical worktree, with HEAD/clean-state/portal-path assertions before
launch and HEAD/clean-state assertions afterward. No duplicate command or
utility was launched. Parent source handle: `29106`; final log:
`/tmp/2026-11-11-session-archival-failures-G2-focused-final.log`.

The batch passed with exit 0, 65.387 seconds total. Go packages passed:
monitoroperation 5.644 seconds, archive/lifecycle selector 18.676 seconds, full
repository counts/blob-diff suite 15.563 seconds. App/browser/harness syntax
checks passed, as did 29 preparation browser cases and composer retry contracts.
Exact script supplied to `nix develop --command bash -c`, from the canonical
runtime worktree:

```sh
set -e
go -C portal test -mod=readonly -count=1 ./internal/monitoroperation
go -C portal test -mod=readonly -count=1 ./internal/web -run 'TestArchivePreparation|TestLifecycleOperationErrorsAreBoundedAndHideCommandInvocation|TestLifecycleSnapshotGETDoesNotWaitForGenerationOrReceiptMutex'
go -C portal test -mod=readonly -count=1 ./internal/repository
node --check portal/internal/web/static/app.js
node --check portal/internal/web/browser_contract_test.cjs
node --check test/archive_lifecycle_browser.cjs
cd portal/internal/web
node browser_contract_test.cjs --unit http://127.0.0.1 /home/aither/go/pkg/mod/github.com/aither64/codex-web@v0.0.0-20261108185431-dd90fb4308ba/conversation/assets/conversation.js
```

Parent source handle `29106` joined with exit 0. Before/after assertions prove
exact HEAD and a clean worktree/index. Base-to-head diff check also passed;
the feature remains 13 files, +565/-7. No full `./...`, package/VM build,
deployment or lifecycle check was run. Both the failed utility source and the
successful parent source are complete, with no G2-owned cell/session remaining.
The exclusive runtime source/index/rebase/commit window is released. G2 is
ready for lead acceptance and its applicable independent final review.

G2's feature documentation and all recovery/monitor contracts retain the
existing G/R/R2/R3 routing and fidelity inventory. The upstream count behavior
is a substantive baseline change relative to R3's base, so this is not an
automatic review-reuse claim. Lead will invoke the applicable independent
affected-lane composition/history review after passing quick checks, retaining
unaffected feature-review evidence. Old exact-head CI is not final G2 CI;
verification reuse still needs exact derivation and input proof.

F2's generated pins wait for the lead's accepted/published G2 head. No push,
merge, claim, long integration, build/copy, deployment, live archive retry,
monitor resolution or session/service lifecycle action was performed by G2.
Session remains open.

### G2 follow-up: creation CI failure diagnosis

Exact-head run `43280290315`, attempt 1, finished with fast and archive passing,
creation failing and host skipped. Creation job `131399463289` failed at
`switch_done`, generated test-script line 453, corresponding to
`nix/tests/session-creation.nix:631`. The failure is the maintenance
`deadline-stop` scenario's caller service result, not a naming fixture failure.
No rerun or source edit was performed during diagnosis.

Retained full log: `/tmp/session-archival-ci-43280290315/creation.log`.
Its JSON-encoded maintenance journal was decoded read-only into
`/tmp/session-archival-ci-43280290315/maintenance-journal.txt` for inspection.
The failed VM derivation is
`/nix/store/kjkr9580ma1wb4srg8gxq2b18yhl32nq-vm-test-run-dev-workspace-session-creation.drv`.

Proven sequence:

- The fixture launched `creation-maintenance-deadline-stop.service`, caller
  PID 44607, through the selected profile's `workspace-host switch --source
  /nix/store/n38crv46k6qj3m5g8xwd34jgaxymgj7i-dev-workspace-0.2.0
  --enable-maintenance --pause-timeout 30`.
- Operation `8403a093-2544-466a-aa72-a3834d3f651a` used the matching worker
  `workspace-maintenance@8403a093-2544-466a-aa72-a3834d3f651a.service`, PID 45178.
- The worker completed activation/restoration and returned at 19:00:57 UTC.
  The caller logged `requires maintenance recover; journal retained` in that
  same second and exited 1.
- `switch_done` subsequently observed phase `complete`, native/portal active,
  sources stopped, activation intent, continuations settled and restoration
  completed. It checked the worker's settled successful result first, then
  checked the caller. Log lines 10125–10139 show that order. The final caller
  assertion failed with `Result=exit-code`, `ExecMainStatus=1`, invocation
  `7a1c0f1e690340fd8111f96380772e25`.
- The relevant maintenance Ruby source, creation VM, browser and external model
  are unchanged between passing `43085d5d` and failed `e1c67dbe`.

The concrete runtime flaw is in `start_maintenance_switch`: it inspects the
operation, checks complete/cancelled, then queries the worker's systemd state.
The worker can persist completion and exit between those two reads. The caller
then raises recovery-required from its earlier nonterminal snapshot although the
operation is complete. The CI's successful worker/completed operation and failed
caller match that reachable race; the log does not timestamp each internal
inspect response, so the precise interleaving still needs a deterministic
regression. This is not evidence to weaken the VM assertion or increase a
deadline.

Proposed bounded fix, pending architect/lead brief and release: after observing
a stopped worker, inspect the same operation again and honor its existing
complete/cancelled handling. Preserve the current recovery error for a fresh
nonterminal record. A deterministic existing Ruby host fixture should force
nonterminal inspect → worker inactive → complete inspect, and preserve genuine
stopped/nonterminal refusal and cancellation behavior. No recovery execution,
restart, new operation, state/schema change or fence bypass is proposed.

After a sufficient accepted fix brief: focused Ruby regression/syntax checks,
commit and affected independent review precede the necessary creation VM proof.
Existing passing fast/archive and composed package/system receipts retain only
their proven exact revision/derivation/input scope. Watcher-effect reconciliation
belongs to the lead and was not duplicated here.

### Implemented maintenance caller correction

After the architect's bounded brief and lead's explicit implementation release,
the correction is committed separately as
`eabb56a278bd8eb1759041467eaebfa6392ddcb2`
(`maintenance: recheck completion after observing worker exit`), exact parent
`e1c67dbee3188df9dc7c37fa1d1e724515530fea`. The original CI diagnosis and
failed creation receipt above remain unchanged historical evidence.

Exactly two source files changed, +89/-3:

- `libexec/workspace-maintenance.rb`: remember a non-active/non-activating
  worker observation and immediately inspect the original operation once more.
  Reuse the existing complete/cancelled handling. If that fresh record remains
  nonterminal, raise the identical recovery-required error. Inspection errors
  still propagate. Active/activating polling retains its existing sleep.
- `test/workspace_host/maintenance_test.rb`: existing host fixture forces the
  stale-inspect/worker-exit/fresh-inspect ordering. The 15-case matrix covers
  inactive/failed/deactivating worker states against complete, cancelled,
  source-recovered, still-nonterminal and inspection-error outcomes. It asserts
  the same UUID on every control request, exactly one prepare/start, no extra
  recovery/activation actions and no sleep after the stopped observation.
  A separate case preserves active/activating polling.

All error strings, persisted fields/formats, source-package ownership,
generation/profile/claim admission and native fences remain unchanged. This is
one ordinary read added at the observed race boundary, with no automatic
restart, recover action or new operation. The VM assertions/deadlines and the
reviewed 60-second hydration gate are untouched. A corrected target does not
replace retained older callers/workers; their original recovery contracts still
govern them.

Deterministic reproduction and quick verification:

1. Added the regression before changing runtime code, then ran
   `nix develop --command ruby test/workspace_host/maintenance_test.rb --name
   test_maintenance_switch_rechecks_operation_after_worker_exit` against the
   original `e1c67dbe` caller. It failed at the first stale→inactive→complete
   case with the same `requires maintenance recover; journal retained` error:
   1 run, 2 assertions, 1 error, test time 0.180 seconds. Complete tool output
   is preserved at
   `/tmp/2026-11-11-session-archival-failures-maintenance-old-regression.log`.
2. After the bounded fix, ran both new tests using the exact name selector
   `/test_maintenance_switch_rechecks_operation_after_worker_exit|test_maintenance_switch_preserves_active_and_activating_polling/`.
   Passed: 2 runs, 209 assertions, no failures/errors/skips; test time 2.735
   seconds, command elapsed 9.777 seconds. Log:
   `/tmp/2026-11-11-session-archival-failures-maintenance-new-regression.log`.
3. Relevant subset and both syntax checks passed through the fresh native
   Luna/low utility under the current selected `s0g…` policy. The actual script
   embedded an absolute worktree `cd`, HEAD and required-file preflight before
   entering Nix, then ran:

   ```sh
   nix develop --command bash -c 'set -e
   ruby -c libexec/workspace-maintenance.rb
   ruby -c test/workspace_host/maintenance_test.rb
   ruby test/workspace_host/maintenance_test.rb --name "/maintenance|restoration/"'
   ```

   Both syntax checks passed. Subset: 27 runs, 1,036 assertions, no
   failures/errors/skips, test time 12.428958 seconds, source `83944` exited 0.
   Its original stdout was subsequently preserved without another command at
   `/tmp/2026-11-11-session-archival-failures-maintenance-subset-first.log`.
4. `git diff --check`, staged diff check and final complete base-to-head diff
   check passed. No declared hook framework, configured hook path or active
   hook exists; no bypass was used. Final worktree/index are clean.

Process deviation, explicitly retained: the utility initially performed its
session check from the wrong default directory and launched no tests. After a
same-operation clarification it completed the assigned batch, then repeated the
already passing batch to capture a missed log, contrary to its explicit
no-repeat instruction. The duplicate source `21036` also exited 0, with test
time 12.194 seconds; log
`/tmp/2026-11-11-session-archival-failures-maintenance-subset.log`. This duplicate
is not needed for acceptance and adds no distinct verification scope. Both
sources are joined and no operation-owned cells/sessions remain. The deviation
was reported promptly to the lead; no further checks were run.

The checked and committed byte identities match:

| File | SHA-256 |
| --- | --- |
| `libexec/workspace-maintenance.rb` | `9228f7b0730cc4ed434dee04da7242756c905d936f6506bf8f076ab98d95dd97` |
| `test/workspace_host/maintenance_test.rb` | `88250c71ce7896705c5fbbd5f4c985fecc3180f8efe2ddd11e005b0627be47b9` |

Complete final runtime series from base
`db4b0fa62633b925e1917ec880737e1776f82cc8`:

1. `f124fd4e4fa34b20aef5063247a3ae8cb57a6d48` — monitor report invariant.
2. `e1c67dbee3188df9dc7c37fa1d1e724515530fea` — archive contention/status.
3. `eabb56a278bd8eb1759041467eaebfa6392ddcb2` — maintenance caller completion race.

D/C commit identities and accepted content are preserved exactly. The third
commit is the necessary independently reviewable CI correction; it is not a
mechanical equivalence claim for the new runtime. No obsolete approach,
repeated pin stream, migration or transitional schema path was introduced.
The migration inventory remains empty; no migration consumption lineage changes.

Documentation placement: the source comment preserves the concurrency rationale
for maintainers; this record preserves failure/reproduction/check provenance.
The fix restores the existing terminal-result contract, so no new product
procedure or user-facing text was needed, and the two-file boundary was retained.
Existing maintenance operations/recovery guidance and all supported paths remain.

The exclusive runtime source/index/commit window is released. Lead owns the
affected independent host/compatibility review before the necessary packaged
creation/maintenance proof and final-head workflow. F pins/artifacts must select
the accepted published successor under their ordinary graph/hook/pair checks.
No push, build, claim, merge, deployment or live recovery/lifecycle action was
performed. Implementer1 retains review-fix ownership and capacity after acceptance.


## P1: runtime CI observer core and archive-local proof

Implemented the lead-released A15 package against accepted P0 base
`eabb56a278bd8eb1759041467eaebfa6392ddcb2`. P1 component checkpoint is
`269e2e92849f7920b59cb1817beee4fdd9fe0a17`, tree
`42bf492bbefaa0050166b21a139f9215f4d9f900`. Component commit:
`monitor: observe existing CI without native utility turns`. No rebase or
dependency/pin update was introduced. Earlier integrated D/C/maintenance commits and reviewed refs are
unchanged. The component range is `eabb56a2..269e2e92`; this is not a standalone
buildable or publication-ready feature range.

Delivered direct registration/driver replay; strict shared-lock dual-format
storage; exact legacy local attestation; durable poll claim/result receipts;
read-only local assessment and accepted archive quiescence/detachment; existing
submission-ledger delivery/reconciliation for direct events; monitor CLI/MCP and
inherited EX-lock authority transport; source/candidate capability gates. Existing
maintenance inventory now includes direct-only uncertain execution/delivery and
samples ordinary native proof without requiring an idle attached reader to be
archived for a package transition. This is admission wiring, with no automatic
request cancellation, lifecycle action or new maintenance participant.

The private archive DTO contains `{authority,local,pending}`. `pending` is true
only for blocked IDs whose records are direct CI, quiescing, retain the exact
accepted binding and have an unjoined poll with known delivery. A fresh complete
local assessment excludes hard native/proof/delivery blockers. It is a bounded
wait hint; `local.state` remains blocked and neither current ownership nor unsent
execution is inferred after a crash. Omitted target can select only an existing
stored binding; ordinary v2 target/receipt validation still runs before effects.

Exact P1 committed paths (P2 paths remain unstaged):

```text
docs/workspace-portal.md
libexec/workspace-host
portal/cmd/workspace-portal/maintenance_monitor.go
portal/cmd/workspace-portal/monitor.go
portal/cmd/workspace-portal/monitor_archive.go
portal/cmd/workspace-portal/monitor_archive_test.go
portal/cmd/workspace-portal/monitor_mcp.go
portal/cmd/workspace-portal/monitor_test.go
portal/internal/monitoroperation/delivery.go
portal/internal/monitoroperation/lifecycle.go
portal/internal/monitoroperation/observer_delivery.go
portal/internal/monitoroperation/observer_delivery_test.go
portal/internal/monitoroperation/observer_lifecycle.go
portal/internal/monitoroperation/observer_service.go
portal/internal/monitoroperation/observer_store.go
portal/internal/monitoroperation/observer_test.go
portal/internal/monitoroperation/observer_types.go
portal/internal/monitoroperation/observer_validation.go
portal/internal/monitoroperation/service.go
portal/internal/monitoroperation/store.go
portal/internal/monitoroperation/types.go
portal/internal/session/contract.go
portal/internal/session/runtime-contract.json
portal/internal/session/turn_retry_contract_test.go
test/workspace_host/agent_team_registration_test.rb
```

Known quick checks ran inline in the repository Nix environment. All tool
sessions joined; no operation-owned check remains running:

| Check | Result |
| --- | --- |
| `go -C portal test -mod=readonly -count=1 ./internal/monitoroperation` | Passed, 5.944 s. Includes retained immutable report/replay/recovery tests and new direct/legacy proofs. |
| `go -C portal test -mod=readonly -count=1 ./cmd/workspace-portal -run "TestMonitorArchive|TestMonitorMCP|TestMonitorRequest|TestMonitorRecovery|TestMaintenanceMonitor"` | Passed, 0.286 s. |
| `go -C portal test -mod=readonly -count=1 ./internal/session -run TestMonitorObserverCapabilities` | Passed, 0.012 s; inputs unchanged in final P1 commit. |
| `ruby -c libexec/workspace-host` | Syntax OK. |
| `ruby test/workspace_host/agent_team_registration_test.rb --name "/monitor_state|observer_state/"` | Passed, 2 runs / 16 assertions, zero failures/errors/skips, 0.053 s. |
| Scoped Go formatting; `git diff --check`; `git diff --cached --check` | Passed. No declared hook framework, configured hook path or active pre-commit hook; no bypass. |

Focused new tests prove zero native launch on new CI registration, original native
driver replay, strict absent-state/duplicate-key/private-file handling, immutable
legacy bytes, exact proof refusal and changed-report invalidation, separate calls
for identical sources, continuation-only cancel, minimum poll interval, lost-handle
restart refusal, positive join outside the ID lock, no late event after detachment,
unknown delivery retained then reconciled with the original receipt/no duplicate
send, cross-format corruption refusal, inherited FD ownership/no downgrade,
partial Begin/lost reply/detached binding reuse and conflict refusal. The initial
joint CLI compilation exposed P2's shadowed local error variable; owner0 corrected
that boundary before the passing CLI checks. No command was repeated solely to
capture output and no long check was launched.

Final batch tool source `62528` exited 0; earlier focused sources `61479` and
`69833` exited 0. Commit source `69352` exited 0. The sorted 25-file SHA256 map
at `/tmp/session-archival-p1-final-files.json` has SHA256
`4f4efe1542b82ef83fe66205d454ede166bee941292dc5b31033891dacd92ec4`.
Post-commit checks matched every listed worktree byte and committed blob to this
map, and confirmed empty index. Shared P2 working changes were excluded; these
quick checks are implementation proofs, not the complete final P1+P2 integration
or packaged runtime/native proof.

Persistence/compatibility: this adds schema-1 `observers/<id>.json`; it does not
migrate or rewrite schema-1 native operations, reports or existing resolutions.
Native capabilities remain integer1. Any observer directory additionally requires
integer1 `monitorObserverStateSchema` and `monitorObserverLifecyclePolicy` in
both source preflight and candidate activation. No destructive downgrade or
conversion is supplied. No database migrations, migration consumption lineage,
new native launch identity or archived-state rewrite. Existing unknown native,
delivery, recovery, resource and file-removal fences remain independent.

Documentation inventory: the runtime monitor section in
`docs/workspace-portal.md` owns lasting execution-owner, local-proof, persistence,
shutdown and capability contracts for developers/operators. Root applied the
required public prose pass before the final batch, including MCP help. P2 owns
caller/skill/archive recovery guidance. This record owns exact package/evidence
and temporary review state; no product docs depend on this initiative's rollout.

The exclusive source/index/commit window is released. Root owns acceptance,
final P1+P2 independent review and subsequent integration checks/publication.
Long packaged monitor/native/archive proof remains required after that review.
No build, push, claim, deployment, merge or live monitor/session lifecycle action
was performed. Implementer1 retains P1 review-fix ownership and capacity after
acceptance. Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-session-archival-failures/.


### P1 acceptance and pending history consolidation

Lead accepted P1 technical delivery and quick proof. The checks compiled P1 with
P2 working-tree sources: `monitor_archive.go` calls P2's new
`web.ValidateMonitorArchiveAuthority` in `archive_preparation.go`, which is absent
from the isolated component commit. Therefore `269e2e92` is an exact component
checkpoint only, not an independently buildable/publication-ready feature head.
Retain its component manifest and check receipts; no independent push is planned.
Root will authorize P2 to amend the unpublished component with completed P2 files
into one coherent A14 runtime feature commit after both manifests and final checks.
This consolidation must preserve the integrated `eabb56a2` base and does not rewrite
merged history. Final readiness and whole-feature history conclusions belong to
that consolidated range and its independent review.

P1 source/hash inputs remain frozen. No additional source, check, index or history
action was taken for this correction. Implementer1 confirms capacity and retains
P1 review-fix ownership. Lead owns consolidation/review coordination.


### P1 retained-owner fix: ordinary archive operation IDs

P2's production-shaped queued-CI archive fixtures exposed a format mismatch:
`validateArchive` applied monitor `validID` (32 hex or UUID) to the ordinary
lifecycle `OperationID`, while real archive journals/preludes/browser operations
use exactly 64 lowercase hex characters. Canonical source evidence is
`session.validLifecycleJournalID` in `portal/internal/session/lifecycle.go`
and `SecureRandom.hex(32)` plus explicit 64-hex validation in `libexec/dev-session`.
The CLI pre-journal allocator also generated only 16 random bytes.

Under lead's narrow retained-owner release, changed only `validateArchive` to
use the existing exact 64-hex pattern and changed the private CLI allocation to
32 random bytes. Monitor/attestation ID validation, authorization callbacks,
source/target/mode/binding identity, schemas and native contracts remain unchanged.
Related P1 archive fixture IDs now match the ordinary lifecycle format; no P2
fixture was weakened. New boundary proof accepts real64 and refuses monitor32,
UUID, uppercase, wrong length and nonhex archive IDs. The existing partial-Begin,
lost-reply/detached retry test now asserts generated64 and exercises it end to end.

Focused known-quick Nix batch source `55668` joined0:

- `go -C portal test -mod=readonly -count=1 ./internal/monitoroperation -run "TestObserverArchiveAuthorityUsesLifecycleJournalID|TestDirectPollQuiescence|TestObserverCrashIntent|TestDirectDeliveryUnknown"`: passed, 0.239 s.
- `go -C portal test -mod=readonly -count=1 ./cmd/workspace-portal -run "TestMonitorArchiveSelection|TestMonitorArchivePending"`: passed, 0.182 s.
- Scoped Go formatting and diff check passed. No full core/web rerun by P1; P2 owns the exact two observed web failures.

The original component manifest remains unchanged at
`/tmp/session-archival-p1-final-files.json`, SHA256
`4f4efe1542b82ef83fe66205d454ede166bee941292dc5b31033891dacd92ec4`.
Updated complete 25-file P1 manifest is
`/tmp/session-archival-p1-lifecycle-id-fix-files.json`, SHA256
`9d16839b889e0814b60efffbf04a65a7ca198e6a92588650080d1398c689b186`.
Exactly these five P1 bytes differ from the component manifest:

| Path | New SHA256 |
| --- | --- |
| `portal/cmd/workspace-portal/monitor_archive.go` | `5bfeb2c99e65b543e0d85e8a092d4f9cd6eae7c5abdee035dc64b40dcb7783fa` |
| `portal/cmd/workspace-portal/monitor_archive_test.go` | `1f16afca22b05598511b38f2721b9ddc9e9c9c161bf6f79e11c089bf9696e1c1` |
| `portal/internal/monitoroperation/observer_delivery_test.go` | `70782d8e82395c68f6f42aa08695766dbd88c576d7cdee61dd0e6a7c52a4e5e8` |
| `portal/internal/monitoroperation/observer_test.go` | `e3d9c5652834ee2d3c635675d137a615b7f2e9cec418f4da34bf0195e8a9e184` |
| `portal/internal/monitoroperation/observer_validation.go` | `ac620a1e273a054288cc6d99859ede23b0f0ba87e23edf316cbe04e004b2a01f` |

No index/commit/history/push action was taken; HEAD remains component269.
The source window is released, this fix remains unstaged for the root-authorized
joint amendment, and P1 source hashes are frozen again. No migration or existing
persisted-record conversion was added. No live observer or lifecycle action ran.


### A16: observer-aware retained MCP helper cutover

Implemented the lead-released saved A16 brief with no production switch-code
change. `livePackageSwitchPolicy` advances from1 to2; reporting remains3, exact
MCP startup arguments/tool names/native binary and original schemas/replay stay
unchanged. The existing source-compatible restart predicate handles the mismatch;
only a real target activation/restart can publish target launch provenance.

The small support fixture `test/support/live_switch_policy_one.rb` freezes the
exact eabb `live_package_switch_contract?` source method and literal policy1,
independent of the newly compiled default2. It records the original method hash
and uses the existing transition/maintenance harness for all other paths; no full
historical implementation or new fixture framework was copied. Tests prove a
policy1 source accepts reporting3/target2, retains equivalent native argv, selects
restart/maintenance, refuses active/unknown execution before profile mutation,
and enters the actual target `_activate` path. Injected restart failure preserves
the source launch marker and exact forward target; stable target retry replaces
the marker. A later2-to2 update stays live and preserves actual launch evidence.
Representative existing completed-maintenance retry/source-recovery coverage also
passed without changing operation protocols or resume/receipt behavior.

Prepared, but did not execute, tagged packaged acceptance in the existing
`TestNativeMonitorOperation/native-restart` fixture. It requires candidate policy2/
reporting3, queries the actual retained lead's daemon-start MCP inventory after
its owned restart for the `attest-local` schema, then calls real status through
that helper and verifies the new NativeStatus acknowledgement digests/execution
owner without waking the lead. This is not a standalone fresh-helper assertion.
Actual packaged/native execution remains required after final committed review;
the Ruby source/target proof alone does not establish that native helper result.

Lead completed the public prose pass on existing switching/reporting passages in
`docs/workspace-portal.md` and `docs/workspace-updates.md` before the final batch.
The portal reference owns policy/launch-marker compatibility; the updates guide
owns ordinary enabled-maintenance, idle refusal and same-operation forward retry.
No new restart command, flag, daemon, protocol, lifecycle authority or recovery
framework was added. No session state or live runtime was touched.

Known-quick Nix policy batch source `5646` joined0:

- `go -C portal test -mod=readonly -count=1 ./internal/session -run "TestObserverHelperCutover|TestMonitorObserverCapabilities"`: passed0.019s.
- `go -C portal test -mod=readonly -tags live_switch_integration -run "^TestMonitorToolSchemaSurface$" ./cmd/workspace-portal`: passed0.062s; compiles tagged packaged/native assertions without running them.
- `ruby -Itest -r ./test/workspace_host/agent_team_registration_test.rb -r ./test/workspace_host/live_switch_test.rb -r ./test/workspace_host/maintenance_test.rb -e "" -- --name "/test_observer_policy_cutover|test_reporting_package|test_failed_live_activation|test_maintenance_owned_activation_accepts_completed_retry_and_admitted_source_recovery/"`: passed6tests/90assertions,1.317s.
- Scoped Ruby syntax passed in source34879; Go formatting and final `git diff --check` passed. No long test/build or duplicated watcher was launched.

Final complete P1 scope is30files: the previous25 plus:

- `docs/workspace-updates.md`
- `test/workspace_host/live_switch_test.rb`
- `test/workspace_host/maintenance_test.rb`
- `test/support/live_switch_policy_one.rb`
- `portal/cmd/workspace-portal/monitor_native_integration_test.go`

Original component and canonical64 manifests remain unchanged. Final complete map
`/tmp/session-archival-p1-a16-files.json` SHA256
`dd1118ba77cd22f0f48cc893f031a105c41e1e4ff72c02f2fca48bdf73b0c4c7` includes the canonical64 correction and these A16 changes:

| Path | A16 final SHA256 |
| --- | --- |
| `docs/workspace-portal.md` | `460fc9d3e83db622a1107413d4e996eb07bb41ff486e0d870f221bea4b6b32e3` |
| `docs/workspace-updates.md` | `d39e9e357533038ced66b93417cfb56ff00da951c680a26a4bf7dad62525481f` |
| `portal/cmd/workspace-portal/monitor_native_integration_test.go` | `fb28c780ca8ab01d52d3d0083f23f900fd2a3b7f1ec9c40b40fce31ca6861536` |
| `portal/internal/session/runtime-contract.json` | `1f8b91d7e2a587912c7e8b8cb094e754ff2f156837d8bc6ccfbafe2daf26ea5f` |
| `portal/internal/session/turn_retry_contract_test.go` | `e3a5b46b12cd51ae08de7056702b73c8b1cb6646c186d4dfe56e2f6ae7a0dd7a` |
| `test/support/live_switch_policy_one.rb` | `879aefadedaf74656945981a4897428ca25a8dab8ef10ff1ad7e8b5e0030c8f2` |
| `test/workspace_host/live_switch_test.rb` | `f0dcbe0def5738a22737211faf67200aa2f3b891e4be79460462a75be6a46c9b` |
| `test/workspace_host/maintenance_test.rb` | `9b33b28f25526607ab8a3cd7ae21335581617d95f47e1e0bf7ca0a44c1b9bde3` |

HEAD remains component `269e2e92849f7920b59cb1817beee4fdd9fe0a17`; no index,
commit, history rewrite or publication action by P1. Index is empty, all check
sources joined and P2 paths remain outside this manifest. The source window is
released and P1 bytes are frozen for the root-authorized final coherent joint
amendment. Component269 is still not independently buildable/publication-ready.
No database migrations or native/observer state conversion were introduced.
Reporting-policy1/2/3 and source-owned maintenance recovery remain supported.


### Final coherent A14 amendment receipt (implementer0, 2026-11-13)

Root accepted both complete manifests and released the exclusive final runtime
index/commit window. Component `269e2e92849f7920b59cb1817beee4fdd9fe0a17`
was preserved by atomic create-if-absent at
`refs/checkpoints/2026-11-11-session-archival-failures/a14-p1-269e2e92849f`.
A collision would have required that exact same object; no foreign ref was
replaced. All original merged eabb ancestry and older reviewed/built refs remain.

Only the approved combined48 paths were staged. Ordinary repository Nix Git
`commit --amend -F <temporary-message>` produced:

- Final head: `b9b408710e5c20ffa470afde10e4f7afc33919d2`.
- Final tree: `2c6e10d1104a9fc942088a5872694b2a35d6b788`.
- Sole parent/base: `eabb56a278bd8eb1759041467eaebfa6392ddcb2`.
- Complete base-to-head count:1; final scope48 files,4546 additions/131 removals.
- Combined approved manifest SHA256:
  `c6701ebd6a0d20590c64792cc0beadfdbf11dacecb7a9dc4da7b1d094f6296fa`.

Every committed blob and working file matches the approved map. The exact
base-to-head changed-path set equals those48 paths; whole diff check passes.
Existing modes are unchanged;14 new source/test files are100644. Final index and
working tree are clean, including untracked-file inventory. Repository hook
framework search, default `core.hooksPath` and non-sample-hook inventory remain
empty; no hook was bypassed. The first missing-checkpoint probe used `show-ref`
without `--quiet` and exited128 before any mutation; the corrected documented
quiet probe returned absent, then atomic create succeeded. This was command
setup only, with no source/index/commit uncertainty. The amendment command and
all verification cells joined exit0.

The final series contains the complete P1/P2 implementation and narrow source
fixes in one buildable logical commit, rather than retaining the incomplete
component or follow-up fix streams. New persisted state is separate observer
schema1 under explicit observer-state/lifecycle capabilities1+1; native schema1
receipts and historical reports remain unchanged. No database migration, eager
conversion, destructive downgrade or intermediate externally consumed A14 format
exists. Final live-switch policy2 requires ordinary helper cutover for the new
MCP surface; reporting policy3 and native/package interfaces are preserved.

Previously passing quick evidence applies to identical final source bytes.
No test/build rerun, publication, deployment, merge or live lifecycle/monitor
mutation was performed in this commit window. Exact machine-readable receipt:
`/tmp/session-archival-a14-commit-receipt.json`. Source/index/commit window
released to root immediately after joined clean proof. Independent final review
and post-review packaged/native verification remain root-owned; implementer0
retains P2 review fixes and has available capacity after acceptance.


### R9 retained P1 remediation: admission and completed retirement

Implemented only the two accepted Important findings from the preserved verbatim
`final-review-r9.md`, against reviewed
`b9b408710e5c20ffa470afde10e4f7afc33919d2`. Original component269, canonical64,
A16 maps/checkpoints and raw review are unchanged. This is a narrow source
correction pending the root-authorized final joint amendment; no commit/index
or publication action was taken by P1.

1. `ValidateDirectCISource(Source) error` now owns the exact existing fixed GitHub
   adapter grammar (owner/repository, positive numeric workflow/run/attempt and
   full40/64 lowercase-hex commit). `StartCIObservation` invokes it only after
   legitimate exact stored replay and before a NEW direct record is written.
   Generic `validateStart`, native/persisted readers and original schemas remain
   untouched. P2 consumes this export and owns the original-call positive
   pre-Start refusal receipt correction; P1 made no web/processgroup edit.
2. A private naturally-completed direct predicate requires observing phase,
   validated completed remote snapshot, matching immutable terminal event and
   positive exact joined poll. Existing receipt checks still run first.
   RequireIdle/Assess can recognize that completion without synthetic archive
   authority. The existing Lifecycle.Revoke now suppresses unsent direct events,
   retaining accepted/submitting receipts and all poll/source/phase/binding state.
   Ordinary Archive continues through Revoke then RequireIdle. RequireArchived
   additionally requires detached state or naturally-completed plus revoked
   continuation. Queued/nonterminal, missing/intent/running/lost execution and
   unknown/submitting delivery retain their refusal paths. No delete authority,
   schema, new lifecycle command or general shutdown framework was introduced.

New proofs cover adapter-invalid NEW creation without any observer/poll/native
effects; exact historical native named-workflow/badnumeric source read/retry with
unchanged bytes; exact historical direct replay before new-only validation;
completed pending/held/accepted continuation through ordinary revoke/retirement
without archive binding, no future poll/send and preserved accepted receipt;
and queued/error/missing poll/intent/running/unknown delivery/missing terminal
event refusal before and after continuation revocation. P2 owns the independent
ordinary Ruby delete ordering/refusal and original-bound pre-Start adapter tests.

Known-quick Nix proof:

- Source9600: `go -C portal test -mod=readonly -count=1 ./internal/monitoroperation` passed6.298s, including retained native immutable report/replay/recovery tests. The subsequent CLI compile was blocked by P2's moved local `err` declaration in monitor_ci.go172/173, reported directly to P2.
- P2 corrected that specific compile boundary. Source10634 reran ONLY the blocked command: `go -C portal test -mod=readonly -count=1 ./cmd/workspace-portal -run "TestMonitorArchive|TestMonitorMCP|TestMonitorRequest|TestMonitorRecovery|TestMaintenanceMonitor"`, passed0.322s, followed by clean `git diff --check`.
- Scoped Go formatting passed; source9600 and10634 are joined. The passing core result was retained rather than repeated. No long/native/VM/build or unrelated suite was run.

Root supplied and prose-passed the related source-format/completed-retirement
wording in `docs/workspace-portal.md` and lasting source-owned upgrade prerequisite
in `docs/workspace-updates.md`. Both are included in the final P1 map. All four short
technical errors were accepted unchanged by root; no machine-significant
identifier/error parsing changed. Source/activation hold and real packaged/native
acceptance remain root-owned and unresolved by these quick tests.

Complete P1 scope remains30files. Reviewed-b9 baseline map
`/tmp/session-archival-p1-r9-base-files.json` SHA256
`dd1118ba77cd22f0f48cc893f031a105c41e1e4ff72c02f2fca48bdf73b0c4c7` records exact original committed blobs.
Final complete map `/tmp/session-archival-p1-r9-files.json` SHA256
`5d90b0192d79faff8e761f58cedacc519ad6f5caa82f446ff5ce2897f0e958e4` has exactly these8changed paths relative to b9:

| Path | Final SHA256 |
| --- | --- |
| `docs/workspace-portal.md` | `87a77116a6bc48a1cda0529960a0c341167d18a8729e71d4b3328531602dc125` |
| `docs/workspace-updates.md` | `5a6679c9de6a4d9bb1502e5b1d6a8e9f2e6eb521b9a1bc82a7d3eaa36671b801` |
| `portal/internal/monitoroperation/lifecycle.go` | `d589feee2fa62933ed56771a354706555c9311c703ce66efda046ec3c9f79620` |
| `portal/internal/monitoroperation/observer_delivery_test.go` | `c7ef6bb272501d429ba0db58bcadd135cfb548e78efb0252e7ba2491fd6bc180` |
| `portal/internal/monitoroperation/observer_lifecycle.go` | `442eecab4760080e5c67bf4d4d08e89fd94d3f1ef8de40240dc713bc71eaf43f` |
| `portal/internal/monitoroperation/observer_service.go` | `11ecfcb9fcc561de8a91c8e3eca68555ddebd70275916c6ec4565fd523c90577` |
| `portal/internal/monitoroperation/observer_test.go` | `7bd574dcbe45ce9f6f47913e417fcbb16a3f731c2dfb5977d9af607276a5b946` |
| `portal/internal/monitoroperation/observer_validation.go` | `c1a127454724ec540b7087900756bae4c77bf591ab92318c9fa22541e2e07da8` |

All other P1 bytes match b9. No migration, eager record conversion, policy/format
bump or merged-history rewrite is part of this remediation. P1 fixes remain
unstaged for one coherent final joint amendment after P2's distinct proofs.
Source window released; P1 map is frozen and retained finding ownership continues.


### R9 final joint amendment and narrow-fix lineage

Root inspected the exact12-path remediation and all new tests, accepted the
errors/docs and resolved R9 findings1/2 under mandatory-review step9. The
original report remains unchanged: reviewed runtime range
`eabb56a278bd8eb1759041467eaebfa6392ddcb2..b9b408710e5c20ffa470afde10e4f7afc33919d2`.
The amended runtime is:

- Final head `4f99d2eb84e35750108fdc6fbc1449b185d48f9a`.
- Final tree `2a08df578c861fb99dc2e9ece1993377a366f146`.
- Sole parent/base `eabb56a278bd8eb1759041467eaebfa6392ddcb2`; exactly1 commit.
- Final scope49 paths,5031 additions/132 removals; exact combined map
  `362800c3927db2448cb1c5062b8e714889ed941265f53d8f8abfbb735bb4d4d0`.
- Reviewed predecessor b9 is retained atomically at
  `refs/checkpoints/2026-11-11-session-archival-failures/a14-r9-reviewed-b9b408710e5c`.
  The original269 checkpoint, original maps/check receipts and R9 report remain.

The explicit narrow comparison is
`b9b408710e5c20ffa470afde10e4f7afc33919d2..4f99d2eb84e35750108fdc6fbc1449b185d48f9a`:
12 paths,505 additions/21 removals. It contains P1's six core/test files, P2's
adapter/test/delete-order coverage and the three root-reviewed docs/skill
passages. It introduces no design, authority, schema, data-format, migration,
eager conversion, framework or operator-action expansion. The A14 separate
observer schema1/capability gate and unchanged native schema1 remain as reviewed.
Neither predecessor nor final A14 format has been installed, released or
externally consumed by these implementation packages. Root's separate activation
hold is unchanged by the two fixes.

Source proof retained without repeating passing suites: P1 fullcore6.298s,
blocked CLI-only0.322s; P2 helper2.057s, corrected blocked web-only0.302s,
exact delete Ruby2tests17asserts0.203s plus syntax/gofmt/diff. All proof applies
to unchanged final source bytes, verified against the two disjoint maps and all49
committed blobs/working files. Original first compile failure remains recorded.

Root's final exclusive window staged only the approved49 paths and used ordinary
repository Nix `git commit --amend -F <temporary-message>`, preserving the eabb
ancestry. The reviewed-b9 ref used create-if-absent, with any collision required
to match that exact object. An initial commit-message length guard stopped after
staging but before commit; the message was wrapped and resumption revalidated
all staged paths/blobs and no unrelated source. No source changed during that
setup correction. Final command91316 joined exit0; no uncertain commit effect
remains. Hooks used the unchanged default path; no framework or active hook was
present and none was bypassed.

Final whole diff check passes,49 committed+working hashes match, existing modes
are unchanged and14 new files are100644. Index, tracked tree and untracked
inventory are clean. Exact receipt:
`/tmp/session-archival-a14-r9-commit-receipt.json`.
The source/index/commit window was released immediately after verified completion.
No extra test/build/VM, push, merge, claim, activation or live session/monitor
mutation occurred. Root owns publication and subsequent exact-head verification;
implementer0 retains P2 follow-up fixes and available capacity after acceptance.

Original unchanged R9 report SHA256: `feac82b0d175b2818cd6ff6ca9067b3cbc48cc1406fc643cabcb257bfc0c89ed`.


### C4 committed correction and window release

Root inspected/accepted the exact two-file C4 diff and focused evidence, then
released the short amendment window. Exact published/reviewed predecessor
`4f99d2eb84e35750108fdc6fbc1449b185d48f9a` was preserved by atomic
create-if-absent ref
`refs/checkpoints/2026-11-11-session-archival-failures/a14-c4-reviewed-4f99d2eb84e3`;
a collision could only reuse that exact object. Existing269/b9 checkpoint refs,
original review reports, maps, CI/job logs and F3 pins/receipts remain unchanged.

Only the accepted two frozen paths were staged from an empty index. Ordinary
Nix Git `commit --amend -F <temporary-message>` retained the complete feature
message and produced final runtime:

- Head `1e5f566e4dc77a7d45d545b06bf345bdf5d82edc`.
- Tree `9417a48d198e29ee76aa4a17063f896260267617`.
- Sole parent/base `eabb56a278bd8eb1759041467eaebfa6392ddcb2`; count1.
- Original narrow range `4f99d2eb84e35750108fdc6fbc1449b185d48f9a..1e5f566e4dc77a7d45d545b06bf345bdf5d82edc`:
  exactly `nix/tests/session-archive-lifecycle.nix` and
  `portal/internal/web/monitor_ci_test.go`,39 additions/2 removals, no mode change.

All49 complete source blobs/worktree files match the prior approved map with
only the two accepted C4 hashes replaced. The complete frozen map
`/tmp/session-archival-ci-43438190694/c4-complete-files.json` SHA256 is
`b5c9389d7ce7c2ace22cdf17c856ddf3828ea496cf5ca005594b468ffc6cfdf8`;
C4's two-file map stays
`b7675c923ff2b787207089daddddd573de516cd369b6625afa80a0ab1685e0fc`.
The focused0.092s originating-turn regression and generated-syntax/order proof
bind these exact final C4 inputs; no successful check was repeated for amendment.
Earlier fast/creation/package receipts keep their exact old-head/input scope.

Final complete diff check, one-commit history, index/tracked/untracked/unmerged
cleanliness and modes pass. Runtime still declares no hook framework, uses the
default hook path and has no active non-sample hook; no hook was bypassed.
Command46139 and all cells joined exit0. Exact machine-readable receipt:
`/tmp/session-archival-ci-43438190694/c4-commit-receipt.json`.

The fixture correction is consolidated into the one complete A14 feature commit;
no obsolete unapplied fixture-fix stream remains. No production admission,
assertion/deadline waiver, new schema/persisted-format/database migration/eager
conversion/operator action or runtime recovery change was introduced. Merged
eabb ancestry and the original reviewed A14 observer capability/format contract
remain. Neither correction nor publication authorizes activation or live lifecycle
work. Source/index/amend window released immediately on joined proof. No push,
CI/job rerun, VM/build, pin refresh, claim or live action occurred. Root owns the
affected committed review/publication; F3 config29075/workspace689 checkpoints
still select4f99 until root settles the new final runtime head. Implementer0
retains C4/P2 follow-up fixes and available capacity after acceptance.


## C5: real threadless monitor CLI/Ruby response contract

Bounded package assigned after accepted P1/R9 and C4, against reviewed/published
runtime `1e5f566e4dc77a7d45d545b06bf345bdf5d82edc`. Source edits are initially held
while root's already-launched exact1e5 managed-native batch uses the same checkout.
No source/test/index/history edit by C5 has occurred at this checkpoint.

Fetched ONLY the completed archive job131955004087 log for CI43445868248/attempt1,
once, through `gh api --allow-escape-sequences repos/aither64/dev-workspace/actions/jobs/131955004087/logs`.
Retained `/tmp/session-archival-ci-43445868248/archive-failure.log`,814255bytes,
SHA256 `1dd278fc398b8f729e5fdb88779410e41112ceff7ffe83f34920b46e251caf92`.
Download source27469 joined0; C5 neither watched nor reran CI.

The authoritative failure is the later threadless roundtrip slug
`2026-10-17-roundtrip`, not the preceding queued-observer case. Its accepted
currentTarget has empty threadId and readiness is monitorLocalquiescent with an
empty operation list. The worker fails at14:54:20 with `monitor shutdown returned
invalid output`; the final VM assertion at log4985 preserves the real request,
receipt, journal and target identities. The preceding observer scenario makes
the workspace monitor store exist, so Ruby invokes the helper even though this
threadless slug owns no monitor record.

Source diagnosis: `monitorLifecycleCommand` validates empty-root ownership and
returns nil/no stdout for begin-archive or complete-archive. The real Ruby
`quiesce_archive_observers!` always JSON.parse's the successful output and requires
the typed authority/local DTO. Exit0 plus empty stdout therefore causes its exact
JSON error; this is a producer/consumer no-op contract mismatch.

Faithful pre-fix reproduction, source77714 joined0: temporary
`/tmp/session-archival-ci-43445868248/c5-reproduce.rb` loads the existing aggregate
Ruby harness, runs the actual DevSession::CommandRunner and real admitted
quiesce_archive_observers! caller with its real inherited EX lock, and executes
unchanged Go monitor-lifecycle CLI through `go run -mod=readonly`.
The actual begin-archive returns stdoutempty/stderrempty/exit0; the real Ruby
parser raises the exact CI error. Result1test/5assertions,3.288s; complete output
`/tmp/session-archival-ci-43445868248/c5-reproduce.log`. No Nix package build,
VM, native request, session lifecycle mutation or source edit was needed.

Two setup-only attempts are retained honestly: a Minitest filter without slash
syntax selected zero tests; loading just monitor_archive_test.rb lacked the
existing aggregate NullTmux fixture. Both ran no CLI. The existing aggregate
harness fixed that setup once; no new fixture framework was introduced and the
actual reproduction was not repeated for logging.

Proposed bounded correction: monitor.go routes empty-owned threadless begin/
complete through the existing monitor_archive.go selected-generation, admitted
parent-descriptor and ordinary v2 target/real receipt adapter. Once that exact
no-owned-record proof succeeds, return truthful quiescent[]/pendingfalse JSON
without calling a native/core shutdown or fabricating a root/receipt/authority.
Regression belongs in existing monitor_archive_test.go, using actual CLI process
stdout in the real Ruby parser/caller, with empty/structured response branches
and owned/live/unknown refusal cases. All ordinary native/resource/readiness/
file-removal assertions and the VM scenarios remain unchanged. Root owns source
release after its existing native batch completes; C5 does not observe it.


### C5 implementation and frozen focused proof

Root released the source window after its existing exact1e5 managed-native batch
became terminal/joined. Implemented saved design section C5 without changing
monitor/core signatures, core nonempty-root validation, Ruby production, observer
state/schema, delivery/native/resource fences or any VM scenario/assertion.

Only these three P1 files changed:

- `portal/cmd/workspace-portal/monitor.go`: threadless Begin/Complete use the same admitted archive adapter instead of returning empty stdout; scalar idle actions retain their original response contract.
- `portal/cmd/workspace-portal/monitor_archive.go`: after existing generation, inherited EX-parent descriptor or real browser receipt, current target/root/journal selection and ordinary receipt validation, verify normalized threadless manifest and a fresh readable empty list from both owned stores. Retain canonical64 operation ID, accepted mode and bounded receipt checks while skipping the real-root-only core. Return the existing authority/local/pending envelope with actual absent root, quiescent non-null empty operationIds and pendingfalse. A recorded null journal root now matches actual root absence; nonempty mismatches still refuse. No core/native/revoke/detach/observer write or successful-archive assertion occurs.
- `portal/cmd/workspace-portal/monitor_archive_test.go`: actual command child process stdout/exit/FD enters the real Ruby production caller under existing admitted locks. Other focused cases use production command/adapter and ordinary persisted receipt validation, with exact binding/journal/no-op/refusal proof.

The new real CLI→Ruby regression accepts both Begin and Complete, verifies same
selected64 ID and archive progress handoff, preserves the absent root and optional
receipt field, and still exercises scalar require-idle and structured assess-local
through their real Ruby caller. No monitor record is created. Command/adapter
proof also covers real receipt-backed browser binding; same-ID ordinary journal
with null root; wrong journal root/mode; invalid32/uppercase operation IDs, empty/
oversized mode/receipt, changed target, missing parent FD, wrong generation,
root mismatch, unnormalized manifest, malformed legacy/observer stores, foreign
owned observer/intent/running records, and wrong receipt. An unrelated intent
record remains byte-identical, without adoption or cancellation. A direct core
assertion retains its nonempty-root refusal. Existing inherited-lock, accepted
binding, pending-join and threadless observation/native-negative checks remain.

Final known-quick Nix batch source53234 joined0:

```sh
nix develop --command bash -c 'set -e
 gofmt -w portal/cmd/workspace-portal/monitor.go portal/cmd/workspace-portal/monitor_archive.go portal/cmd/workspace-portal/monitor_archive_test.go
 go -C portal test -mod=readonly -count=1 ./cmd/workspace-portal -run "TestMonitorArchive|TestExplicitThreadlessArchiveUsesRealObserverAndPreparedReceipt"
 git diff --check -- portal/cmd/workspace-portal/monitor.go portal/cmd/workspace-portal/monitor_archive.go portal/cmd/workspace-portal/monitor_archive_test.go'
```

Passed1.700s; formatting/scoped diff check clean. Initial new-case subset17964
passed1.075s before adding the necessary ordinary null-root journal retry and
unrelated-record preservation coverage. That concrete source/test change justified
the final related batch. No VM, package build, CI rerun/watch, broad suite or
new utility was launched. All own commands/processes are joined. No source edit
preceded root's release, so its exact1e5 native batch did not consume C5 bytes.

No new public error string was introduced: existing authority/ownership,
unsupported-action and normalized-tracking errors are reused. This restores the
already documented A15 typed CLI response, so no C5 product-doc change was needed.
Root's disjoint `test/README.md` inner-ELF invocation correction is preserved
unstaged and excluded from this three-file map; root inventories it separately.

Exact base/unchanged HEAD:
`1e5f566e4dc77a7d45d545b06bf345bdf5d82edc`.
Baseline map `/tmp/session-archival-ci-43445868248/c5-base-files.json` SHA256
`4597a395a892a347cfcccbc01436f713e7c47c2720bb7c1cec5c92e7dc9e74bc`.
Frozen final map `/tmp/session-archival-ci-43445868248/c5-files.json` SHA256
`cbfc32f7d43b8e49f87b74b54bd9a8e0d32f8688eaccad24ac3fffbe5555aef3`.
Exact owned diff `/tmp/session-archival-ci-43445868248/c5-owned.diff` SHA256
`60e3910e7e7248023fa48265f9bdc19dab03d96e23c0b3a2c205c19d699b6d00`.

| Owned path | Final SHA256 |
| --- | --- |
| `portal/cmd/workspace-portal/monitor.go` | `1f2706300dfe208d3c1f983f1e680f3af238f8a5a7cfd8595788ac4ddb279ef2` |
| `portal/cmd/workspace-portal/monitor_archive.go` | `7054adaed47b493e5ad126572a723997ddfb8ee993aa06933802817f89cd5cc2` |
| `portal/cmd/workspace-portal/monitor_archive_test.go` | `3d99bad1bd5b9b5593f64915566ac30461ed8dfd3f2f3b0899d2c9238f7747bc` |

No index/commit/rebase/history rewrite or push was performed. Index is empty;
original reviewed/published history, checkpoints, review/CI/build receipts and
maps remain intact. No database migration, persisted conversion or capability/
policy bump was introduced. Root owns narrow inspection/prose, eventual coherent
commit/review/publication and final-head packaged evidence. The source window is
released, the three-file map is frozen, and implementer1 retains C5 fixes ownership
and capacity after acceptance. No claim, activation, deployment, merge, live
attestation/resolve/cancel/archive/delete or other session lifecycle action ran.


### C5 final joint amendment and window release

After root accepted the complete production/test diff and exact four-path map,
used the released exclusive runtime index/amend window. Atomically created
`refs/checkpoints/2026-11-11-session-archival-failures/c5-reviewed-1e5f566e`
at original published/R10-reviewed
`1e5f566e4dc77a7d45d545b06bf345bdf5d82edc`, with an expected-absent ref guard.
Retained all prior own refs unchanged, including component269, reviewedb9,
reviewed4f99 and original797/43085 checkpoints. Original review, CI, build and
frozen-map receipts remain intact.

Staged exactly the three accepted C5 paths plus ROOT-owned `test/README.md`,
whose assigned SHA256 is
`f39ebe7e38ee1588c91644d0f8a51cfcdf61ae08d392e8539b626167343d2de4`.
Root owns that disjoint prose correction to select the packaged inner ELF at
`LIVE_MONITOR_PACKAGE/libexec/codex/libexec/codex/bin/codex`; root's C6 probe proof
is retained separately. P1 did not rerun that native probe or edit its fixture.
The approved combined map
`/tmp/session-archival-ci-43445868248/c5-final-four-files.json` has SHA256
`05cd1989b757eb79ff6662189b729579007e6f51a574875468aa906fb6240a3c`.

Committed through ordinary repository Nix environment with
`git commit --amend -F /tmp/session-archival-ci-43445868248/c5-commit-message`;
source12488 joined0. No hook bypass, declared framework or active pre-commit hook.
The subject remains `monitor: separate local CI observation from remote completion`;
the body now also states the admitted threadless response and exact bindings.
No successful test was repeated for the amendment.

Final head `9678f71d44780d3c49130372e7944a770fc5e3b6`, tree
`ec9563dadbfa95272ab1fcf8ba6553e7141ceb3c`. Direct parent is unchanged merged
`eabb56a278bd8eb1759041467eaebfa6392ddcb2`; complete final range is
`eabb56a2..9678f71d`, exactly **one** coherent full A14 feature commit,
50files/+5412/-134. All four worktree bytes and committed blobs match the
approved map. Worktree and index are clean. Exact original1e5→final9678 delta
contains ONLY those four paths, each retaining mode100644; no unrelated content
or index entry entered the commit.

The complete series retains integrated D/C/maintenance ancestry and contains no
obsolete partial commit/fixup stream or dependency/pin stream. There are **no
database migrations** or new C5 persisted conversions. The full A14 addition
remains auxiliary/direct observer schema1 with native schema/policy1 unchanged,
observer capability fields1/1 and live-package switch policy2/reporting3.
C5 introduces no further format/capability/policy change. Full-series new files
are ordinary100644 source/tests; existing executable modes remain unchanged.
The reviewed older heads are checkpoints, not literal ancestors of the amended
feature; this source-changing successor requires its affected final review and
exact-head CI/native acceptance.

Complete source/provenance receipt:
`/tmp/session-archival-ci-43445868248/c5-commit-proof.json`, SHA256
`e567415e30e02a3dd35d1677451e8445ec4d9a20b57628d6c6016a97209279b1`,
contains exact base/head/tree/count, four-path hashes/raw blob+mode delta,
complete base-to-head diffstat/history and clean result. Retained refs are in
`c5-own-refs-before.txt` and were compared after mutation.

The exclusive index/amend window is released. All own effects are joined;
no push, pin update, build, VM/tagged rerun, CI action, claim, merge, deployment,
activation or live/session lifecycle action occurred. Root owns affected committed
General/Risk/Scope review and publication. Implementer1 retains C5 finding/fix
ownership and capacity after accepted delivery. Session remains open.


## D1 — source-owned maintenance preparation diagnostics

Accepted A24 implemented in the separate runtime worktree
`worktrees/2026-11-11-session-archival-failures/dev-workspace-diagnostics`, branch
`2026-11-11-session-archival-failures-maintenance-diagnostics`. Current session
and trusted binding matched; the retained implementer1 roster is Sol/xhigh,
workspace_write. Base/direct parent is exact merged
`eabb56a278bd8eb1759041467eaebfa6392ddcb2`. Final head is
`b8329e32f1132fd947f4a9c803bf44e3ed9ce481`, tree
`8f538c947869f736bf8c68ddd2f35067894d373c`. The complete range contains one normal
commit, `maintenance: identify failed preparation gates`, with six changed files
(+402/-28), all retaining mode100644:

- `portal/cmd/workspace-portal/maintenance_control.go`
- `portal/cmd/workspace-portal/maintenance_control_test.go`
- `portal/cmd/workspace-portal/maintenance_inventory_test.go`
- `portal/cmd/workspace-portal/maintenance_monitor_test.go`
- `test/workspace_host/live_switch_test.rb`
- `docs/workspace-updates.md`

The only production edit adds preparation-stage diagnostic reasons, exact
ownership-ambiguity classification and deterministic deduplicated blocker
categories. Unknown errors use the failed stage's fixed reason. No raw errors,
paths or peer identities enter Response.reason. Exact native child-ownership
ambiguity uses the architect-confirmed existing literal; decorated/native error
text remains on the native-proof fallback. inventoryUnavailable.Unwrap retains
the original cause: focused tests cover wrapped ProofError, cancellation,
deadline and original-cause identity. The original transport type remains
available to errors.As. No admission, inventory or recovery gate changed.

Quick proof in the declared eabb Nix development environment (Go1.26.6,
Ruby3.4.9), final frozen related batch joined0:

- `go -C portal test -mod=readonly ./cmd/workspace-portal -run
  'TestMaintenance|TestInventoryWaitsOnlyForTypedTransportLossWithExactSource'
  -count=1`: PASS10.132s.
- `ruby test/workspace_host/live_switch_test.rb -n
  '/test_reporting_|test_claim_profile_switch_keeps_ownership_and_recovers_forward|test_busy_switch_refuses_missing_malformed_or_incompatible_launch_evidence|test_failed_live_activation_retains_forward_target_and_retries_while_busy/'`:
  PASS6cases/111assertions,1.619s.
- Ruby syntax, Go formatting and `git diff --check`: PASS. Frozen six-file hashes
  were verified before/after the batch and again before staging/after commit.

The Go proof exercises actual target/source-capture/inventory/Create refusal
paths and no operation/active/startup publication on pre-creation refusal. It
covers a real exited-but-unwaited child for executable capture failure, real
monitor state plus a transitioning member and unknown loaded writer for mixed
categories, exact native child ambiguity and private-sentinel near matches.
Success remains prepared with its original stored preparation. A deterministic
filesystem publication failure proves that the already-written journal remains
a fence and the existing RecoverPointer path can complete publication.
The first targeted check compiled but found two fixture omissions (second
session lacked plan/state; creating member lacked retained instructions); only
fixtures were corrected. Its affected rerun passed0.458s. No successful suite
was repeated merely to capture logs.

The focused Ruby fixture uses the existing production policy/registration
predicates: policy1/reporting3 package-path change preserves the launch marker
and native selection, skips maintenance operations, and recovers forward after
an activation failure while busy. A policy2 target still requires maintenance.
Retained claim and incompatible/missing-marker refusal tests pass. These are
source/host-fixture proofs, not actual package activation or live-native proof.

Root applied the writing skill directly to the two new workspace-updates
paragraphs and accepted the finite reason inventory unchanged before the final
batch. Documentation describes maintained refusal and partial-persistence
semantics; this rollout's branch/artifact state stays in this record.

Full committed six-path SHA256/blob/mode inventory:
`/tmp/session-archival-d1-diagnostics/committed-files.json`, SHA256
`ac4b387e7b802215df35cb8c3c260e99734bbe312a8c9d8cd526df7c1098e3a4`.
Final quick log: `/tmp/session-archival-d1-diagnostics/final-quick.log`.
Exact whole patch: `/tmp/session-archival-d1-diagnostics/d1.patch`.
The manifest also records direct parent/tree/clean state and preserved primary
feature9678. No repository hook framework or hooksPath override is declared;
the actual common hook directory contains samples only. Commit used normal
Nix `git commit -F`, with exact owned staging and no bypass or common config edit.

Complete history is eabb plus one diagnostic commit; no obsolete fixup/pin
stream, migrations, new persisted formats, inputs, schema, markers or capability
changes. All tree changes are the six paths above. The unchanged contract keeps
live switch1/reporting3, maintenance schema2/policy2/held-completion1. D contains
no A14 observer feature. Primary runtime9678 remains exact and untouched;
config72cb/workspace35bd were not modified. Existing refs/receipts remain retained.
D may become a consumed source/recovery owner under A24; do not fold it into the
frozen9678 checkpoint or treat old-reader D as supported after A14 observer state.

Worktree/index are clean. The exclusive D1 source/index/commit window is released;
all setup/check/commit effects are terminal and joined (59727 failed targeted
fixture check;80852 affected PASS;2292 final PASS;27351 normal commit PASS).
No push, runtime build/CI/long check, claim, merge, deployment, retry, live-native
or session lifecycle action occurred. Root owns affected independent committed
review and any later publication/composition/activation. Implementer1 retains
D1 review fixes and has capacity after acceptance.
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-session-archival-failures/


## F6 — compose the A14 successor above retained diagnostic source D

Lead released F6 after D1 acceptance and R14's four lanes reported no findings.
The trusted current binding and saved implementer1 Sol/xhigh/workspace_write
roster matched. Fresh SSH fetch confirmed origin/master exact merged
`eabb56a278bd8eb1759041467eaebfa6392ddcb2` and published diagnostic D exact
`b8329e32f1132fd947f4a9c803bf44e3ed9ce481`. D's worktree/ref and temporary
compositions were not modified or used as mutable checkouts. No CI was watched.

The exact previously published/reviewed A14 head
`9678f71d44780d3c49130372e7944a770fc5e3b6` was retained atomically at new ref
`refs/checkpoints/2026-11-11-session-archival-failures/f6-reviewed-9678f71d`.
Original receipts and earlier refs remain intact. Ordinary Nix
`git rebase --onto b8329e32f1132fd947f4a9c803bf44e3ed9ce481 eabb56a278bd8eb1759041467eaebfa6392ddcb2`
replayed the one coherent A14 commit onto D. The only conflict was the existing
reporting helper in `test/workspace_host/live_switch_test.rb`; no production
conflict occurred. The clean documentation merge preserves both maintained
passages in `docs/workspace-updates.md`.

The test-only resolution retains D's actual-contract reporting helper and both
original D/A16 tests. The D diagnostic fixture explicitly declares policy1 on
both packages and extends the existing frozen LiveSwitchPolicyOne predecessor
predicate. It retains all 18 original assertions; the A16 actual-target2,
busy/unknown refusal, restart failure, forward recovery and 2-to-2 live assertions
are unchanged. No host production, policy, launch, contract, native guard or
public prose changed. The one new test comment explains the frozen predecessor
predicate; root was sent that exact wording before the final batch.

Final primary runtime head:
`635c6e6c8d894fee55d226245c94a2cf1537b8a4`, tree
`b4d67403a4032f3cacacc66177ff1b21d5662f2e`. Direct parent is exact D. Complete
ordered series from merged eabb has **two** logical commits, D then one coherent
A14 successor, 54files/+5809/-159. Successor range D..635 has
50files/+5408/-132. D is an independent potentially consumed source/recovery
owner, not an obsolete fixup; it was neither amended nor folded. The unpublished
successor is not literally descended from reviewed9678.

Ordered final stable patch IDs:

- eabb..b832 diagnostic D: `50fe97a5f41d964c20616deb8c8e49a124aa0159`
- b832..635 successor A14: `8664a904c2b388fddc7c84a5f9058541fa326ea2`

Original eabb..9678 A14 stable patch ID:
`c8f8e49cef093457eb064c9de49c95751908c1a7`. The complete retained range-diff
(`eabb..9678` versus `b832..635`) differs only in the Ruby test helper/base and
explicit policy1 fixture adaptation; the successor is therefore not advertised
as an identical whole-patch replay. The production A14 patch is preserved, with
D diagnostics added as its separately reviewed ancestor. Only overlapping files
are workspace-updates documentation and live-switch tests. All six final
635-versus9678 changed paths are precisely D's six-path set.

Independent whole-tree reconstruction starts from the exact9678 tree, overlays
D's four disjoint blobs, uses an independent ordinary three-way merge for docs,
and reconstructs the Ruby helper/test from the two retained original methods
plus the explicit policy1 adaptation. It produces tree
`b4d67403a4032f3cacacc66177ff1b21d5662f2e`, matching the staged and committed
trees exactly. D's production maintenance_control.go blob remains exact
`a6e49fa62b2d460c9f10d1652e36c7406b4e9e60`. Every one of 757 tracked input
hashes stayed unchanged through the final related batch and rebase continuation.

Focused known-quick proofs in the repository's Nix environment, all joined0:

- Exact interacting D/A16 cases, selected by
  `/test_reporting_three_diagnostic_switch|test_observer_policy_cutover/`:
  PASS2cases/44assertions0.518s; Ruby syntax/diff pass.
- `go -C portal test -mod=readonly ./cmd/workspace-portal -run
  'TestMaintenance|TestInventoryWaitsOnlyForTypedTransportLossWithExactSource|TestMonitorArchive|TestMonitorRequest|TestMonitorMCP|TestMonitorRecoveryOwner|TestExplicitThreadlessArchiveUsesRealObserverAndPreparedReceipt'
  -count=1`: PASS11.413s, covering the merged diagnostic/inventory and actual
  CLI/Ruby no-op/authority contract as well as monitor tool dispatch.
- Remaining retained Ruby reporting/package, claim, incompatible-marker and
  forward-recovery cases selected by
  `/test_reporting_package_|test_claim_profile_switch_keeps_ownership_and_recovers_forward|test_busy_switch_refuses_missing_malformed_or_incompatible_launch_evidence|test_failed_live_activation_retains_forward_target_and_retries_while_busy/`:
  PASS5cases/93assertions1.460s. The two already-passing interaction cases were
  not repeated.
- `go -C portal test -mod=readonly -tags live_switch_integration
  ./cmd/workspace-portal -run '^$'`: PASS0.034s, compilation only; no native
  tagged case executed. Working/staged diff checks passed.

Unchanged A14 core/web quick evidence is reused only within exact source/input
identity: complete portal/internal tree is
`93cbc9a95cfee0d0d217f581c5022b876f227cef` at both9678 and635. portal/go.mod,
go.sum, flake.nix, flake.lock, complete nix and libexec trees and the tagged
native fixture blob also match exactly; the manifest lists all object IDs.
This does not reuse9678 as exact635 package/CI/deployment proof. Root still owns
new affected independent final review and any later exact-head long proofs.

Full 54-path SHA256/blob/mode and history/input/ref inventory:
`/tmp/session-archival-f6-composition/final-manifest.json`, SHA256
`dc2431ec03afa1e18613648d8d01efa442c6bd196108a5a14ef2306d5f31d1c3`.
Full range-diff is `range-diff.txt`; complete/successor/from-reviewed patches,
independent composed overlap files and frozen all-input inventory are retained
in that directory. Final related quick log is `final-quick.log`; the separate
successful interaction command/result is retained in tool95441. No passing
check was rerun merely for logs.

No new migrations, formats or state/capability/protocol changes beyond reviewed
A14's auxiliary/direct observer schema1; native schema1/report replay and all
admission/fences remain unchanged. Final live policy2/reporting3 and observer
capabilities1/1 remain exact9678 contract bytes. D remains an old reader and is
not supported after first observer state. All supported source-owner/recovery
boundaries and original refs/receipts remain retained. No obsolete fixup,
superseded dependency pin or transitional migration stream remains.

Worktree/index are clean, no unmerged entries remain, and all command effects
are terminal/joined (fetch37509, interaction95441, final56105, ordinary rebase
continuation175264; the initial conflict exit was reconciled). The exclusive
primary-runtime source/index/rebase/commit window is released. No push,
force-push, build/long check, CI action, claim, activation, merge, live monitor,
private helper or session lifecycle action occurred. Root owns acceptance,
affected independent final review and publication. Implementer1 retains F6
finding/fix ownership and has capacity after acceptance.
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-session-archival-failures/


## C7 — completed D creation-job failure diagnosis only

Lead assigned bounded read-only diagnosis of D CI43472027059 attempt1,
creationjob132046092083 after F6 acceptance/R15. Current binding and saved
implementer1 roster matched. Used only the already downloaded
`/tmp/session-archival-ci-43472027059/complete.log` (4,147,193bytes, SHA256
`e5ddc83ce246cb7ae6a3ff5cb7227ec33ddb581d1e4f0bca310c0390a9c22bac`)
and existing run-after.json; no download, CI poll, retry or check execution.

Actual first causal error is log13372 at17:43:24.494Z:
`error: another dev-session command is changing 2026-11-13-before`.
The exact retained-session `dev-session start ... --as-is --no-attach --json`
started at13368/17:43:22.884Z; its exit1 is fatal at13375 in the subtest
"proxy-created roots regain source permission and actual managed clients".
This is the per-slug nonblocking SessionBusyError before lock yield, not a
proved maintenance/controller or native failure. The saved log does not identify
the competing lock holder. Nearby tracking-sync unit output is insufficient to
attribute ownership; no further owner census is needed for this bounded cause.

Source D session-creation.nix1327 calls raw user(start) after restoring/listening
source permission. Its existing sync_source helper198-233 already retries only
the exact same admission-refusal output/status1, within one20s ceiling with
bounded command timeout; every other failure is fatal. libexec/dev-session1000
acquires with_slug_lock before retained-start publication; with_host_lock8271-
8306 raises SessionBusyError before yield. This invocation has no initial goal,
so the later postprompt reacquisition is not on its path.

D and reviewed F6 share exact fixture blob
`37a6ac37041a0dcd0c84c5a36651e239b1974baa` and maintenance-worker blob
`880b9e0e56d580d0656c6757d6af1bdb692aba38`. Whole dev-session differs only in
reviewed A14 monitor/archive scopes; extracted start, with_host_lock,
with_slug_lock and observation-lock methods are byte-identical at D/F6. Their
SHA256 values respectively are:
`372dcca6e07bb299b6e07daef54574b49397ec28e4081c9686f1033b5c934c10`,
`a7a17c1a47ba01e6f50635064a752756eacd553198b04e1bafb989a7891720d1`,
`ee3b89be8732dbf7713cda6f5b390d4e4469dbf2dbb7ed9e1805fa4237ee45f7`,
`254870234331e921c736d614e047ff7d154de56e89ae74456946589e22e3c53c`.

Smallest proposed correction: reuse this fixture's bounded exact-admission
handling for the fixed retained-start argv as well as sync, preserving all later
same-thread/permission/team/client assertions. No Ruby production, controller,
lock policy, state or admission change is indicated. A seconds-scale extracted
helper regression can inject machine.execute/clock outcomes for busy->success,
nonexact/decorated/other-status failures, malformed results, timeout and deadline
exhaustion; it must prove no retry of any other failure. This is a proposed
fixture correction, not an authorized or executed change/test. D and F6 remain
frozen; root owns fixbrief/release/disposition before another expensive VM run.
No source/index/history/build/native/live/claim effects occurred. C7 diagnosis
is complete within that scope; implementer1 retains eventual bounded fix ownership.


### C7 primary-F fixture correction and committed quick proof

Root released this exact one-path correction after accepting the diagnosis.
Current/roster binding was reverified. Preserved reviewed635 atomically at
`refs/checkpoints/2026-11-11-session-archival-failures/c7-reviewed-635c6e6c`.
Only primary `nix/tests/session-creation.nix` changed. D b832 and its worktree/
refs, and D2 temporary compositions, remain untouched.

The existing sync_source helper is now session_source with two fixed argv
branches: unchanged sync, or retained start with `--as-is --no-attach --json`.
The failing actual start assignment now consumes this helper's JSON. Both old
sync callsites retain their original behavior. Only status1 with the exact
same-slug busy refusal (optionally one final newline) retries. The original
absolute20s budget, integer positive driver timeout, bounded diagnostics and
0.25s maximum sleeps remain. Every other outcome remains fatal. No controller,
worker, Ruby/Go production, deadline policy, lifecycle, native, authority, state,
schema or input selection changed. The adjacent comment describes exact
pre-admission refusal; no product documentation or public error changed.

Seconds checks used actual Nix-generated Python and its extracted helper/caller,
with a fake clock and machine.execute outcomes. The original real caller fails
on exact busy; the new caller retries and returns the same retained identity.
Both accepted newline shapes pass. Nine negatives (near-match, prefix, unknown,
non1, string/bool status, malformed output/result, timeout) fail after one attempt
without sleeping. Exhausted command time, success arriving at the deadline and
repeated exact contention remain bounded by the original20s ceiling. The old
sync argv and behavior also pass. Command construction is checked against the
actual fixed package/slug/flags. All221 VM Assert ASTs are unchanged, including
source-permission, root/thread, team, client and maintenance assertions.

`nix-instantiate --parse nix/tests/session-creation.nix` passed. Lightweight
Nix evaluation selects the real testScript but substitutes only explicit package
path strings; complete generated Python parses/compiles. This is syntax/caller
proof, not a derivation, VM or packaged/native acceptance claim. The first
syntax-only extractor omitted coreutils from its disposable standins; that
harness setup was corrected once without any application edit. Only blocked
Nix evaluation and the regression were then run, successfully. Scoped diff
check passed. No successful application check was repeated for log capture.

Final successful exact command batch used repository `nix develop`,
`nix-instantiate --eval --strict --json /tmp/session-archival-c7-fix/script-syntax.nix`,
`python3 /tmp/session-archival-c7-fix/regression.py` and scoped `git diff --check`.
Tool41263 joined0; result/source hash are in
`/tmp/session-archival-c7-fix/quick-after-harness-fix.log`. Initial blocked
extractor44853 joined1; its log is retained separately. No new harness/framework
was committed. Generated script, temporary regression and exact old fixture
remain in that directory for review.

Frozen source SHA256:
`a4fdeab13c0d17665fe01896f58a900eec8eb3152f3816645a524fe55c9615d9`.
Original fixture blob at D and635:
`37a6ac37041a0dcd0c84c5a36651e239b1974baa`; new blob:
`af30d9d1a2555ab7bbe208a8c07def45f9967822`, mode100644 unchanged.
Normal Nix `git commit --amend -F` staged exactly this one path, retaining all
required hooks and the complete A14 message with the fixture rationale added.
No common hook/config mutation or bypass occurred.

Final head `084dcd6d88ccd18e24561364732774805db1b178`, tree
`3b411ecb45784df2c8231d4a18f17c67affd1abe`. Direct parent remains fixed D
`b8329e32f1132fd947f4a9c803bf44e3ed9ce481`. Complete merged-eabb range remains
**two** logical commits: independent retained diagnostic source D, then one
coherent A14 successor. Full range55files/+5825/-173; D..084 range
51files/+5424/-146. Exact635..084 source delta contains only the fixture path;
all other F6 production/protocol/native/contract bytes and accepted proof scopes
remain unchanged. No obsolete fixup, new migration or format was introduced;
A14's original observer schema1 and policy2 cutover remain intact.

Full55-path hashes/blobs/modes, exact heads/tree/history and clean proof:
`/tmp/session-archival-c7-fix/final-manifest.json`, SHA256
`d2f8281301f722aea408dddde113e7ae500f8433a43d6f3bf5c63e80c3dca514`.
Exact one-path patch is `one-path.patch` there. Worktree/index are clean, all
effects are terminal/joined and the primary source/index/amend window is released.
No push, build, CI/VM run, claim or live/lifecycle action occurred. Original D
CI43472027059 remains failed; this correction is not evidence that D CI passed.
Root owns affected committed review and any separate exact-D packaged check with
the corrected fixture. Implementer1 retains C7 fixes and has capacity after
acceptance.
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-session-archival-failures/


## V2 — realized public configuration route (A27)

Root4804 exited2 before VM start because this actual installed driver rejects
A25/V1's `--test-script`. This is a verification-invocation error, not a D result.
V1's original receipt, input proofs, copied scripts and failed argv artifacts
remain unchanged; V2 supersedes only that proposed execution route.

Actual qxz wrapper `--help` passed0 (tool67438), confirming public `--config`.
Parser-only tool83087 passed0 using the exact unchanged installed main prefix
through parse_args, with actual module imports/argparse action; main, Driver and
VM construction were excluded. The installed module and its source match SHA256
`be3f8e47865a0fdb076380ea380da0d28e3496f990c051a31b525478bf6d6750`.
The effective argv contains the original wrapper's default config first and
appended copied config last; the real parser selects the copy. The actual
installed configuration loader accepts it without constructing a Driver.

Original10ywv configuration SHA256
`ea6ca98cd89de9f5096a04942d1d45b0916bafbbdbc69fad2e1b87bf15c3c88e`;
private `v2-driverConfiguration.json` SHA256
`49f89353f5ca9a33b7b1bc6760478373293a2970d5e0d255b8af3b71704f54dc`.
Its sole semantic/byte-literal change is test_script to the unchanged frozen
d165 corrected D script. Every other field is deep-equal: original VM/start
script, timeout3600, VLAN1, empty containers and disabled SSH backdoor. Complete
configuration diff, installed wrapper/Python/import identities and parser proof
are retained in the new receipt. All221 assertions/59 script store references
and V1 type/lint/helper receipts are retained by exact equality, without reruns.

Readonly `v2-final-receipt.json` SHA256
`b1519c253f600b9ef709e71da2f1730d580662e33645fab6496bb755ef0033b8`
in `/tmp/session-archival-d-creation-acceptance` records the full original qxz
public argv with appended `--config`, `-o`, `--junit-xml`; fresh empty cwd/output
are `v2-acceptance-run` and `v2-acceptance-output` there. No interactive, debug,
retained-state or timeout option is added. Root owns acceptance and one full VM
launch. No VM/build/CI/source/index/ref/claim/native/live mutation occurred;
all V2 effects are joined. D CI and original check remain failed/unverified.
Implementer1 retains harness fixes and has capacity after acceptance.


## C8 — pinned first-stream-open supersession diagnostic (A29)

Implementer2, 2026-11-13; first sufficient proof delivered for lead acceptance.
One disposable case passed against exact codex-web
`dd90fb4308ba85617ee2a4267cc835aa9a4f11ce`. The original
`test/sync_browser_contract_test.cjs` is an unchanged prefix of the private copy;
its existing `Clock`, `Source`, fixture and controlled-promise pattern are reused.
The sole diff appends 44 lines. Its unchanged relative import resolves through a
private symlink to the actual immutable Go module-cache `sync.js`, which imports
the actual `refresh.js`; no replacement controller or product code was authored.

Original inputs match the full pinned Git commit blobs byte-for-byte and remained
unchanged after the run:

| Input | SHA256 |
| --- | --- |
| `test/sync_browser_contract_test.cjs` | `2a7b3eba5b87a68a8a16d2044647ff72711ab9d2eea6382524b956108c7cbf3c` |
| `conversation/assets/sync.js` | `e6220cf481188b894cb1a5447939dd3db41e42857fd63fef2040a87e2e4083b6` |
| `conversation/assets/refresh.js` | `ba63d9299020d4b3d1a7c3733d37ec41c434806d0858dbdef88a74b168975241` |
| `flake.nix` | `2433d282f734888456cb7b8d4b5279710226aacdd593410a06138c0abb52df51` |
| `flake.lock` | `1fb6d5e068728cef2602ca43c2a667cee3df81fd7b3279bccb7978a56c1775af` |

Exact focused invocation (cwd `/tmp/session-archival-c8-sync-proof`):

```sh
timeout --kill-after=2s 25s nix shell --offline --inputs-from path:/home/aither/go/pkg/mod/github.com/aither64/codex-web@v0.0.0-20261108185431-dd90fb4308ba 'nixpkgs#nodejs' --option max-jobs 0 --option builders '' --command bash -c 'command -v node; node --version; exec node --test --test-name-pattern="^C8 first stream open supersedes a pending initial snapshot$" /tmp/session-archival-c8-sync-proof/test/sync_browser_contract_test.cjs'
```

The repository's locked nixpkgs `6aefcda9401be8acc2b74244fb3b37520ea1f0a8`
supplied Node `v24.19.0` at
`/nix/store/viadyk3hg56ib6vky4cm3sb2y3n305aw-nodejs-24.19.0/bin/node`.
Nix copied an input source from its cache; no source build ran. Invocation exit0,
10.966 seconds including environment resolution, selected exactly one case
(pass1/fail0); Node total174.226ms, case14.481ms. The command was bounded at25s
with2s kill-after and needed no retry. Tool47214 joined exit0.

Observed: initial snapshot pending before the first stream-open; its first
signal aborts immediately on open; exactly one replacement starts with a fresh
signal and the same callback-bound fixture identity (`c8-conversation`,
`c8-root`), retaining one event source. Nothing applies or publishes connected
while the replacement is pending. Resolving it with `CREATION_REPLY_C8` applies
once and publishes connected once. Resolving the old read afterward (deliberately
ignoring its abort) produces no stale apply, extra read or state change. Both
promises settle; explicit destroy closes the stream and leaves zero fake timers.

Private artifacts: `provenance.json`, `focused-case.diff`, `command.sh`, `run.log`,
`run-receipt.json`, `post-run.json` and the copied test under the cwd above.
Diff SHA256 `3adaa86df0698077ddfd1e98334141ad3f5391085813cd8cd948da76b7d7e78a`;
log SHA256 `75b393e090533ad158626582ea3851574aef25ba78bea6047a90c4379f498912`.

Limits: this proves the shipped controller's first-open supersession ordering
under the existing fixture, including its fixed read-callback identity. It does
not exercise HTTP identity resolution, browser import/hydration timing, CPU/load
attribution, or full D creation acceptance, and does not uniquely identify the
historical cancellation callback. D remains failed/unverified. No full suite,
VM retry, timeout change, model/native/live/build/CI action, source/pin/index/ref
change or other-session inspection occurred. All C8 commands are joined; lead
owns the next supported harness boundary and shared state update. C8 has no
remaining execution effects; idle capacity is available after this report.


## C9 — committed creation-hydration fixture and frozen exact-D adapter (A30)

Implementer2, 2026-11-13. Source and adapter are prepared for lead acceptance and
independent final review; no publication or long run was started.

Normal repository-Nix `git commit --amend -F` produced
`da64cf0999bd876836658c9f14b11f9f4b1ff60e`, tree
`a41577c3069b0c5001d1625e9b99e47348150265`, retaining direct parent D
`b8329e32f1132fd947f4a9c803bf44e3ed9ce481`. Old reviewed084 is preserved atomically
at `refs/checkpoints/2026-11-11-session-archival-failures/c9-reviewed-084dcd6d`.
The merged-eabb `eabb56a278bd8eb1759041467eaebfa6392ddcb2` range remains two
logical commits, D and one coherent A14 successor. Complete range58paths,
+6053/-187; D..head54paths,+5652/-160. C9 alone is three paths,+228/-14:
`test/creation_acceptance_browser.cjs`, its narrow
`test/creation_acceptance_browser_test.cjs`, and root-released one-line
`nix/workspace-portal.nix` checkPhase wiring. Existing modes remain100644;
the new test is100644. Worktree and index are clean. No hook framework or custom
hooksPath is declared; ordinary Git ran without a hook bypass or config change.

A30's receipt-root attribution was corrected with architect0: ready status has
no root field. Existing exact-slug public `/api/sessions/<slug>/details`
`currentTarget` supplies the independent root and retained targetId. The helper
requires exact slug, work location, unarchived/nonempty target, document root,
and successful200 browser GET snapshot root to agree. The passive observer is
armed before admission through the existing requestfinished boundary, independent
of diagnostic ring capacity. It retains early completed bodies and requires a
returned fixture marker in an actual visible `data-transcript-entry-key` row on
the canonical document. It neither refreshes the browser nor injects content.

One180s absolute deadline begins at usable entry and covers ready polling,
public identity, redirect/document and hydration. The original30s reply locator,
45s follow-up API loop and every scenario, initial-count/settings/notification/
root/reload check remain. `assert(record.threadId)` is replaced by the stronger
independent-target/document equality; the complete settings/followup functions
and reply-wait-through-scenarios/diagnostics tail are byte-identical apart from
final observer close. No additional readiness listeners are installed; observer
state closes on success/failure and browser teardown. Adjacent test comment is
the only useful technical documentation change; no product behavior/prerequisite
or product documentation changed.

Final frozen known-quick batch: repository `nix develop`, Node syntax for both
files, `nix-instantiate --parse nix/workspace-portal.nix`, the exact normal
checkPhase command `node --test ../test/creation_acceptance_browser_test.cjs`
from portal, and scoped diff check. All passed:23tests,7.397s overall/Node287ms;
tool88795 joined0. Cases exercise the actual imported helper and actual rendered
predicate, including early completion, abort/replacement, wrong root/URL/origin/
method, HTTP/JSON/body/entries failures, absent/hidden/uncorrelated rows, wrong
document, shared expiry with only25ms remaining, late promise completion after
closure, fork/plan markers and invalid public target. This is a focused fixture
proof, not a real browser/VM acceptance run. C8 was reused without repetition.

Source proof `/tmp/session-archival-c9-source/final-manifest.json` SHA256
`04c2ea2777cebb3c26931fed8b773b7141406d40a5406ca258f8ac7cce9963ed`
contains all58 changed-path hashes/blobs/modes and755 unchanged tree entries,
complete base/head history, patches and frozen check inputs. All production,
contracts, native selection, dependency selectors and other source paths equal084.
The sole Nix delta is test wiring. This does not establish new-head derivation or
built-output equality or permit artifact reuse. C9 adds no migration or input-pin
stream; original A14 separate observer schema1 and live switch policy2 are
byte-identical. No obsolete follow-up commit was added; existing lineage and
review inventory remain applicable.

Private adapter `/tmp/session-archival-c9-adapter/final-receipt.json` SHA256
`c1b74457a2be25191680d66db584f0eab463c0c2aa4ecb6da50171b3d6f60481`
binds the committed candidate and immutable D047 original browser
SHA256`46e6b8887ad86c0fd3f05d917178079dc82e4c6f81bba899864b2e0285c1fc04`.
The copied corrected helper equals the committed blob exactly,
SHA256`9c2f053cf885d497e7000dc6946cc16c7ee59568a8ffc8bb92e6caab56bebe97`,
mode0444. V1 C7 script is retained, with only a public copy_from_host plus guest
readability/mode/digest check after startup, and browser()'s helper argv changed
to `/tmp/session-archival-c9/creation_acceptance_browser.cjs`. Candidate Python
SHA256`02bb4d6979f980e95e6c1c1a883c8a1760df1057240ff69478f54c91c1ae2581`.
All221 original Assert ASTs and all58 other ordered store references are retained;
047 is the single explicitly named harness substitution. Full inverse-transform,
browser/script/config diffs, original hashes and actual installed copy interface
are recorded. D application/maintenance/native executable and contract hashes
were read and confirmed unchanged without invoking them.

The same original qxz driver, original10ywv configuration fields and zz6 VM are
retained. Copied config SHA256
`2f6a18d52f3c6d0b9cd457e31228cdecd9b78059f7a18285ed9b8bd3b4d9516d`
changes only test_script; global3600, all VM/native/application targets and flags
remain. Actual unchanged installed parser prefix and config loader accept the
public `--config COPY -o OUTPUT --junit-xml junit.xml` argv, with no Driver or VM
construction. Candidate script plus actual pinned prepend/type hints passed
compile, pinned ty0.0.38 and ruff0.15.14/F against the actual driver imports;
tool95162 joined0. The AST-extracted guest digest command also passed locally
with only its file path substituted. A disposable probe's wrong class import
and a generator's refusal to overwrite its own readonly helper were corrected
before final freeze; initial evidence is retained, with no product/input effect.

V1/V2/D originals and failed receipts remain unchanged. Candidate payloads and
receipt are readonly; fresh run/output directories are empty. Root owns final
committed review and any later run/publication decision. Original D CI and V2
remain failed historical results. All C9 tools are joined, source/index/amend
window is released and capacity is available; C9 follow-up fixes remain owned.
No VM/native/model/live/build/CI/push/pin/claim/deployment/lifecycle action ran.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-session-archival-failures/).


## S1 — two A32 reductions, committed for affected review

User “proceed” and the accepted A32 release authorize only removal of legacy
attestation and threadless archive authority handling. J2/H3 remain parked.
Current/environment binding and own live roster were verified: exact session,
both environment variables absent, implementer1 Sol/xhigh/workspace-write.

Primary runtime final is `734a85fea42c8f8276e6b037196c24cf8903cd12`, tree
`ccb7a1dc68750b5316e170fb5cefa9ca7ecc1ea5`. The complete series remains merged
`eabb56a278bd8eb1759041467eaebfa6392ddcb2` → consumed standalone diagnostic
`b8329e32f1132fd947f4a9c803bf44e3ed9ce481` → one coherent A14 successor.
D is unchanged. Original DA64 is atomically retained at
`refs/checkpoints/2026-11-11-session-archival-failures/s1-reviewed-da64cf09`;
all earlier refs and receipts remain. This is a substantive reduction, not a
patch-equivalent refresh. No migration was introduced. The unreleased legacy
auxiliary format/API is removed; original native schema-1 reads, exact replay,
report immutability and evidence-bound ResolveEffects remain. Direct observer
schema1/source and poll bindings, collisions, deliveries and rollback gates stay.
Live policy2/reporting3 and observer capability fields remain unchanged.

S1 changes 20 files, +152/-608 (456 lines removed net). Complete eabb..head is
58 files, +5580/-170. The source delta removes attest-local/auxiliary native
proofs and uses strict both-store require-idle from the actual threadless Ruby
archive caller under its admitted EX lock. Rooted browser/FD/receipt/replay
behavior stays. Existing rooted Ruby fixture coverage now uses a retained root.
The smaller real CLI→Ruby test covers no owned records and both malformed-store
refusals; owned observer observing/intent/running states also refuse without
mutation. Existing legacy resolution proof now checks local assessment before
and after the original evidence resolution. Lead applied and accepted the docs,
skill, MCP and CLI prose before the frozen batch.

One related Nix batch passed (session51396 joined0): full monitoroperation
6.487s; CLI `^TestMonitor(Request|Recovery|MCP|Archive|Threadless)` 1.197s;
`live_switch_integration` tagged compile-only 0.052s; focused seven Ruby cases,
78 assertions, 0.175s; Ruby production syntax and diff check clean. Exact commands
and output: `/tmp/session-archival-s1/quick.log`, SHA256
`1bbe1f006b9820493109140e0b1561ea51faa4cacc95aac909b92204ab839746`.
The retained-native MCP proof now requires actual status acknowledgement with
executionOwner:native and exact native identity; no legacy digest/action assertion.
Only compilation ran here; actual packaged/native acceptance remains unrun.
Unchanged host/maintenance/contract/input/creation and rooted-web source blobs
are recorded in the receipt; old verification retains its original exact scope.

Normal Nix amend finished0; no hook framework/active hook is declared or bypassed.
A message-wrap assertion did not stop its shell, so the first amend completed
at1e2a3bdc; its effects were reconciled from clean index/HEAD, then a normal
message-only wrap amend produced the final head with identical tree. No source
check was repeated for that correction. Final source/index are clean and frozen;
source/index window released. No push/build/VM/native/provider/CI/claim/live or
lifecycle action ran. Capacity available following acceptance, S1 fix ownership
retained; root owns independent affected review and any later publication.

Frozen 20-path map `/tmp/session-archival-s1/files.json` SHA256
`a1bbcf35da2c16765e7731308eec52b3aa241e6250624d65ea88db851f7a4eb7` matches
committed blobs and source bytes. `/tmp/session-archival-s1/receipt.json` SHA256
`1bd662c25969c08d62ba0aa747377b3bca5d5ec81928e7bd4da4f1bd6a373462` binds
head/tree/checkpoint/complete series/counts and unchanged input scope. Full
range-diff, final complete diff and exact S1 delta are adjacent private artifacts.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-session-archival-failures/).


## E1: one read-only own-monitor gate result and global authority limit

Root assigned E1 after finalprofile prepare42666 refused before Create with
`prepare-inventory-blocked:monitor-operation-unresolved`; its failedprepare/journal
absence and all earlier reports remain unchanged. Bound session/root, full matching
DEV_SESSION environment and saved implementer0 settings were verified before reads:
thread01a1cbe8-03b7-7342-aff7-7b55d56125e2, Sol/xhigh/workspace_write. Architect0
validated A34's ordinary selected-D public own-session path before any diagnostic
native/CLI request. No lead identity flags or lead-only monitor API were used.

ONE command ran: `dev-session archive-check
2026-11-11-session-archival-failures --as-is --json`, with optional Git locking
disabled. Owned command52467 joined0; actual CLI exit0, started
2026-11-13T22:58:16.923333Z, finished22:58:24.288639Z. Full receipt matches exact
workspace and slug: readyfalse, passedChecks5/totalChecks6, readyStage5, complete
blocker list1/1. No conversation/monitor blocker or own operation ID/reason is
returned; the only blocker category is coordination. No lifecycle/claim-release
permission follows from that unrelated blocker.

A34 explicitly confirmed these counters mean the conversation stage PASSed for
this invocation, not an earlier-stage skip: every stage runs, and only final
coordination added a blocker. This removes the earlier-stage and cap128 caveats
for this receipt. It does not prove that every internal proof branch ran or
reproduce maintenance's extra Inventory/IdentityFor/SameOwner gates/5s bound.
The global category remains unlocalized; this result neither identifies nor
excludes another session's blocker, and does not prove a foreign-session fault
or clear the historical prepare refusal. No own monitor ID is established as
needing resolution by this evidence. Global/root authority decisions remain lead-owned.

Once this sufficient result was known, all further operational reads stopped.
Known monitor JSON/status/producer histories were not scanned or expanded, and
the provided6d status/API was not duplicated. No peer records, root conversation,
transcripts, broad census or all-JSON filter was read. No internal monitor-lifecycle,
provider/helper mutation, prompt, observer/report write, CI query/poll, source/
index/default/build/deploy/lifecycle/resolve/retry occurred. All owned commands,
receipt parsing and routine architect messages are terminal/joined. E1 is ready
for acceptance; capacity available, retaining follow-up ownership within scope.

Full own archive receipt/stderr and command receipt are private under
`/tmp/session-archival-e1-monitor-evidence/`. Compact `finding.json` SHA256 is
`94ca61eed2865dbcd82bf1230865b6b29c10b0a2797020d9a6a6ba809dd44eb7`; it binds the immutable full receipt hash and exact invocation.
The first sufficient finding was reported promptly; architect's stage confirmation
adds interpretation without another request or probe. No new program, framework,
test, source package or automatic recovery is introduced by E1.


## E2: approved central metadata snapshot (no active-owner adjudication)

User explicitly approved “Inspect metadata only (Recommended)” for the A35
central namespace; approval reference call_93c44436b90d4008a5596fb34c7ad340.
Own binding/env matched; retained E1 saved settings were used without a roster
query. A35 and architect's exact selected-D bound/field/predicate clarification
were read before the ONE pass. Read interval2026-11-14T08:58:53.114506Z through
08:58:53.165670Z; command joined0 with no pending handle. It projected206 native
records into20 recorded owner tuples, with complete per-owner counts. Only regular
0600/bounded524288-byte native records were read; JSON/selected-metadata boundary
checks reported no observed error. This does not reproduce fullvalidateOperation
or unknown/excluded-field checks. Raw records and excluded contents were neither
saved nor printed; only the exact allowlisted projection/receipt were retained.

No duplicate native identity or Inventory.Unresolved conditional candidate was
found within recorded slug/root groups. The first later conditional
HasUnresolvedEffects candidate is `3b57fd25-6069-4e96-bda7-9eb1b2714b14`, recorded
owner `2026-10-30-oomd-abuse-policy`. Allowed terminal metadata is `{"outcome": "incomplete", "slot": "terminal", "stillRunningPresent": false}`,
resolution-present=false. Literal nonempty stillRunning is a boolean only; no
report text/meaning was read into the predicate. Current active/nonarchived session,
root/incarnation/socket applicability and full D validation are unproved. This
candidate is not adjudicated as the actual faileda1 cause or a foreign-session
fault, native liveness, timeout/load attribution, or safe-resolution target.

The first result was reported immediately before prose. No second store read,
owner lookup, index-status/details, native/provider/API/status call, peer project/
tracking/transcript/roster read, cross-session communication or mutation followed.
No repo/source/index/ref/pin/default/eval/build/CI/deploy/lifecycle action occurred.
The failedprepare/old reports and selected D/system observations remain unchanged.
All tools are terminal/joined; E2 is ready for acceptance with capacity available.
Root owns any further scoped identity proof, communication or supported action.

Private allowlisted artifacts: `/tmp/session-archival-e2-monitor-metadata/`
`projection.json`, `command.json`, `receipt.json`, `finding.json`. Finding SHA256
`e46bc626fdf69f07320f8db6d5d2076ca06602bab8117c671b53b2c70e74359d` binds the original projection/receipt. Snapshot is not atomic and
records can change after its interval; no freshness retry was performed.


## E3: one public current-owner metadata response; freshness remains unproved

Following E2 acceptance, lead released one dependent public index projection.
Current/session environment matched the bound slug/workspace. Selected D source
`server.go:113–124,1055–1071` exposes the allowed fields and cached timestamp;
`workspace-host:1689–1711,3825–3833` supplies the existing portal socket.
One finite `curl --unix-socket /run/user/1000/dev-workspaces/vpsfree-cz/portal.sock`
GET of `http://localhost/api/index-status?progress=1` ran
2026-11-14T09:06:30.748451+00:00–2026-11-14T09:06:30.779929+00:00, exit0/HTTP200.
The progress query returns the existing public cache without triggering another
refresh. Only approved owner-set fields and freshness/error flags were retained
in-process; no raw response was saved or printed, no central-store reread occurred.

All20 E2 recorded owner slugs were represented. The index reports
`2026-10-30-oomd-abuse-policy` nonarchived with no pending lifecycle and observation
identity `eee6ed1111d0ff077c08d2f180ecf0301f752f74b57356d27f4fac19208c1b01`,
matching E2 operation `3b57fd25-6069-4e96-bda7-9eb1b2714b14`'s incarnation.
Its saved E2 terminal metadata is incomplete/stillRunning=false/resolution=false,
so HasUnresolvedEffects remains a conditional source candidate. The index flags
are authoritative=true/loading=false/no warning/error, but generatedAt is
`2026-11-13T22:31:22.901819353Z` (38107.847s before this request).
That overnight cache cannot prove present-time applicability. No simple current
root, creation/terminal state or socket is exposed; full IdentityFor/SameOwner,
excluded-field validation, native proof and historical failed-prepare cause remain
unknown. This is not adjudicated as another session's fault or a resolution target.

First result was reported before this appendix. Operational STOP: no second
index/store read, refresh, details/roster/tracking/native/provider/monitor call,
communication or mutation. All source/discovery/HTTP commands joined; capacity
available after acceptance. Redacted receipts:
`/tmp/session-archival-e3-index-applicability/{index-projection,receipt,finding}.json`;
finding SHA256 `5608cb15d04f6d902e9189ff1b088ea03da4a106337ed4bd6b9d2f81fe8dc70c`. Root retains decisions and any further scope.


## E2 offline followup: all static effects candidates

The accepted E2 redacted206-record snapshot yields8 HasUnresolvedEffects matches
using the unchanged selected-field predicate, with no missing needed flags.
Only existing projection/command files were read; all dispositions were included
without current applicability filtering. Exact ID+owner-slug list is in
`/tmp/session-archival-e2-monitor-metadata/has-unresolved-effects-offline.json`
(SHA256 `cfae7c6336ab90454624b172077c4383cdad2d445949fc9757de84d9c83cbf28`).
The2026-11-14 08:58:53UTC snapshot predates the lead-supplied later3b57 resolution.
This establishes neither current blockers, historical a1 cause, original command
completion nor authority. No store/index/native/API/peer reread, communication or
mutation occurred. Count/list reported before this pointer; all tools joined0.


## E5: single approved metadata refresh

Binding/current environment and own roster were checked. One sanitized D-store
pass at2026-11-14T14:47:51.517421–14:47:51.576715UTC read208 records/20 recorded
owner tuples under the unchanged regular0600/524288-byte/selected-field boundary;
no observed read/field errors. Full D validation and atomic snapshot are not claimed.
No static Inventory flags appeared under recorded slug/root grouping and source
archived skip. Two HasUnresolvedEffects candidates remain: known
`a8c49117-6d98-4afd-9b5d-15afe4132919` (2026-10-30-oomd-abuse-policy), and new
`8045c95c-e2b8-410a-b80f-56b794a56230` (2026-11-13-osctld-start-recovery-errors).
All seven lead-named resolved old IDs remain present with resolution metadata
and no effects flag. Recorded owner tuples/conditional flags and comparisons are
retained only in `/tmp/session-archival-e5-monitor-metadata/{projection,command,receipt,finding}.json`;
finding SHA256 `1f54f3be36a9b5a3a4bc02dfdaac1fd0799b4d5cdf544e4660f07b2756b60335`.
First result was reported before this pointer. Current owner applicability, native
proof, original command completion, historical failure cause and action authority
remain unknown. E2 files unchanged; no second store read/index/API/native/peer
lookup/communication/mutation followed. All commands joined0; operational STOP.
