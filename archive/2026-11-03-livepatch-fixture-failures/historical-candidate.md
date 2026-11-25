# Historical expected-candidate provenance

Historical bytes are restorable and independently verified. The corrected
exact-target cache copy completed in 3.38 seconds without building anything;
the restored module SHA256 equals the expected pin. Nix content and signature
verification both passed. Both requested historical revisions resolve to this
same output; pin-introducing source also reproduces its published deriver.

Owner: implementer2. Investigation only; no application edits, integrity-pin
changes, builds, CI reruns, integration, deployment or lifecycle actions.

Session identity and both environment values match
`2026-11-03-livepatch-fixture-failures` and
`/home/aither/workspace/ai/vpsfree.cz`. The assigned worktree is clean at
`dd188397abe37d0bc33f4c5dfb3605206ce5e326`.

Expected module SHA256:
`573e8d1e05433be7c4eab361bb733e92977496f6437b43a4af1e5d21d2452d9d`.

At last all-nine-green source `d9be8c4bada590c0405df85444600d40e6f3caa6`,
read-only Nix evaluation of the fixture reproduces the wrapper reported by
implementer0 from run `40296454457`, artifact `12646139312`:

- Source: `/nix/store/40a1yny1kkd9i822np06q3hwr6l2xk5r-source`.
- Wrapper: `/nix/store/m3ig6h5s0ldclfyl3mrss6n5psrw0j7d-livepatch_7-exact-candidate.ko`.
- Wrapper derivation: `/nix/store/7asp65b723v0bjmm2scsp3l6bxcbl2fp-livepatch_7-exact-candidate.ko.drv`.

The wrapper's narinfo currently returns HTTP 404 from
`https://cache.vpsadminos.org/m3ig6h5s0ldclfyl3mrss6n5psrw0j7d.narinfo`.
This establishes absence at that exact cache endpoint, not absence of the
underlying module producer.

The pin-introducing commit is
`3ddca3e6b84017f37499568d3efaefa7c4e2e72f` (2026-10-15). Its commit message
records the normal producer, strict fixture, all 711 imported CRCs, and focused
v5/v6 retention/admission checks. That is historical recorded evidence.

The fixture, livepatch builder, patch payload and frozen-boot helper are
unchanged between those two revisions. Relevant changes in that range are
`flake.lock` and Linux package metadata.

## Exact producer

Both historical source revisions evaluate to this module:

`/nix/store/6hiwxy4nmpnb18xmsn9a5mh5g8mb246p-livepatch_7-6.12.95/lib/modules/6.12.95/extra/livepatch_7.ko`

| Identity | Pin-introducing revision | Last all-nine-green revision |
| --- | --- | --- |
| Revision | `3ddca3e6b84017f37499568d3efaefa7c4e2e72f` | `d9be8c4bada590c0405df85444600d40e6f3caa6` |
| Evaluated source | `/nix/store/q1ggnbfzai169la9xh0l29fyaiq0m0xv-source` | `/nix/store/40a1yny1kkd9i822np06q3hwr6l2xk5r-source` |
| Wrapper drv | `/nix/store/pg1avaj3y4fwfm6cpwvhnpcb67hax17h-livepatch_7-exact-candidate.ko.drv` | `/nix/store/7asp65b723v0bjmm2scsp3l6bxcbl2fp-livepatch_7-exact-candidate.ko.drv` |
| Producer drv | `/nix/store/50irawqs0aaks9d6n2brj411hz4w4nhd-livepatch_7-6.12.95.drv` | `/nix/store/maa7anq6rx7id4hwzc6z1fagv46xv9i6-livepatch_7-6.12.95.drv` |
| Root stable Nixpkgs | `a033e66ab94a6bedf2c3d58d93a36319d3cbbbaf` | `1f607aa79b6356ed45d3cd3c8079c196e79efa2c` |

The pin-introducing evaluation reproduces the cache's published producer
deriver exactly. The later producer has identical environment, builder,
arguments, source-path inputs and output, with different derivation edges for
the Linux archive fetch and builtin ZFS. Different derivation identity alone
does not establish different module bytes or explain a regression.

## Published artifact and restoration

At the investigation checkpoint on 2026-11-03,
`https://cache.vpsadminos.org/6hiwxy4nmpnb18xmsn9a5mh5g8mb246p.narinfo`
returns:

- Store path: `/nix/store/6hiwxy4nmpnb18xmsn9a5mh5g8mb246p-livepatch_7-6.12.95`.
- NAR URL: `https://cache.vpsadminos.org/nar/6hiwxy4nmpnb18xmsn9a5mh5g8mb246p-0ff0c27m1vsfwxrpi5hr3wj147fn389gk5hnskdl8mxhqq10xvcr.nar`.
- Compression: `none`; NAR size: `172084880` bytes.
- NAR hash: `sha256:0ff0c27m1vsfwxrpi5hr3wj147fn389gk5hnskdl8mxhqq10xvcr`.
- Published deriver: `/nix/store/50irawqs0aaks9d6n2brj411hz4w4nhd-livepatch_7-6.12.95.drv`.
- Direct output reference: `/nix/store/63wdfxcylc7rzym8iwhv84yppg8gj3vv-binutils-2.46`.
- Signature key: `cache.vpsadminos.org`, matching the repository-documented
  trusted public key.

The wrapper and published producer derivation themselves return HTTP 404 at
their respective narinfo endpoints. The producer derivation is nevertheless
recovered by exact historical evaluation. Copying the producer output does
not require building or retrieving its derivation or build inputs.

The first fresh Luna/low utility attempted the copy, but its receipt shows an
extra `.` operand: punctuation in the parent handoff was interpreted as a
second target. The lead bounded that batch at 300 seconds. SIGINT interrupted
the wrapper (exit 130); the exact child status and captured output were lost.
Watcher and independent parent process checks found no matching copy client.
The sole historical output is absent and `nix-store --check-validity` exits 1.
That malformed attempt establishes neither artifact unavailability nor slow
transfer of this historical target.

The lead authorized one correction of this tool error: a fresh Luna/low
watcher, one exact five-entry argv, and a 60-second client deadline. Parent
verified its argv before giving GO. No `.` or extra operand is present:

```sh
nix copy --from https://cache.vpsadminos.org /nix/store/6hiwxy4nmpnb18xmsn9a5mh5g8mb246p-livepatch_7-6.12.95
```

The corrected copy exited 0 in `3.3831847429974005` seconds, copied exactly one
path, and required no cancellation or build. The parent then measured:

```text
573e8d1e05433be7c4eab361bb733e92977496f6437b43a4af1e5d21d2452d9d  /nix/store/6hiwxy4nmpnb18xmsn9a5mh5g8mb246p-livepatch_7-6.12.95/lib/modules/6.12.95/extra/livepatch_7.ko
```

`nix store verify --sigs-needed 1`, with the repository-documented cache key,
exited 0, checking both local content and trust. Local registered metadata
matches the published NAR, including:

- SRI NAR hash `sha256-me0OAsawV0Tb1BaW+RIa1h0SJB8Zlnhz507vUI9gwDk=`
  (same hash as the Nix-base32 narinfo value above).
- NAR size `172084880`, published deriver `50irawqs…`, and binutils reference.
- `cache.vpsadminos.org` signature; local `ultimate` is false.

Both watcher operations are terminal. Parent reconciliation found no matching
copy client after cancellation of the first operation; the corrected child
exited 0 normally. No owned operation remains running, no repository changed,
and no build/retry beyond the explicitly authorized tool correction occurred.

This confirms restoration of the expected historical bytes from the published
cache. It does not establish that an independent clean rebuild would produce
the same module or qualify these bytes for deployment.

## Source and input graph

Read-only evaluation used Nix `2.34.9`, `builtins.getFlake` of the exact local
canonical Git revisions, then imported `tests/fixtures/livepatch` with its
default package set. It reproduced the CI wrapper independently of CI logs.
Evaluation substituted source inputs but realized no build derivation.

Complete recursive graphs are saved under
[historical-candidate-evidence](historical-candidate-evidence/). Each contains
2,870 derivations and 371 unique source-path inputs; every derivation edge
resolves within its graph. The JSON includes selected output edges,
fixed-output hashes, structured fetch attributes and source paths, rather
than only a runtime closure.

| Graph file | SHA256 |
| --- | --- |
| `pin-3ddca3e6-graph.json` | `bf7c92e30a414f98e659697c1e29707dc43bf3efcc6322e0a198d440d0d85e17` |
| `d9be8c4b-graph.json` | `f27cd8b5bd1495e6877ef5d2a4f8390eca300d1d05b460fb18542e7af4898701` |

The same evidence directory holds both wrapper and producer records, complete
lockfiles, the 27 direct producer input records, source-path inventory,
narinfo/HTTP results and utility copy receipt. Raw JSON/logs are disposable
session evidence; this Markdown retains the consequential identities.

Key graph boundaries:

- Patches: `/nix/store/87q0xai9qh5hfwj9lc9addfbpznbvxya-livepatches`;
  production patch SHA256 `6dfef5b7e56e1038a881e77a594aeadcddf50381d63aa196cd946dde6899097d`,
  uname patch SHA256 `75b87e7964146b4ce417df0b36af120ee32c6cab66f48582e8c76b7b03727c10`.
- Linux source: `a2384967b90f24d2470c9eb15f0e66d938df7e08`,
  `/nix/store/4jcdch0myxf11872ncmp4cgh91mg546r-a2384967b90f24d2470c9eb15f0e66d938df7e08.tar.gz`,
  fixed SHA256 `sha256-QlwV4uFeX7ZbWHMuU14rFXswmpqpb1hdVmYUAGOWRh8=`.
- Builtin ZFS source: `481845fca6ae3f61ca2262c1a5693a58ae364650`,
  `/nix/store/gfbfdram71x5imp44590b04pc0wch182-source`,
  fixed NAR SHA256 `sha256-/zeZH5EJYa0zaNcbMUoeHp6UnHNAMUrjgok/VgWI88A=`;
  producer input `/nix/store/jrvl3zlk1jb61b6vc9v6iphym7rd1m06-zfs-builtin-2.3-vpsadminos-6.12.95`.
- Kpatch source: `dynup/kpatch` at `bea635fbbeb11c5f0f5c0d4ffce34c2e9d2e8a6a`,
  `/nix/store/xdvj0vn3dal8rc68gs1a756nqyppr1c7-source`,
  fixed NAR SHA256 `sha256-bVoNNtzNGCd1+8RmxDeLPr/6g4KdYmDFuCmJYET5AIU=`;
  packaged input `/nix/store/bwrigg0hkqy7711h1b8yfb0y2jk1yhd5-kpatch-build`.
- Frozen boot helper source: vpsAdminOS
  `c065fa2f8485399737e20e8ef9e44299d0766654`, stable Nixpkgs
  `21a67dc470149f337cecafbe965d8d252a390518`
  (`sha256-ugpsyk3NM2s87vXfUiIIiibbJ4Pp0JPS5p/3mfs+q+c=`).
  Restored SDK `/nix/store/i1kpp81z029hdl4hyxzbm4sxni181yg0-linux-6.12.95-frozen-boot-dev`,
  helper derivation `/nix/store/hpjypr6g0sfaa3ygahvcmi5vgxb33b7m-linux-6.12.95-frozen-boot.drv`.
- Frozen config `/nix/store/np082gl8insab5lisjdhqlh4128jlm9m-linux-config-6.12.95`;
  boot-line compiler `/nix/store/hbsz2ngi9ixbhd9na1xagh2yc8qnmj7y-gcc-wrapper-15.2.0`.
  The surrounding build also depends on
  `/nix/store/dy6j7267wrgjlr2z748sbx83zj16vs3c-gcc-wrapper-15.3.0`
  and `/nix/store/l325vp92jbs1xz51vrniwq02m6wdnbyi-stdenv-linux`.

This establishes graph identity and artifact availability, not clean rebuild
reproducibility, runtime qualification, or restoration of every transitive
build input. No rebuild, VM test, CRC recomputation or CI rerun was performed.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/>.
