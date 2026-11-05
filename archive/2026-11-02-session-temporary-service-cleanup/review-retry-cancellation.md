# Final affected lifecycle retry-cancellation review

## Findings and disposition

No new Blocking, Important or Advisory source findings in the assigned general
and risk/compatibility lanes. Accept the completed cancellation correction at
`a5d47d2292bb57cb3dd031defbc1bed066e094d7`.

This clears this affected independent source-content gate. Native archive/restart
acceptance at the corrected source remains outstanding. The separate creation
diagnostic package is outside this immutable review and does not hold this source
conclusion. No publication, CI, deployment, integration or lifecycle permission
is granted, and historical first ambient-fixture effects are not certified.

## Identity and reviewed boundary

Same independent retained `reviewer0`, thread
`01a19ca7-8da1-7e63-852f-72d8332c553a`, purpose `review`,
`gpt-6.1-sol` / `xhigh` / `read_only`. Fresh live roster revision 27 confirmed
ready state and these exact saved settings. No override, fallback, nested agent
or substantive authorship.

Before accessing records, `dev-session current` returned exact bound slug
`2026-11-02-session-temporary-service-cleanup`; both environment markers matched
that slug and `/home/aither/workspace/ai/vpsfree.cz`, also matching the trusted
developer binding. Read mandatory-change-review and its general/risk references,
applicable runtime instructions and lifecycle procedures, the final packet section,
authoritative receipt, architect cancellation brief, committed source/diff, callers,
regressions and retained logs. Unchanged procedures and unaffected earlier review
conclusions are reused. Risk remains **High** because persisted automatic-retry
authority and uncertain submission recovery participate in lifecycle cancellation.

Repository/target: `git@github.com:aither64/dev-workspace.git`, `master`.
Complete final range:
`c2182254d29c4175c3e9fe4267e5a92dd1da6b79..a5d47d2292bb57cb3dd031defbc1bed066e094d7`.
Head tree: `ade07fb3b0ed122e11b1a7f50497c327ded75385`.
Immediate affected range:
`1e138a552c1cc355d0b05a9d47a25d8e391aa85c..a5d47d2292bb57cb3dd031defbc1bed066e094d7`.
Two paths, 169 insertions: one production assignment in store.go and 168 supporting
test lines. The immutable source below governs this review; subsequent mutable
creation-fixture edits are neither inspected nor accepted here.

## Correctness and recovery assessment

`portal/internal/turnretry/store.go:353-355` now clears ManagedTurn immediately
beside the existing Binding=nil inside CancelSession's existing per-thread
transaction. The compact authority validator correctly requires its binding
(`managed_turn.go:40-49`). Previously lifecycle cancellation could clear the binding
while retaining dependent compact authority, so the existing Save refused it.
The retained archive log shows the exact `cancel-retries`/`managed turn authority
is invalid` failure. The component red reproduces that cause through actual fold,
durable Save and Store.CancelSession, rather than only an in-memory Cancel call.

This is the smallest correction to that invalid pair. Generic State.Cancel stays
unchanged because ordinary managed-input cancellation need not revoke the loaded
binding. InvalidateSettings still owns epoch advancement. The change adds no
validator exception, repair reader, state field, schema, capability or new reset
mechanism. Existing lifecycle and scoped-provider consumers use the same Store API.

Cancellation, Binding=nil and ManagedTurn=nil reach the existing single atomic
Save together, after the existing receipt-only reconciliation. Save validates
before creating/replacing the file, then writes/fsyncs/renames the complete record.
The old validation failure did not publish the inconsistent pair. Later I/O errors
still propagate; after a post-rename failure, recovery must reload the complete
old/new record under existing locks. This review does not invent an all-session
transaction: already saved members stay canceled if a later member fails.

Pending's UUID, action, source failure, immutable settings snapshot and quota
reservation remain intact for uncertain submissions. Unknown/error/no backend
preserves uncertainty, saves cancellation and returns the existing blocker.
Other retained members are still canceled. Exact Accepted or positive
NeverSubmitted reconciliation keeps its existing outcome handling; neither path
calls Continue, creates another UUID, rebinds settings or restores compact authority.
Existing Cancel/Accepted rules for clearing nonuncertain Pending, consuming an
accepted result, recording its snapshot and anchoring a quota charge are retained.
Epoch, preferences and enrollment are not reset by the new assignment.

Reader hints cannot restore the discarded proof: their key includes Binding and
ManagedTurn (`workspacecodex/turn_retry_reader.go:37-40`). Existing restart and
recovery holds remain authoritative. Corrupt retained records still fail on load;
this is not a repair of arbitrary persisted state. Schema-1 records without
compact proof retain their normal supported save/upgrade path.

Reviewed regressions cover compact proof with no Pending and scheduled work;
uncertain no-backend/unknown cases and another member; a new Store instance after
restart with exact Accepted, NeverSubmitted or continued unknown outcome; repeat
cancellation without fresh dispatch, duplicate charge or authority resurrection.
They compare retained tuples and charges and exercise real temporary Store files.
Strict nil/mismatched-binding controls still reject Save and preserve valid
preimage bytes/loadability. The existing atomic-save boundary is unchanged;
another fault framework is not warranted for this assignment.

## Complete history, migrations and inputs

Independently inventoried complete five-commit history:

1. `19dd03b79a2997098934afafbe70c63b978c1ca7` — Resources/Team UI.
2. `f7add7cea8a836810d32688ef2d1cf4cc011af19` — registered service owner/lifecycle.
3. `5b4b711748343f4ffe88b96c50d88a9f98eeb04d` — dependent portal/package integration.
4. `2b21f9708fc8e0ad2ba3049f6ab893a1c06e0d3f` — capacity proof and this correction.
5. `a5d47d2292bb57cb3dd031defbc1bed066e094d7` — machine claims and prior closures.

First three commits are exact/range-diff equal. Fifth machine patch is `=` against
published 1e138. Fourth incorporates only the assigned two-path cancellation
delta relative to its immediate predecessor. The intervening pre-1e138
plan-delivery change is fixture-only alignment to compact proof, with explicit
UUID/text/epoch/digest assertions; unaffected accepted conclusions are reused.
Retained fixup `7a6c4412c4b3cfc2ed332eba8851b828455e3b36` and final head have
the exact same tested tree. Independently matched the saved two-path diff to the
committed delta. Earlier published/reviewed refs, sources and failed-CI evidence
remain retained. **No obsolete fixup, abandoned implementation or transitional
approach remains in the final series.**

**No database migrations.** This correction changes no schema/API/capability or
supported predecessor/recovery contract. Previously reviewed local service schema
1, production claim/retry schema-1 predecessors and direct feature schema-2
introductions retain their provenance. Snapshot/Pending/UUID/charge, policy,
submission and lifecycle formats remain unchanged. No transitional migration or
bulk state rewrite is introduced.

**No repeated dependency/generated input stream exists in the runtime series.**
The lock and full nine-node graph including root remain unchanged from c218.
Extension f8da, workspace48b and current downstream selections are outside this
delta and retain their prior scoped conclusions. Actual final pin consolidation,
source/NAR/full-graph equivalence and consuming-composition proof remain required;
no hypothetical pin or final readiness is accepted.

## Evidence and remaining limits

Independently hashed readable source
`/nix/store/hbbdlafi719g78bbf5bi9axzbdi0lnwb-source`:
`sha256-vKuR8PpzwgkBOjcTEr8mnA+2rAZO5g//yQpyWqGDPoU=`.
All 679 Git entries matched the committed submission, worktree and immutable
source bytes, symlink targets and executable modes, without extras/omissions.
Source/index were clean at that check, before the separately assigned diagnostic
edits. Lock SHA256 remains
`fa808c04beeaf2ea5d6dfb4b76b1bd6ff1a166e298771de3756a646a5294a955`;
actual metadata graph matches the lock. The ordinary active review root is intact.

Read and independently matched all three causal/focused/package log hashes to
`runtime-postreview-1e138a55/cancellation-remediation-receipt.json`. Six causal
cases fail on the original compact-authority error in 0.446 s. Focused four
top-level/16 leaf cases pass in 1.088 s; the full owning turnretry package reports
44 top-level/74 leaf cases passing in 7.837 s, no failures/skips. Formatting and
whitespace evidence passes. These are disposable Store/component checks, without
a native helper or socket.

Recorded 1e138 CI's fast/package pass is scoped to that older source. Its archive
VM reached the cancellation failure; it has not passed this corrected boundary
natively. Creation separately timed out waiting for compact turn/count before
the native page proof and did not log the mismatching values. This cancellation
fix is not evidence of that separate failure's cause or correction. Host skip is
not a pass. Exact corrected native/package and composed-input verification remain
outstanding; separate committed diagnostics need their own affected inspection.

The first historical ambient confirmation invocation still lacks retained exact
argv/stderr, so its branch and native effects remain unknown. This unrelated
disposable correction cannot retroactively establish no effects or close that
incident. No live audit, status request, cleanup or replay was performed or
requested here.

No reviewer tests, builds, GH/CI reads, live/native probes, lifecycle actions,
cleanup, source/Git/store mutations or nested agents were run. Read-only source,
history and hashing inspection plus this permitted report write only. Prior
reports and source roots remain unchanged. Subsequent check selection and
operational disposition remain with the lead under existing authorization.

Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/
