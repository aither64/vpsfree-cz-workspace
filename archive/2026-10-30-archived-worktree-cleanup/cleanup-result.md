# Archived worktree cleanup result

The reviewed maintenance script completed recovery-only compaction successfully
(exit 0, 522.86 seconds) using the selected policy-3 runtime and registered
workspace authority locks. No runtime package or configuration deployment was
needed. The user separately authorized archiving
`2026-10-18-archive-live-acceptance`; its ordinary archive command completed.
The current cleanup initiative remains open.

Private recovery storage decreased from 26,417,045,504 to 2,813,952 allocated
bytes: **24.600 GiB reclaimed**. The 58 session directories contain 60 schema-3
inventories and 249 committed recovery records across 21 repositories. All 248
original inventory entries are unchanged; the additional record comes from the
explicitly authorized archive. Every saved commit exists and its retention ref
resolves to the exact recorded head. Runtime compaction verified the complete
saved Git trees before discarding files. No files/admin payloads or unexpected
files remain. Git branches and committed history were retained.

The final preview agrees with every apply result's remaining bytes. Repeatability
and partial-cleanup recovery passed in the focused suite; a second live apply was
unnecessary because only metadata remains and would repeat several minutes of
Git-object hashing. Compact metadata totals include directories outside the
per-inventory byte totals reported by the script.

267 terminal tracking entries were eligible. Nine historical entries remain
excluded by nonterminal lifecycle or unfinished-operation metadata; none has a
private recovery directory, so no worktree snapshot is left behind by those
exclusions. Their metadata was preserved.

Filesystem availability after cleanup was 122,468,999,168 bytes (about 114 GiB).
The whole-filesystem change includes concurrent activity and is not attributed
to this operation. Only the measured recovery-root delta above is task-owned.

Detailed untracked evidence: recovery-before.json, cleanup-apply.json,
cleanup-apply-result.json, cleanup-verification.json and cleanup-after-preview.json.
The compact Markdown result is the durable summary for later archive projection.

The Rust-client-generator recovery payload decreased from approximately
9.26 GiB to 32 KiB of inventory/record metadata (excluding its parent directory).
The workspace fix was fast-forward merged and pushed to remote master at
0548c2fbb6e7fa70bc99f0fb5511dae99f38410b after successful checks, independent
review and the live cleanup verification above.
