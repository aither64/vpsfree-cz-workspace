# Run 3 verification-contract correction: affected final review packet

FINAL UPDATED PACKET: both source units committed/published/clean/quickchecked.
B d819ad044ef7fcc7bb4a111dc7676fe251383249 replaces b695 below after one
bounded test-only notification synchronization correction. Review may resume on
the exact final A c1f/B d819 set; no source mutation or native execution is active.
All earlier packet observations are retained, not a final disposition.

Session: `2026-10-22-codex-thread-retries`, workspace
`/home/aither/workspace/ai/vpsfree.cz`. Read [plan](plan.md), [state](state.md),
the accepted **Native direct-writer race disposition (run 3, accepted)** in
[design](design.md), and [native verification contract](native-verification.md).

## Requested review and boundary

Use the same retained independent reviewer0, Sol/xhigh/read_only, after a fresh
same-session roster check. HIGH risk because the changes alter what protocol
compatibility and managed concurrency verification certify. Review affected
general, architecture and risk/compatibility lanes under the mandatory review
skill and their full references. Prior full reviews, I3 review and
[native-status review](review-native-status.md) remain evidence for unchanged
production behavior and unchanged scope. No affected scope expansion is intended;
retain the prior scope conclusion, escalating any concrete new concern.

Required outcome: assess the committed final tests/docs and complete branch
histories, including consolidation, migration provenance, actual wrappers and
assertion integrity. No source edits, tests, builds, claims, activation,
integration, lifecycle actions or nested reviewers. This is final source review
before the next native campaign, not empirical native success or live readiness.

Lead's session-local `native-final-command.sh` is the prepared execution wrapper
for the next campaign. It has not run; `bash -n` passed. Inspect its two exact
commands against the native brief: explicit A and B/portal cwd, literal reviewed
head arguments, clean-source checks, full pinned binary hashes, separate full
JSON/stderr/exit/elapsed files and no retry. The watcher receives a new directory
and invokes this wrapper once rather than reconstructing its commands. This
orchestration file adds no product behavior.

## A: codex-web

- Worktree: `worktrees/2026-10-22-codex-thread-retries/codex-web`.
- Base: `ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5`.
- Prior reviewed head: `665fd35e3b29e07c29cd990c2067a3dba295fbf7`.
- Final head: `c1f415ad5602c23e6443cced73cb59267a796f05`.
- Final tree: `7e3523236dc4500b68a008398305b2290beabcc8`.
- Complete three-commit series: `df00fa36c820fc7a62ee5b8dd6e1745940ff8e15`
  client/context/predicate/docs; `6c828759440705c632e1902fa8309ccac446b050`
  optional UI; `c1f415ad5602c23e6443cced73cb59267a796f05` native fixture.
- Old-to-new delta only `codex/continuation_integration_test.go` and
  `docs/reference.md`; no product/API/schema changes. UI patch unchanged.
- Evidence: `a-native-run3-diagnosis.json`, retained reviewed665 bundle, full
  old/new ranges/diffs/range-diff, tree and checked-file hashes.
  Lead independently captured `a-run3-final-inventory.json`,
  `a-run3-final.diff`, `a-run3-delta.diff`, `a-run3-range-diff.txt` and confirmed
  the clean final tree, complete three-commit series and empty excluded-product
  delta. These are acceptance evidence, not independent review.
- Owner quick receipts: focused races 8.554s; delayed-history/wrong-text/
  absent/deadline-unknown fake tests and races 1.283s; native compile/list of
  both exact top-level names, format and whitespace pass. No native rerun.
- Metadata: `v0.0.0-20261022181203-c1f415ad5602`, Go sum
  `h1:2ziyC3nOv4CwKI1+axdbJA+fDEt3pPuZEY5eSyZ3HyM=`, unchanged go.mod sum
  `h1:SfoFFfEnXQusGm701eWJpCbrkwia5g1biF5KD9RIqr0=`, NAR
  `sha256-L7N67MpgM8DcQUcaI7Tx+oc693ZmmQm3mFqqO22LKiY=`.

Inspect bounded same-identity reconciliation with no new send/UUID and retained
submitting state on timeout. Exact accepted native receipt, one original
dispatch, one continuation input/provider request and cached same-ID continuation
must remain asserted. The direct-native probe must assert the exact pinned
implicit-steering observation and eventual same-turn history, without accepting
arbitrary success/refusal, replacing a turn or claiming managed exclusion.

## B: dev-workspace

### Final replacement after the review hold

**This block overrides B b695 labels below.** Final B
`d819ad044ef7fcc7bb4a111dc7676fe251383249`, tree
`6f1f05da60b09743d3716eb1a0adf794b90cf5a3`, same basebf6d. Complete final series:
`7262c24e4fbe9dbf8604e73590f9b5ef3d5dce99` core;
`b3c7187c6e26e269994433716a0ee719d0a7edf7` capability;
`aafaf4195d695c4641ce4f9342d56a1786f237c3` runtime/tests/docs;
`d819ad044ef7fcc7bb4a111dc7676fe251383249` sole A c1f pin, patch unchanged.
No production changes. New final inventories/full diffs/range-diff:
`b-run3-sync-final-inventory.json`, `b-run3-sync-final.diff`,
`b-run3-sync-delta.diff`, `b-run3-sync-range-diff.txt`. Prior b695 packet/range
and verified bundle are preserved. Lead independently confirmed clean exact
head/tree/base, four-commit series, identical lock graph and only one changed
file from b695 (`b-run3-sync-only.diff`).

The sole additional delta is `portal/internal/web/attention_browser_test.cjs`
(+7/-5). Prior731 fast CI failed in its unchanged baseline fixture at the
registration phase; archive/creation passed. Full metadata/logs are preserved:
`implementer1-731-ci-run.json`, `implementer1-731-ci-job119988219484.log`
(3332lines, SHA256e6eda7f03d1ae461139e2b2552250262b092b0d80433b13c31e097a1172fc2cf),
plus original failed-step log. No empirical WebCrypto-delay rootcause is claimed.
The fixture now awaits an explicit stageEntered Promise signaled after deferred
callback installation in permission/registration paths, with a two-second Node
test bound and synthetic phase diagnostic. All later Disable, storage and
unsubscribe assertions remain unchanged. Quick log
`implementer1-731-ci-synchronization-quick.log`: Node syntax PASS; exact failed
case PASS1/1 zero skips288.437639ms; full file PASS71/71 zero skips7954.224506ms.
Go source is identical to b695; its quick race/compile receipts remain applicable
to the same Go tree, not an exact-source Nix derivation reuse assertion.
Final owner receipt `implementer1-d819-final-receipt.json` and prepended
`implementer1-evidence.md` bind all artifact hashes, twelve-case inventory and
original bundles. Full731-to-d819 range diff is
`implementer1-731-to-d819.range-diff`. No more source work is pending.

### Preserved prior packet and substantive run3 package

- Worktree: `worktrees/2026-10-22-codex-thread-retries/dev-workspace`.
- Base: `bf6d4b0c49600c15e17fe71248807ef43424e932`.
- Prior reviewed head: `731bb742e07b4374cb8ee9a3a1379eb751cf44c4`.
- Final head: `b6956520331e4043f011fbb028521fefb48a7111`.
- Final tree: `b703a8e553fe897a896cd179ce82d83e7059f706`.
- Complete four-commit series: `7262c24e4fbe9dbf8604e73590f9b5ef3d5dce99`
  core unchanged; `b3c7187c6e26e269994433716a0ee719d0a7edf7` capability unchanged;
  `3b67b0e034a4c3408a98051715012a036723a78b` owning runtime/tests/docs;
  `b6956520331e4043f011fbb028521fefb48a7111` sole final A pin.
- No production/core/schema/API delta from reviewed731. Only native fixture,
  composed contention/wire tests, portal docs and five pin metadata files change.
  Lead independently captured `b-run3-final-inventory.json`, `b-run3-final.diff`,
  `b-run3-delta.diff`, `b-run3-range-diff.txt`, clean head/tree and complete series.
- Owner evidence: `implementer1-evidence.md`, verified reviewed731 bundle and
  full old/new range diff/tested-tree proof. Final quick log
  `implementer1-run3-final-quick.log`: contention/warm/status runtime races21.646s,
  core lock/recovery races4.836s, real resolver/roster races6.892s, secure
  construction/proxy races1.225s, native compile0.044s/list0.045s, pin/whitespace
  PASS. Twelve contention cases passed. No native rerun.
- Sole A selects `c1f415ad5602c23e6443cced73cb59267a796f05` across Go/Nix/vendor.
  Vendor NAR `sha256-CUZc7zj3bNr75y+7Rv3mPjEtVLT+iUNaLQ7EOH7RkQE=`;
  owner reports only vendor modules.txt pseudo-version differs. All superseded
  pin updates folded; original reviewed ranges preserved as evidence.

Required package: actual managed SendWithOptions/QueueWithPolicy versus real
Controller.Step under the authoritative fence; independent client connections;
root/member policy/MCP cases; manual wins => cancellation/supersession and zero
automatic start/steer; automatic owns fence => no manual native mutation until
receipt critical section ends, then ordinary explicit manual behavior; unknown
automatic result => exact ledger/pending uncertainty retained and manual held.
Keep barriers outside the fixture mutex and real ledger acceptance rather than
manufacturing authority. Existing cross-process/roster primitive tests remain.

Run3b fixture HTTPS URL correction must preserve product secure-origin checks
and has a quick fixture-construction regression. That regression also exposed
private transition.lock creation and inherited host provider-catalog isolation;
the fixture now uses a private0600 lock and absent private catalog, without
relaxing production checks. Lasting portal docs state the shared-fence boundary
and native implicit steering/settings limitation; lead exact copy applied.

## Failed evidence and residual gates

Original [run3](native-verification/run-3-731bb742/) and corrected-CWD
[run3b](native-verification/run-3b-731bb742/) are preserved. Four A665 native
subcases passed; the whole gate failed. B reconnect passed. B retry reached
genuine native acceptance/completion but failed constructing its portal fixture
with an HTTP base URL. Resolver/opt-out proof remained unexecuted. Do not turn
source/fake tests into native success or retroactively certify a new head.

Public native turn/start has no compare-and-start and can steer an active
regular turn/apply persistent settings. This accepted diagnostic records a
limitation outside the managed fence. Managed safety requires the separate
composed regression. No Codex patch, public CAS, new override or product fallback.

No migrations or new persisted formats. Retry schema1/capability1, provenance
epochs/UUID charges and native ledger3 remain unchanged; unmerged, unreleased,
undeployed and no external retry-state predecessor/consumer. Original ranges are
preserved as evidence; obsolete iteration pins must not remain in final series.

C/W remain frozen at W06ea83416387ebb16ecbb91acbf079cfdda1500b and
C01634abe06fc618fd3d55fea1df455dbe574cbf0 selecting old3f/A b6. They are not
ready for final composition. Only after final A/B native success, the C owner
will consolidate one pin commit per stream, preserve extension/unrelated edges,
and supply full graphs before package checks/build/deployment. No integration,
machine release or session closure is authorized by review.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/>
