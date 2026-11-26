# D3 wording precedence

The accepted D3 contract supersedes the D2-specific instructions below. Current
shared interface wording is [ui-copy.md](ui-copy.md). Do not restore public phases,
preservation_chain labels, notifier/Nix text, Continue forms or browser-exit
cancellation. Prior sections remain historical evidence only. Owners provide
corrected one-chain guides/API errors for a final bounded lead wording pass.

## Current D3 storage guide and rejection wording

Lead read the complete D3 storage guide and current operation/chain rejection
strings, applied the writing skill directly, and approved the messages unchanged.
The guide is approved with three bounded replacements sent to I1: completion
means task success plus refreshed plans/snapshots; an unknown submission requires
inspection of existing tasks even if the receipt was lost; existing wire
parameters refer explicitly to node commands. No behavior or frozen runtime
input changes are requested. I1 owns applying these doc-only edits and committing.
Added CLI example/recursive/no-block sentences and empty dataset response example
received a final bounded main-agent pass and are approved unchanged; command
semantics remain the technical owner’s verified responsibility.
The one-chain/old-gap rejection, irreversible suffix, retained history, normal
reenable and deployment/recovery facts remain protected. This is wording review,
not independent technical review.

# Lead wording review (D2 historical, D3 current)

Reviewed the complete docs/storage/disable-backups.md, storage README insertion
and new API EN/CS locale entries with vpsfree-user-facing-writing and its EN/CS
guidance. Technical facts are settled by the owner. I1 retains all application
file edits and Git ownership; these are the final wording decisions.

## API labels

Preserve machine keys, choices and placeholders. Use these human-readable labels:

| Key | English | Czech |
| --- | --- | --- |
| backup_first | Back up existing snapshots first | Nejprve zálohovat existující snapshoty |
| phase | Phase | Fáze |
| phase.choices.preserving | Backing up snapshots | Zálohování snapshotů |
| phase.choices.cleaning | Removing primary snapshots | Odstraňování snapshotů z primárního úložiště |
| phase.choices.complete | Complete | Dokončeno |
| preservation_chain | Snapshot backup transaction chain | Transakční řetězec zálohování snapshotů |
| recursive | Include subdatasets | Včetně vnořených datasetů |
| transaction_chains.dataset.disable_backups | Disable backups | Vypnutí záloh |
| transaction_chains.dataset.preserve_for_disable | Back up snapshots before disabling backups | Zálohování snapshotů před vypnutím záloh |

The recursive wording applies to this dataset operation; preserve unrelated API
terminology if the generic key is already used in a different meaning, and use
its existing action-scoped localization convention rather than broad changes.

## Storage guide

The guide is approved with one plain-language replacement. Replace:

> Construction failure rolls back these changes. Once accepted, cleanup failure
> keeps this disable intent committed: it does not reconnect heads or restore plans.

with:

> If cleanup cannot be queued, these changes roll back. Once cleanup is accepted,
> a later failure does not reconnect heads or restore plans.

Keep the remainder, especially complete coverage, explicit request/response
wrappers, two-phase continuation, client exit, unknown outcome, retention,
irreversible partial deletion, receipt trust boundary and mixed-version/rollback
constraints. Commands, JSON and links remain unchanged.

## Storage README insertion

Use this final introductory paragraph (wrapping as needed):

> Administrators can [disable scheduled backups and remove source snapshots](disable-backups.md).
> By default, the action copies existing snapshots to every open backup destination
> before removing plans and source snapshots. Removing a plan on its own leaves
> existing snapshots in place.

This wording review does not constitute independent technical change review.
Owner must reconcile factual drift from any later implementation change before
final review. No completed public deliverable has been independently reviewed yet.

## I2 PHP guide

Lead read the complete docs/webui-backup-cleanup.md and I2 evidence after the
explicit Continue POST correction. The guide is approved unchanged under the
required user-facing writing workflow: it uses plain English and preserves
authorization, immutable scope, CSRF/session serialization, polling/continuation,
client exit, unknown outcome, partial failure, deployment constraint and recovery
facts. Existing commands, keys, routes and test paths remain unchanged. Browser
assertions are implementation references; execution evidence remains in the I2
packet and does not claim an unrun browser check passed. This is wording review,
not the mandatory independent technical review. I2 retains source/edit/commit ownership.

## I1 final error and scheduler text

Lead read every new Rejected message in Operations::Dataset::DisableBackups and
the final scheduler paragraph. Error strings are approved unchanged: plain admin
messages identify the blocked object/reason without filler. Preserve the literal
`retry-needed:` prefix, API identifiers, interpolation and rejection semantics.
No broad error-message or translation refactor is requested.

In the scheduler paragraph, replace only:

> Notification is bounded to one second; unavailable, rejected or timed
> out notification logs a diagnostic without changing the committed result.

with:

> Notification is bounded to one second. If it fails, is rejected or times out,
> the API logs a diagnostic and keeps the committed result.

The remaining scheduler facts are approved as supplied by the technical owner.
Owner retains factual verification of periodic refresh, post-lock guards and
actual socket/service identity. Lead did no duplicate source diagnosis or tests.

## Final target-availability paragraph

Lead read the new paragraph after preservation target selection. Use this small
clarification so "only metadata" cannot describe primary snapshot destruction:

> Target availability checks apply to nonempty sources with `backup_first:true`.
> With explicit opt-out or an empty source, cleanup changes only metadata on backup
> copies, so it can detach confirmed heads while a backup node is unavailable.
> Source safety checks, all-copy locks and pending-state checks still apply.

All facts match the technical owner's settled predicate. Apply after the active
source freeze, with owner retaining edits and checks. No new technical behavior.


## Current D3 PHP guide review

Lead read the complete corrected docs/webui-backup-cleanup.md. One-submit,
ordinary receipt, bounded polling/task link, browser-exit behavior, partial failure
and recovery prose is approved. Keep commands, identifiers and paths unchanged.
Replace the API-coverage paragraph's first two sentences with:

> The API independently validates authorization and the locked scope. With
> backup_first enabled, it requires complete existing or planned backup coverage
> and verifies transfers before deleting source snapshots. The UI offers no force
> option and never turns backup-first off automatically after an error.

Use inline code formatting around backup_first as in the owning guide. This
clarifies that explicit opt-out does not promise backup coverage. Keep the
existing deployment/scheduler constraint and storage-reference link. This is
wording review only; I2 retains all source edits and factual/test ownership.

The shared D3 backup-first help now explicitly says normal-transfer preservation
failure prevents cleanup, matching the accepted one-chain ordering. Owners use
the updated EN/CS row rather than adding phase-specific UI.


## Current D3 React SDK instructions

Lead read the full updated docs/design/HAVEAPI_CLIENT.md and changed packed-client
recipe/backup-cleanup dependency section after technical facts settled. Applied
vpsfree-user-facing-writing directly and approved unchanged: commands/flags,
peer/input/output types, links, lock verification, publication-before-merge and
Nix release limits remain intact. Owner retains exact dependency-graph proof and
source/check/commit responsibility; wording approval is not independent review.


## Final React source prose checkpoint

Lead read the complete changed passages in ActionContracts, Requirements,
Workflows, EvidenceMatrix and dated implementation record at9e6ed96, following
the prior full SDK-guide pass. Approved unchanged: scope, capability/task facts,
publication/Nix limits and unrun verification/KB claims remain accurate to the
owner packet. No source amendment or test repeat requested. This is main-agent
wording acceptance, not the independent technical review now dispatched.
