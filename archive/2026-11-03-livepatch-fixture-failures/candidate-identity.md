# Current livepatch candidate identity

Measured 2026-11-03 by implementer1, from the session-owned clean vpsAdminOS
worktree at `dd188397abe37d0bc33f4c5dfb3605206ce5e326`. Investigation only;
source, immutable pins, Git refs and running systems were not changed. No
kernel or livepatch compilation was launched.

## Result

The exact candidate selected by `tests/fixtures/livepatch/default.nix` is
published in the vpsAdminOS binary cache. Its module has SHA-256
`7c4da9d643d45ad9c07bde72b0180175519c5e7a15a6f2aec9e54831aee8455f`,
whereas the reviewed fixture pin is
`573e8d1e05433be7c4eab361bb733e92977496f6437b43a4af1e5d21d2452d9d`.
Running the fixture's checksum assertion directly against these cached bytes
returns exit 1. This establishes the immediate fixture preparation failure
without building the fixture, running a VM or rerunning CI.

The fixed pin remains an independent qualification requirement. This measurement
does not establish that the new bytes are safe, equivalent to the qualified
module, or suitable for repinning.

| Identity | Measured value |
| --- | --- |
| Module path | `/nix/store/qi47yi2g9kp89dv0h8jxwndm89vbq6az-livepatch_7-6.12.95/lib/modules/6.12.95/extra/livepatch_7.ko` |
| Module size | 82,769,056 bytes |
| ELF | x86-64 relocatable; debug info present; not stripped |
| GNU build ID | `fd8cbfe4c314ddac8f35d87bee4bb8b909e479d5` |
| modinfo name | `livepatch_7` |
| vermagic | `6.12.95 SMP preempt mod_unload modversions` |
| ELF `.comment` | `GCC: (GNU) 15.2.0` (four entries) |
| Producing derivation | `/nix/store/161r03nnqvqw9g2ar5kjsbz00zr7xydg-livepatch_7-6.12.95.drv` |
| Guard derivation | `/nix/store/vg23dzka1i0dw28fy3kl4wssyms484yx-livepatch_7-exact-candidate.ko.drv` |
| Guard output (not built) | `/nix/store/kmm41zgxg3ai8r84jqm2mk02r4py6cdv-livepatch_7-exact-candidate.ko` |

## Cache provenance

`https://cache.vpsadminos.org/qi47yi2g9kp89dv0h8jxwndm89vbq6az.narinfo`
identifies the same producing derivation and output. Its metadata is:

- NAR SHA-256: `sha256-nfaVMIS8W4Cqw0OSyR8gZHtG4u6hHPE6XUS9FwAtcmw=`.
- NAR size: 172,088,608 bytes, uncompressed (`Compression: none`).
- URL: `nar/qi47yi2g9kp89dv0h8jxwndm89vbq6az-0v3j5l01gga4blxg2751xvi4cyv440gwk4j3qfm80nxwhhq9bxlx.nar`.
- Reference: `/nix/store/63wdfxcylc7rzym8iwhv84yppg8gj3vv-binutils-2.46`.
- Signature: `cache.vpsadminos.org:U2q9BdS50IyxYJNLuR7Fg9Ektwb4gX3BebdMaGexvkHpJ5604XPebj/9koFh6rsAJHRGV46LNexl7WGGskWgAw==`.

The fresh policy-resolved Luna/low watcher copied this named output using
`nix copy --from https://cache.vpsadminos.org /nix/store/qi47yi2g9kp89dv0h8jxwndm89vbq6az-livepatch_7-6.12.95`.
It exited 0 after four seconds; no operation remains running. Both
`nix store verify --no-contents OUTPUT` (trust) and `nix store verify OUTPUT`
(contents and trust) then passed. The host's configured trusted key matches the
repository's documented public key:
`cache.vpsadminos.org:wpIJlNZQIhS+0gFf1U3MC9sLZdLW3sh5qakOWGDoDrE=`.

Full copy output is disposable evidence in
[candidate-cache-copy.log](candidate-cache-copy.log); the watcher receipt is
[candidate-cache-copy-result.md](candidate-cache-copy-result.md).

## Source and build input identity

The clean root flake source is
`/nix/store/cgk63vdx1wjl4ybd53abkd5aqyzc7sfa-source`, revision
`dd188397abe37d0bc33f4c5dfb3605206ce5e326`, NAR hash
`sha256-LXZP7Ghcr+1obFUD+LjlJRO63qRo/GZtSve5AX5MZ7c=`.
The fixture imports the root flake's current `nixpkgs` and current package
overlay, then the `.95` boot-base configuration. Relevant source files are
`tests/fixtures/livepatch/default.nix`,
`tests/configs/vpsadminos/livepatch-6.12.95-boot-base.nix`,
`os/modules/services/livepatches/default.nix`,
`os/packages/linux/boot-6.12.95.nix`,
`os/packages/linux/boot-6.12.95/default.nix`, and
`os/packages/kpatch-build/default.nix`.

Root lock graph (root `nixpkgs` selects node `nixpkgs_2`; the separate
`nixpkgs` node belongs to impermanence):

| Lock node | Source | Revision | NAR SHA-256 |
| --- | --- | --- | --- |
| `home-manager` | `nix-community/home-manager` | `c47b2cc64a629f8e075de52e4742de688f930dc6` | `sha256-kkgA32s/f4jaa4UG+2f8C225Qvclxnqs76mf8zvTVPg=` |
| `impermanence` | `nix-community/impermanence` | `fa627f4c8b8e92f58f58a73d99ee4e1304e64eb2` | `sha256-s0TeXWG5Ci75Y/Hzon0Z7NrN/fG773Rc54/z6oPFszQ=` |
| `netlinkrb` | `vpsfreecz/netlinkrb` | `d9de53d843d2586ffa5b7b404887fa801c697ddf` | `sha256-0bXTWUdUDr2XP+bEIfIbxXap8Niva/IoPXTxFeXXImg=` |
| `nixpkgs` | `nixos/nixpkgs` | `e4bae1bd10c9c57b2cf517953ab70060a828ee6f` | `sha256-Kell/SpJYVkHWMvnhqJz/8DqQg2b6PguxVWOuadbHCc=` |
| `nixpkgsUnstable` | `NixOS/nixpkgs` | `0bb2eedc20e4739f29e8045034f2828ad7054f8f` | `sha256-fiPJ88izTVucjeo2EQ3jk4aWmLg03I1D4vxnX2QjEgE=` |
| `nixpkgs_2` | `NixOS/nixpkgs` | `7dcdd87373d72e7a2173e4db02e20d3d7f495cfd` | `sha256-tItrb9M8eYA6WhFgmT9tpGKueri3+wRuVA952o/2xSU=` |
| `ruby-lxc` | `vpsfreecz/ruby-lxc` | `004bf35eb90d41ba60b347b5b1e73d868a4f95d9` | `sha256-guAdOSP9MyCL3BQ1LGXAhcCoXgEU1fUE69d2ATMqUGE=` |

The `.95` boot helper separately imports immutable vpsAdminOS producer
`c065fa2f8485399737e20e8ef9e44299d0766654`, source
`/nix/store/dmn3x6swkhfcwfl7lszbbqsh8i43760w-source`, NAR hash
`sha256-rOrRlg6tmFJVheYArq8Ug45gZE6J/fuHhe5cUrvcVVk=`. Its stable
nixpkgs is `21a67dc470149f337cecafbe965d8d252a390518` at
`/nix/store/i2wrp0fbhvysy6bcanmwn6smd3jw938f-source`, NAR hash
`sha256-ugpsyk3NM2s87vXfUiIIiibbJ4Pp0JPS5p/3mfs+q+c=`. This is boot
provenance within the current candidate graph; it is not a historical-green
candidate comparison. The imported producer's complete lock identities are:

| Lock node | Source | Revision | NAR SHA-256 |
| --- | --- | --- | --- |
| `home-manager` | `nix-community/home-manager` | `c47b2cc64a629f8e075de52e4742de688f930dc6` | `sha256-kkgA32s/f4jaa4UG+2f8C225Qvclxnqs76mf8zvTVPg=` |
| `impermanence` | `nix-community/impermanence` | `7b1d382faf603b6d264f58627330f9faa5cba149` | `sha256-03+JxvzmfwRu+5JafM0DLbxgHttOQZkUtDWBmeUkN8Y=` |
| `netlinkrb` | `vpsfreecz/netlinkrb` | `d9de53d843d2586ffa5b7b404887fa801c697ddf` | `sha256-0bXTWUdUDr2XP+bEIfIbxXap8Niva/IoPXTxFeXXImg=` |
| `nixpkgs` | `nixos/nixpkgs` | `e4bae1bd10c9c57b2cf517953ab70060a828ee6f` | `sha256-Kell/SpJYVkHWMvnhqJz/8DqQg2b6PguxVWOuadbHCc=` |
| `nixpkgsUnstable` | `NixOS/nixpkgs` | `eaad089433ca2bb662274377d33df3d0e51ef28b` | `sha256-H6GwaZzZf+4npqv0tph94w9tZddSjFjmQrVsW0z78uk=` |
| `nixpkgs_2` | `NixOS/nixpkgs` | `21a67dc470149f337cecafbe965d8d252a390518` | `sha256-ugpsyk3NM2s87vXfUiIIiibbJ4Pp0JPS5p/3mfs+q+c=` |
| `ruby-lxc` | `vpsfreecz/ruby-lxc` | `004bf35eb90d41ba60b347b5b1e73d868a4f95d9` | `sha256-guAdOSP9MyCL3BQ1LGXAhcCoXgEU1fUE69d2ATMqUGE=` |

The candidate inputs deliberately combine frozen `.95` boot ABI/configuration
and GCC 15.2 with current build support. Concrete current identities:

| Role | Exact identity |
| --- | --- |
| Livepatch source tree | `/nix/store/87q0xai9qh5hfwj9lc9addfbpznbvxya-livepatches`, NAR hash `sha256-ZN5m/9gDlqZiKEGmh/M/cgY72ZlcRp4Fm1tyklZRjyU=` |
| Patch set | `bp-6.12.95-production.patch`, `bp-6.12.95-uname.patch`; module version 7; ordinary full target set |
| Linux archive | `/nix/store/4jcdch0myxf11872ncmp4cgh91mg546r-a2384967b90f24d2470c9eb15f0e66d938df7e08.tar.gz`; vpsfreecz/linux `a2384967b90f24d2470c9eb15f0e66d938df7e08`; flat hash `sha256-QlwV4uFeX7ZbWHMuU14rFXswmpqpb1hdVmYUAGOWRh8=` |
| Frozen boot derivation | `/nix/store/hpjypr6g0sfaa3ygahvcmi5vgxb33b7m-linux-6.12.95-frozen-boot.drv` |
| Frozen boot dev input | `/nix/store/i1kpp81z029hdl4hyxzbm4sxni181yg0-linux-6.12.95-frozen-boot-dev` |
| Frozen boot out | `/nix/store/050sh2hfrnpc8j5abr2npp7bnlxvpb8a-linux-6.12.95-frozen-boot` |
| Frozen config input | `/nix/store/np082gl8insab5lisjdhqlh4128jlm9m-linux-config-6.12.95` |
| GCC used in kpatch invocation | `/nix/store/hbsz2ngi9ixbhd9na1xagh2yc8qnmj7y-gcc-wrapper-15.2.0`; derivation `/nix/store/8wjz435nqc46mz0ndzh02hwa6fnpip3n-gcc-wrapper-15.2.0.drv`; underlying compiler `/nix/store/6hjng4hd5c688hjgdcyb1rzfjz220srh-gcc-15.2.0` |
| Boot GCC's declared bintools | `/nix/store/la0zcwbbm1jazcjqf80m49xfyj14k4b3-binutils-wrapper-2.46` |
| Current module/kpatch stdenv | `/nix/store/bds9i60lxg8viivxw59b9l18hl8h1vcd-stdenv-linux`; derivation `/nix/store/xhal618qb5gx0na1gq07mvvgxilg26c6-stdenv-linux.drv` |
| Current `depsBuildBuild` / default stdenv CC | `/nix/store/0592hadxldzhhd3ppc6nskslzd39fwlz-gcc-wrapper-15.3.0`; derivation `/nix/store/sxf2064rx5xmhq2x4zj3ffjjgn6239nw-gcc-wrapper-15.3.0.drv`; bintools `/nix/store/c1a2l64csn5lrwjqqnaman6hdici70vq-binutils-wrapper-2.46` |
| Current kpatch-build | `/nix/store/fq3zwdkn8z92g3l1hkp20amb44zb89cm-kpatch-build`; derivation `/nix/store/haknsj0g1z0bb7945xkwz8ihjmq7f80w-kpatch-build.drv` |
| kpatch source | dynup/kpatch `bea635fbbeb11c5f0f5c0d4ffce34c2e9d2e8a6a`, version 0.9.11; `/nix/store/xdvj0vn3dal8rc68gs1a756nqyppr1c7-source`; hash `sha256-bVoNNtzNGCd1+8RmxDeLPr/6g4KdYmDFuCmJYET5AIU=`; six repository patches |
| kpatch direct libraries/tools | `/nix/store/4hl1k36jid0x1a50qnkm9cbw6zp3la43-gnumake-4.4.1`, `/nix/store/j3j4i3dsgan9c1wa4qyfi7nfc5zxp1pg-elfutils-0.194-dev` |
| Current ZFS builtin input | `/nix/store/ylwgnr882jgla2d8m5h95qavlzxdai0l-zfs-builtin-2.3-vpsadminos-6.12.95`; derivation `/nix/store/padca4x3klcsakr8abrfid3gv6ymfc92-zfs-builtin-2.3-vpsadminos-6.12.95.drv` |
| ZFS source | vpsfreecz/zfs `481845fca6ae3f61ca2262c1a5693a58ae364650`; `/nix/store/gfbfdram71x5imp44590b04pc0wch182-source`; hash `sha256-/zeZH5EJYa0zaNcbMUoeHp6UnHNAMUrjgok/VgWI88A=` |
| ZFS configure compiler | `CC` and `HOSTCC` explicitly use `/nix/store/0592hadxldzhhd3ppc6nskslzd39fwlz-gcc-wrapper-15.3.0/bin/cc`; configuration probes use `/nix/store/sv79x5grw9hzmc2fa31rpd2yyz47005k-linux-6.12.95-dev` |

The archived output contains an 88,727,145-byte `livepatch-evidence/build.log`.
For example, line 15728 records
`/nix/store/63wdfxcylc7rzym8iwhv84yppg8gj3vv-binutils-2.46/bin/ld.bfd`.
That is an observed linker identity. It **does not prove compiler/toolchain
pin leakage**: the pinned boot GCC wrapper itself declares a binutils 2.46
wrapper. The module's `.comment` confirms GCC 15.2.0. Attributing the SHA change
to a particular input requires a historical byte/input comparison; architect
and implementer2 own that separate package.

### Direct candidate derivation edges

Every selected direct derivation input/output is listed below. Paths in the
first column are relative to `/nix/store/`. Source inputs directly declared in
addition to these derivations are `87q0xai9qh5hfwj9lc9addfbpznbvxya-livepatches`,
`l622p70vy8k5sh7y5wizi5f2mic6ynpg-source-stdenv.sh`, and
`shkw4qm9qcw5sc5n1k5jznc83ny02r39-default-builder.sh`.

| Derivation | Selected outputs | Resulting output |
| --- | --- | --- |
| `2hc4lagg0zg9if60xpq2jwvfr15q8f5l-bc-1.08.2.drv` | `out` | `/nix/store/rcr7ah4vljqyfg77kdpn6mh13lxy56gp-bc-1.08.2` |
| `2lm0iggkcsxyqpc5rd2h56g9frilkq35-python3-minimal-3.13.17.drv` | `out` | `/nix/store/r1xplla5spsclbn3ccj2ph2kkwj8987p-python3-minimal-3.13.17` |
| `2ngcskbndvpacixi2wsbl0v9lhfnhc42-zstd-1.5.7.drv` | `dev` | `/nix/store/x735fzw5abldd4sk10lasz1dkayi3bwr-zstd-1.5.7-dev` |
| `3d07cbkazmhq8h0j1l1saxbzq8s23fr7-kmod-31.drv` | `dev` | `/nix/store/y45spmy4vih65la39ws1130kzj9cz8ms-kmod-31-dev` |
| `3v41l7mln0vvgzkkix9fragil6c98r1a-bison-3.8.2.drv` | `out` | `/nix/store/j5x3x612ajan2ck9f3wq1s8adqylwig3-bison-3.8.2` |
| `44zvgyz39g2yyvd246s1j80w8fqrxzav-a2384967b90f24d2470c9eb15f0e66d938df7e08.tar.gz.drv` | `out` | `sha256-QlwV4uFeX7ZbWHMuU14rFXswmpqpb1hdVmYUAGOWRh8=` (flat) |
| `74236fra8jhfd714bxjdsm18dqsj7z29-pahole-1.31.drv` | `out` | `/nix/store/f44vj1awchf88gw53riil0k92my69xjw-pahole-1.31` |
| `8wjz435nqc46mz0ndzh02hwa6fnpip3n-gcc-wrapper-15.2.0.drv` | `out` | `/nix/store/hbsz2ngi9ixbhd9na1xagh2yc8qnmj7y-gcc-wrapper-15.2.0` |
| `cl3hgm0bxp6pfa64xjs85gdfvwhgbf5v-gawk-5.4.1.drv` | `out` | `/nix/store/xj3xxr99c1zx418k604q0gi0jhpx0dhy-gawk-5.4.1` |
| `cvvdjxcbbcdks08sgv6ipg7rf2r732a7-elfutils-0.194.drv` | `dev` | `/nix/store/j3j4i3dsgan9c1wa4qyfi7nfc5zxp1pg-elfutils-0.194-dev` |
| `haknsj0g1z0bb7945xkwz8ihjmq7f80w-kpatch-build.drv` | `out` | `/nix/store/fq3zwdkn8z92g3l1hkp20amb44zb89cm-kpatch-build` |
| `hpjypr6g0sfaa3ygahvcmi5vgxb33b7m-linux-6.12.95-frozen-boot.drv` | `dev` | `/nix/store/i1kpp81z029hdl4hyxzbm4sxni181yg0-linux-6.12.95-frozen-boot-dev` |
| `hrgw9al643kmplvffgc5f59dwlx48sm7-bash-5.3p9.drv` | `out` | `/nix/store/hc49zakwkkyp9zlyl80b71jhxkpn4hsx-bash-5.3p9` |
| `hwicvf2hqj3342n9dx2kpvfwmffay7w5-mpfr-4.2.2.drv` | `dev` | `/nix/store/klb0k0ykng6az1iky0a3shm91zq5iycs-mpfr-4.2.2-dev` |
| `jbl5zaqxrchkwsvg1dnhkly4xhnsx8cb-net-tools-2.10.drv` | `out` | `/nix/store/rq2n61sfqyz4bf97cs85pwryrn3rbn2n-net-tools-2.10` |
| `kvn2lqg5j5678j19yi2945djgd8l1h3v-linux-config-6.12.95.drv` | `out` | `/nix/store/np082gl8insab5lisjdhqlh4128jlm9m-linux-config-6.12.95` |
| `p215xj7kf67zxi95711xjvz6np7qxx3i-libmpc-1.4.0.drv` | `out` | `/nix/store/9wxp73cmlcjzgi78i2109365jdxvqzgq-libmpc-1.4.0` |
| `padca4x3klcsakr8abrfid3gv6ymfc92-zfs-builtin-2.3-vpsadminos-6.12.95.drv` | `out` | `/nix/store/ylwgnr882jgla2d8m5h95qavlzxdai0l-zfs-builtin-2.3-vpsadminos-6.12.95` |
| `q4xrx5m1fwccy6p56kpsja9nqs0zkxjj-cpio-2.15.drv` | `out` | `/nix/store/bszflkd1v8dn96819llfhx7zqrk15qil-cpio-2.15` |
| `ry6djzipigxhmr5yyr93zndwjzyhf0a9-flex-2.6.4.drv` | `out` | `/nix/store/0d8ckwcrg443bkpk7h85j96s3mgm2v28-flex-2.6.4` |
| `s15q1amf92q01css2c9q1bn0q00fgwrb-perl-5.42.3.drv` | `out` | `/nix/store/cxcwzvbichfrlsv40j5clf60b9s7kp6y-perl-5.42.3` |
| `sxf2064rx5xmhq2x4zj3ffjjgn6239nw-gcc-wrapper-15.3.0.drv` | `out` | `/nix/store/0592hadxldzhhd3ppc6nskslzd39fwlz-gcc-wrapper-15.3.0` |
| `vz9ri9j08jpg5jvac9lvdjisglws7cd6-zlib-1.3.2.drv` | `dev` | `/nix/store/i4w1mj6rawirh6m26k8d9hpcjmrgd3pp-zlib-1.3.2-dev` |
| `wb3dqhks5px2rxdsbhvrdfqv256al294-openssl-3.6.5.drv` | `dev` | `/nix/store/f0lcjigadrvilgw2fprzdd96fw055q0b-openssl-3.6.5-dev` |
| `xaiqm3ipm2bmzgay7n5d8vnb047khn7q-rsync-3.5.0.drv` | `out` | `/nix/store/dfzxlyvvjs4agvrb3qy709rl71j3bf8b-rsync-3.5.0` |
| `xhal618qb5gx0na1gq07mvvgxilg26c6-stdenv-linux.drv` | `out` | `/nix/store/bds9i60lxg8viivxw59b9l18hl8h1vcd-stdenv-linux` |
| `xm2s18zsz83r2jshyy9196qbadahwfbn-gmp-with-cxx-6.3.0.drv` | `dev` | `/nix/store/gqix853zzc42gx77vp81xg3wq5bi9s8b-gmp-with-cxx-6.3.0-dev` |

Complete recursive fixture/candidate derivation graph was captured using
`nix derivation show --recursive /nix/store/vg23dzka1i0dw28fy3kl4wssyms484yx-livepatch_7-exact-candidate.ko.drv`.
The disposable [candidate-derivations.json](candidate-derivations.json) contains
2,874 derivations, 8,948,367 bytes; SHA-256
`89db60eaa48659f58d6075aa969eea8dcfd9468632893f5ac8ecda57d8d54839`.
It preserves all derivation environments, phases, source inputs and selected
edges, including the current and frozen package sets. Recreate it from the
immutable root revision and recipes above if raw evidence is later discarded.

## Cache-only reproduction and limits

From the session-owned clean worktree at the recorded revision:

```sh
nix-instantiate tests/fixtures/livepatch -A corrected
nix derivation show /nix/store/vg23dzka1i0dw28fy3kl4wssyms484yx-livepatch_7-exact-candidate.ko.drv
nix copy --from https://cache.vpsadminos.org /nix/store/qi47yi2g9kp89dv0h8jxwndm89vbq6az-livepatch_7-6.12.95
sha256sum /nix/store/qi47yi2g9kp89dv0h8jxwndm89vbq6az-livepatch_7-6.12.95/lib/modules/6.12.95/extra/livepatch_7.ko
printf '%s  %s\n' 573e8d1e05433be7c4eab361bb733e92977496f6437b43a4af1e5d21d2452d9d /nix/store/qi47yi2g9kp89dv0h8jxwndm89vbq6az-livepatch_7-6.12.95/lib/modules/6.12.95/extra/livepatch_7.ko | sha256sum --check --status
```

The final command's expected result is exit 1. These commands resolve the
recipe and copy existing bytes; none asks Nix to build a kernel or module.
Use the mandatory fresh watcher for a long/uncertain copy. If this exact cache
output disappears, the copy fails rather than compiling a replacement; that
failure does not authorize a rebuild.

This proves that the currently published candidate fails the immutable byte pin,
and supplies its declared source/input graph. It does not prove a clean rebuild
is bit reproducible or identify the byte-changing input, establish import CRC
compatibility, qualify runtime transitions/performance, or establish the last
green's exact module identity. Nix input-addressed derivation identity alone is
not a byte reproducibility guarantee. The repository specifically documents
random signing-key generation for the original boot kernel; its frozen boot
archives and identity checks must remain intact.

No production state, schemas, APIs, protocols, deployment order or rollback
behavior was changed by this package. No correction is implemented or endorsed
by changing the reviewed hash. The lead and architect own the proposed smallest
correction and further acceptance boundaries.

## Revised proposal: current producer and fixed boot ABI

Read-only source/receipt analysis after the user's direction to keep nixpkgs
moving and eliminate strict candidate-byte checks. No further Nix evaluation,
copy, build or test was run. The fixed digest described above is a requirement
of the existing fixture, not a requirement to retain that fixture design.

Pinning build support does **not inherently require recompiling the guest's
boot kernel**. `boot-6.12.95/default.nix` restores its `out` and `dev` from
checked archives. The recorded restore derivation has no original Linux build
edge. The boot-base configuration substitutes these restored outputs while
deliberately retaining current package metadata/native inputs. A narrowly
changed helper can therefore have different derivation inputs without changing
the restored boot bytes. This does not establish that an arbitrary proposed
support pin would be cache-complete or inexpensive; no alternate graph was
evaluated, and a freeze is not necessary to the revised ordinary-CI proposal.

The ordinary current livepatch producer has a separate real kernel dependency.
Its current ZFS builtin input
`padca4x3klcsakr8abrfid3gv6ymfc92-zfs-builtin-2.3-vpsadminos-6.12.95.drv`
selects `dev` from
`402pp8zff2p4d5gyxgb27q063b60bwnz-linux-6.12.95.drv`, yielding
`/nix/store/sv79x5grw9hzmc2fa31rpd2yyz47005k-linux-6.12.95-dev`.
`boot.kernelForBuiltinsConfig` supplies that current plain kernel;
`os/packages/zfs/default.nix` uses its development tree for configure probes.
The Linux recipe produces `out` and `dev` together, builds `vmlinux` and
modules, and installs `vmlinux` in `dev`. An unavailable required `dev` can thus
cause a full plain-kernel build. It is distinct from the archived guest boot
kernel. Removing a candidate SHA assertion does not remove this dependency.

For the recorded current inputs, the completed signed-cache copy already
provides the full candidate output. Existing `ci-toplevel` wiring includes the
ordinary current `.95` livepatch package, and CI builds, uploads and caches it
before lifecycle jobs (`needs: build`). Ordinary CI can consume that current
producer without freezing root nixpkgs or requiring equality with the historical
`573e...` candidate. This is a proposal about which artifact CI tests, not proof
that the measured `7c4d...` module is ABI-compatible or runtime-qualified.
Existing cache policy still applies: an unexpected local kernel build must stop
for diagnosis; a missing required output belongs in builder/cache coverage,
not in recurring local rebuilds. Cache availability for a future or alternate
graph is not established by the present receipt.

Fixed boot-image/notes identity and current candidate-byte equality answer
different questions. Moving build support and removing historical candidate
equality need not alter the fixed boot ABI. Root input drift remains a likely
regression mechanism; the particular byte-changing input and the new candidate's
ABI/runtime behavior are not proven by this package.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/>
