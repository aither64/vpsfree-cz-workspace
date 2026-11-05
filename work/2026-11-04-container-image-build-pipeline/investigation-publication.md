# I2: public image repository publication

Investigation only, 2026-11-04. Owner: implementer2. No application edits,
builds, tests, CI, remote Git operations, deployment or commits performed.
Only this evidence file is written. Findings describe configured source behavior,
not an inspection of the live machine or current published filesystem.

## Source identity and boundary

Session identity verified by `dev-session current` and matching
`DEV_SESSION_SLUG=2026-11-04-container-image-build-pipeline` /
`DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz`.
Live same-session roster confirms implementer2 and architect0 addresses.

Read canonical bare repositories using explicit commit IDs; no peer worktrees
or fetch. References below use these abbreviations:

| Name | Repository/ref | Exact source |
| --- | --- | --- |
| C | vpsadminos-org-configuration origin/master | `ca96c95a1fee04793468785d8323a759615b2b4e` |
| O | vpsadminos origin/staging (origin/HEAD) | `2951a632c4254a44747a8da326e3dde897eaa0e2` |
| H | historical vpsadminos origin/master | `4658d40f8ca459194b578aa30b0f9bb344cd7ee2` |
| B | vpsfree-cz-configuration origin/master, producer evidence supplied by lead/I1 | `f4069909b55fbed907cb658f350ec6a59f97e05a` |

Initial consumer inspection used H before checking origin/HEAD. All current
consumer conclusions below were rechecked at O; H is only an old-client
comparison. C's `flake.lock` root `vpsadminos` input points through node
`vpsadminos_2` to `e2b2b9186de6e0aec66f87a0e4d16e86bc2d7854`, not O.
Therefore O is current source behavior, not proof of the host's deployed package.
C `flake.nix:7-9,21-23` selects staging for the `os-staging` channel.

Required workspace AGENTS and sessions, documentation, projects, verification,
git and agent-teams procedures were read. Documentation and handoff skills read.
At C, no tracked AGENTS, README or docs tree exists. O's AGENTS, README,
container-images/repositories and specifications/image-repository docs read.

## Host, URL and authority boundary

- C `cluster/org.vpsadminos/int.images/module.nix:3-19`: NixOS host
  `images.int.vpsadminos.org`, internal address `172.16.4.15`, nginx service.
- C `cluster/org.vpsadminos/int.images/config.nix:15-24,35-43`: imports base,
  container profile and fancyindex; allows proxy HTTP traffic and directly
  serves `/srv/images` at `images.vpsadminos.org` with directory indexing.
- C `cluster/org.vpsadminos/proxy/config.nix:100-104`: public hostname uses
  ACME and forced HTTPS, proxied to the internal nginx service.
- C `environments/base.nix:25,48`: SSH enabled and root accepts configured
  `admins ++ builders` keys. This proves broad configured root SSH authority;
  key contents were not read, so no claim about per-key options or which
  credential the running producer uses. Images config declares no dedicated
  upload user, forced receiver command, staging-only permission or promotion
  privilege separation.
- C contains no configured rsync, image-repository publisher, publication lock,
  retention job or `/srv/images/current` layout. `/srv/images` ownership/mode,
  actual symlinks, disk layout, receiver rsync installation and live processes
  are not established by these files. The inherited container profile does not
  establish a publication protocol.

I1's finalized [builder evidence](investigation-builder.md), read back by I2,
locates the actual producer at B
`cluster/cz.vpsfree/machines/build/config.nix:131-134`:
`postRun` invokes `rsync -av --delete -e <pinned-openssh>/bin/ssh` from
`/var/lib/vpsadminos-container-image-repository/vpsadminos/repository/` to
`images.int.vpsadminos.org:/srv/images/`. No remote username or identity flag
is given. Root-default systemd execution implies root's SSH configuration,
but destination username/credential overrides remain unverified. The builder's
guest inbound authorized key does not prove the outbound publisher identity.
Lead additionally checked pinned
vpsadminos `dd188397abe37d0bc33f4c5dfb3605206ce5e326`
`os/modules/services/misc/build-vpsadminos-container-image-repository/shared.nix:127-131`:
wrapper runs postRun and exits with buildRc. This is attributed peer evidence,
not a direct I2 read of B. The example rsync in O docs is not production proof.

Consequences of those producer flags: `-a` preserves symlinks and timestamps;
`--delete` removes destination paths absent from the source. No flags shown
provide a transaction over the whole tree or force INDEX last. Ordinary rsync
file replacement can prevent partial individual regular files, but copying
INDEX and its referenced artifacts/deletions remains a multi-file operation.
Actual runtime identity and any additional external serialization remain unknown.

## Repository layout and compatibility

O `osctl-repo/lib/osctl/repo/version.rb:4` has `SCHEMA = 1`.
`local/repository.rb:10-12` and `remote/repository.rb:7-9` append `v1` to
the configured root. Expected public paths, below `/srv/images`, are:

```text
v1/INDEX.json
v1/default -> <vendor>
v1/<vendor>/default -> <variant>
v1/<vendor>/<variant>/<arch>/<distribution>/<tag> -> <version>
v1/<vendor>/<variant>/<arch>/<distribution>/<version>/image-archive.tar
v1/<vendor>/<variant>/<arch>/<distribution>/<version>/image-stream.tar
```

O `docs/specifications/image-repository.md:5-16,34-51` describes this layout.
INDEX has `vendors` (default vendor and each vendor's default variant), and
`images` containing identity tuple, tags, and `image` format keys `tar`/`zfs`.
O `base/image.rb:30-38,42-67` is the implementation authority. Promotion must
preserve the complete tuple set, actual formats, default mapping and tags;
do not flatten variants or assume only one architecture/format. Defaults in
O `os/configs/image-repository.nix:11-14` are vendor `vpsadminos`, variant
`minimal`; NixOS impermanence is also represented (`:168-177,319-328`).

The critical consumer behavior is unchanged between H and O:

- O `remote/index.rb:21-32` resolves default vendor/variant and tags in JSON.
- O `base/image.rb:3-12` retains only the keys of each `image` map. It ignores
  the supplied pathname values. `:42-67` reconstructs canonical tuple paths;
  `remote/template.rb:5-8` joins them to the repository URL.
- O `downloader/direct.rb:36-50` makes separate index and artifact requests.
  Cached path also loads index then requests artifact (`cached.rb:95-121`).
  Neither request pins a server generation or uses the HTTP tag symlink.

Putting a generation path only in INDEX `image` values is incompatible with
these clients. An atomic `current` pointer swap produces a consistent tree
per path lookup, but does not bind the index response and the later image GET
to the same generation. Old tuple paths must remain readable in the newly
selected tree, or a client holding the old index can get 404.

## Existing atomicity, locking and retention

O local writer `local/repository.rb:24-60` copies payloads directly to canonical
filenames (`FileUtils.cp`, `:40-42`), updates tags by unlink/symlink
(`:44-56`), then saves the index. Same-version replacement first removes
dropped formats/tags (`:35-38,141-149`). Default symlinks also use unlink then
symlink (`:122-138`). These are not a repository transaction and concurrent
direct readers can encounter truncation, gaps or mixed state.

INDEX itself uses tempfile-and-rename: O `local/index.rb:70-76` calls
`libosctl/lib/libosctl/utils/file.rb:5-19`. The helper closes the new file then
renames it, without fsync. Local repository/index/CLI mutation paths have no
publication lock. Concurrent processes can read an old index and overwrite
each other's updates despite each final index rename being atomic. The helper
already has atomic symlink replacement (`utils/file.rb:22-29`), but the local
writer does not use it here.

Consumer cache locks (`remote/repository.rb:20-21`, `remote/template.rb:18-22`)
serialize local cache activity only. They provide no server-side exclusion.

O `os/configs/image-repository.nix:252-350` configures keep=4 for matched rolling
version families, including separate minimal/impermanence unstable NixOS.
`gc.rb:32-54,80-99` groups by vendor/variant/arch/distribution, applies the first
matching rule and removes earliest candidates beyond keep via `local rm`.
There is no age-based reader grace. `local/repository.rb:70-86` removes the
index entry first, then payloads/tags, without waiting for old-index readers.
`build.rb:80-88,217-234` runs GC before postBuild, logs failure status and
continues. Keep-count is not a publication rollback or reader retention policy.
Host C supplies no independent retention policy. Producer `--delete` carries
source disappearance to the public target.

## Minimal compatible promotion proposal

Proposal only; no implementation or accepted operational procedure:

1. Build/test independently, then upload a complete candidate into a unique
   nonpublic incoming directory on the images host. Never upload with delete
   against the served root. Give the builder authority to its staging area;
   reserve public replacement/retention for one server-side promoter. Preserve
   SSH key verification. A failed or incomplete candidate cannot change public
   state. A force command or dedicated receiver account can bound upload authority.
2. Promoter serializes publication and public pruning using one host-side lock.
   Validate candidate identity, JSON/defaults/tags, safe relative paths/symlink
   targets, and existence/formats of every referenced canonical payload before
   mutation. Preserve tar and zfs when declared, all variants and architectures.
3. Prepare the whole served tree on the same filesystem and atomically replace
   a serving pointer, retaining tuple paths needed by prior indexes in the new
   tree. Alternatively, atomically install each complete payload and symlink,
   then atomically publish INDEX last, with no public deletions during transfer.
   The first has the stronger whole-tree visibility property; neither pins two
   old-client HTTP requests to a generation. Do not mutate hardlinked old
   payloads in place. Keep a previous validated tree/index for rollback.
4. Separate public pruning from candidate synchronization. Define a reader-grace
   interval and rollback retention based on the supported operations; source
   keep=4 alone supplies neither. Do not immediately remove old referenced tuple
   paths or formats on promotion. An unbounded paused client cannot be protected
   by any finite grace, so document that boundary explicitly.
5. Preserve HTTP freshness for mutable URLs. Cached clients only use
   `If-Modified-Since` (`cached.rb:174-200,205-245`) and ignore ETags. Changed
   artifacts/index require advancing Last-Modified at HTTP date precision or
   server behavior that returns full changed content despite old IMS. Restoring
   old mtimes on rollback can otherwise make cached clients keep newer content.
6. Record source/input identity and validation result with the candidate, and
   selected/previous publication identities after success. Failed promotion
   leaves the old selection available; retry must not publish an incomplete tree.

This supports the existing URLs and mixed old/new v1 clients without requiring
all nodes to update. Same-version rebuilds can still supply complete newer bytes
after an older index; v1 has no immutable content identity or generation binding.
Exact snapshot identity across requests requires immutable unique tuple versions
or a separately designed consumer protocol change, not merely a pointer swap.

Current O downloader does not send Range/If-Range or resume byte offsets.
`downloader/base.rb:25-27,75-81` supplies identity encoding only; cached retries
the whole transaction (`cached.rb:95-121`), writes complete `.new` files then
renames (`:205-260`). Direct refuses retries after yielding any data
(`direct.rb:26-32,55-57`). Therefore there is no range-splicing requirement for
these entry points. Validators remain relevant to freshness, not byte-range
consistency. Arbitrary external HTTP clients were not traced.

## Verification and next dependency

Read-only checks: explicit-ref `git show`, `git grep`, `ls-tree`, symbolic
origin/HEAD resolution and bounded historical diffs. No builds or tests are
appropriate to this investigation package. No credential file contents read.
I1 supplied the exact producer path, pinned wrapper revision, root-default
execution and whole-tree format/variant preservation, incorporated above.
Live rsync identity, receiver state,
current directory contents, undeclared locks and deployed revisions remain
unverified. Lead owns acceptance and proposal synthesis; architect0 received
settled findings and corrected provenance directly.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-04-container-image-build-pipeline/>
