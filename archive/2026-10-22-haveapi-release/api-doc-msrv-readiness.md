# Rust rendered-example MSRV readiness

Observed 2026-10-22, 16:27–16:32 UTC. Exact session/environment binding verified.
Read-only source/toolchain inspection; this receipt is the only file written.
No installs, builds, acceptance execution, application changes or Git mutations.

## Conclusion and exact selection

The repository development compiler is **Rust 1.99.0**, not 1.95. Its pinned
Nix shell selects Cargo 1.99.0. An independently selected **Rust/Cargo 1.95.0**
pair is already present locally; use the non-bootstrap Nix packages below.
Thus the existing runner can exercise two distinct compiler versions without
changing the flake or installing a toolchain. Available paths were checked by
executing only `--version --verbose`.

| Purpose | Executable | Reported identity |
| --- | --- | --- |
| Development Cargo | `/nix/store/1jwkiz96iwqdhm4bh2hvgd86ysb0b67q-cargo-1.99.0/bin/cargo` | 1.99.0, commit `5f94df4789f005f9a352888e8355ffc645b7ed0e` |
| Development rustc | `/nix/store/6l9kbzxwq9ij2lcmwl2qb1jdpqisjr8l-rustc-wrapper-1.99.0/bin/rustc` | 1.99.0, commit `b940084d7eb6a299eb4bfeb8e34901bc051e7ac4`, LLVM 21.1.8 |
| MSRV Cargo | `/nix/store/rai05nypxnmj22l65nwsk5xjsaq8s4vc-cargo-1.95.0/bin/cargo` | 1.95.0, commit `f2d3ce0bd7f24a49f8f72d9000448f8838c4e850` |
| MSRV rustc | `/nix/store/m4hrdkg9ypcw8y1banfc26q3f27kfqvb-rustc-wrapper-1.95.0/bin/rustc` | 1.95.0, commit `59807616e1fa2540724bfbac14d7976d7e4a3860`, LLVM 21.1.8 |
| Generation formatter | `/nix/store/zfrqd9ahnccql0zgzgc5swwi4zmm14zl-rustfmt-1.99.0/bin/rustfmt` | `rustfmt 1.10.0` |

All compiler hosts are `x86_64-unknown-linux-gnu`; Nix system is x86_64-linux.
The MSRV Cargo wrapper appends its matching rustc package to PATH, but the
runner additionally sets explicit `RUSTC` for the MSRV pass. Do not substitute
the separately present bootstrap compiler. Keep generation on the fixture's
declared formatter, not an MSRV formatter selected by accident.

## Source and input identity

HaveAPI HEAD observed during source inventory:
`34174e86ef451c21ab9b7c29d47b3f1a7887f535`. Work was still being committed;
this is an observation, not the final reviewed verification head. Record the
final exact head and working-tree state before execution, and retain the actual
generated fixture Cargo.lock and generator manifest in verification evidence.

The only flake input is NixOS/nixpkgs revision
`02c087f3fe673c9e317f206a627cb6b910336dbe`, NAR hash
`sha256-IoNisKcGbUjdd45qCqywGMCYmZ5EnkxezvLII0FWwNA=`. Evaluated source is
`/nix/store/87lfqfz7mc5dm4w75qikxhd6lkr9jisr-source`. `flake.nix` imports this
input directly; `devShells.x86_64-linux.client-rust.nativeBuildInputs` supplies
the development executables above. No rust-overlay/fenix/rustup input exists.
The ambient shell has no rustc/cargo/rustup selection.

MSRV packages are independently identified by their retained Nix derivations;
they are not claimed to come from the current HaveAPI flake's default Rust.
The historical nixpkgs revision producing them was not established or needed
for the exact local selection. Their derivations retain the complete input graph:

- Cargo: `/nix/store/gc1x597lnjw05j6w6kmvhpzammzymyi9-cargo-1.95.0.drv`
- Compiler wrapper: `/nix/store/dmr4d3bakwng8mjqij1x5q28ng5byrdv-rustc-wrapper-1.95.0.drv`
- Compiler: `/nix/store/l4l7ijl3ixk0fnkplsd5piwixqcihn38-rustc-1.95.0.drv`
- Shared source: `/nix/store/6wq4v4hfgx2875qszshp9x06wmlc5z65-rustc-1.95.0-src.tar.gz`,
  derivation `/nix/store/51j2ljrnyx9h7nw34j867284gm3ip5wa-rustc-1.95.0-src.tar.gz.drv`,
  flat source hash `sha256-6puCqD5GlnU3w1ac6db6FoEcBDqW5lE3bDSecCQcpRU=`.

`nix-store --query --requisites` of the Cargo and compiler-wrapper derivations
produced 1,644 unique input/source paths. SHA-256 of sorted paths, joined with
newlines and one trailing newline:
`cbac22d4dcfde45b94bc1d32728b989fa36d1166f547f87496691103805c53e1`.
Use those two derivation roots to inspect/reproduce the complete graph; do not
substitute a package selected only by a matching version string. Cargo's inputs
include its two CVE patches and matching compiler; the graph also pins LLVM,
bootstrap tools, build scripts and native libraries.

NAR hashes from the local Nix database:

- MSRV Cargo: `sha256:06ziy9i9g1q57vxl2dzm8kkf8ydi7vv81mlajb7hfmjbkfx2zzj6`
- MSRV rustc wrapper: `sha256:034d87pfdh8r3xag92lb71zv8j3bfsczfpkpy9f5dzxw8kdz7ly5`

Observed file SHA-256 values (refresh after final review if changed):

| File | SHA-256 |
| --- | --- |
| flake.nix | e5b1103d90acadf0929ee7a6e2ff2e7527fb4c5985baeccf2da6d59df8c4870c |
| flake.lock | a52bdf3a3b9a069175d3af298234c3cf7adeba54540833eed6ad902e9ccc0a64 |
| clients/rust/Gemfile.lock | aed5ca5faa7faa3439069bda4982663108083131bcd996b4c160f2641416e23a |
| clients/rust/runtime/Cargo.lock | 48e682446003c37e3ec111308a35a49fb895affe8b0ea3f7ae109b6655f00746 |
| clients/rust/spec/documentation/run.rb | 8c2b7c19191610d85955ce74420ebc96e5ab1ee46f4590285a6eb069384eda0a |
| clients/rust/spec/documentation/cases.rb | 00a1cceefe313748be471118e675c64d2e17954b7048fefc0b96d0cf7247ab9b |
| clients/rust/lib/haveapi/rust_client/documentation.rb | e628cd3dc72703cba30721b372a9d0e1aae46bd9989a8e92e7770627c9a81f01 |

## Smallest post-review command — not executed

Use the final reviewed HaveAPI worktree and a fresh verification watcher. Rust
and server bundles must be prepared under repository procedures; the component
shell may run dependency setup. This inspection deliberately did not enter it.

```sh
HAVEAPI_RUST_DOCUMENTATION=1 \
HAVEAPI_RUST_MSRV_CARGO=/nix/store/rai05nypxnmj22l65nwsk5xjsaq8s4vc-cargo-1.95.0/bin/cargo \
HAVEAPI_RUST_MSRV_RUSTC=/nix/store/m4hrdkg9ypcw8y1banfc26q3f27kfqvb-rustc-wrapper-1.95.0/bin/rustc \
nix develop .#client-rust --command ruby clients/rust/spec/documentation/run.rb
```

Before execution record `cargo --version --verbose`, `rustc --version --verbose`
and `rustfmt --version` from the selected development shell, plus the explicit
MSRV paths. Refuse inherited `RUSTC`/compiler wrappers that would substitute the
development pass. The inspected runner validates MSRV rustc starts with 1.95,
generates once using the development formatter, creates a dependency lock, then
checks/runs rendered async and blocking examples with both toolchains at `/`
and `/mounted/api/`. It does not yet prove acceptance until actually executed.
The generated lock is distinct from the private runtime harness lock above;
record it rather than treating the harness lock as its dependency graph.

No alternate compiler is needed. If future pins select 1.95 for development,
two identical-version passes prove that exact MSRV and reproducibility, not
forward compatibility with a newer compiler. The smallest alternate then is
an explicitly pinned newer compiler/Cargo pair for the development pass while
retaining these 1.95 paths. No new flake/toolchain feature is required now.
