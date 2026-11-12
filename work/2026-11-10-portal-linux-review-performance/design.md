# Stage 1 design and verification brief

Lead-owned design; no retained application team. Scope is the first staged
performance delivery described in plan.md. Core reader, web API, browser copy
and focused tests/docs are one cohesive implementation unit.

## Contract

Committed metadata reads raw tree differences with exact-content rename detection
(--find-renames=100%), never --numstat or similarity matching on the normal path.
Each file carries explicit pending line counts; totals count pending separately
from binary/limited files and suppress incomplete additions/deletions. On-demand
content computes exact hunks and counts, retaining per-file missing/oversized/
timeout behavior. No automatic fetch or maintenance, external diff, filters or
textconv; preserve bounded output, deadlines and admission.

History returns immediately after its commit page with summaryDeferred=true.
The browser requests a summary for the frozen snapshot separately and ignores
responses for replaced snapshots. Existing summary responses remain supported.
Comparisons return metadata without waiting for an automatic first preview;
selected content goes through the existing bounded file queue.

Use stable path-derived IDs for new metadata views. Old durable file links encode
an index/path hash based on 50% similarity rename results. Only when an explicitly
requested file ID is absent from normal metadata, try the old raw rename policy
under the existing deadline and no-fetch restrictions, verify membership, and
retain that legacy representation in a separate ephemeral snapshot. It needs no
persisted schema change; comparison descriptors and frozen commits stay intact.
Reject invalid IDs, and never interpret a stale link as another file. Legacy
similarity views may still hit their old deadline; normal browsing stays fast.

## Compatibility and recovery

Additive pending/count metadata and summary endpoint. New browser reads old
inline summaries; old browsers can show unavailable totals against the new
backend until refreshed. Saved review/manifest schemas are unchanged and older
packages can load their existing state. Staged/unstaged capture semantics stay
unchanged. New file IDs resolve on the new portal; rolling back retains comparison
revisions but cannot promise navigation to new-generation file IDs in old code.
No database migration, deployment ordering among daemons or system configuration.
Deployment, if requested later, selects the user-profile package atomically.

## Checks and acceptance

Metadata succeeds with missing historical blobs and never invokes a fetch;
unchanged rename maps without content. Edited rename stays add/delete in normal
mode and old links retain their original representation. Unknown counts never
appear as binary or zero; successful per-file diffs provide exact counts. Slow
summaries do not delay history, stale summary results do not replace fresh data,
and comparison listing does not preload a slow blob. Existing snapshots, archived
links, files with tabs/newlines, mode changes and malformed input remain covered.
Run targeted Go and browser tests in Nix, then independent review of committed
branch, then broader tests and CI. Benchmark the real 4163-file Linux pair through
the candidate reader with lazy fetching disabled and record timings, not universal
latency promises. Large-list pagination, editor virtualization and preparation
operations remain the separately proposed second stage.

## Follow-up: automatic counts (supersedes content-only counting)

One bounded numstat read enriches a copy of immutable metadata using the same
rename policy, paths, exact revisions and diff algorithm. Cache counted files
separately with the existing single-flight/LRU helper. Summary uses counted files;
a small snapshot-authorized counts endpoint returns IDs, counts and totals for
the comparison browser. Raw file metadata still returns independently.

The browser starts counts automatically after rendering a comparison, including
unopened and collapsed files. It ignores stale responses, resumes canceled reads
after suspend, and shows an explicit failure with retry if calculation fails.
Known aggregate counts survive limited/failed previews. Staged/unstaged snapshots
retain existing behavior. No persisted schema, native protocol or package contract
changes; assets ship together. Existing legacy rename links use their own cache.

Validate NUL-delimited rename/binary/unusual paths, immutable metadata, actual
overview totals, shared count cache, snapshot guards, browser automatic completion,
suspend/resume and stale/error responses. Quick tests precede committed review;
full packaged/browser checks follow. Verify public HTTPS and actual NFS/Linux
counts after guarded deployment; retain candidate GC root until selection.
