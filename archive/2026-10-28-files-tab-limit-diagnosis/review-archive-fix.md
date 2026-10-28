# Affected final review: archive repair corroboration

No Blocking or Important findings. Runtime `d0e4318c` may proceed to the planned
longer acceptance. This conclusion covers the committed runtime, not forthcoming
pins or deployment. Preserve [review.md](review.md),
[review-successor.md](review-successor.md) and
[review-deployment-baseline.md](review-deployment-baseline.md) for unchanged scope.

Retained `reviewer0`, native thread `01a182d1-b79b-7060-a7dc-f20d38733788`, was
reverified as ready, review-purpose, read-only, saved `gpt-6.1-sol` / `xhigh`.
`dev-session current` matched the trusted session binding; both environment
markers were absent. Read the mandatory skill and all four lane references;
independently covered general, architecture, scope and high-risk lifecycle/
compatibility concerns. No nested reviewer, application edit, long test, CI
monitoring, claim, merge, deployment or lifecycle operation was performed.

## Findings and scope

The user explicitly added investigation and correction of the archive failure
after the Files implementation. The separate archive commit is coherent with
that authorization. Its four-file delta (+301/-31) contains the classifier,
focused consumer tests, a three-line VM assertion improvement and the owning
recovery guide. It introduces no observation framework, dependency upgrade,
grace period, second send or new retry authority. Further diagnostic expansion
or optional hardening is unnecessary for this supported boundary.

The local consumer defect is supported by pinned codex-web `5830018`:
`codex/turn_state.go:36` reads passive metadata, then latest history, and
explicitly permits activity/history disagreement. The previous raw-history-only
classifier ignored that distinction. The original CI log confirms the generic
unsuccessful-repair path, but does not retain its raw status. Successful isolated,
VM and hosted probes are nonreproductions; they do not establish the original
native ordering or validate this fix. The final source, commit message and
design retain that limit. No historical `interrupted` or `failed` tuple is
asserted here.

## Correctness and boundaries

Inspected `archive_preparation.go:90–157`, the complete caller/polling path,
the pinned passive client implementation, focused regressions and VM/docs diff.
The runtime correctly owns this consumer decision and reuses the existing
client interface; no provider or public protocol change is needed.

`archiveRepairComplete` checks exact accepted/latest/thread identity before
activity. Only loaded `idle`, `active` and `systemError` are accepted. Known
`inProgress` remains pending; cold or unknown observations refuse. Every terminal
candidate gets a fresh passive metadata read after history, with exact ID/CWD
and loaded-status validation. Either valid active sample keeps preparation
pending. `completed` succeeds only with idle activity on both sides; an inactive
failed or interrupted result remains a failure, and `systemError` cannot prove
success. Unknown/cold states do not become pending merely because another sample
is active. This matches the final design matrix.

The caller retains the initial ID/CWD check, admission/message locks, execution
hold, stable delivery reconciliation/receipt, blocking-input check and two-second
polling interval. Locks do not survive polling. Active samples neither hand off
to archival nor create another repair delivery. Successful repair still runs the
ordinary independent archive-check. Cancellation and existing transport-error
handling remain unchanged. Refusal logs use existing observations and quoted
IDs/status/category, excluding message contents and tool arguments.

The 36-case matrix, invalid/cold/changed-identity cases, active-to-success and
active-to-genuine-failure sequences, one-send and active input/cancellation
regressions cover the changed consumer policy. Existing restart and lost-reply
tests retain delivery identity. These scripted observations test the permitted
client contract, not a deterministic native scheduler claim. The VM now captures
one operation snapshot and asserts both `running` and `lead_fixing_blockers`
before restart; phase alone previously allowed a failed preparation to pass.

## Whole history, persistence and consumer status

Reviewed current runtime range
`76c9ad4fbd877992464d2a7f2a1a2fe60db043b1..d0e4318cb1872feb69f3109f032870c310f14bdf`:

1. `dd445cb0627f93375f1378af6b59d30ef8b34875`: lazy Files browsing.
2. `d0e4318cb1872feb69f3109f032870c310f14bdf`: archive repair corroboration.

The complete initial `4a002f52` series is nine commits: `cc106266`, `e9153e61`,
`d0a9c5f6`, `fd9128a1`, `2beb55e2`, `2caa9419`, `76c9ad4f`, `dd445cb0`,
`d0e4318c`. Prior reports cover the unchanged seven deployed predecessors and
Files. Independently confirmed all 14 Files paths, workflow, native/dependency
files and runtime contract are unchanged by the fix. Current range is 18 files,
+1,441/-123. The two task commits have separate authorized purposes; no obsolete
approach, task fixup, transitional migration or repeated runtime input stream
remains. The temporary diagnostic `9270118f` is not a product ancestor; its
instrumentation/workflow stays outside delivery and is retained only as evidence.

**No database migrations.** This fix changes no preparation schema, lifecycle
journal, receipt, manifest, on-disk format or input/native selection. The full
inherited communication/reporting/drop persistence remains non-neutral and
supported under the earlier recovery conclusions. There is no unapplied
intermediate migration to consolidate.

Fresh read-only SSH proof confirms runtime feature at `d0e4318c`, remote master
at `76c9ad4f`, workspace feature at
`10344897ad051dd68ec3adfc21f949e7cc52ec47` and configuration feature at
`c8e9701614fdb3735d086f7591a29cdfe1e4d453`. Those unchanged consumer heads still
select `dd445cb0`; they are **not final pins for this runtime fix**. Their earlier
review remains limited to their exact heads. The future mechanical successors
need exact same-node graph and whole-history/consolidation proof before use;
this report does not review uncommitted or future selections.

## Remaining acceptance

Inspected quick-check receipts: focused archive tests 15.532s, command boundary
0.149s, Nix/embedded Python parse and whitespace checks passed. Reviewer used
read-only source/history/equivalence checks and did not rerun tests.

Next: targeted native/disposable archive acceptance, then the required final
pin/artifact/contract verification for the exact selected inputs. A passing
acceptance establishes the corrected contract while preserving uncertainty
about the historical CI tuple. No extra diagnostic campaign is requested.
Deploy-only direction remains in force: leave all branches unmerged, preserve
ordinary recovery and machine-ownership rules, and keep this session open.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-28-files-tab-limit-diagnosis/>
