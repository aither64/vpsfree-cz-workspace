# I8: central run-scoped repository feasibility

2026-11-05, implementer2; prior I2 accepted, capacity confirmed; current session
and both environment bindings match. Investigation/proposal only; only this file
written. Reused workspace/repository guidance and accepted I0–I7/design evidence.
All new source reads use canonical bare vpsadminos **V =
`2951a632c4254a44747a8da326e3dde897eaa0e2`**; no builds/tests/live/Git mutations.

## Minimal fit and native tooling

Feasible as a small receiver/catalog wrapper on the existing images server,
with separate staging storage and HTTP prefix; no blobstore or database needed.
Suggested layout: `staging/<repository>/<run_id>/<attempt>/{incoming,views,current}`
plus small run/tuple receipts; serve `.../<run-key>/v1/...` through `current`.
Run identity must bind authorized repository/source and attempt, not branch name.
These directories, SSH commands and endpoints are proposed, not existing service.

Below paths are under V `osctl-repo/lib/osctl/repo/` unless fully qualified:

| Native operation | What the service can reuse / constraint |
| --- | --- |
| `local init` | `cli/repo.rb:6-10`, `local/repository.rb:10-21`: creates empty `v1/INDEX.json`; refuses existing index. No baseline clone/import operation. Seed the complete tree at filesystem level instead. |
| `local add --archive FILE --stream FILE --tag TAG ...tuple` | `cli/app.rb:34-46`, `cli/repo.rb:37-69`: accepts one/both formats and tuple, copies inputs into catalog. No build verification, receipt authentication or SSH service. Preserve actual format set, including stream-only images (I0). |
| `local default VENDOR [VARIANT]` | `cli/repo.rb:88-103`, `local/repository.rb:102-111,122-138`: updates aliases/index, requires target directory. Preserve baseline defaults; change only when planned targets exist. |
| `local rm ...tuple` | `cli/repo.rb:105-114`, `local/repository.rb:70-99`: saves index then unlinks payloads/tags. Wrapper must require exact stored version: lookup also accepts tags. Failed/missing builds are never removal requests. |

`local/index.rb:70-76` saves via tempfile+rename; no writer transaction lock.
`local/repository.rb:35-60,141-149` removes dropped formats/tags, directly copies
payloads with `FileUtils.cp`, changes aliases via unlink/symlink, then saves index.
Native add is neither crash-transactional nor safe on a concurrently served tree.

## Complete baseline and storage choice

Capture one complete public baseline, including INDEX, all payloads/formats,
variants/architectures and relative aliases. Unchanged distributions remain local
to this run; never point baseline entries at mutable live-public directories.
Serialize capture with public publisher/GC, or pin an immutable public generation
until capture completes. The legacy direct writer must participate/be disabled.

- **Full independent copy:** conservative fallback; new file inodes, portable
  semantics, potentially expensive space/time. Hold a stable source during copy.
- **Reflinks / filesystem snapshot+clone:** preferred only after filesystem proof;
  independent COW changes retain baseline bytes after public unlink/overwrite.
  Reflink copy alone does not make a changing multi-file source consistent.
- **Hardlinks:** plain `cp -al` plus native add is unsafe: direct copy mutates
  shared payload inode. Requires immutable source inodes and unlink/atomic-replace
  of every would-write payload before native add in an unserved working view;
  shared chmod/chown/mtime changes also leak. Directory/alias metadata must be
  private. Avoid initially; do not claim native add already breaks hardlinks.

Independent copies/CoW snapshots protect active-run bytes from public GC; after
capture, public keep=4 may prune normally. A snapshot/clone reference retains
underlying blocks until the run releases it. A symlink or an index-only copy
does not protect anything. If source generations are referenced instead of copied,
server leases must prevent physical reclamation while an active run depends on them.

## Per-image ingest, visibility and atomicity

Receive each verified candidate to unique incoming files, outside served views.
Restricted SSH admission validates run/source/tuple, test receipt and full-file
hashes/size/formats; forbid arbitrary paths/commands and public-write authority.
A failed/partial upload leaves both baseline and ready state untouched. Repeated
identical delivery may acknowledge the receipt; conflicting same-tuple bytes need
an explicit attempt policy. Store receipts as ordinary files under the run key.

Selected first flow, per architect/lead clarification: per-image build/test/export
and upload/result remain immediate; selected-build phase ends, then finalize/seal,
then full CI consumes **one immutable run URL**. No per-image consumer scheduler
or served generation per upload is needed. Keep the mutable run tree unserved.
One server writer applies successful candidates in configured order (I6), sets
defaults, validates catalog/files/aliases and required-workitem receipts, then
atomically exposes the sealed directory/manifest. Failed/unknown required changed
tuples cannot pass on seeded old bytes; the tuple/hash gate rejects that full-CI
input, without erasing unrelated verified outputs or making public eligibility
depend on unrelated failures. Later deliveries require another immutable attempt.

Native add/default/rm suffice inside the unserved tree; no source fix is required
for this flow. Do not publish a partially failed finalization; retain its inputs
for retry/reconstruction. If early rolling consumer views are later selected,
use private generations+selection, or small atomic payload/alias source fixes plus
serialization/recovery (`libosctl/lib/libosctl/utils/file.rb:22-29` already has
`replace_symlink`). File-atomic updates alone are not a catalog transaction.
I2 still applies: v1 ignores INDEX path values and reconstructs tuple URLs.
Keep the sealed URL immutable; public mutable URLs still need safe HTTP mtimes.

## Lifetime, public GC and remaining gaps

Server owns per-run byte/run-count admission quotas, incomplete-upload timeout,
finite TTL plus renewable producer/consumer leases, and bounded abandoned-run expiry.
Choose actual limits from capacity; reject expired runs explicitly, never fall back
to public bytes. Leases preserve reads while active; runner disappearance cannot
make storage immortal. Deleting a run removes only that run's copies/references.
These are staging lifetimes, not new public image GC rules: preserve I6's exact
configured matcher/order/keep counts; do not GC unchanged baseline out of active runs.
Public promotion uses eligible deltas against fresh public state, not the stale whole
run baseline, then existing full-catalog GC under the public writer lock (I2/I6).
Unknown: host filesystem/CoW support, available storage/quotas, HTTP reachability,
effective SSH identity, and trusted receipt issuer; no runtime feasibility asserted.
