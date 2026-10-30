# Exact MSRV linker-support restoration

Restored only literal `/nix/store/qlbksf73w77ifwrr466r2f10g60kaz1d-rustup-1.29.2`
and its declared signed runtime closure from configured cache.nixos.org.
Registered deriver `/nix/store/2j417fcdm415qgsda7hippv5133gim2p-rustup-1.29.2.drv`;
NARHash `sha256-nzR+K/2lpiSqMoRZrOtvAD1GTUCHN8hsOP/gaAmXNyA=`.

Parent static proof tied the literal to retained independent1.95 ld.lld wrapper
line5, original pinned-Nixpkgs3ec636… preparation and unchanged official manifest/
compiler/Cargo hashes. No rustup/version/toolchain-install command ran. The old
claim that this absent output was merely an unnecessary preparer is corrected:
its nix-support/ld-wrapper.sh is an actual MSRV linker runtime dependency.

Before copy: trusted-cache native metadata declared27paths/86730904NARbytes,
only literalqlb absent14479384bytes. All27advertised cache.nixos.org-1 signatures;
existing26local NARHash/references matched. One exact nix copy --from
https://cache.nixos.org <literalqlb> exited0. Default require-sigs/trusted keys
unchanged. Native nix store verify --recursive actually exited0; registered
StorePath/NARHash/Deriver/references/requisites equal the exact remote closure.
Signature advertisements alone are not treated as integrity proof.

Ordinary session indirect GC root added beneath existing tool-roots for qlb;
native query confirmed it. All22earlier roots unchanged, total23. Referenced
ld-wrapper.sh exists, SHA2567f3341148afd64b9a1c530b783bbc29898769dbf06580ef236482c6392028044.
Independent1.95 compiler/Cargo/ld.lld wrapper/official manifest hashes unchanged.
All2148inputs/root-server-Go-Rust locks and source511clean remain exact; declared
stdenv/rustc-wrapper/cc support hashes unchanged. No binary rewrite, replacement,
Nix eval/build/shell/profile, dependency update, trust/config change or other
missing-output restoration. No gate ran during restoration.

One NEW retained3ff7 Luna/low native01a18535-bd21-7b51-8b4a-9a11fbcd68c8,
actual full-access-never header/turn_context verified before launch. Operation
exit0/3.753s. Initial lead progress prose contained a wrong unverified nativeID;
it was corrected immediately, with no operation/ref/source effect. Actual proofs
and corrected identity are in native-launch-proof.json and parent-reconciliation.json.
All commands/metadata/stdout/stderr/exits/roots/inputs are retained adjacent.

Restoration utility explicitly RELEASED; no active/uncertain owned process.
Next, a distinct fresh Rust-only watcher may run the unchanged native driver.
There is no supported partial selector: one full run necessarily replays old
rootdev52 before completing MSRV/root+mounted lanes. No new resume harness,
source/program rewriting, Go/TS rerun or automatic failure retry is introduced.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
