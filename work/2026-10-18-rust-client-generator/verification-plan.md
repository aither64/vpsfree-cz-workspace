# Post-review verification operations

Do not execute until all intended deliverables are committed, quick checks pass,
and mandatory independent final review is complete. Fresh watcher per operation;
retain exact revisions, logs and exit codes. Owners diagnose/fix failures.

## HaveAPI runtime

In session HaveAPI worktree, pinned client-rust environment:

- cargo test --locked --manifest-path clients/rust/runtime/Cargo.toml
- cargo test --locked --manifest-path clients/rust/runtime/Cargo.toml --features blocking
- cargo clippy --locked --manifest-path clients/rust/runtime/Cargo.toml --all-targets --all-features -- -D warnings

## Generated fixtures and actual vpsAdmin

Generic HaveAPI runner:
`env HAVEAPI_RUST_INTEGRATION=1 nix develop .#client-rust --command ruby clients/rust/spec/integration/run.rb`
Set TMPDIR to existing private session-artifacts directory; harness owns children.

Actual vpsAdmin runner:
`env VPSADMIN_REAL_INTEGRATION=1 ruby clients/rust/spec/integration/run_vpsadmin.rb --source-root /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-18-rust-client-generator/vpsadmin --client-root /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-18-rust-client-generator/vpsadmin-rust-client --artifacts SESSION_PRIVATE_ARTIFACTS`
The wrapper owns loopback server/private DB and exact real_vpsadmin ignored target.
No production mutations; no existing arbitrary database allowed.

## Actual generated crate and package

In committed client worktree pinned shell:

- cargo test --locked --all-targets
- cargo test --locked --all-targets --features blocking
- cargo doc --locked --all-features --no-deps
- cargo package --locked
- public read-only Cluster public_stats smoke via generated clients
- generator gem build/extract and generation using saved snapshot, package inventory

## MSRV1.95

Use same committed client Cargo.lock, current Nix native dependencies, separate
exact Rust1.95 evaluated from historical nixpkgs29916453413845e54a65b8a1cf996842300cd299.
No cargo update, formatter change, or current Nix pin downgrade. Exact compiler
and cargo paths supplied by architect; acquire only as part of post-review watcher.
Check --locked --all-targets both default and blocking. Runtime behavior already
covered by current pinned compiler matrix; avoid redundant full-suite repetition.

## Exact MSRV environment (architect verified read-only)

From the committed client root, after review:

```sh
nix develop --no-write-lock-file .#default --command \
  nix shell \
    github:NixOS/nixpkgs/29916453413845e54a65b8a1cf996842300cd299#rustc \
    github:NixOS/nixpkgs/29916453413845e54a65b8a1cf996842300cd299#cargo \
    --command bash -euo pipefail -c '
      export RUSTC=/nix/store/wnhmqix7bippbbzasj29qiyb422g9asg-rustc-wrapper-1.95.0/bin/rustc
      export RUSTDOC=/nix/store/wnhmqix7bippbbzasj29qiyb422g9asg-rustc-wrapper-1.95.0/bin/rustdoc
      export CARGO_TARGET_DIR=target/msrv-1.95
      unset RUSTC_WRAPPER RUSTC_WORKSPACE_WRAPPER
      msrv_cargo=/nix/store/z480b23kymbmrijrl49246mrzyphli15-cargo-1.95.0/bin/cargo
      "$RUSTC" --version --verbose
      "$msrv_cargo" --version --verbose
      "$msrv_cargo" check --locked --all-targets
      "$msrv_cargo" check --locked --all-targets --features blocking
    '
```

Evaluated x86_64-linux output paths, not acquired/executed yet. No current Nix
input change or implicit lock refresh. Expected rustc/cargo1.95.0.

## Public read-only generated-client smoke

Verification-only external harness at artifacts/live-public-smoke. Two fixed
https://api.vpsfree.cz cluster.public_stats GETs, async then blocking outside
runtime, no auth or mutations; output PASS only after described field presence.
Source sha a5a5ffb4d4333baf036a462f0c41ecd3090dbc26250711f48e97bfd3118fd302.
Prepared headfe7f7a7; guard must bind final post-review head if remediated.
Run exact README command through fresh watcher after review/build; no live call
executed at preparation. Artifact uses path dependency actual client and locked
deps, publish=false; not part of product package.
