# B1: browser tooling preparation

Preparation only, 2026-11-10; owner implementer2. Session identity, environment
identity and live roster match the bound session. Retained settings:
`gpt-6.1-sol` / `xhigh` / `workspace_write`. Application worktree HEAD observed:
`e560b43b01b7b387f1cd7a40a635d27f3b7fba2b`.

No application edits, Git mutations, installs, builds, preview launch, browser
launch or browser tests were performed. B2 requires a separate lead assignment
after its preview/review prerequisites. The lead owns the registered service.

## Available tooling

The repository's `flake.nix` dev shell provides Go, Make, Lefthook, Perl and a C
compiler; it does not provide Node or browser tooling. No browser tool/plugin
is exposed in this member's active tool list. Existing Nix-store packages are
sufficient, without changing the application shell, lock or dependencies:

| Component | Exact existing path |
| --- | --- |
| Node 24.18.0 | `/nix/store/lnfxdsvvm1srsa9kk94s7jqw06yq1h2d-nodejs-24.18.0/bin/node` |
| Playwright 1.61.1 API | `/nix/store/5cwkzbaxg65vbbnjvz05w8jm9m9kbam7-playwright-test-1.61.1/lib/node_modules/playwright` |
| Playwright CLI | `/nix/store/5cwkzbaxg65vbbnjvz05w8jm9m9kbam7-playwright-test-1.61.1/bin/playwright` |
| Matching browser collection | `/nix/store/bcf8w1529mgspizwjsp3iwvaq26plrgj-playwright-browsers` |
| Headless Chromium | `/nix/store/0zny6ldfisrpgizb87j1igva6s13xk8f-playwright-chromium-headless-shell/chrome-headless-shell-linux64/chrome-headless-shell` |

Playwright's bundled metadata identifies Chromium 149.0.7827.55 / revision
1228. The collection contains matching Chromium, headless shell, Firefox and
WebKit. Use the matched collection, rather than the separate existing 1.59.1
module or unrelated browser versions. Avoid `npx`, `npm install` and
`playwright install`; none is needed.

Verified quick discovery: CLI `screenshot --help` exited 0; importing the API
with the listed Node exited 0 and reported version 1.61.1; its resolved Chromium
executable and headless-shell executable exist. Launch compatibility has not
been tested. These store paths are a preparation receipt, not newly created GC
roots or permanent tooling dependencies.

## Minimal proposed invocation

For a single system-dark Czech screenshot, after the lead supplies the local
preview URL and B2 is dispatched:

```bash
PLAYWRIGHT_BROWSERS_PATH=/nix/store/bcf8w1529mgspizwjsp3iwvaq26plrgj-playwright-browsers \
/nix/store/5cwkzbaxg65vbbnjvz05w8jm9m9kbam7-playwright-test-1.61.1/bin/playwright \
  screenshot --browser chromium --color-scheme dark --lang cs-CZ \
  --viewport-size '390,844' --full-page --timeout 15000 \
  "$B2_PREVIEW_URL/?lang=cs" "$B2_OUTPUT_DIR/390-cs-system-dark.png"
```

The CLI wrapper defaults to that matching Nix browser collection; setting it
explicitly also overrides any inherited browser path. Set the
following environment for a disposable CommonJS script using the programmatic
API (the script is to be prepared in B2 once final controls/routes are known):

```bash
PLAYWRIGHT_BROWSERS_PATH=/nix/store/bcf8w1529mgspizwjsp3iwvaq26plrgj-playwright-browsers \
NODE_PATH=/nix/store/5cwkzbaxg65vbbnjvz05w8jm9m9kbam7-playwright-test-1.61.1/lib/node_modules \
  /nix/store/lnfxdsvvm1srsa9kk94s7jqw06yq1h2d-nodejs-24.18.0/bin/node \
  "$B2_CHECK_SCRIPT" "$B2_PREVIEW_URL" "$B2_OUTPUT_DIR"
```

`require('playwright')` then supplies `chromium`; `chromium.launch({headless:
true})` uses the matched shell. No application test framework is needed. Keep
the script and disposable screenshots/results beneath this session's tracking
directory. The commands above are proposals and have not contacted a preview.

## B2 coverage using the API

- Use `browser.newContext({viewport:{width,height:900},colorScheme,locale})`
  for widths 320, 390, 768, 1024 and 1440. Request `?lang=cs` and `?lang=en`
  explicitly; browser locale alone does not select a query-based locale.
  Capture `page.screenshot({fullPage:true})` after styles/fonts are ready.
- For every supplied representative route, capture both languages and four
  cases: system light/dark with no stored preference, and explicit light/dark
  selected through the real UI while the system requests the opposite theme.
  This is 40 screenshots per route; route inventory and any proportionate
  reduction belong to the lead's B2 acceptance brief.
- For system behavior, use `page.emulateMedia({colorScheme})` after load and
  check the rendered theme changes. For manual behavior, activate the actual
  control, check its accessible state and rendered theme, change system theme
  again, reload, and navigate to another supplied route/locale. Verify stored
  preference and theme persist. A new context with captured `storageState`
  can check restoration; do not count pre-seeding a preference as testing the
  UI. Test return-to-system behavior and denied storage if required by the brief.
- Use `page.keyboard.press('Tab')`, `Enter`/`Space`, arrows and `Escape` as
  appropriate to the implemented native/select/menu controls. Record visible
  focus and accessible state. For touch use a separate Chromium context with
  `hasTouch:true`, a 390px viewport and `locator.tap()`; verify language/theme
  and representative navigation. This proves emulated touch behavior only.
- Collect document `scrollWidth` versus `clientWidth` plus element bounding
  boxes at each width. Distinguish intentional inner table scrolling from
  whole-document overflow. Verify long labels and actual fixture content;
  screenshots remain necessary for clipping/wrapping and visual hierarchy.
- Collect representative computed foreground/background colors using
  `page.evaluate()`/`getComputedStyle()`, composite transparent ancestors and
  alpha colors before calculating WCAG luminance ratios. Record selector,
  state, resolved colors and ratio. Use 4.5:1 for ordinary text, 3:1 for large
  text, and 3:1 for applicable UI boundaries/focus against adjacent colors.
  Include statuses, badges, links, muted text, tables and controls in both
  themes. Mark gradients/images or unresolved layering for visual assessment;
  a sampled color report is not a complete accessibility audit.
- Collect console errors, failed local asset requests and relevant HTTP
  failures. Preserve concise results and screenshot names with the exact tested
  application head, preview URL and tooling paths.

Full browser execution may exceed one minute. B2 should use the required fresh
verification watcher under `dev-session-monitor`; no long run was launched in
B1. No blocker to B2 tooling is currently known. Remaining dependencies are the
separate assignment, lead-owned preview URL/final head, final control selectors,
and representative routes/fixtures from the accepted verification brief.
