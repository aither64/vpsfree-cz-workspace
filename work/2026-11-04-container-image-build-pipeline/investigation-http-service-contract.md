# I10: compatible Go HTTP repository and run fallback

2026-11-05, implementer0; prior work accepted, capacity/session/env confirmed.
Unchanged workspace guidance/skills reused; vpsadminos AGENTS reread. Fixed
bare sources: O=`2951a632c4254a44747a8da326e3dde897eaa0e2` (vpsadminos),
C=`ca96c95a1fee04793468785d8323a759615b2b4e` (org configuration; no tracked
AGENTS/README/docs). Reuses I2/I9. Only this file written; no runtime/HTTP/
mount/build/test/CI/Git mutations or lifecycle actions. Production unverified.

## Wire contract: ordinary v1, no new client protocol

- Configured repository root R must serve `R/v1/INDEX.json`
  (O `osctl-repo/lib/osctl/repo/remote/repository.rb:7-9,28-29`). A workflow
  root such as `/runs/<id>` works without changing clients.
- INDEX contains `vendors:{default:<vendor>,<vendor>:<default variant>}` and
  `images:[{vendor,variant,arch,distribution,version,tags,image}]`, where
  `image` has format keys `tar` and/or `zfs` and conventional relative path
  values (O `docs/specifications/image-repository.md:34-50`;
  `base/image.rb:30-38`). Preserve complete variants/architectures/formats.
- Existing clients ignore those path **values** (`base/image.rb:3-12`). They
  reconstruct `R/v1/<vendor>/<variant>/<arch>/<dist>/<version>/` followed by
  `image-archive.tar` or `image-stream.tar` (`:42-67`). Go must resolve these
  canonical paths internally to object references; rewriting INDEX paths to
  object URLs or issuing redirects is insufficient.
- Default vendor/variant and tag lookup use JSON
  (`remote/index.rb:21-32`). Move claimed tags off baseline entries when adding
  replacements, matching `local/index.rb:34-44`; reject ambiguous resolution.
  Virtual default/tag routes can also preserve documented alias URLs without
  filesystem symlinks (`docs/specifications/image-repository.md:5-25`).

## Smallest safe run lookup

Persist a run manifest: pinned baseline catalog, expected changed tuples/
variants/formats/claimed aliases, verified candidate object receipts, and
status. At seal, synthesize one complete INDEX and canonical-path→object map.
Select by manifest ownership, **never** by candidate file existence:

1. Expected changed tuple or claimed alias: resolve only to that run's verified
   successful candidate object/format. Pending, failed, missing or corrupt
   candidate blocks ready and has **no** baseline fallback. A missing candidate
   format is absent/error, never borrowed from old baseline bytes.
2. Unchanged tuple: resolve to its pinned baseline object. Missing preexisting
   tuple is an explicit coverage/dependency error, not live fallback.
3. Unknown path/tuple: 404. Before successful I9 finalize, do not expose a ready
   run INDEX. Keep producer outcomes independent from full-CI readiness and
   preserve independently verified authorized publication successes.

The Go service opens the selected object and streams it at the canonical URL.
No overlayfs, hardlinks or per-run payload tree copies are needed. Frozen
catalogs/mappings are small; payloads can be shared immutable objects retained
while referenced. Verify all required suite tuple/tag resolutions before seal.

| Baseline backing | Semantics |
| --- | --- |
| Fetch current public canonical path on each miss | Simple best-effort live view; public tags/bytes/deletions can change mid-run, including same-version rebuilds. Cannot promise pinned/frozen CI. A broad miss fallback can also mask selected failures. |
| Pinned catalog mapped to retained immutable payload objects | Repeatable full-distro run view with no per-run copies. Requires stable object identity/hash and reference retention across public updates/GC; missing backing object is failure. |

A pinned INDEX pointing to current mutable `/srv/images/...` files is **not**
the second option. Existing writer overwrites tuple payloads and prunes them
(I2). Publisher/storage must establish immutable backing first; if only mutable
files exist, metadata alone cannot create that guarantee without retaining
their bytes. An immutable upstream URL is sufficient only if it truly retains
the pinned bytes. No full-copy storage mechanism is prescribed here.

## HTTP details that matter to existing clients

O downloader `direct.rb:36-51` requires GET 200; cached `cached.rb:174-245`
uses `If-Modified-Since` and accepts 200/304, retaining Last-Modified. ETag
alone is ignored. For frozen run URLs use stable Last-Modified; mutable public
URLs must never incorrectly return 304 after changed bytes/rollback, including
same-second replacement. Always returning 200 for mutable views is compatible.
Do not redirect to blob/upstream URLs: these downloader paths do not follow
redirects. Proxy or stream the object internally at the requested path.
`downloader/base.rb:25-27,93-143` requests identity encoding and verifies a
single valid Content-Length when present; do not emit CL with Transfer-Encoding
or transform archive bytes. I2 establishes no Range/If-Range/resume requirement
for these clients; external browser/client compatibility is not inventoried.
Cached downloader can serve old cached files on HTTP/network errors
(`cached.rb:31-79`): CI must use fresh run-scoped caches and ready preflight;
server-side errors alone cannot prevent a prepopulated stale cache being used.

## Integration/change surface and limits

Keep current HTTPS proxy front door (C
`cluster/org.vpsadminos/proxy/config.nix:100-104`); route internally to Go
instead of static `/srv/images` (C
`cluster/org.vpsadminos/int.images/config.nix:35-43`). Public
root service is optional; first release can serve only run paths. Public
generation swaps retain I2's old-index reader/same-tuple compatibility limits.
No osctl/osctld client changes are needed. Full CI needs only I9's common
default-run-URL/readiness wiring for all pools, preserving explicit repository
fixtures; no per-test changed-tuple dispatcher. SSH upload/control and object
publication remain separate from HTTP reads. Unresolved: immutable legacy
payload backing/retention, manifest/alias expansion and run-ready interface;
no live-public fallback may be labelled a pinned complete test view.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-04-container-image-build-pipeline/>.
