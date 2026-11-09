# Independent final review after baseline refresh

## Findings

### Important R3: Stop becomes subject to the maintenance new-work fence

Commit: `387448e442b5fc37ec3d02b636dbe660cc086a77`.
Location: `portal/internal/workspacecodex/turn_retry.go:764`.
Lanes: general; risk and compatibility.

The refreshed baseline deliberately sends interruption through
`retryAdmissionUnfenced`: `cancelRetryAdmission` selects it for reason
`interrupted`. The new immediate-settlement implementation replaces that path
with `retryAdmission`, which calls `maintenance.RequireAdmission` before taking
the retry lock. An active, nonterminal schema-2 maintenance operation always
refuses that admission (`maintenance/admission.go:34`).

`maintenance.SuppressActive` still runs first, but only saves Stop revision and
continuation suppression; it does not finish the maintenance operation or send
a native interrupt (`maintenance/controller.go:49`). Consequently, while
maintenance is pausing or resuming, an otherwise authorized Stop can save its
suppression intent and then return “new work is held” before reaching
`c.Client.Interrupt`. Already running work continues. This is a concrete rebase
regression: the upstream maintenance commit explicitly exempted interruption
from this fence, and the web resolver also exempts the interrupt mutation from
its ordinary maintenance admission check (`web/server.go:3881`). Ordinary
package/runtime/roster admission remains required.

Use the existing unfenced retry-admission path for this interruption method,
preserving suppression-before-wait, durable cancellation, uncertain-attempt
refusal and exact pre/post turn settlement. Add a focused client regression with
an active maintenance operation and matching participant. Assert that Stop saves
suppression and reaches native interruption while Send/Queue/Activate remain
held. The current interruption scenarios have no maintenance record; the
maintenance admission test exercises only Send/Queue/Activate, so neither
detects this interaction.

No Blocking findings and no other Important findings identified. R3 needs a fix
or explicit recorded disposition before continuing under mandatory review.

## Scope, architecture and rebase assessment

The deliverable matches the approved delivery/storage design plus the user's
queue-recovery addition. SQLite evidence replaces aggregate snapshot admission
limits; native delivery receipts remain authoritative, and proof paging stays
in the automatic worker. The new ref scanner addresses an observed refusal
without changing claim schemas, logical identities or reservation policy. I
found no speculative framework or checks against a hostile local operator.

`turnretry` owns evidence persistence and migration; `workspacecodex` owns native
delivery/proof integration; the existing `MachineSource` owns source-ref
rechecks. The SQLite view preserves unloaded rows and rejects stale revisions.
The ref scan uses bounded chunks sized for the wanted line, requires a complete
exact record, ignores suffix lookalikes and oversized unrelated records, and
preserves loose-ref precedence. Its queue-grant test covers a packed inventory
larger than the old request bound; existing tests cover source changes and
read-only verification. No finding in `849bfdda`.

The rebase retains managed delivery timing, resumable native-history discovery,
and conservative admission for canceled capture. The stale snapshot-capacity
diagnostic was correctly removed with its eliminated error. Maintenance Stop
suppression survives, but its unfenced native interruption path does not, as R3
describes. Outside that defect, confirmed interruption still requires matching
pre/post turn identity and terminal native state; pending stop and turn turnover
do not acquire a handled watermark.

The prior R1/R2 remediations are present in the consolidated delivery commit.
`ErrMigrationPending` reaches locked recovery through cancellation and scheduler
entry points while passive idle reads fall back to that path. A completed marker
with a missing database still refuses. Held cold-delivery activation logs optional
binding failure and lets its recovery owner save execution permission; native
activation errors still propagate. The new application-level tests cover empty
and legacy interrupted cutover, retained uncertain UUIDs, cold root/member
acknowledgment and exact replay.

## Complete branch history and repeated-update conclusion

Reviewed the complete runtime series and final diff from merge base
`32a5e31bc32362b436ccc0cfc45b5d1b74f64cb6` to
`849bfdda6e1598b1e169e22bd741079941bb2d60`:

1. `c96503ea15eb571b3aa8cfbeee08ebbc7ed40a6b` — delivery/evidence storage,
   direct conversion, affected consumers, diagnostics, tests and documentation.
2. `387448e442b5fc37ec3d02b636dbe660cc086a77` — confirmed interruption settlement,
   with its tests and documentation.
3. `849bfdda6e1598b1e169e22bd741079941bb2d60` — streamed packed-ref source lookup,
   queue-admission regression and operational diagnosis.

The support changes in the first commit serve the same storage/admission
replacement. Interruption and packed-ref lookup remain independently reviewable
commits. No obsolete unmerged approach, unapplied intermediate migration,
fixup-only commit or abandoned compatibility layer remains. R3 should be folded
into the interruption commit rather than retained as a development fixup.

Companion complete ranges inspected:

- Workspace: `8aae9bd4af090260a92ec0296472fadce13c6cd7` to
  `bcee53dd6b0058b1c2f18ce402a40dd42309dfdf`, one final runtime-pin commit.
- Configuration: `1072f89f932ad570fb6d14007387d230549ccd14` to
  `2d050cfc26b23dce824e88ee61e83e2e929e7d0d`, one generated runtime-pin commit.

Each selects runtime `849bfdda` and the same content hash; extension, native
Codex, sibling inputs and follows relationships are preserved. There are no
repeated update streams in these final branch series. Earlier pin iterations
were dropped, not retained behind development-deployment justifications. Runtime
only promotes the already pinned SQLite version from indirect to direct use;
Codex and codex-web revisions do not change in its feature range. No further
history consolidation is required apart from folding the R3 remediation.

## Migration and compatibility conclusion

Inventory: one direct migration from supported JSON schemas 1/2 to the schema-3
identity/cutover marker and SQLite state, snapshots and shared settings. No
intermediate branch schema exists. The packet and state record that neither the
original nor refreshed feature migration has been merged, released, deployed or
externally consumed; only disposable fixtures have used it. No migrations occur
in the interruption/ref-scanner commits or the companion pin branches.

Migration lineage is sound. The backup precedes the incompatible marker, the
complete database precedes the ready marker, and locked recovery distinguishes
an interrupted conversion from later loss of a completed database. Original
scope, epochs, pending submission tuples, charges and valid proofs are retained.
No schema-existence guards accommodate discarded branch iterations.

Old strict readers reject the marker. Package compatibility requires exact
integer `turnRetryEvidenceSQLite: 1` while retaining predecessor capability
keys for the first forward upgrade. After conversion, software recovery must
use a compatible package; restoring stale JSON or selecting an old reader is
unsupported. Native submission ledgers, session policy and machine claim formats
are unchanged. The ref fix has no state migration or resource-identity change.

Inspected consumers include browser scheduling/idle hints, browser cancellation,
send/queue and cold team-recovery wrappers, lifecycle cancellation, package
compatibility checks and native creation-test readers. Companion workspace and
configuration pins select the same provider revision. The provider's owning
recovery/portal guides document the changed behavior and forward recovery;
coordination operations document the waiting-without-holder diagnosis. Those
documents remain discoverable from the repository documentation entry points.

## Evidence and limits

This was read-only source review across all four mandatory lanes: general,
architecture/repetition, scope/proportionality, and risk/compatibility. Overall
risk is high because of persisted-state conversion, uncertain delivery and
forward recovery. I read the packet, prior report, plan/design/state, rebase
comparison, repository instructions, applicable procedures, relevant source,
tests and documentation. Runtime and companion source worktrees were clean at
review start. This report is the only file written; no tests, builds, deployment,
live state changes, source edits or nested agents were performed.

The supplied quick-check logs show 25 machine-identity tests / 257 assertions
passing and focused Go packages passing in 18.136 s and 7.290 s. I inspected
those results without rerunning them. Earlier successful broad evidence remains
limited to its original revisions; refreshed packaged and deployment checks are
the lead's subsequent work. The missing maintenance-plus-interrupt regression
is the material coverage gap found here.

Reviewer: `/root/final_review_nov8`, fresh independent standalone fallback;
launcher-selected `gpt-6.1-sol` / `xhigh`. The threadless initiative has no valid
retained roster and the prior reviewer was unavailable in native listing, as
recorded in the assignment. No roster change was made. This review grants no
deployment or integration approval.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-06-portal-message-delivery/>.
