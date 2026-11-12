# C2 corrected provider pin: mechanical review binding

Owner implementer1. Status: committed and published, awaiting the lead's explicit
mechanical pin/review release before any new package or host realization.
No new candidate binary/system is built. Earlier75b/4gb/3vv review, build, NAR and
V receipts remain historical; they do not verify the corrected HTTP candidate.

## Exact history and content range

Repository `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`, own worktree
`worktrees/2026-11-10-rust-syslog-exporter/vpsfree-cz-configuration`, branch
`2026-11-10-rust-syslog-exporter`.

- Unchanged fresh remote default/base:
  **3c088a4b71881b3649441ce3c4e92c71757708e6**.
- Superseded reviewed/published head:
  **75b0af0323db1412de457cb73362fd741941eef4**, tree
  **0c409ea0ea31d6ffebba40fa6229dcc46bbef575**.
- New published head:
  **a839ccf7e7ff07ac616ad7994af33f07975bd1b5**, tree
  **514c410ea4de2e24fc4cef288eac22a359ff2465**.
- Complete new series: one coherent commit, a839ccf7,
  `syslog-exporter: use the Rust implementation`.
- Exact75b→a839 source diff: only `packages/syslog-exporter/default.nix`,
  2insertions/2deletions, substituting provider revision and source hash.
  The full tree was independently reconstructed by this exact substitution.
- Commit message updates the exact provider SHA and wraps to72columns. No other
  source difference, follow-up chain or superseded pin remains in the new series.
  SSH push used a lease requiring remote75b, then fresh SSH ls-remote verified
  a839 and unchanged master3c. Tree/index clean.
- Old and new reviewed ranges are respectively3c..75b and3c..a839. Full range-diff,
  exact tree diff, original75bcommit object and old/new tree IDs are preserved in
  `c2-artifacts/i2-{range-diff.txt,consumer-tree-diff.patch,mechanical-pin-proof.json}`
  and `c2-pre-i2-commit-object.txt`.

**No migrations**, persisted-state change, new C2 application/module/docs logic,
consumer option or input-channel change. Old75b was built/tested but never
merged/released/deployed. This amendment consolidates its unmerged provider pin
as directed; historical proof is preserved, not called merged or reverified by
old builds.

## Provider and vendor identity

Lead released provider **faf06c1185ad2f6d39286d2e33896a6455b7bea6** after reviewer0's
affected HTTP review found no findings;19quicktests/current CI42921690945 passed
per the released brief. I2 implements the accepted one-encoder/one-bounded-waiter
correction for two legitimate monitoring consumers.

Independently compared canonical exporter8ef..faf: only `src/http.rs`,
`docs/reference.md`, `docs/verification.md` differ. Full Cargo.toml/Cargo.lock,
rust-toolchain.toml, shell.nix, scripts/benchmark.py, scripts/check and pre-commit
hook bytes/blob IDs are identical. Release profiles are contained in identical
Cargo.toml; Rust1.95/package0.14.0 and all dependency records remain unchanged.
Final Cargo.lock SHA256:
`031d0b542c8a95a8e0293cd7c62aa3c052b17c29342bbec4d4195feabb78ea1e`.
Full equivalence inventory is `i2-provider-equivalence.json`.

New exact unpacked provider source:
`sha256-2ChtOI8cW7zKer4jbaD5b77Eut+Mf/NzsLc/Hwhy2TE=`,
`/nix/store/1ifcmrq7w2d86cjhqf7lsk6fcs226nqq-source`.
The missing vendor output was reconstructed from the new recipe's `.cargoDeps`
only, through a fresh installed-policy Luna/low watcher. Exit0 in16.434s proves
the unchanged hash and exact output:
`sha256-dvnEEbDRJoHlHLj/EDXp21PYrnvx5+J1+BGYQkmN7yI=`,
`/nix/store/dfpq620acg07r3zvy3kbzkrs9y92vbci-syslog-exporter-0.14.0-vendor`.
No Rust candidate compilation or host build occurred. Source/vendor are retained
under separately named own I2 input roots; prior roots remain untouched.

## Consumer evaluation and quick checks

- Package Nix parse and whitespace checks pass.
- Focused `syslog-exporter-config` flake check passes; this is the unchanged
  default/custom/disabled configuration assertion check, not a candidate build.
- Mandatory active pre-commit and commit-msg hooks pass (Nixfmt and subject/text
  checks); no bypass, reinstall or unrelated full setup check was used.
- Package derivation comparison: environment differs **only `out` and `src`**;
  builder/args/name/system and release/check/native Python inputs are identical.
- Rendered service unit differs **only the package output prefix**. CLI,
  Type=simple, account, FIFO/stateDir/listener/port/restart semantics are identical.
- Generated JSON, rsyslog.conf and logrotate.conf derivations are exactly
  unchanged. JSON remains the same67-host `k5a6bd...` path.
- All consumer module/tests/docs/flake/lock and other tree files are byte-identical
  to75b except the two recipe fields. Existing C2 review covers their logic.
- Full corrected source/lock graph and evaluated derivations are preserved as
  `i2-flake-metadata.json`, `i2-{package,host}-derivation.json`,
  `i2-host-derivation-requisites.txt`, `i2-anticipated-host-unit.service` and
  `i2-mechanical-pin-proof.json`. These are evaluation receipts, not new builds.

Anticipated corrected outputs, **not realized**:

- Package drv `/nix/store/21lm6pl39ly86srnk28417pmdqd4invk-syslog-exporter-0.14.0.drv`;
  output `/nix/store/3hk34i2k760dirn1xrarxqsrwrcryaj5-syslog-exporter-0.14.0`.
- Normal Git-flake host drv
  `/nix/store/nc86mbf1kmkwakxy1lcg87n60bxw8b1b-nixos-system-log-26.05.20261026.718f670.drv`;
  output `/nix/store/nw3d0j9hb1mrwf7hd0daxm6gk1vcfabc-nixos-system-log-26.05.20261026.718f670`.
- Corrected configuration source
  `/nix/store/xvr7fkwhwkljagh8wx5mdcrvq5a5lz4v-source`, narHash
  `sha256-/kaoo5e86AT3mvXx3XgDRqBa9mKFqHsEFbqiDj4wkEY=`.

## Review reuse boundary and remaining gates

The original C2 review bound3c..75b; I2's provider HTTP review bindsfaf. This
packet supplies the exact mechanical consumer substitution, unchanged input/
module/docs/history/no-migration proof for the lead to bind review reuse or
request bounded affected pin/history coverage. It does not self-approve reuse
or claim the new binaries pass Nix runtime checks.

After explicit release: rebuild corrected package with full19tests, then normal
host; verify exact outputs/closures and rerun V using the new Nix release binary.
Old14-test/4gb performance evidence is historical. Actual production959e/oldkgr
source/closure/retention and selected-input comparison remain applicable and
are reused without further production reads or pulls. No new deployment, copy,
dry-activation, activation, default integration or resource claim is authorized.
Stable-root migration/cleanup remains held until the new V quiescence release.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-rust-syslog-exporter/>.
