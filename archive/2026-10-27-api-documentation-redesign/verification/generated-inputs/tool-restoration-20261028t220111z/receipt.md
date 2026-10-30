# Exact verification-tool restoration

Restored only the four literal declared outputs from cache.nixos.org with one
`nix copy --from https://cache.nixos.org` command, exit0. No flake evaluation,
shell hooks, build-from-source, profile install, replacement version, lock/graph
change or trust bypass. Default require-sigs was true; existing trusted keys
unchanged. This is prepared-input restoration, not a gate/application pass.

- `/nix/store/fkz7zn1a0yiryf9kri2yh1s12k1sv557-go-1.26.10`: `sha256-TFzcmMB2/qWIp6RZmgoKHEqmLMA1TY0A8tIVh7US6w0=`; deriver `/nix/store/mxqlh07a9kdcabldzlwwrpacvf4qnnzq-go-1.26.10.drv`.
- `/nix/store/l3jrya2cdjmzxgdpnxzwvx3h416lcbr6-cargo-1.99.0`: `sha256-xeAl+jN8MZRUIkWQKKLAuU/ER3xOoo5WKHVJZi7pvxg=`; deriver `/nix/store/45ial5wyx19y9hbfz1asqbzyx1vq4gdz-cargo-1.99.0.drv`.
- `/nix/store/vwgbz9vm1gyxqn6z4fg1jd6va2nzfa3m-rustfmt-1.99.0`: `sha256-M7Xd9Ib6to0rJTCz9NU6GBr29emGo0UnNVPPfz0RNu0=`; deriver `/nix/store/s4cslhsi7814q0a8ph8pk9z64i5sigjz-rustfmt-1.99.0.drv`.
- `/nix/store/lgrjxh2j5dqvdifh2lhrj2w0c0g5i1jg-uv-0.13.4`: `sha256-F9JrOlA1CmUl4RQwjF+iuEt1t+Ns9KsKo5E2ldyX//s=`; deriver `/nix/store/j99d3cz8m58bz6bf7fpfq8rjcqjcvnmp-uv-0.13.4.drv`.

Before: exact33-path remote metadata closure,29 paths locally registered with
equal NAR hashes/references, only four absent;339127832 uncompressed NAR bytes
missing (complete closure2100758160 bytes). Four StorePath/Deriver/NAR hashes
match the design literal table and retained locked-shell provenance.

After: native `nix store verify --recursive` actually succeeded, exit0, with
content/signature verification enabled. All33 locally registered StorePaths,
NARHash, Deriver, references and requisites equal exact trusted-cache metadata.
No merely advertised HTTP200/signature is treated as integrity proof. Exact
commands/exits/stdout/stderr/metadata are adjacent. Registered GC roots confirmed
through native `nix-store --query --roots`, using ordinary indirect add-root
mechanism under verification/generated-inputs/tool-roots; no roots removed or
global configuration changed. Root names equal the exact four output basenames
and gc-roots.json contains absolute root/store pairs. Keep roots while M8
verification is pending; no delayed cleanup or lifecycle action scheduled.

Static runtime support proof: declared rustc-wrapper6l9kbzxw... executes exactly
rustc1qg7z7...; both occur in the verified33 closure. Recorded root stdenv
an9g93vg... remains present, its setup binds gcc-wrapper r5ri78..., existing cc
resolves within that declared wrapper; pkg-config/OpenSSL/libffi declaration
paths remain present. Scripts/hashes/exact paths are in runtime-and-linker-
support.json. No restored compiler/tool-version command executed. Presence and
this static support binding do not claim successful later compilation.

Fresh standalone watcher native01a18488-1026-7ef2-ad1f-0304f36c79fc used retained
3ff7 catalog Luna/low utility dw_261a107...; current installed495e catalog selected
full_access. Explicit CLI --sandbox danger-full-access/--ask-for-approval never
and actual native header/turn_context were verified before command launch;
policy.json/native-launch-proof.json/native-turn-context-proof.json retained.
Watcher owned the sole operation/logs/PIDs; no retries/substitutions/diagnosis.

Operation elapsed11.228s; copy2.444s, native recursive verification5.670s.

All2148 protected files match before/after, including publishedTS0.30.2 exact
runtime/declarations, independentMSRV1.95, root/server/Go/Rust graphs/locks,
Python/JS, preview and calibrated frozen performance Ruby7b77/budgets/reference.
Owner0 source/Git/hooks package was untouched; no source/index/head/config/Git
command occurred here. M8 final affected source must bind later acceptance.
Cargo/generated-lock and npm/uv isolated dependency-cache completeness remain
unproven. No Go/TS/Rust/installed/performance gate, test, tool-version, listener,
fixture, compiler, service/provider/TLS/peer action ran.

All command and watcher handles complete; no active owned process or uncertain
effect. Utility capacity explicitly RELEASED. Later M8 gates require separate
review/execution/capacity grant. Prior missing-input records remain historical;
the restoration adds this receipt without rewriting their actual observations.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
