# P1 UI package evidence

Owner: implementer0, retained Sol/xhigh/workspace_write. Accepted architect
brief: [design.md](design.md). Lead owns final review, acceptance and publication.

Source worktree: `worktrees/2026-11-10-status-theme-responsive-preview/vpsf-status`.
Branch: `2026-11-10-status-theme-responsive-preview`.
Base: `e560b43b01b7b387f1cd7a40a635d27f3b7fba2b`.
Final consolidated UI head: `2d448fd21e8ea5ec3b2a1322bb170d35617470ce`.
Reviewed/previewed U3 head: `3568d8fbacbbe253bcc9785ffc01ef7167f0c093`.
Reviewed/previewed U2 head: `6188366420342fdcf5b5f73c76dc0ccffede80b8`.
R2-reviewed U2 head: `660ccfad579faa010e74fa9ee809509292f7f937`.
Previously reviewed and previewed P1 head:
`9958b0375eb4d7c655cdc505a76e46ec95301cd4` (retained as U2 comparison base).
Parent / P1 delta base: `63d34fe341f759455d81e262ffc38fccad8c3cb5` (P2).
P1/U2 committed only the 16 owned files; repository worktree and index clean.

## Changed scope

- `templates/{layout,index_header,about,entity,history_bar,status}.tmpl`: shared
  header; localized native display controls; guarded first paint; versioned
  local assets; real localized mobile field labels with retained table headers;
  contained history tracks. No application handler changes needed.
- `public/{status.css,theme.js}`: semantic light/dark palettes and Bootstrap 5.2
  overrides; browser-local preference and storage-failure fallback; responsive
  tables; history hover/focus/tap, position, dismissal and recent-end scrolling.
- `internal/i18n/catalog/messages.go`, `i18n/{cs.toml,cs.active.toml,en.active.toml}`:
  four new theme messages. Lead reviewed English/Czech wording unchanged before
  generation.
- `ui_routes_test.go`: shared header on all four real HTML routes in both locales,
  loading controls and localized incident labels. `app_routes_test.go`: eight
  existing structural snippets adapted to changed markup, preserving assertions.
- `docs/reference/appearance.md`: supported theme, cache, responsive and rollback
  behavior. P2 owner adds its README entry link within existing README ownership.

Initial P1 diff: 15 files, 595 additions / 300 deletions (including new files).
Final consolidated UI diff: 16 files, 704 additions / 301 deletions, plus the
official 4049-byte dark PNG described below.
No edits to `app.go`, `main.go`, preview files, dependencies or monitoring logic.
No new framework; existing Bootstrap versions retained.

## Checks and remaining acceptance

- Session identity and both environment variables match the exact binding; live
  same-session roster verified before work.
- `nix develop -c make i18n-update`: passed.
- `nix develop -c make i18n-health`: passed.
- `nix develop -c gofmt -w ui_routes_test.go app_routes_test.go internal/i18n/catalog/messages.go`:
  completed; source formatted.
- `git diff --check`: passed.
- First actual shared batch failed on stale inline-style expectations in
  `TestRoutesServeIndexOperationalState`, before later batch steps ran. The
  corrected test now checks versioned asset references in HTML and retrieves
  the actual served CSS for underline and popover-size contracts. Related test
  snippets were inspected for the same extraction/markup issue.
- `nix develop -c go test . -run '^TestRoutesServeIndexOperationalState$' -count=1`:
  passed (0.199s). After retaining CSS size assertions, a focused batch of that
  test and the three new UI tests passed (0.680s). No UI behavior changed for
  this correction; shared complete checks remain lead-owned.
- `nix develop -c make hooks`: passed. Executable common-repository
  `hooks/pre-commit` verified; invokes Lefthook, with declared gofmt and i18n checks.
- UI commit executed with `nix develop -c git commit -F
  /tmp/status-ui-commit-message-2026-11-10`; Lefthook 2.1.5 passed gofmt (0.05s)
  and i18n (0.38s), total 0.46s, no bypass. All 98 source hashes still match the
  passing frozen manifest after hooks; no logical formatting or other effects.
  Lead directly reviewed the appearance documentation unchanged before commit.
- Shared batch after the narrow correction: lead-owned watched operation
  `cc13cc10-1201-4975-b2ef-1a23437c1c6f` passed normal `go test ./...`, preview
  `go test -tags preview ./...`, `make i18n-health`, normal `go build` and preview
  `go build -tags preview` in the repository Nix shell (28s, lead report).
  Frozen input manifest:
  `db934b29c5ad544bd3c2138f01d80cb86b6e4f35bdd86ee6d36c5e9ec17b7032`.
  First actual batch `ee660d1d-8212-4948-8ef0-58935e2ec16a` failed on the stale
  test described above; earlier `e5fc0374-99d4-459f-b541-e410c5aedf55` never
  launched its source command and lead reconciled its no-command effects.
- R1 final independent review of old head
  `1b39ba205bebc2f8d5a0754c1cfd08f94711e9fc` found one Important focus race,
  no Blocking or Advisory findings. Delayed focusout/pointerleave callbacks
  could close a newly active day. Both callbacks now require `active === wrap`
  before closing. The JS cache URL is v2, with matching route expectations.
  Old P1 was amended to `9958b0375eb4d7c655cdc505a76e46ec95301cd4`;
  P2/base untouched. That delta against the R1-reviewed old head was four files,
  five additions / five deletions. U2 supersedes it as recorded below.
- Focused `TestRoutesServeIndexOperationalState` and
  `TestHTMLRoutesShareLocalizedDisplayControls` passed (0.458s) after that narrow
  fix. Required Lefthook checks during amend passed gofmt (0.04s), i18n (0.35s),
  total 0.42s; no bypass, source edits or unexpected logical hook effects.
  Worktree and index clean. The original commit message was retained via a
  temporary file; no push or rebase performed.
- Lead/reviewer accepted narrow-fix reconciliation without a full rereview;
  B2 browser acceptance remains pending on a fresh matching preview candidate.
  Browser owner implementer2 has Tab/focus and delayed pointerleave regression
  cases. P1 retains UI finding/fix ownership.

## Original P1 browser handoff (superseded by U2 below)

Theme selector `#theme-select`, values `system` / `light` / `dark`; wrapper
`.theme-control` remains hidden without JS. Origin storage key
`vpsf-status.theme`; root `data-theme` absent in System, `light` or `dark` for
manual choices. Native language menu `.language-menu` uses `details`/`summary`.
Real routes `/`, `/entity`, `/group`, `/about`; both languages use `?lang=en|cs`.
P2 owns representative synthetic fixture routes and registered preview launch.

Wide tables `.stacked-table` stack below 768px using `.cell-label` and
`.cell-value`. Small status matrices remain tabular. History `.history-track`
contains scrolling; `.history-day-wrap` receives focus/tap and `.history-popover`
opens within `.is-open`. Escape/outside pointer dismisses. `any-pointer: coarse`
uses 28×44px day targets and starts at the recent end, including after accordion
expansion. Verify all accepted viewport, theme, contrast, keyboard/touch, storage
and no-JS scenarios from the brief; none is claimed browser-verified here.

## History and compatibility

No migrations, schema, API, JSON, metrics, status-calculation or configuration
changes. P1 is one logical UI commit after the independent P2 preview commit;
no superseded implementation commits, transitional migrations, deployment or
externally consumed versions. Templates,
assets and matching embedded catalogs ship together; older code ignores the
browser preference. No production deployment or default-branch integration
authorized by this package. Session stays open.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-status-theme-responsive-preview/)

## U2: user-directed visual refinements

Accepted D3 brief, owner implementer0. U2 amends old reviewed/previewed head
`9958b0375eb4d7c655cdc505a76e46ec95301cd4` to
`660ccfad579faa010e74fa9ee809509292f7f937`, preserving P2 parent and initiative
base. Delta: 12 files, 162 additions / 66 deletions, plus a 4049-byte PNG.
No migrations, production release, persisted-state boundary, backend, dependency
or protocol changes. Retain the old review/browser receipts; this successor
adds the three requested visual refinements and requires final review/browser
acceptance. No obsolete UI commit remains in the two-commit branch series.

- One `.settings-menu` native details with a 44px ellipsis summary, labelled
  Settings/Nastavení. `.settings-panel` holds native `input[name="theme"]`
  radios (`#theme-system`, `#theme-light`, `#theme-dark`) styled with display,
  sun and moon icons. Native `#language-select` uses exact generated switch
  URLs. `.settings-enhanced` starts hidden; `.settings-fallback` language links
  work without JS. Theme changes keep the panel open; focus exit/outside
  interaction dismisses it; Escape returns focus to summary.
- Original light palette from base `e560b43` restored: OK `#198754`, maintenance
  `#ffc107`, outage `#dc3545`; `.history-day-*` and `.history-lane` fills use the
  same mapping. Coverage stripes alias maintenance/outage. Base/current
  `historyStateClass` defaults all other states to OK; no separate unknown or
  missing gray selector exists. Dark fills/coverage stay `#86efac`, `#fcd34d`,
  `#fca5a5`; accessible semantic text unchanged.
- `public/vpsfree-dark.png` copied unchanged from web revision
  `7fec3e3ccc5a1aa41bad7f06f83d01fa6cd15fe9`,
  `obrazky/vpsFree-bile.png`, exact blob
  `41a78b8dc4f2ee76d847453b7d2da85ae4f037f6`, transparent 173×50. Existing
  light logo retained. `.brand-logo-light`/`.brand-logo-dark` CSS follows
  system/manual theme before paint; no white plate or image enlargement.
  Brand link has one accessible name, with decorative image alternatives.
- Cache URLs CSS v2 / JS v3. R1 active-wrap dismissal guards preserved.
  Settled selectors and palette sent directly to implementer2 for B3.
- Lead directly approved actual Settings/Nastavení, existing labels and
  updated `docs/reference/appearance.md` under the writing skill.
- Focused five route tests passed (0.788s), including language query preservation.
  `node --check public/theme.js` passed. `nix develop` warm batch passed normal
  `go test ./...` (root 10.856s), preview `go test -tags preview ./...` (root
  14.760s), and `make i18n-health`. `git diff --check` passed. No build/CI or
  browser batch duplicated by U2.
- Amend ran through Nix and required Lefthook 2.1.5, preserving useful subject
  and updating the final behavior description via a temporary message file.
  Hooks passed gofmt 0.05s / i18n 0.37s, total 0.45s. All 99 checked input hashes
  in `u2-quick-inputs.json` still match afterward, digest
  `444bf2d3c9fce3ca64957adaafb02edb3178a8ae6ee0b1f29c99bfde907bd376`.
  No unexpected hook effect; worktree/index clean; commit window released.

U2 inventory: `app_routes_test.go`, `ui_routes_test.go`,
`docs/reference/appearance.md`, `i18n/{cs.toml,cs.active.toml,en.active.toml}`,
`internal/i18n/catalog/messages.go`, `public/{status.css,theme.js,vpsfree-dark.png}`,
`templates/{index_header,layout}.tmpl`.

### R2 reconciliation

R2 final report found Important U2-R1: wrapped Back/settings action rows at
320/390px could place their right-aligned dropdown beyond the left viewport
edge. Removed only the mobile `margin-left: 0` override, preserving the existing
global `margin-left: auto`. Focused real static stylesheet route test passed
(0.190s), diff checks passed. B3 owns actual open-panel bounds on entity/group/
about at both widths; this is not yet claimed browser-verified.

Advisory U2-A1 corrected the documentation's blanket query-preservation claim.
Entity/group language choices preserve route/query; the preexisting cached
About page switches to the overview. Lead directly approved the exact factual
paragraph; no application cache or routing change was made.

Amended `660ccfad579faa010e74fa9ee809509292f7f937` to
`6188366420342fdcf5b5f73c76dc0ccffede80b8`, preserving parent/base and prior
review/preview receipts. Delta only CSS and docs, two additions / two deletions.
Original message retained through a temporary file. Required Nix/Lefthook i18n
passed (0.35s, total 0.37s); gofmt correctly skipped without staged Go files.
All other 97 full-suite inputs unchanged. Worktree/index clean; window released.
No broad test/build/browser repeat, push, rebase or services. CSS v2 remains the
new final user-facing version; prior published UI used v1. Lead owns final
candidate snapshot and B3 before refreshing the user preview. Reviewer/lead
accepted this direct narrow reconciliation without automatic full rereview.

## U3: faithful pointer fix, smaller gear and inline timestamp

Old reviewed/user-preview head `6188366420342fdcf5b5f73c76dc0ccffede80b8`
amended to `3568d8fbacbbe253bcc9785ffc01ef7167f0c093`. P2 parent and initiative
base unchanged. Six files, 23 additions / 15 deletions: `public/status.css`,
`templates/{index_header,layout}.tmpl`, `app_routes_test.go`, `ui_routes_test.go`,
`docs/reference/appearance.md`. No JS, catalog, logo, palette, backend, dependency,
migration or stored-state changes. Prior source/review/preview receipts retained;
two logical commits, without superseded UI implementations in the branch series.

Faithful BEFORE evidence: `u3-pointer-before.cjs` and `.jsonl` against the frozen
user preview on port 4567, old head above. Real `page.mouse` pointer coordinates
on the visible moon glyph, without programmatic check or event dispatch:
zero-delay down/up succeeded (panel open, dark selected/applied/stored), while
holding down 100ms before up failed (panel closed, System remained selected,
no stored preference). Event trace shows mousedown on the nonfocusable label
blurs summary to BODY; focusout RAF closes the panel during the hold, so up/click
retargets outside and label default radio activation never happens.

Each native radio now covers its visible icon tile as a transparent full-size
input, retaining input/label association, default pointer focus, radio keyboard
behavior and the existing focus-visible label outline. No dismissal JS policy
changed; R1 active-wrap guards remain identical. The gear glyph is 16px, trigger
32×32 on fine pointers and 44×44 on coarse pointers. Timestamp moved into the
right action group, unconditional full-row basis removed; outer header still
wraps naturally. CSS URL v3, unchanged JS v3. B4 owner received settled selectors
and the exact held-pointer reproduction for independent final-candidate tests.
Lead explicitly retained final after verification with B4; U3 created no extra
after harness, candidate or service.

Targeted repository Nix checks passed: localized real route/loading/query/index/
entity/group/about tests (1.042s), preview-only tests (3.993s), i18n health and
diff checks. No unnecessary full suites or builds repeated. Lead directly applied
the writing skill to the actual documentation diff, accepting wording unchanged.

Amend used a temporary message file with the useful original subject and final
gear/radio/timestamp behavior. Required Lefthook 2.1.5 passed gofmt (0.03s) and
i18n (0.37s), total 0.43s. All 99 tested input hashes still match
`u3-quick-inputs.json`, digest
`26c56d360fd7c9857677a95558ce219e047a047f221514c90394c96892ba603e`.
No unexpected hook effects; worktree/index clean; amend window released.
Final independent review and B4 actual gesture/layout verification remain with
the lead and assigned members. No push, rebase, master integration or services.

## U4: phone gear placement and titles on actual hit targets

U3 was accepted before U4. Amended reviewed/user-preview head
`3568d8fbacbbe253bcc9785ffc01ef7167f0c093` to
`2d448fd21e8ea5ec3b2a1322bb170d35617470ce`, preserving P2/base and the two
logical commits. Delta: five files, 14 additions / 10 deletions: CSS, shared
header/layout and the two route-test files. No JS, new prose/catalog strings,
logo/palette, backend, migration or persisted-state changes.

Below 768px the nonsemantic action wrapper uses `display: contents`, so the
actual brand and gear are first-row flex items while timestamp/Back navigation
wrap independently below. The wrapper has no mobile layout box: B5 measures
actual brand/summary/timestamp geometry. Desktop is unchanged. Existing 16px
glyph, 32px fine/44px coarse targets, right-anchored popup, full-tile native
radios, keyboard/focus/no-JS behavior and held-pointer guards remain intact.

Actual native inputs now carry titles: EN System/Light/Dark; CS Podle systému/
Světlý/Tmavý, reusing approved catalog messages. Updated route assertions verify
the input titles in both locales on all HTML routes. CSS v4, unchanged JS v3.
No permanent doc change was useful for this bounded placement/title correction.

Targeted route checks passed (1.047s), preview-only tests (3.821s), i18n health
and diff checks passed. Lead accepted source/strings and granted the amend
window. Current useful message retained via temporary file; required Lefthook
2.1.5 passed gofmt 0.04s / i18n 0.37s, total 0.44s. All 99 tested input hashes
still match `u4-quick-inputs.json`, digest
`3575aec76bcfe0ea4270dac80c0530f4ac1f14f56574d89411324a9bb5099098`.
Worktree/index clean; no unexpected hook effects; window released. Prior
review/preview receipts remain historical evidence. Final independent review
and focused B5 phone/title/held-pointer checks remain lead/member-owned; no
browser framework, services, broad suites, push, rebase or integration by U4.
