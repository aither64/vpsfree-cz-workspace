# Legacy recovery compaction correction

The lead owns this bounded maintenance fix; there is no managed team roster.
The initial plan served as the implementation brief. This records the final
design before independent review.

## Scope and interfaces

Keep `bin/compact-session-storage` as the site maintenance entry point. The
installed policy-3 runtime owns actual snapshot conversion and payload removal.
No runtime/schema/API change or configuration pin is required. The workspace
script is executed from its reviewed feature checkout against the selected
installed runtime; it is not installed in the system or user-profile package.
Deploying an unchanged aitherdev configuration would not deploy this script.

The existing SLUG.*.json exclusion is intentionally conservative for lifecycle
and unknown operation records. Exempt only the exact SLUG.creation.json regular,
nonsymlink file when its JSON object contains the matching slug and ready state.
Malformed JSON, wrong type, incomplete state and wrong slug remain blockers.
Do not remove/rewrite creation metadata to make cleanup proceed.

## Invariants and compatibility

Preserve transition-lock then creation-lock then session-lock ordering and the
selected installed-runtime check under transition admission. Preserve active
tracking, terminal lifecycle, pending tracking-sync and all other journal checks.
The runtime's existing schema-1/2 to schema-3 conversion pins/verifies retained
Git objects, writes committed recovery metadata before deletion and supports
resuming an interrupted conversion. Old schema-2 readers cannot restore the
compacted state; the installed policy-3 boundary already handles that contract.
No new migration is introduced. Uncommitted and ignored files in eligible old
snapshots are intentionally discarded under the user's all-session cleanup
authorization. Active/revived sessions remain untouched.

## Verification and delivery

Quick tests exercise ready records and preservation of incomplete/wrong/malformed
records, real pending lifecycle work and tracking sync. An existing runtime
legacy-capture fixture proves files/admin payload removal, retained Git-head
validation, schema conversion and idempotence. Export the previously unexported
storage-retention test suite through the workspace Nix checks using the selected
runtime source and declared Ruby/Git tools. No platform/service restart is needed.

After independent committed-branch review, run the new Nix check via a fresh
utility watcher, preview all archives, apply recovery-only cleanup using real
authority locks, and verify every retained head and remaining root. Measure
allocation deltas in the affected private directory and report any active or
unfinished exclusions explicitly. Merge the successful fix only after live
cleanup verification, as authorized by the user.
