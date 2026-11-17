# Linux 6.12.118 port evidence

Owner: implementer1, package K. Design: [accepted brief](design.md).
Current phase: full replay, quick checks and verified topic publication complete.
Lead accepted source-preservation evidence subject to independent global final
review. Archive-byte hashing/source realization is R-owned; product builds/tests
remain after that review.
Process P was accepted by lead at OS `46cd1215337a36fbab5b796a956a6cd096ef3384`
and its skill/runbook were read in full before replay.

## Authority and recovery

The current versioned `os/packages/linux/available-kernels.nix` selects stable
6.12.117 at `764acbb0ca8c4b60ee5b98f89406b152e992b1d6`. The selected version's
config/features, package-level `bridge_stp_helper`, ZFS
`481845fca6ae3f61ca2262c1a5693a58ae364650` and
`zfs235-free-account.patch` are preserved by the design. The 6.12.109-only NFS
package patch does not apply. Unstable remains 6.18.49. No vpsadminos file or
index mutation is part of K.

The isolated Linux worktree is
`worktrees/2026-11-17-stable-kernel-update/linux`, on dated topic branch
`2026-11-17-stable-kernel-update`, initially exactly at the package pin. Its
working tree/index are clean. No Linux AGENTS.md or hook framework is present;
the canonical hooks directory contains sample hooks only, and no hooksPath is
configured. No configured rerere/rebase override was found. The permanent OS
[patch-series policy](../../worktrees/2026-11-17-stable-kernel-update/vpsadminos/docs/os/patch-series-policy.md)
and workspace team/commit rules apply.

Exact recovery ref, created with an all-zero expected prior value and verified:
`refs/heads/backup/2026-11-17-stable-kernel-update/6.12.117-before-port`
→ `764acbb0ca8c4b60ee5b98f89406b152e992b1d6`.

## Deliberate source acquisition

Every preflight Git source/object command uses `GIT_NO_LAZY_FETCH=1`.
Fresh kernel.org `ls-remote` returned:

| Release | Tag object | Peeled commit |
| --- | --- | --- |
| v6.12.117 | `3edfb92cd34f439b2e2878c3544a1683871d29ee` | `d3417611a3b40b7f04a29e558cebac2bf69889d7` |
| v6.12.118 | `c246b196b4fd25cf49df43b2803caab5f81df459` | `b869a5313cbfe7102873d3de318ddb68675146d0` |

The target was confirmed absent with lazy fetching disabled, then fetched from
`https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git` using:

```sh
GIT_NO_LAZY_FETCH=1 git -c gc.auto=0 -c fetch.writeCommitGraph=false fetch \
  --no-auto-maintenance --no-tags --no-write-fetch-head --filter=blob:none \
  --negotiation-tip=d3417611a3b40b7f04a29e558cebac2bf69889d7 \
  https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git \
  refs/tags/v6.12.118:refs/tags/2026-11-17-stable-kernel-update/upstream-v6.12.118
```

Fetch exit 0; local dated tag and peeled target match the fresh upstream values.
The server reported that filtering was unsupported. Negotiation from the known
old base still completed promptly; the fetch process is gone. No automatic
maintenance or broad ref fetch was invoked. The old base is an ancestor of both
the old packaged head and target base. Target Makefile reports 6.12.118; old
head Makefile reports 6.12.117. Upstream old-base..target-base contains 680
commits. No release/default/maintenance ref was promoted. The stale local
`origin/vpsadminos-6.12` remains at `9ccd5d6597a6ddbe5b44fb885ddf96e4dbc332dd`
(6.12.109), and did not select this update.

## Dynamic original inventory

Independently regenerated the entire old range with native Git:

```sh
git log --reverse --format='%H %s' "$old_base..$old_head"
git rev-list --count "$old_base..$old_head"
git rev-list --merges "$old_base..$old_head"
```

The resulting full list matches every row of the execution-specific
[original inventory in design.md](design.md#this-executions-original-patch-inventory):
50 commits, no merges, including generic backports without a product prefix.
The complete correspondence below was produced after process P acceptance and
replay. No migrations, deployment or integration occur.

Preflight path comparison found 113 downstream-changed paths and 709
upstream-changed paths, intersecting in seven: `fs/nfsd/nfsctl.c`,
`include/linux/memcontrol.h`, `include/linux/sunrpc/clnt.h`,
`mm/memcontrol.c`, `mm/shmem.c`, `mm/swapfile.c`, and `mm/vmscan.c`.
This predicts review focus; it does not predict all semantic conflicts.

Stable session portal:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-17-stable-kernel-update/>.
Lead owns shared state/portal and tracking commits; K reports this preflight
for the next state update without touching those shared files.

## Complete old-to-new correspondence

Native `git range-diff` reports `=` for every ordered pair below. Each row also
retains the exact author/name/email/date and complete message, with the same
per-commit path/status delta. All are unchanged transplants: no version bump,
new upstreamed disposition, omitted/extra commit or adaptation was needed.

| # | Old commit | New commit | Disposition / rationale |
| --- | --- | --- | --- |
| 1 | `3e5a54f0672c5ff95d52993c4f4b14d299d81bf0` | `5f080b7bee110d6aab945bfb65331b2549047386` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 2 | `82297e403d2036b455f4c2dc994423a835dcc047` | `f7a01466a953b5c7e140019405b0091fb4625c87` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 3 | `5efab7ae8e6885183f12f9d2d96ff62be9e5ea99` | `ac8e87592de403b0acc37127bd1816a707e44683` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 4 | `05b61d005e87f0c21d53cddc284f6687734f1c0d` | `6e7f40f3bbf5606592af7560be736205694f3b69` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 5 | `002fd814fdfaa232078fdbcfe1c2009199116316` | `0d7f6d7cefc9db13e2c2dfd9e37c11d5e2f01356` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 6 | `d5144f0f349b39e65d9d25fd86ac38a99d154bb8` | `ef467b5e173a641a66fd7c710bd991223f8490ef` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 7 | `cb230c6957349739e2f9360db856297f2f551dc5` | `0f8044674ecc9d2822097decc7468ab2c0f5e2f9` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 8 | `4e832e7e29a02fa05674bc789bf92d49ca943d61` | `d2355bc89099b2bce9561d57356f94b9425de0ab` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 9 | `cd19e0d6aefe3039ab76fc4da240b56fcda4e5ac` | `780a664ed03a11afe0de49be951db3d3730121fd` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 10 | `9ed81a1d5a228a39d12c573867890b4c0faf9513` | `0fd551e37adaadd8d6f6169e5c2d9195f0706bc2` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 11 | `8bcb24c31b1db48432e5c4f249d0737d26046c70` | `16c0e92435afa3664b9ceed4841dd631dd5dd70d` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 12 | `0174c680e26babf1c5db16bdc62be96a58751280` | `0c674741b67626cbdbd2acfafa3dd6c9305b75e7` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 13 | `802109c7a2767a2ee858a9c3911198dcf17bd2bb` | `8bd4d3983a00cc2031de872b1385b1f1d6df3ff7` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 14 | `7c3081b7c795b9e18f52df5b8906f296dd481f16` | `9485ae50424c15dfd4ff217ea6950585958f4ec3` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 15 | `ba8d5482aa1bee1689025ce454c582c8cd7b9566` | `c67899aa152fe4edeeef70da98caf9268d6c5fff` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 16 | `d18afd1d95067a440d04fe9e263328a83da50a26` | `af5c2c40ed53e9a7c8c5ec497efb3910ff00ff68` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 17 | `4cd22bd91cdb20ef37f6515d719574734b61d60e` | `372a9b2a4b7e74b47d7c5e1168fee6fc59f3247e` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 18 | `c1c6e00524e5db2ca52e39262fecfd34f145755f` | `8f7916f7e4cf526e55e91ed24f1046d158315c98` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 19 | `0a9bf91d91238dfb3aa545d017b8286cf748b3bc` | `07c1b2ef830616bd7ffc32a6f8156623f4c47b7a` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 20 | `ab3d74408297143884b1f55afd9ef550a712ab3f` | `ffda621248096628e7a2ddf58bb632b85536abc9` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 21 | `20133b5c8beb7b39d80dc7e2c2818692b8b8a1f5` | `40130614ed0589bb5cf273043d58865e9cb1fb23` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 22 | `38f4d1530b026a10f552b08352e541bc797b6c86` | `3f23248e13814872fbf8e0c88ffbb64cd7e15a56` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 23 | `93b74b767b800d6193251c19db1ccfc04738d319` | `5f033fc8e921c1d1ab1f839797f36f6c4d9c8a96` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 24 | `a82a0174bc0671d4ab77e067fbb86e14df101640` | `71e607b05441f3bd4e9c29fb437303bf95bcb341` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 25 | `99de4472d8189d311ee6ada4b440abd64d4d2df7` | `25c8debcb7defc6ddea69d911ba64859de1f588d` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 26 | `d91a8efe6d62e8f95c02903f0677928e94f18e54` | `e07e5e3429e42ed472fd84fea9341fe730ee4d8e` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 27 | `eea799b303f5308c398896d40b69b1619c607ab2` | `043be1a4e6a5db09db24d23548478b0b18288bf8` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 28 | `b2645b594e6fe7844c00b282f7947f21714b4027` | `3040962882c0bf79ff6530949861e391026577c6` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 29 | `57c08d059697ba740923b3c2dbab2de7463e0ff9` | `e716c3af2ed2428b6f3fadd17fa9af2b090fef86` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 30 | `9102ae0d8b574724dc24ae6c5433f956b9361a5e` | `4043312ea3e3c1fcabc76bb0e8135ec0a8e3a0e6` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 31 | `23c7f07516b2302970ef8f370df1b3c9160c8442` | `109befbd4e01ce3b826b7ebdab7c20ee5111f731` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 32 | `93fdd27d765f41a5080ee3192ef1eaf9cfcb99bb` | `591e202d529f227721edf00cf1c9d68b18863cfb` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 33 | `90827283b536264a5865ee67082daa69c9875b0f` | `075f9c0e950d21f31fce89bce5b09c51d42333fe` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 34 | `05797039c77bad208dfbde132fc71dff021f88b5` | `365f64c9bee03e90a401cd66b75765f55ec96321` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 35 | `657977908b2fb9f7976f451554c8994436e282fc` | `620355cacc76691afe84abbba0a09b58132f0341` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 36 | `0dbe29eee0ec03632ca03453958db6d434bdca53` | `fca3ce37aa081fcd75261f4624ed68e03f87c4d5` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 37 | `ef969339798fd90eba22f0186d469524e5b05c3c` | `74401186b85b5f0693e2b6550e1b7e80c6f6a5ce` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 38 | `22614c48017b882d222d5ff67d2d0636114f8c23` | `64ad42c9eb28f799d722971deffe556c94f9ea08` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 39 | `8176f94a65e00301d0d1eb66ae341d08f7d94733` | `030eb5b9cdb209a3245634d600bd59a764ad00c4` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 40 | `4e710587c301b6ee4a1c36e270decbebd5a8d0b8` | `2c300d9249a680e8b8d411cc9f945b6cad45ff80` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 41 | `9c2e5c52772086d057825f3f80a066337c1c276c` | `6c90b3ce59022436d0084a0964605183c60c562b` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 42 | `a82668abba10764e043cb938daf21775f7cd70a8` | `fc22ae5fbafd09722a723e6f258d0c6c33c87002` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 43 | `5fb54ae2dd75d0308c9ecefad17bdb8b7624c457` | `3ad5c50bc03d76ff5edac830256bb32bc274c4e8` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 44 | `28d178a9995d6919eeed7d58127a06b4bb0344ba` | `91d1dcc40dddd54ccb572fc9a69bcaa4f6968839` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 45 | `274f0a3c23a26746cb9f52aeac0e0b95a7088fc6` | `cb41a34072ca1433640fd72906d573a6be8c9468` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 46 | `2dfe7e7bd04c643df28360e11d402ecf169f057f` | `179bc48e7d9d23dcc8b1b8a776e28df75fdaf904` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 47 | `79efe5a11ae82179f84a351c603434df866ac97b` | `b82822cf9c89c0c480e05fd8899bcee3d89ec825` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 48 | `5e383c2411cbd1b22ec0073ad4639a628b48de02` | `30debdf77eff185338e2f91661af661b578b6970` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 49 | `02beaa9040c47f489991bac14c0bdc00b7a737c9` | `c1a4905a610d408150cb1f4a6d5ff34f4bbcc1f2` | Unchanged; native range-diff `=`, metadata/path delta equal |
| 50 | `764acbb0ca8c4b60ee5b98f89406b152e992b1d6` | `3bba27296b6f4f4a2b1568d65cea6037368f229b` | Unchanged; native range-diff `=`, metadata/path delta equal |

## Replay result and demonstrated process correction

Final topic head: `3bba27296b6f4f4a2b1568d65cea6037368f229b`, based on upstream
`b869a5313cbfe7102873d3de318ddb68675146d0`. There are 50 linear downstream
commits, no merges, no empty/omitted/upstreamed/extra patches, no manual source
conflicts or compatibility adaptations. All versions/messages remain unchanged
because this is a pure transplant. Existing historical release mentions in
messages describe their original version's development, not this transplant.
No version bump or fabricated new port history was introduced.

The runbook command was used with `GIT_NO_LAZY_FETCH=1`, rerere disabled,
`--no-update-refs --reapply-cherry-picks --empty=stop`. At original owner 20,
Git emitted the lazy-fetch-disabled warning and spent over three minutes in
CPU-active promised-object classification without a network child or source
conflict. The exact owned process was interrupted and joined (exit 130).
Affected old-parent/old-commit/current blob identities were locally available;
native per-commit diff and `git apply --check --3way` confirmed availability.
A trace-bounded retry showed no missing-loose-object open or fetch.

Command-local overrides for the clone's three existing promisor remotes let the
same owner replay promptly and the remaining stack complete:

```sh
GIT_NO_LAZY_FETCH=1 git \
  -c remote.origin.promisor=false \
  -c remote.git@github.com:gregkh/linux.git.promisor=false \
  -c remote.git@github.com:torvalds/linux.git.promisor=false \
  -c rerere.enabled=false rebase --continue
```

The workaround changed no stored/shared configuration and performed no
object-store repair or broad hydration. The deliberate filtered kernel.org
fetch in preflight automatically recorded that URL as an additional promisor
remote; it is not a source/config change from the replay workaround.
The classification diagnosis is bounded to this observed success; no absent
source blob was found. Two diagnostic interruptions consumed todo bookkeeping
before the interrupted commit completed. Owner 20 was explicitly requeued only
while HEAD/index remained clean at owner 19; owner 38 was applied but uncommitted
and was committed from its original full message with exact author/date. A
later transient `index.lock` refusal at owner 46 likewise left its exact staged
patch; no lock or Git process remained after join, and the original metadata
commit completed it before continuation. Final native range-diff and metadata
checks prove all originals occur exactly once, despite retry bookkeeping.
No lock was deleted and no patch was skipped. The successful conditional
recovery was sent to P/R owner; it was incorporated in P at
`435d83468d7a3089eeb45f171d0ab244748f43b4` per owner report.

## Direct source and tree review

Reviewed the old intent/messages and final overlapping paths against upstream:

- `fs/nfsd/nfsctl.c`: the namespace mount flag remains intact; upstream listener
  extack/rpcbind failure reporting is in separate functions and is retained.
- `include/linux/memcontrol.h` and `mm/memcontrol.c`: downstream kmem query,
  warning-free counter read, dump context, root rstat guard and RCU-protected
  reclaim-iterator walk remain. Upstream safe jiffies reads, high-work CSS
  lifetime/max-high cleanup, failed-charge max events and MGLRU protection-path
  helper remain, without changing these downstream helper contracts.
- `mm/vmscan.c`: the downstream slab-reclaim gate remains under
  `current_is_kswapd() || cgroup_memory_kmem_enabled()`. Upstream reclaim-target
  abort handling, real page-table pointer walking and MGLRU protection path
  apply to separate code and are retained.
- `mm/shmem.c`: downstream finite-memcg default sizing and userns ID rendering
  remain separate from upstream folio/truncation/fallocate/swapin/error-marker,
  swapoff interruption and seal/ACL fixes, which are all retained.
- `mm/swapfile.c`: downstream swaps view/reference lifetime is unchanged;
  upstream interrupted swapoff handling occurs in the unuse path.
- `include/linux/sunrpc/clnt.h`: upstream only names the existing rpcbind
  declaration parameters. Downstream terminal cancellation state, global list,
  pinned net reference and cancellation declarations remain intact; upstream
  listener-related SUNRPC code does not alter their NFS-client ownership.

All 106 downstream paths outside the seven-path intersection have exact Git
blob/tree equality between old packaged head and final head. Native
`git merge-tree --write-tree --merge-base=$old_base $old_head $new_base`
produces `944e5a57917938df529d6eebb3e30eba40e4afef`, exactly equal to
`git rev-parse $new_head^{tree}`. This independently proves the final tree is
the straightforward combination of the complete old downstream tree and all
upstream changes, without an accidental rebase-resolution delta.

## Quick checks and review boundary

Passed on exact final Linux head:

- `git range-diff old_base..old_head new_base..new_head`: 50 `=` pairs, no other
  dispositions. Full native output retained in `/tmp/stable-kernel-range-diff.txt`
  as disposable support; the complete durable correspondence is above.
- Native ancestry/version/count/merge checks: target is ancestor, Makefile
  6.12.118, 50 commits, zero merges; exact backup ref preserved.
- All 50 author names/emails/dates and full messages match their old logical
  owners; all per-commit path/status deltas match. No policy-relevant source or
  message revisions require a new version or new provenance.
- `git diff --check new_base..new_head`: exit 0. Changed added lines have no
  conflict markers; subjects have no fixup/squash/WIP residue. Worktree/index
  clean after completed replay. No declared Linux hook framework is present.
- Full native three-way tree equality and direct seven-path preservation review
  described above passed.

All intended Linux changes are committed. There are no database migrations,
transitional schema versions, intermediate pins or repair commits. This is a
50-owner maintained source series transplanted intact, not a new mega-commit.
No source compilation or runtime qualification has run; these remain for global
independent final review followed by the lead-owned exact pinned build/tests.
K's source checks establish preservation, not runtime correctness. OS catalog,
selector, archive source realization and ZFS package checks remain R-owned.

## Publication receipt and R handoff

Fresh SSH `git ls-remote origin` before push found no topic branch. Published
only `refs/heads/2026-11-17-stable-kernel-update` via `git push --set-upstream`
over canonical `git@github.com:vpsfreecz/linux.git`; exit 0. Fresh post-push
`git ls-remote` exited 0 and returned:

| Ref | Exact remote head |
| --- | --- |
| `refs/heads/2026-11-17-stable-kernel-update` | `3bba27296b6f4f4a2b1568d65cea6037368f229b` |
| `refs/heads/master` (same before/after) | `4939902ea21d81d97a3f47517dd46d1b6eb9a5fe` |
| `refs/heads/vpsadminos-6.12` (same before/after) | `9ccd5d6597a6ddbe5b44fb885ddf96e4dbc332dd` |

Final immutable archive URL:
<https://github.com/vpsfreecz/linux/archive/3bba27296b6f4f4a2b1568d65cea6037368f229b.tar.gz>.
R owns the single archive-byte prefetch/hash and actual package source
realization to avoid a duplicate large transfer; its receipt will be linked here.
K's publication commands have exited, with no utility watcher or command left
running. R was notified directly that publication proof is complete and the
utility slot is free. All Linux feature/source refs and the original backup
remain retained. No PR, default/maintenance promotion or deployment was done.

R archive receipt (reported by implementer0): the single monitored raw-archive
prefetch completed with exit 0 in approximately 50 seconds, with no running
effects. For the final published source URL above:

- Raw-byte SHA256: `sha256-tXgl0RdF3YigscvXI/tD5QHbujUV+6bVW+KIyESG93U=`.
- Archive store path:
  `/nix/store/y9smdxxh7z7df58hzybqpyrx11rmjrvq-3bba27296b6f4f4a2b1568d65cea6037368f229b.tar.gz`.
- Disposable supporting stdout: `/tmp/stable-kernel-archive-prefetch.json`.

R reports the final catalog revision/hash and stable selector were inserted
once. Actual package-source realization remains pending at this receipt; no
compilation or runtime test is implied by archive hashing.

## Version branch publication (L-publish)

Lead relayed the user's explicit branch-only Linux publication policy and
approval of `vpsadminos-<upstream-version>`, specifically
`refs/heads/vpsadminos-6.12.118` for the already reviewed/tested exact source
`3bba27296b6f4f4a2b1568d65cea6037368f229b`. Linux is retained in its kernel
branch rather than merged to a default. The dated topic remains retained and
the OS source remains pinned by exact SHA. This authorization adds no tags,
floating maintenance updates, default merges, deployment or lifecycle action.

L-publish owner implementer1 confirmed capacity and session identity, reread
Git/commits and the full patch-series policy. Fresh destination `ls-remote`
returned no version branch; local `for-each-ref` likewise found it absent.
The dated branch and original backup were exact and preserved. Published with:

```sh
GIT_NO_LAZY_FETCH=1 git update-ref refs/heads/vpsadminos-6.12.118 \
  3bba27296b6f4f4a2b1568d65cea6037368f229b \
  0000000000000000000000000000000000000000
GIT_NO_LAZY_FETCH=1 git show-ref --verify refs/heads/vpsadminos-6.12.118
GIT_NO_LAZY_FETCH=1 git push origin \
  refs/heads/vpsadminos-6.12.118:refs/heads/vpsadminos-6.12.118
GIT_NO_LAZY_FETCH=1 git ls-remote origin \
  refs/heads/vpsadminos-6.12.118 \
  refs/heads/2026-11-17-stable-kernel-update \
  refs/heads/master refs/heads/vpsadminos-6.12
```

All commands exited 0. Normal SSH push created the new branch, without force.
Fresh remote evidence:

| Remote ref | Exact SHA | Result |
| --- | --- | --- |
| `refs/heads/vpsadminos-6.12.118` | `3bba27296b6f4f4a2b1568d65cea6037368f229b` | New version branch verified |
| `refs/heads/2026-11-17-stable-kernel-update` | `3bba27296b6f4f4a2b1568d65cea6037368f229b` | Retained exact source |
| `refs/heads/master` | `4939902ea21d81d97a3f47517dd46d1b6eb9a5fe` | Unchanged before/after |
| `refs/heads/vpsadminos-6.12` | `9ccd5d6597a6ddbe5b44fb885ddf96e4dbc332dd` | Floating alias unchanged before/after |

No collision, source edit, commit, rebase, review/retest, tag, merge, force push,
manifest mutation or lifecycle action occurred. Linux worktree remains clean
on its dated branch. All publication commands have completed. No repository
merge claim was required for the explicitly authorized new source branch.
