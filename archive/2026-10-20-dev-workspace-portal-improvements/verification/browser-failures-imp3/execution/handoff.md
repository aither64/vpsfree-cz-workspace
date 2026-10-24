# Three fixture corrections: committed and published

Final B: `965aadc51dfb4a7d838a401b20ecafa38c8a70db`, clean and SSH-published by
exact lease from `bf477e4fd39b2f66f71d40838a38511c92e3e5cd`. Remote default remains
`968646471b1190c16a8cf60ff50736cd0525fa3f`. See `publication-proof.json` and `push.log`.
B source/index/Git ownership returns to the parent after this handoff.

The exact immutable candidate patches were applied to exactly three CJS files.
The receipt selectors are folded into delivery-recovery group `fdd6f77c1`.
The preexisting scoped-read mock repair is its own final group `965aadc51`.
No transient fixup remains on the final 17-group branch. There are no migrations.
The practical grouping follows the lead's latest direction: no combined model
and limits mock commit was needed.

All candidate hashes match. A disposable-index reconstruction of bf477 plus
`approved-candidate.patch` equals final tree
`9f4ebf19d2cc4ecfef64751980d0a14f02892e6e`. Every other blob (526 files), every mode
and every pathname is identical to bf477. This includes all imp0/imp2 fixtures,
production source/assets, dependencies, documentation and pins. `source-proof.json`
binds the complete comparison, retained bf477/3671/d617/reviewed133/deployedf8 refs,
and stable patch IDs. Fifteen of the prior sixteen group patch IDs remain equal;
only the owning recovery group differs, plus the new limits test group.
`final-series.json`, `final-series.patch` and `range-diff.txt` inventory the whole
base-to-head series. `final-three-fixtures.patch` is the exact three-file delta.

Quick verification: Nix-provided Node syntax passed for exactly the three CJS
files, and working diff whitespace passed, exit 0 in 7.906 seconds. The final
whole-range diff also passes whitespace. See `quick.sh`, `quick.log` and
`quick-result.json`. The repository declares no hook framework; its default
common hook directory contains no active hook files. Commits and autosquash used
ordinary Git in the Nix environment, with no hook bypass. No actual browser,
package, CI wait or test rerun occurred here. Parent direct narrow-follow-up
inspection remains the accepted review path; broader behavior must return to
lead/architect. Existing product docs already describe the tested behavior, so
no documentation or visible prose change was useful.

The original d617 failed logs, failed launchers, candidate directory and passing
notification receipts remain unchanged. These syntax checks do not establish
browser acceptance. The exact-head guarded targeted command is prepared, not run:

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/browser-failures-imp3/execution/post-commit-three-fixtures.sh
```

It selects the existing pinned Playwright 1.59.1, Chromium 1217 and Firefox 1511,
uses the absent-provider fixture environment and review-assets overlay, and runs
only the three actual TestQuestionBrowser subfixtures. Parent fresh Luna owns
long execution or the converged full suite. C/config pins remain for implementer1.

`cancellation.json` records a single read-only post-publication CI inventory.
The prior Actions cancellation 403 is retained without retry or credential
changes. Any obsolete active run is recorded as cancellation unavailable;
current-head and other-branch workflows remain untouched. No CI waiting.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-dev-workspace-portal-improvements/
