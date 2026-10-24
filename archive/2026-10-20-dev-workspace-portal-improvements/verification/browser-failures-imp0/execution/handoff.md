# Three browser-fixture corrections — execution handoff

B final clean published feature head:
**bf477e4fd39b2f66f71d40838a38511c92e3e5cd**.
Base/SSH default remains **968646471b1190c16a8cf60ff50736cd0525fa3f**.
Exact SSH lease was **3671c7901a9337d70fee0a48e2b3094926488a84**.
[Remote proof](remote-proof.txt), [CI metadata](branch-runs.json) and
[superseded-only cancellation record](cancellation.json) are retained; no CI wait
or rerun. This is source/syntax completion, **not actual-browser acceptance**.

The exact previously inspected patch75e27496 was applied to its three verified
original byte hashes. Files draft setup now precedes Files navigation; the
session-settings mock matches only `/api/models?session=example` and proves the
second model exists before selection; paging checks static normal-flow/no-overlap
plus SAME-node viewport-relative anchor continuity. Native input/singleflight,
original-byte downloads, draft preservation and original displacement bounds
remain in the fixture. No product behavior, warning/prose, asset/cache version,
dependency, API, TLS policy or timeout was changed.

The candidate and diagnosis remain preserved in `../candidate.patch`,
`../manifest.json`, `../diagnosis.md` and `../proposed-commands.md`.
No other member's source was authored or committed.

## Verification and exact scope

Only these requested quick commands ran, from the declared Nix environment:

```sh
nix develop --no-update-lock-file -c bash -c 'set -e
node --check portal/internal/web/portal_improvements_browser_test.cjs
node --check portal/internal/web/team_settings_browser_test.cjs
node --check portal/internal/web/paging_browser_live_test.cjs
git diff --check
'
```

PASS exit0; [quick.log](quick.log), [result](quick-result.json).
Whole-range whitespace also passed after consolidation. No actual browser,
Go/Node test suite, full package, build or utility was launched. Ordinary hooks
were retained; no declared hook framework/bypass. There were no rebase conflicts.

Final tree **18a3cce76465d80683294c3f82d3477422358ed9** equals the exact
syntax-checked pre-fold tree and a disposable-index reconstruction from3671
plus only [the saved three-path delta](three-path.delta.patch).
[Effective final delta](effective-three-path.diff) is byte-identical to that saved
patch. Every one of the **526 other file blobs** equals3671, including all four
of imp2's Firefox files, every production file, dependency and prose file. This
also proves no context resolution altered the final result.

Before3671 series/tree/patches are retained in [before-series.json](before-series.json),
[before-series.patch](before-series.patch) and [before-tree.txt](before-tree.txt).
New own safety refs preserve:

- `refs/safety/2026-10-20-dev-workspace-portal-improvements/before-three-browser-fixtures-3671c790` →3671.
- `refs/safety/2026-10-20-dev-workspace-portal-improvements/history-remediation-d617ef39` →d617.

Existing reviewed133 and deployedf8 safety refs, receipts and original provenance
remain untouched. Rewritten feature lineage is not described as literal deployed
ancestry or default integration.

## Complete logical series and pin disposition

There are **16 groups**. Paging geometry is folded into presentation/history
66fe576; draft order is folded into Filesd104c1d. The preexisting session-model
mock defect has one new focused test commitbf477e4. Of the previous15 ordered
stable patch IDs, **13 are unchanged**; only the two owning feature groups change.
No temporary fixup remains. The sole A6e dependency commit4a2fadd and every pin
file are unchanged, with no C/config edits or interim pins. There are **no
migrations** or migration merge/release/deployment/external-consumption changes.

| Group | Exact head | Purpose |
| --- | --- | --- |
| 1 | `4a2fadd106d5eb9a7dcd92fb7ab28fb8cbd94458` | deps: update shared conversation presentation helpers |
| 2 | `db1e91ebd008f479cc1021b25e9756c588c5949a` | team: project full-team names from actual implementer counts |
| 3 | `b006196781869aec5d267b790ef0a839e4aa57dd` | portal: add authorized file downloads and source copy actions |
| 4 | `54169426248448119fd257ffbf3d652b1f3b5172` | portal: keep large artifact catalogs compact and stable |
| 5 | `7d9392e6643e8d856688ee1dc08ba86146f41ddc` | portal: publish session membership before optional enrichment |
| 6 | `5a764b28d654c9b00538f333fd550067da7a121d` | portal: retain member settings through sequential additions |
| 7 | `66fe576595cc0038e81722eff1fb29048d2ea7b8` | portal: present team messages and decorated Markdown |
| 8 | `2366b1bb630b56aefeb08afb669941f8955ff244` | portal: show delivery recovery beside the composer |
| 9 | `d104c1decae03f8099ebbe0f7c85a73b8ca69a50` | portal: browse eligible session files in a lazy tree |
| 10 | `fe89ed685a1edeaa60131a9cc16057b44aa0e7ba` | portal: retire paused read cycles and recover on tab resume |
| 11 | `36f081f2d74a40a0801b564010231bdda94a48fd` | coordination: derive claims from registered repository identities |
| 12 | `02236771c6ff425f31f4348b8edfe188c248c020` | portal: measure read stages without logging session content |
| 13 | `96bd7937b701acd4fa3e3ef630156fab2922e08f` | test: prepare ordinary Firefox acceptance across fifty native tabs |
| 14 | `90779020e4e6cbef3b2b3f3e7ed06cb271ef3eb4` | notifications: drop deliveries from disabled browser epochs |
| 15 | `1afddaf8cb4575e088ecbaa7570df4ce12d96716` | coordination: retain deployed machines through explicit user release |
| 16 | `bf477e4fd39b2f66f71d40838a38511c92e3e5cd` | test: match session-scoped model catalogs in settings fixture |

[Final inventory/proof](final-series.json), [range-diff](range-diff.txt),
[full series](final-series.patch), [complete base-to-head diff](final-diff.patch),
[file names](final-names.txt) and [diffstat](final-stat.txt) bind the final branch.

## Cancellation permission limit

Publication/remote/clean proofs succeeded. Canceling superseded same-feature
run **39657466104** returned **HTTP403: Resource not accessible by personal access
token**. No cancellation was confirmed, no retry or credential/permission change
was attempted, and no CI wait/status poll followed the refusal. Parent must own
any permitted cancellation follow-up. Current-head/other-branch runs were untouched.
The exact target snapshot and refusal are in `cancellation.json`.

## Ownership return and actual verification still needed

B is clean and returned to lead for explicit transfer to imp3's separate three
fixtures. Implementer0 stops source/index/Git writes here. Parent owns later
actual-browser commands once all six accepted fixture corrections are committed
and inspected, then downstream sole pins/guards. Imp3's optional/recovery/
usability files were not edited or diagnosed here; imp2's four Firefox files are
byte-identical to its published3671 result.

The exact proposed three-subtest argv remains in `../proposed-commands.md`:
`go ... -run '^TestQuestionBrowser$/^(portal_improvements_browser_test[.]cjs|team_settings_browser_test[.]cjs|paging_browser_live_test[.]cjs)$' -count=1 -timeout=20m -v`,
with the same rooted PW1.59.1/browsers, absent provider sentinel and review overlay.
Bind the future final B head in parent guards after imp3 completion. Do not reuse
old failed receipt paths or infer later first-stop paths passed. No blind rerun,
assertion weakening, budget increase or production fix is authorized here.
No live, claim, roster, lifecycle, merge or deployment operation occurred.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-dev-workspace-portal-improvements/
