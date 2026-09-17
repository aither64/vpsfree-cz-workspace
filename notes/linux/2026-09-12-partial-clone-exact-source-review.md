# Exact-source review in the partial Linux clone

`git --git-dir=repos/linux.git cat-file -t <commit>` can trigger an automatic
promisor fetch even though it looks like a local object query. During
`work/2026-09-12-nfs-cancellation`, a lookup for `563bbb35e8753e1bb34dad19ebeec8962ee3c1cd`
started indexing a 7.7-million-object pack. The clone has `blob:none` and
`remote.origin.promisor=true`; a missing commit can fetch far more history
than an exact-source review needs.

Check local availability with lazy fetching disabled where supported by the
installed Git (`GIT_NO_LAZY_FETCH=1`). For bounded read-only review, use
`gh api repos/vpsfreecz/linux/commits/<sha>` for commit/patch metadata and
`https://raw.githubusercontent.com/vpsfreecz/linux/<sha>/<path>` for exact
source files. Record the SHA. Avoid broad history walks just to read a file.

Stopped only the owned lookup and its child fetch/indexing processes, then
retrieved all requested NFS/NLM/SUNRPC/namespace files through the exact raw
URLs successfully. Do not interrupt another session's Git operations.

The installed Git accepted `--no-lazy-fetch` and spawned no fetch in a follow-up
check, but local object inspection itself still exceeded 30 seconds and was
stopped. Disabling lazy fetch prevents networking, not expensive local lookup;
use a timeout and prefer exact raw files for this review workflow.

Implementation follow-up found 64,132 pack files, mostly tiny promisor packs.
`git --git-dir=repos/linux.git multi-pack-index write` builds a shared lookup
index without deleting/repacking any objects or changing refs. After it finished,
the previously slow missing-object check completed in 0.24 seconds with lazy
fetch disabled. A normal blob-filtered fetch of the two required Linux branches
then completed successfully. Avoid listing every pack: summarize counts/sizes
instead. Rebuild this index when many separate promisor fetches slow lookups.

The first feature commits still spent several minutes using one CPU in Git,
with no child fetch process. Both completed successfully; do not assume a hung
commit solely from quiet output. The multi-pack index fixes lookup latency but
does not make all partial-clone tree/connectivity work cheap.
