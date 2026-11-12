# B2 browser acceptance script

Prepared by implementer2; execution remains lead-owned and blocked until final
review passes. No browser or preview request was made during preparation. The
only check run was Node `--check` on `browser-check.cjs`, which passed.

Use the existing Node runtime; the script selects the exact matched Playwright
1.61.1 module and browser collection recorded in `b1-browser-tooling.md`.
No installs, package edits or additional framework are needed.

```bash
/nix/store/lnfxdsvvm1srsa9kk94s7jqw06yq1h2d-nodejs-24.18.0/bin/node \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-11-10-status-theme-responsive-preview/browser-check.cjs \
  http://127.0.0.1:18081 \
  "$B2_NEW_RESULTS_DIR" \
  "$B2_FINAL_HEAD"
```

Arguments are loopback base URL, **new** results directory, exact tested
application head. The script refuses to reuse an existing directory. The caller
must establish the preview's exact source head; the script records that receipt
without Git commands. Update the head and directory if reviewed source changes.

The single batch includes 20 overview captures (five widths, CS/EN, light/dark),
12 distributed entity/group/about captures at 390/1440, and focused interactions:
manual choices under opposite OS, system changes, reload/navigation/locale
persistence, return System, invalid/blocked storage, no-JS, keyboard focus/menu
(including sequential history A→B, delayed pointerleave(A) while B is open,
into/out of B's incident link, and B→C after focusout animation-frame callbacks),
event pagination, 200% reflow equivalent and independent root text scaling,
emulated touch history targets/recent-end/edge popovers/link/dismissal and
accordion expansion. Captures record document overflow and real stacked-cell
labels. Wide-page samples collect normal/muted/status/link/control colors with
alpha backgrounds composed; unresolved image/layer cases get null ratios.

Expected execution: roughly 2–5 minutes depending on CDN response and expanded
page capture cost. Run through the required fresh verification watcher. Fatal
prerequisites stop the batch before the matrix (HTTP/mixed preview/header/theme,
Bootstrap CSS/JS and final `theme.js?v=2`). Individual actions have 8-second limits, navigation 20 seconds,
screenshots 15 seconds; an eight-minute total budget closes the browser. Collect
the first run's precise failures for one correction batch; avoid unchanged full
reruns. There is no scenario simulator, preview startup, installation or app edit.

Output: `results.json`, named PNG screenshots and compact per-check stdout.
The JSON includes the exact application head, script digest, tooling versions,
checks, sampled contrast, overflow candidates, console errors and failed local/CDN
requests. Synthetic `.invalid` link targets are fulfilled locally to test link
activation without contacting external targets. Exit 0 means all assertions
passed. Screenshots still require visual inspection; sampled contrast is not a
full accessibility audit. Reflow/text scaling are documented approximations of
browser zoom. Preparation has not established runtime assertions or visual
acceptance.

## Focused diagnosis after first matrix

The first full matrix at head `9958b0375eb4d7c655cdc505a76e46ec95301cd4`
completed in 33.3 seconds. Its four functional failures and aggregate console
failure were harness issues: navigation assertions ran before the new document's
styles loaded; Enter on the native select opened its picker so the next Tab did
not move to the language summary; the invalid-storage init script also ran on
`about:blank` and raised a security exception. The responsive page-2 capture had
`table-cell`/`inline` styles because it preceded CSS readiness.

The script now waits for DOMContentLoaded, load and fonts after clicked navigation,
uses Home/ArrowDown then Tab for native select operation, and confines invalid
storage seeding to the preview origin. Optional final argument `--focused` runs
only prerequisites, manual choices, invalid storage, keyboard/history and pagination,
with console/assets aggregation; it does not repeat the passing screenshot matrix.

Focused run `browser-focused-9958b03/results.json` passed all seven check groups,
including actual history A→B Tab, delayed pointerleave, linked incident entry/exit,
B→C and Escape. It produced four screenshots; page 2 computed `grid` cells and
390px document width (no body overflow). Console/network failures were absent.
No application edits were required. Combine this result with the first matrix's
successful scope; it is not a second full matrix or proof of visual inspection.
