# Affected final review packet — composed naming fixture hooks

Requested review: general, architecture/repetition, scope/proportionality and
whole-final-history/no-migration conclusion, assigned by lead after handback.
No reviewer was launched by implementer3. Medium risk: a reversible, bounded
compile-only fixture composition correction at an existing package override
boundary. No product/runtime/auth/state/API/native/VM policy changes.

Repository: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-workspace-session-ui/dev-workspace`.
Session plan/state: `/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/plan.md` and `/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/state.md`; lead owns coordination.
Base: `960dd816b7e56cbdd4af0da15bf0b26257775151`.
Prior reviewed/published head: `c31fdd9f6a86f2eb0e6b87001d6892b820bce2fe`, tree `6210fb758fcc80948c1ae842cad0f3520b5b189d`.
Final head: `f520a39511602cf83f3dda96b6a007a596d3b258`, tree `d293ea527954b62432ba67b4b97c7b5c8abba113`.
Both owning-unit parents: `20cf16b22487e2dc2fdfdbfa1ae1d3208fb48b9a`.

## Outcome and acceptance criteria

The fixture's final composed derivation clears postInstall/postFixup after
`package.override` returns, including extension overlays replayed around builder
argument re-entry. Keep the replacement buildGoModule, both inner clears,
package.go/goModules/src/postPatch/preBuild/vendorHash, tag/subPackages,
buildTestBinaries, doCheck=false and empty checkPhase exactly as before.
Product hooks and all original inspector assertions remain immutable.

The actual parent-accepted hook observation429898f2975d98b36814cbd812d4d7c19525238d4c81fe70a1d3145d67711164
proved the condition in architect49776908. The old fixture install string was
precisely the167-byte extension migration symlink suffix, fixup empty, with
exposed/drvAttrs equality and same observed tools path as the product tail.
`observation-confirmation.json` binds raw data, hash and independent source
comparison. That diagnostic is not successful final-fixture evaluation or build.

The complete affected source delta is `c31-to-final.diff`: one wrapper pair,
final overrideAttrs with two empty strings, and one short rationale comment in
`nix/tests/naming-runtime.nix`. The exact prior builder body is preserved by
byte projection. No new helper/export/assertion weakening/test suite. The
constructor remains fixture/manifest/managed/realCanaryDriver only, selected by
existing flake export and documented exact final assembled package/provenance.

## History, inputs and migrations

`final-series.txt` and `base-to-final.diff` cover all11 units/52 changed paths.
`old-series.txt`, `old-base-to-head.diff`, `old-new-range-diff.txt` and
`equivalence-and-history.json` bind the complete comparison. The first10 commits
are literally identical; only the final existing fixture/export/docs unit is
amended. Its original subject/purpose are retained, with an added explanatory
hook-composition paragraph. No extra correction commit remains. This is the
lead's explicitly coordinated consolidation; no fetch/rebase/push/default edit.

The same parent identity proves no other logical unit was rewritten. The
original final unit's four paths stay the same. All608 other files and all609
modes/type inventory remain exactly equal to c31; final full609 blob/mode/byte/
SHA256 inventory equals the source used by quicks and the current filesystem.
`final-manifest.json` and `tested-corrected-manifest.json` provide the proof.
Clean index/worktree recorded in `final-status.txt` and raw final index retained.

No migrations: the full base-to-head migration-path inventory is empty, no
migration version was introduced/rewritten, and the one-file correction cannot
alter persistent formats. No migration merged/released/deployed/external-use
boundary is changed. The prior reviewed no-migration conclusion is retained.
Runtime protected9634151 ancestry check exited0. Extension767 and protected399
lineage remain those of the unchanged accepted input graph/ancestry receipts;
no extension Git window was inspected. One existing dependency/client upgrade
stream remains in bd78848f; no new or repeated input/pin/lock/generated update.

Old c31 is retained under
`refs/dev-session/2026-10-24-workspace-session-ui/implementer3/pre-hook-fix-c31`
and in a verified complete `published-c31.bundle`. The old origin feature
tracking ref remains c31. `preservation.json` binds bundle/index/manifest.
Both old/new commit raw objects and the exact message file are retained.

## Quick verification and documentation

Actual syntax: `/run/current-system/sw/bin/nix-instantiate --parse nix/tests/naming-runtime.nix`,
exit0 in0.116831s, no stderr. The selected alias resolves to
`/nix/store/z4wkkj3ncr69vgrb3020saqx1c8mfsjj-nix-2.34.9/bin/nix`, SHA256 `6b20a492de8d0b2cf67e68d4cad1773a132753aa2909d8ddcdd44345c869e171`.
This repeats the existing declared focused parse command without entering a
Nix shell, evaluating a selection or realizing outputs. Actual whitespace/style:
`git diff --check -- nix/tests/naming-runtime.nix`, exit0 in0.018851s.
No formatter configuration/export or framework hook is declared; normal Git
hooks were not bypassed. Exact existing-style/minimal byte projection passed.
Commit --amend -F ran ordinarily, actual0, with preserved author and normal
Git hook selection. `quick-results.json` records selected tools/commands/effects.

Quicks ran c31 plus this exact file correction before amend, then all609 checked
bytes/modes were proven identical to the committed final tree. They are not
invented execution against a new NAR. Unchanged tests were not rerun. No Nix
eval/output realization, Go/Ruby/browser/native/provider/VM action occurred.
One read-only abbreviated-base diff failed128 due ambiguous960dd tree/commit;
full recorded960dd816 was used afterward, with no source/index/ref effect.

Checked `docs/codex-package.md` compile-only contract and package recovery
section in `docs/workspace-portal.md`; no doc edit is needed by architect's
explicit disposition. The short owning source comment explains override order.
Raw0.164/client025, product hooks, manifest bounds, two slots/30s and all managed/
real stop/network/state assertions are untouched. Original inspector
8e21b2457a343c819e1e6bba9c02b391c98555b60d5b3bdf0e8a4c1d918d1ff3 remains unchanged.

## Subsequent gates and exclusions

The prior c31/5dg source/vendor/browser/consumer/eval receipts remain historical.
The new source NAR and source-bound derivation identities are unknown. Separate
lead release must cover affected review, coherent publication/vendor lineage,
consumer repins and final complete input receipts, unchanged full inspector plus
effective-hook evidence, immediate availability/identity and recursive graph
inspection before any output build. Generic vendor proof does not identify the
actual composed d58 package's compiler/modules. No old failure or observed
metadata-only derivation path is promoted to acceptance.

Dedicated disposable real Luna home/account remains unresolved. No production
credentials, native/provider request, VM, build, copy, activation, claim,
integration, deployment, cleanup or session lifecycle operation authorized.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/
