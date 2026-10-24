# Supplemental public live smoke

Verification-only external Cargo harness. It makes exactly two unauthenticated
GET requests to `https://api.vpsfree.cz/v7.0/cluster/public_stats`, one through
each generated transport. It uses the generated output model, checks the three
public statistic fields are present, and prints pass/status only. It never
prints values, bodies, credentials or error details. The async runtime is
dropped before the blocking client's construction, use and drop.

Prepared against client commit
`62753f006d7bd3e5befe1033c49a2c630ca3ff02`. Recheck this binding if review fixes
change the client. Compilation and live execution have not run during harness
preparation. This is supplemental evidence; it does not replace deterministic
generation, feature/MSRV builds or disposable-server acceptance.

After final review and the main build gates, the verification watcher can run:

```sh
workspace=/home/aither/workspace/ai/vpsfree.cz
client="$workspace/worktrees/2026-10-18-rust-client-generator/vpsadmin-rust-client"
harness="$workspace/work/2026-10-18-rust-client-generator/artifacts/live-public-smoke"
test "$(git -C "$client" rev-parse HEAD)" = 62753f006d7bd3e5befe1033c49a2c630ca3ff02
test "$(sha256sum "$harness/src/main.rs" | cut -d ' ' -f1)" = a5a5ffb4d4333baf036a462f0c41ecd3090dbc26250711f48e97bfd3118fd302
test "$(sha256sum "$harness/Cargo.toml" | cut -d ' ' -f1)" = c890f49123db5dff923bbde85db37fd2c39cacf3051b1b1708071599e45ffa4f
nix develop "$client" --command cargo run --locked \
  --manifest-path "$harness/Cargo.toml"
```

The source hash above is for `src/main.rs`; the separate manifest hash is for
`Cargo.toml`. The previous watcher stopped before running because it hashed
`Cargo.toml` while checking the expected source hash. Both files remain unchanged.

Expected successful output:

```text
async public_stats PASS HTTP 200
blocking public_stats PASS HTTP 200
```
