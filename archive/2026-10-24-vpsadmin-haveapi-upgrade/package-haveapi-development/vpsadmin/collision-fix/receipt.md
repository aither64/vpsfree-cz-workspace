# Git-gem collision correction: committed quick-pass packet

Lead-authorized design.md:3373 implemented; awaiting affected independent review.
No actual API/services retry, publication, canonical/live change or activation.

- Complete range: `08c3bd7e3cb4dc324a0381df6a1eec190daab1a7..94ccabc5471a1b8f0ecbca66f3fe0eec4749a338` (four commits, 39 final paths).
- Preserved published/deployed boundary: `8102179cf7f7e9bb534965c8acb3e02ef723045f`.
- Two consolidated unpublished commits: `a15e0882f87e557ac3f66c0efc2893ae98a2ec3d` (package), `94ccabc5471a1b8f0ecbca66f3fe0eec4749a338` (consumer).
- New tree: `65381306e6c32a55f8238ee3a8ec05a7316b1c2b`. Old failed/reviewed head `cba626581a698256e873319983ac51312f40398c`, tree `40375b83d5077e0fe16c0c47b8307ff467a82b4f`.
- Old/new range comparison: `8102179..cba6265` versus `8102179..94ccabc`.
  Only common.nix and the owning docs paragraph differ; every tracked entry outside
  those two paths is byte/mode/identity equal. **No migrations or schema changes.**

[Final proof](final-proof.json), [complete series](complete-series.txt),
[full diff](complete-feature.diff), [two-path delta](old-new.diff),
[range comparison](range-diff.txt), [diffstat](diffstat.txt).
Old failed-cba and reviewed-c413 refs remain; published8102 and its two commits
are unchanged. No obsolete development-pin stream remains: the two unpublished
commits are reconstructed directly on8102. Retaining the released0312 stream
protects supported CLI/PHP/JS and deployed rollback, as previously reviewed.

## Correction and evidence

All five named Git-gem builds now run existing root make-doc before normal
staging/serialization. PostInstall restores RUBYOPT, checks the installer's exact
output path and one HaveAPI cache entry, and removes only checkout/cache index
files before inherited postInstall. Whole source, Git objects/HEAD/cache, source,
serialized specs, libraries/assets/bin and normal installer/discovery remain.
Owning docs now describe this boundary. No pin/lock/dependency/config change.

Command: `bash collision-fix/run.sh` (absolute paths in retained script).
Fresh retained840 Luna/low thread01a184a4-3590-72f0-9cca-97785c60832f,
actual full-access/never policy verified, exec99847; native batch0, about153s.
[Watcher result](watcher-result.md), [normal operation/hooks](operation.log),
[quick result](result.json), [evaluated actual gem hooks](actual-hooks.json).

- All 122 actual gem derivation hooks evaluated; exactly the five HaveAPI
  Git gems receive docs preparation and index removal, with the same immutable source.
- Both exact index paths exist in all five retained real outputs. The new hook
  ran on a disposable copy of the real server output, never on Nix outputs.
  Exactly those two files disappeared; all other file bytes/modes/symlinks matched.
- All five real serialized specs loaded without indexes and retained nested
  library directories. Unset/empty/existing RUBYOPT states were restored.
- Nix format/parse/whitespace, both normal commit hooks and ordinary autosquash
  passed. Fixup message width warnings were advisory; final messages are retained.
  No repeated full/core/sample/archive/compiler/SDK checks.

Immutable HaveAPI remains d67bebcb37f2d4558a97caa208465147da19dbef,
treecd91bf06fd14d297aaa2470844f679f0998d85f9, whole-source hash
0a2y4467shd7w0bl645yc9ga20k792x5pdpjb4siac49d752mfqv.
Ignored and packaged API locks both remain SHA256
4ded33e27ae206ce6f7ea9352a591f4a373634c767c0d58bc1865717bfa1c0a6;
117 unrelated entries and all separate released consumers remain unchanged.

## Limits and handoff

Quick proof does not establish equality of new Nix output overlaps or successful
final API bundle activation. Actual all-five Nix package/docs/Bundler proof is
still pending, including lock4.0.23 versus selected installer2.7.2. Original
cba API build failure255 and five built outputs remain rooted and unchanged at
/tmp/hddc.2945ivos/roots with [original reconciliation](../postreview-continuation/reconciliation.json).
API_PACKAGE_PROOF_PASS was never reached there; services never started.

Source clean; watcher and owned command exited0, no remaining source writer or
active batch. New quick shell root: `/tmp/hdcf.cV93Xp/roots`. Disposable copy retained at
`/tmp/hdcf.cV93Xp/haveapi-output`. No rooted output was mutated or removed. Utility slot released.
Lead owns state/plan updates and assignment of retained reviewer0 packaging
lanes/history/doc compatibility. Stop here pending review before any actual API
build retry, then services. No cleanup or lifecycle action.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
