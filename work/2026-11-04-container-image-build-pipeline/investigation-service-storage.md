# I11: service storage and public adoption

2026-11-05, implementer2; capacity/session/env binding confirmed; prior packets
accepted. Investigation/proposal only, only this file written; guidance and I0–I9
reused. Targeted canonical-bare source reads, no runtime/Git/lifecycle operations.
**V** = vpsadminos `2951a632c4254a44747a8da326e3dde897eaa0e2`;
**C** = org configuration `ca96c95a1fee04793468785d8323a759615b2b4e`.
Unqualified Ruby paths below use V `osctl-repo/lib/osctl/repo/`.

## Current facts and recommendation

C `cluster/org.vpsadminos/int.images/config.nix:35-43` serves `/srv/images`
through nginx/fancyindex; I1/I2 establish legacy whole-tree `rsync --delete`.
V `local/repository.rb:40-42,70-86` copies payloads in place and physically
unlinks removed images. Only INDEX replacement is atomic (`local/index.rb:70-76`).
No immutable shared-file ownership/catalog-reference service currently exists.

| Choice | Consequence for the user's no-copy/no-overlay/no-hardlink goal |
| --- | --- |
| Staging-only service; native public tree unchanged | References to public paths break when old add replaces bytes or GC unlinks files. Must copy/link/pin independent files, or intercept every public writer and physical GC. A creation lock alone is insufficient. |
| Same Go service owns public and run catalogs | One immutable ordinary file per uploaded format; multiple metadata views reference it. Run baseline is a metadata snapshot, not another payload tree. Public visibility can change independently of byte lifetime. |

Recommend the second, within the existing images host. This is new Go service
behavior, not wrapping native local operations unchanged. No ZFS controls, mounts,
overlay, hardlinks, deduplication, distributed registry or new database required.
Ordinary metadata files with atomic selection are sufficient in principle;
persistence/recovery details still need implementation design and verification.
## Minimal storage and lifetime contract

Store payloads under unique immutable local filenames, e.g. `files/<file-id>`;
file ID need not be a content address. Hashes prove uploaded bytes, not filenames.
Catalog records contain full tuple, declared tar/zfs formats -> file IDs, tags,
defaults and HTTP metadata. New content for the same tuple gets a new file ID.
Create run `<repository>/<run-id>/<attempt>` from one coherent public metadata
revision; unchanged images share file references. Only verified same-run receipts
can replace expected changed tuples. I9's finalize gate seals one immutable CI URL.

Commit complete files before catalog references become durable; keep incoming
uploads pending, never publicly visible. Serialize public updates/GC and run
creation/reference changes, with recoverable metadata commits. Reachability must
include public, unexpired live/sealed runs, pending commits and bounded rollback
roots. No racy scan may delete a file concurrently being referenced or opened.
Opening an HTTP file under a read pin/lock protects lookup-to-open; an opened
ordinary file can finish streaming even if its pathname is later unlinked.

**Logical public GC remains exactly I6:** same configured regexes/null selectors,
first matching rule, vendor/variant/arch/distribution groups, native catalog order
and keep counts (`os/configs/image-repository.nix:252-350`;
`os/modules/services/osctl/image-repository/gc.rb:32-54,80-99`). Native saved order
is tuple-string sort (`local/index.rb:70-75`, `base/image.rb:87-90`). Preserve
configured add/tag precedence (`local/index.rb:26-44`), defaults and native alias
removal behavior; no new tagged-image exemption or failed-build deletion signal.
Go must reproduce supported matcher semantics, not silently reinterpret Ruby regex.

GC removes the public record/aliases and makes its public URLs unavailable just
as today; a CI reference does **not** keep that version publicly listed/reachable.
Later physical cleanup deletes only files unreachable from every retained root.
Run leases/TTL, quotas and abandoned-run expiry bound staging lifetime; they do
not change public keep=4 or pin public visibility. Expired run URLs fail explicitly.
An active run retains its files despite public pruning/replacement; no copying
is required. Bounded rollback references are separate from logical public history.

## HTTP and native-tool compatibility

Keep `https://images.vpsadminos.org/v1/INDEX.json` and canonical tuple filenames,
including `image-archive.tar` and `image-stream.tar`. Run URLs add a prefix before
`v1`. V `base/image.rb:3-12,42-67` ignores INDEX path values and reconstructs these
paths: service must resolve requests through the selected catalog, not redirect
only JSON paths to a separate payload tree. Resolve default/tag URL aliases too.
Preserve format omissions, HTTP GET/HEAD/length and freshness behavior. Mutable
public URLs need safe advancing Last-Modified on replacement/rollback (I2);
sealed run URLs always resolve the same metadata/files. Public index and payload
GETs remain separate; existing logical pruning can still invalidate an older
index request. Retaining bytes privately does not promise public snapshot URLs.

Native `osctl-repo remote` and ordinary osctld clients remain v1 consumers.
Native `local init/add/rm/default` expect materialized directories/symlinks and
cannot directly own service metadata; `rm` would bypass retained references and
`add` violates immutable bytes. Keep them for offline fixture/export/import work,
or add an explicit service adapter. Existing GC runner shells out to local rm;
reuse its exact **policy**, not those destructive calls on managed files.

## Minimal migration and operational gaps

Exclude old rsync, all native local writers and destructive GC; inventory one
coherent INDEX, actual payloads/formats, defaults/tags and protected path bounds.
Adopt existing regular files **in place**: allocate file IDs mapping to their
legacy locations, forbid later in-place writes/unlinks, and reference them from
the initial public catalog. New uploads use the private files directory. This
avoids mandatory initial copies/moves; aliases are metadata, not shared symlinks.
Switch nginx's v1/alias routes to the service while preserving hostname/TLS and
paths; never static-fallback pruned paths to adopted legacy files. Keep service
storage outside direct static exposure. Existing open downloads must drain/finish.
Restore legacy service only through a reconciled materialization/export, never
by blindly re-enabling stale `rsync --delete`. Retain migration/file-map receipts.
Unknown: deployed files/revision, ownership, symlink anomalies, space/quotas,
service capacity/admission and route-switch behavior. Directory browsing currently
uses fancyindex; decide/test equivalent listings if retained. Shadow import and
old/new HTTP-client/GC/restart checks are future work, not performed here.
