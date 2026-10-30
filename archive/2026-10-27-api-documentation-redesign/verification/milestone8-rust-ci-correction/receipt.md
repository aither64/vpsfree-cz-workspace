# M8 Rust CI fixture boundary correction

Committed `73c1cc3cc71facf0f17c2f7f44e8e4089907a3d1`, tree
`5b9c52d0f0d81957bbca227d254e2e5b09b53373`, parent
`1cec2cae3c1266e0e569f5b537af1ac4d37a09e4`.
Exactly six approved paths, +61/-48. ready-owned.json/patch and after.json bind
checked=staged=committed=index=current bytes/modes. Owner0's two preceding server
spec corrections remain exact; combined e5ea→HEAD changes exactly eight paths,
listed/hashed in combined-paths.json, with complete combined-e5ea.patch.

CI40789709969 failed162/1 because the real-Rack documentation fixture test ran
with generator units before the server bundle was prepared. Frozen Bundler
rejected platforms[] versus x86_64-linux before fixture requests. Original raw
log remains unchanged at verification/current-CI-e5ea/logs/40789709969/rust-client/
4_Generator unit specs and Ruby style.txt; SHA256da6ec33722ac85a551227634e6cee2e3e007ae115ab50119a47a029384daa501.
No renderer/provider failure is inferred from that CI attempt.

Moved only the complete Rack case from unit/documentation_harness_spec.rb into
existing integration/fixture_actions_spec.rb. The sole case-text change is the
relative fixture path; exact before/after blocks are retained. Existing first
fixture-action case is byte-identical. Normal/documentation modes retain Basic,
invalid Basic rejection, OPTIONS-discovered token request, actual issued-token
value/authentication, valid/arbitrary OAuth outcomes, isolated server Gemfile/
gemhome/clearedGEM_PATH, Bundler.with_unbundled_env and BUNDLE_FROZEN=true.
No fixture/harness implementation, provider or product source changed.

The already-prepared CI protocol stage now runs the existing fixture spec before
the unchanged protocol runner, in one Rust component bash-euc context. All prior
steps, server preparation order and imported action refs are unchanged. No new
action ref was selected or dependency refreshed. Full Makefile test-rust gains
only the fixture spec line before the runner; RUST_ENV and test-rust-unit are
unchanged. Narrow Rust development/integration README text states the real Rack
application requires its prepared server bundle without listener/Cargo; quick
units need only their component bundle. Plain prose was checked with the writing
skill. These component docs are outside packaged shared-doc copy inputs; no
make doc ran or is required for this change.

Actual checks, once each, seed50232:

- Rust component spec/unit:161 examples,0 failures (3.39s examples+.427s load).
- Prepared fixture_actions_spec:2 examples,0 failures (5.72s+.220s load), including
  both normal/documentation modes in the moved example.
- Changed-spec RuboCop:2 files,0 offenses.
- Workflow YAML parsed; exact block relocation, preserved first case, workflow
  preparation/order/fail-fast and unchanged Makefile quick target verified.
- Owned diff whitespace check passed.

Existing isolated Rust Ruby/component bundle and separately prepared frozen
server/root bundle ran under declared immutable Ruby3.4.11 and existing tools.
No Nix, dependency resolution/install/repair, lock/platform change, compiler,
runtime/wire/MSRV/performance gate, listener, network, CIretry or utility.
Routine unit warnings about temporary duplicate version constants are retained
in unit.stderr. No actual test/lint/hook failure occurred. Two local commit-message
width assertions stopped before hooks; paragraphs were mechanically wrapped
without source/staged changes. Normal HaveapiI18n/RuboCop/message hooks passed.
TextWidth warned that the62-character subject exceeds preferred60, within hard80;
no bypass or hook configuration change.

After commit, all902 unrelated tracked hashes/modes, including owner0's two
checked server specs, are unchanged. The complete combined-eight-path inventory
proves application/renderers/runtime/fixture/asset bytes equal published e5ea.
All2148 protected inputs/root-server-Rust locks remain unchanged; logical flags
match preflight/allH. Index/worktree are fully clean. Every owned command handle
returned; no active child/utility or uncertain mutation. Existing e5ea/browser/
installed/all-client/source/review evidence retains its actual scope; no blanket
rerun or new gate acceptance is claimed.

SOURCE/Git/hooks slot explicitly RELEASED. Main owns the short affected-lane
review of the new verification boundary and combined two test fixes, followed by
any mechanical Core fold/scoped input rebinding. No history fold, publication,
preview, peer, provider/TLS, service or lifecycle operation occurred.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
