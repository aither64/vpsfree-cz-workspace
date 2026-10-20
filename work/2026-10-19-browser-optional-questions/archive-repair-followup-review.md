# Archive repair interruption follow-up review

No findings. **AR-1 is resolved** by runtime
`1395387ff02729256ba52cc7c9ded74397cbe1a6`.

Reviewer: `/root/optional_questions_review`, retaining independent
`gpt-6-astra` / `xhigh` settings. This is the requested affected-lane review of
general, architecture/repetition and risk/compatibility. The prior scope and
unchanged optional-question conclusions remain valid. This report supplements
`archive-repair-review.md`; it preserves that report's original evidence.

## Remediation assessment

`ArchiveCleanup#completed_journal` now owns the final operation reconstruction
shared by ordinary receipt discard, the candidate host reader and the locked
Runner verifier. Persisted callers first use the cleanup owner's strict
reader; reconstruction requires `completed`. The host admits this fallback
only when the primary journal is absent and the sidecar is schema 3. An
incomplete orphan receipt still refuses.

The Runner loads the receipt with the expected operation ID under creation and
session locks, compares the reconstructed journal with the host's expected
identity, requires moved tracking and all removals recorded, and revalidates
the sealed inventory, retained refs and archived tree. The host repeats its
identity checks while those locks are held. Existing exact-source,
runtime-contract, profile-token, selected-Codex and transition-lock checks
remain in force.

The ordinary candidate executor recognizes the completed receipt and calls
the existing `discard_completed!` path. It revalidates cleanup and tracking,
requires absent session runtime, and obtains fresh archived root/team proof
before unlinking a journal-less receipt. It does not manufacture a primary
journal, start another archive, or enter remaining checkout cleanup. Sharing
the projection with ordinary discard avoids a second reconstruction contract.
The legacy path retains its prior behavior.

The real-Git regression now forces the precise failure boundary after primary
journal deletion, verifies the completed receipt through the Runner, retries
ordinary cleanup, and compares live replacement file bytes, pointers, HEAD,
status and administration inode. The host regression separately checks
incomplete-receipt refusal and completed-receipt candidate dispatch without a
profile change. Documentation describes the new retry boundary.

## Exact final history and pins

Independently checked actual HEADs, clean project worktrees, merge bases,
complete commit series, changed-file inventories and final downstream diffs:

| Repository | Base | Final reviewed head |
| --- | --- | --- |
| codex-web | `c064ce09cfcea8d8af6bf676635a53cd823f772c` | `641907fb3afa2977050fe61331f9a3411c091245` |
| dev-workspace | `ea3f9d36397e8c2c846bd456e51385d73a3a358a` | `1395387ff02729256ba52cc7c9ded74397cbe1a6` |
| workspace | `f95413431bcff60fd087399a54aeba8a475837b6` | `0383f0bc057e81b6a96acef6ede63ab95e7522bc` |
| vpsfree-cz-configuration | `7ffa98a5761e001ed22b70fa24eecc21ff8c58ca` | `2127f78c6aac40b9bab9b4f1dc74cb732ffc42b6` |

The runtime retains two logical commits: unchanged optional-question
integration `1afca4ab`, then archive repair `1395387f` with this remediation
folded in. Codex-web remains one feature commit. Each downstream remains
one consolidated pin commit; no superseded update or obsolete implementation
iteration remains in the final ranges.

Workspace and configuration select the same runtime revision and narHash.
All codex-web locks remain at `641907fb`, matching the unchanged Go module
selection, and the workspace extension remains
`767dfd587e346168e1443e65ccdb67ce748f3fe3`. The final configuration message
correctly retains baseline `6ab3b48f` and its complete runtime changelog.
There is no retained intermediate pin requiring a consumer/release exception.

**No migrations.** No database, journal, sidecar or other persisted-format
migration was added; there is no migration lineage requiring preservation.

## Verification boundary

The lead reports passing quick checks: 15 host recovery cases with 251
assertions and two real-Git cases with 62 assertions. I inspected the committed
checks and did not execute tests, recovery, deployment, commits or source
changes. Only this review report was written; no nested agents were used.

The new source has not yet performed the actual archives or deployment.
Packaged verification and live recovery/acceptance remain necessary next
steps. No review finding prevents that verification from proceeding.
