# B3 focused refinement verification

Owner implementer2, capacity available after accepted B2. Session/env and live
roster reverified; retained Sol/xhigh/workspace_write. Preparation only until
U2 selectors, final committed review and lead-owned preview URL/head are released.
No browser, services, installs, Git or application mutations during preparation.

Use the existing Node/Playwright paths and corrected navigation-load/font waits
from B2. Keep B2 results unchanged; no repeat of its successful full matrix. B3
has one disposable focused script and new results directory, using caller-supplied
base URL/head. Candidate port 18082 and public-preview replacement port 4567 are
lead-owned. Do not contact either before release.

Intended evidence (~10 screenshots): six closed headers at 320/390/1440 across
EN/CS with light/dark distributed; two open panels; a touch panel; one no-JS
fallback. Report computed geometry/overflow for each. Inspect one compact
settings trigger, panel within viewport and focus/accessible names/state.
R2 follow-up adds geometry-only opened-panel checks on entity/group/about with
Back links at both 320px and 390px, asserting left/right viewport containment
and no document overflow. These six cases add no screenshots.

Focused interactions: native summary Enter/Space, theme radio Tab/arrows/Space,
all choices and System, manual preferences under opposite system palette,
reload/navigation persistence, storage synchronization/blocked storage, native
language selection preserving entity/pagination/current query parameters, Escape
return focus, outside pointer/focus dismissal, and no-JS language links with
CSS-selected theme/logo. Retain the already proven R1 A→B, delayed pointerleave,
into/out of linked incident and B→C/Escape keyboard path in one regression.

Validate **all** original light history fills from base/owner receipt (not only
green), while checking semantic status text and dark mapping stay unchanged.
Accepted base/owner receipt: only OK `#198754`, maintenance `#ffc107`, outage
`#dc3545`, with warning/danger coverage aliases. Other history states map to OK;
there is no separate unknown/missing gray. Semantic success/warning/danger text
remains `#166534` / `#854d0e` / `#b91c1c`; dark history stays `#86efac` /
`#fcd34d` / `#fca5a5`. Check loaded logo source and sole visible/accessibly named brand
in light/dark/System; official dark PNG must have the verified blob identity,
173×50 intrinsic proportions and no white plate. Visual acceptance remains with
the lead; computed fill/asset checks do not replace screenshot inspection.

Owner supplied settled selectors: `.settings-menu > summary`, `.settings-panel`,
`input[name="theme"]` with IDs `theme-{system,light,dark}`, associated labels,
`#language-select`, `.settings-enhanced` and `.settings-fallback`, plus
`.brand-logo-{light,dark}`. Script `browser-refinements.cjs` uses this interface
and passes Node `--check`; no browser execution has occurred. Palette currently
asserts the owner-supplied OK/maintenance/outage day/lane fills and coverage
aliases, all three semantic text colors and retained dark values. No extra
unknown/missing state is invented.

Same-session owner clarification IDs:
`286644c7-c35f-42cf-aabc-3c38d3a1e023` (controls/logo/assets) and
`c9bb7c90-753f-4071-99b9-cce7ae6c64b0` (full original palette receipt).
D3 specifies a three-dots summary; lead's generic gear wording is treated as the
same single Settings control, without an icon-specific assertion.

Expected execution is under one minute using warm tooling, once released. Stop
on missing fresh assets/header/fixture, use bounded action/navigation waits, and
collect precise failures for a single necessary correction batch. If execution
becomes uncertain or exceeds one minute, coordinate the required watcher with
the lead. No generalized accessibility framework or new scenario simulator.

Proposed invocation after review/release (candidate URL supplied by lead):

```bash
/nix/store/lnfxdsvvm1srsa9kk94s7jqw06yq1h2d-nodejs-24.18.0/bin/node \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-11-10-status-theme-responsive-preview/browser-refinements.cjs \
  http://127.0.0.1:18082 \
  "$B3_NEW_RESULTS_DIR" "$B3_FINAL_HEAD"
```

The script refuses an existing output directory, records script/head/tooling
identity and compact check results, and captures precisely ten viewport PNGs on
success. It verifies the official dark PNG with its Git blob SHA-1 receipt using
the HTTP bytes, without invoking Git or inspecting another repository. Individual
actions time out after five seconds, navigation after fifteen. If shared CDN
availability makes duration uncertain, stop and coordinate the watcher instead
of repeating failed launches. Results remain untested until the lead releases
the reviewed preview/head.

## Execution at final head 6188366

Lead released reviewed final head `6188366420342fdcf5b5f73c76dc0ccffede80b8`
and immutable candidate `http://127.0.0.1:18083`. First focused B3 run with script
digest `a1e3f95ac989dc3015af62f02fb2e69cba9e2ef95e6f0aa4d072caa9129963e6`
took 13.8 seconds: 16/17 groups passed, eight PNGs, exit 1. The only failure was
a harness assumption that Playwright's summary `ariaSnapshot()` contains
`[expanded]`. Chromium exposes that native node as `DisclosureTriangle`, which
the Playwright snapshot omits. A minimal reproduction showed details open,
panel visible, AX name Settings and native expanded=true.

The harness now checks actual native details state and CDP AX name/expanded,
including expanded=false after Escape. Final script digest:
`486904b28726adfea1b9f2e94782804f5338b97b8cbc93b95d8377e1158b68a9`.
Only prerequisites and the unfinished keyboard group reran with `--keyboard`:
6 seconds, exit 0, two remaining PNGs. No application change or broad rerun.

Evidence: `browser-refinements-6188366/{results.json,*.png}` and adjacent
`browser-refinements-6188366.log`; focused continuation in
`browser-refinements-keyboard-6188366/{results.json,*.png}` and adjacent log.
Both logs record authoritative exit status. Both results have empty console
and network errors. Combine successful first-run groups with the continuation,
preserving the first failure rather than rewriting it as a passing run.

All six Back-header panel cases pass: entity/group/about at 320px have left 39,
right 295 and document width/scrollWidth 320; at 390px left 109, right 365 and
document width/scrollWidth 390. Full light day/lane/coverage mapping, retained
dark and semantic text, official logo blob/loaded proportions/no white plate,
compact headers, native keyboard/touch controls, cross-tab/blocked storage,
language entity+page2+extra query preservation, no-JS links, dismissal/focus and
the actual R1 A→B/link/timer/Escape path passed. Ten PNGs total. Implementer
visually inspected the dark 390px closed header and open keyboard panel: the
official logo and opaque contained panel render as intended. Lead retains final
visual acceptance; Chromium/emulated-touch limits remain.
