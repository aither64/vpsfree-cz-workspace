# U10 dark failure red and rounded tables

Owner implementer2; direct lead brief for bounded CSS/presentation work. Prior
U6 accepted and capacity released. Exact session/env/live roster verified;
retained Sol/xhigh/workspace_write. Clean baseline and fetched origin/master
both `9fb102e285a2847427ffc1d25919183298630f3b` before editing.

One new polish commit `a9273d225bc35181af7f47dd3ee32955f57dc98a` atop that
merged baseline; prior merged history was preserved. Four files, 18+/11−:
`public/status.css`, `templates/layout.tmpl`, and three cache-version assertion
literals in `ui_routes_test.go`/`app_routes_test.go` explicitly approved by lead.
No Go application source, fixture, translation, input graph, JS, table markup or
permanent user-facing prose change. No migrations or persisted-state/interface
changes; rollback has no conversion. Existing permanent appearance explanation
remains applicable, so no documentation change there was useful.

Both system-dark and explicit-dark `--history-outage` change from `#fca5a5` to
`#ef4444`. Dark warning remains `#fcd34d`; semantic danger text stays `#fca5a5`.
All light fills (`#198754` / `#ffc107` / `#dc3545`) and the existing coverage
aliases remain. Calculated sRGB contrast for the new red: panel `#1f3959`
3.121:1, page `#111f33` 4.402:1. Warning-versus-red luminance ratio increases
from 1.316 to 2.610; this quantifies distinction, not a full accessibility audit.

Exposed tables use separate borders with zero spacing and `.5rem` outer/cell
corners. The last header row keeps a 2px bottom divider. Low-specificity corner
selectors let mobile card styles reset cell corners and borders; desktop tables
do not clip overflow, preserving focus outlines and fixed history popovers.
Phone card radius changes `.3rem`→`.5rem`; stacked table backdrop becomes
transparent so gaps remain page-colored. Existing grouped probe-coverage border
and corner patterns remain at the matching new radius. Actual rendered borders,
corners and focus/popover behavior still need the bounded browser acceptance.

CSS URL v5→v6; JS stays v4. Quick checks in repository Nix environment on final
file hashes: focused normal route batch 1.005s, preview tests 3.926s,
`make i18n-health`, `git diff --check`, all passed. No mirrored CSS snapshot tests
or VM suite were added. Required Lefthook pre-commit passed gofmt 0.04s and i18n
0.38s (0.44s total). Four file SHA256 values were unchanged across hooks:

| File | SHA256 |
| --- | --- |
| public/status.css | b1cca98a115da88a105f48e96215f7c6586913d6cf9049b539f366d6d1f207e9 |
| templates/layout.tmpl | f76654f847edd91229c0d0a83c1229321b9ebd89991d9e9392bdd7ae4c4ea216 |
| ui_routes_test.go | 3b5334ce07d3c3545efc30acd9087ca1b0ec3025d6b66c4328f3f488d961681e |
| app_routes_test.go | adc7b96849ca28c28434814895c02b04aaad2898f322498f5f71bb3a962cf98e |

Index/worktree clean after commit; exclusive index window released. No push,
default integration, service action or preview/browser launch. Lead owns final
independent review and registered candidate/4567 replacement. Browser scope after
release: two captures (dark desktop overview, light phone), explicit/system-dark
computed equivalence, original light fills, actual table/card corners/dividers,
focus/popover containment and no body overflow. Prior unaffected behavior evidence
is retained. Package awaits review/browser acceptance; no unapproved integration.

## Reviewed candidate browser acceptance

Lead reported R8 independent review passed at exact a9273d2 with no findings,
then released immutable candidate `http://127.0.0.1:18087`. Its existing
`u10-preview-inputs.json` binds all 13 assets and independently proves non-test
compiled inputs unchanged from the retained preview binary. Existing matching
Playwright 1.61.1/Chromium tooling was still available; no install was needed.

Focused `browser-u10-polish.cjs`, SHA256
`c59c754e356cb1020d84d901ea3becad8dc3ae4a796b85bf8c5ff7c47219d376`,
passed Node syntax, then ran once 2026-11-10 21:00:02–21:00:05 UTC (3.7 seconds),
authoritative exit 0. Both groups passed, exactly two PNGs. Evidence is
`browser-u10-a9273d2/results.json` and screenshots, adjacent
`browser-u10-a9273d2.log` with complete stdout/stderr and exact exit status.
Errors, console and network arrays are empty. Browser closed/runner finished;
no source, Git or service actions during acceptance and no rerun.

Real settings manual Dark against light OS computes rendered outage day/lanes
`rgb(239,68,68)`, warning token `#fcd34d`, semantic danger text `#fca5a5`.
Selecting System and emulating dark gives identical color values. Explicit
Light against dark OS retains all three original light history tokens/fills.
The three exposed desktop outage/recent/advisory tables and their four outer
cell corners compute 8px, separate borders, 2px header divider, overflow visible.
Focused table link has visible outline and history popup opens within viewport.
Phone stacked rows compute 8px corners/1px borders, cell radius0/grid with visible
localized labels, transparent table backdrop/page-colored gaps. Entity coverage
stripe retains red `rgb(220,53,69)` and 4px width. No document overflow.

Both PNGs were visually inspected: saturated red history failure is distinct
from warning yellow; desktop tables have smooth exposed corners, and phone cards
have rounded surfaces/gaps without a rectangular table background. Lead retains
final visual acceptance and registered 4567 replacement. No push/integration
approval is implied by review or browser success.

## User-requested perimeter correction

The user found rounded tables still looked different from header/service panels
because the table had no outer stroke. Within the same U10 package, add an actual
1px solid `var(--border)` table perimeter, remove the final tbody row's cell
bottom borders to avoid a double bottom edge, and explicitly reset mobile
stacked table border to zero. Individual phone cards retain their 1px borders.
Corners, 2px header divider, overflow-visible desktop tables, history fills and
all other controls stay unchanged. CSS URL v6→v7 plus the same three approved
mechanical route-test URL literals; no permanent prose, JS, backend or fixture.

Old published/previewed, **unmerged** `a9273d225bc35181af7f47dd3ee32955f57dc98a`
is retained at local branch
`2026-11-10-status-theme-responsive-preview-u10-before-border`. Its served preview,
R8 report and browser evidence above remain historical evidence for that source.
Amended replacement: `83b8893455a4042862597c140494f05ed004ca26`, with the same
parent `9fb102e285a2847427ffc1d25919183298630f3b`. Reviewed old range is
9fb→a927; new range 9fb→83b8893. Range-diff confirms only perimeter/bottom-edge/
mobile reset, cache literals and commit explanation changed. This is a substantive
CSS successor, not patch equivalence or integration; new border bytes need the
lead's affected-lane review and fresh rendered acceptance. No migrations or
externally consumed schema exist. No default-branch history was rewritten.

Final border-only quick checks passed: focused normal routes 1.033s, preview
tests 4.042s, i18n health and diff whitespace. Required hooks passed in 0.44s
(gofmt0.03s/i18n0.38s). Worktree/index clean and logical source hashes unchanged
through hooks:

| File | SHA256 |
| --- | --- |
| public/status.css | a4af32ab614c8e11c4fcd53402e4b1809d772fa3866142b71b616d88fbd96202 |
| templates/layout.tmpl | 69d92e313a1be0e50ebf1d87521c38fb804fcaced406889576b91904cea405f6 |
| ui_routes_test.go | feb3e8c3767b3b1d7009228b9f55751c7a390a11239e0fd1f405a5cd2ad7ea28 |
| app_routes_test.go | 9462e97badce6df4f19edfc0d180bb3defe7f8eb1aec8eb45249364237265eae |

The amend had already launched when lead advised a bounded architect color-count
recommendation was pending. No count/palette change was made. Index window is
kept available for any explicit settled same-package direction; no publication,
service action or browser run. Actual browser follow-up must compare all four
table border width/style/color values with header, verify no doubled final row
edge, and verify mobile table container is borderless around 1px cards.

## Matching count badges, final source boundary

Border-only candidate 83b8893 ran once at18088 in3.4s, authoritative exit0,
two groups/two PNGs, console/network/errors empty. Evidence
`browser-u10-border-83b8893/` and adjacent log proves all4 table borders exactly
equal header1px/solid/color, last-row cell bottom0, mobile container border0 and
individual cards1px. No interrupt or broad rerun. Before preview replacement,
the user explicitly chose matching filled count badges.

Final owning U10 amend `3fd10ea793ff727a66a01ac9002a214214b19652` remains atop
9fb102e. Preserve published/unmerged83b at local branch
`2026-11-10-status-theme-responsive-preview-u10-before-count-badges`; a927 ref
remains as above. New range9fb→3fd is a substantive badge+border successor of
9fb→83b and9fb→a927, not patch-equivalence or integration. No migrations.

Eight scoped CSS lines style only success/warning/danger count children as
compact filled badges with exact existing history backgrounds. Light green/red
digits white, yellow digits#16273f; dark digits#111. Slashes/total/global semantic
text tokens and bar palettes unchanged. No markup/JS/Goapp/strings/fixtures.
CSSv8 plus3existing URL literals. Lead supplied/applied writing pass for exact
five-line appearance paragraph. Total final delta5files32+/11−.

Final quick checks pass normal focused routes1.083s, preview5.545s, i18n health,
diff whitespace; hooks0.43s(gofmt0.06/i18n0.35). Five source hashes unchanged by
hooks; worktree/index clean, exclusive window released. No push/services/browser
or default integration. Final SHA256 receipt:

| File | SHA256 |
| --- | --- |
| public/status.css | 26d823e635055304871588471737a93ad6a06a32efc381ff5daf36298e2d4237 |
| templates/layout.tmpl | b1eb7e0c2270cb57947d8b67119269c92982d5669004ff77660eb8a5ac45445f |
| ui_routes_test.go | 715e59c447ccf3f31ee089ab52fc7b6d96ba2e74b740ed804d8e5e50e73b1957 |
| app_routes_test.go | 01a44595df4258480161fd79d9d5400a123d4081e538b419ac45f5c051a1d9c0 |
| docs/reference/appearance.md | 2708af06c5b9d70c69efe4ff16ee25e26480882ac84f523affab2ea16708632a |

Existing two-PNG browser script extended only with count fill/actual digit
contrast>=4.5, h2 and collapsed/expanded accordion samples, separators/total,
manual/system dark and explicit-light narrow bounds. Node syntax passes; script
SHA256`bf4749df53e4e1bfa10c4af062ff8e0a73eea3c61ef3413d48ec96f0f3e64d11`.
It retains border/focus/popover checks and awaits affected final source review
and lead execution release for immutable candidate18089. No further source work.

### Final badge/browser completion at unchanged3fd

R9 passed; lead released candidate18089. First run21:15:51–53 exited1 before
captures because inherited accordion slash ink was sampled during Bootstrap's
150ms native color transition while total ink had already changed. A minimal
real-click reproduction showed `CSSTransition` color duration150ms; awaiting its
actual `finished` promise made slash and total identical. Harness now waits for
that real transition, without disabling animation or changing app CSS.

Settled run `browser-u10-badges-settled-3fd10ea` (3.8s, exit1) passed dark badge
colors/contrast and the entire light-phone group/capture. Its only remaining
dark failure was expecting `.focus()` after a mouse click to imply keyboard
`:focus-visible`. Dark-only continuation `browser-u10-badges-dark-3fd10ea`
(3.2s, exit0) uses a real Tab and records pointer focus-visible=false versus
keyboard table-link focus-visible=true, outline3px. It completes only unfinished
dark scope/capture; passing light scope was not repeated. Source3fd unchanged.

Combined two valid PNGs: dark-desktop-rounded-tables in the dark continuation,
light-mobile-rounded-cards in the settled run. JSON/logs adjacent preserve all
authoritative exits and first failures. Console/network arrays empty throughout.
All3 status backgrounds exactly match history fills in h2 and smaller accordion,
18 actual badge samples per context. Dark collapsed/expanded/System minimum
digit ratio5.0179; explicit-light phone minimum4.5275. Slashes/totals match normal
ink; totals remain transparent. Four table borders exactly match header1px solid,
corners8px/header divider2px/final cell bottom0. Mobile table border0/cards1px,
transparent gaps, no overflow, focus and popup containment pass. No new app
defect, source edit or independent-review invalidation; browser/runner finished.
Final harness SHA256`5ee8e522128325da7e2160f20d13c2c141d360acc0b2a63ed215491dce491395`.
Lead notified promptly for two-PNG visual acceptance and4567 refresh.

## Final user rejection of badges: plain counts restored

User explicitly rejected badge backgrounds and requested colored numbers again.
Final U10 amend is `0600f6fef933b80229cdde504cbebf912a8e71c1`, still one logical
commit atop9fb102e. Removed only eight badge CSS lines and five badge-doc lines;
CSS and appearance document are byte-for-byte identical to reviewed83b8893.
History red, original light fills, table frame/corners and all behavior remain.
CSS URL v8→v9 plus3existing test literals. Compared with83b, only layout/cache
test literals differ (3files4+/4−); no substantive new behavior. Lead reuses
reviewed83b source/browser scope under the narrow-deletion policy.

Rejected preview-only/unmerged3fd is retained at local branch
`2026-11-10-status-theme-responsive-preview-u10-rejected-count-badges`.
Prior83b/a927 refs and exact evidence remain. This restoration does not claim
3fd merged or change default history. No migrations or state conversion.

Final focused normal tests1.065s, preview4.768s, i18nhealth/diff passed. Hooks
passed0.45s(gofmt0.04/i18n0.37); source hashes identical before/after hooks.
Worktree/index clean, exclusive window released, no executing commands.

| File | Final SHA256 |
| --- | --- |
| public/status.css (exact83b) | a4af32ab614c8e11c4fcd53402e4b1809d772fa3866142b71b616d88fbd96202 |
| docs/reference/appearance.md (exact83b) | b4cf10a3b66b3e3743fad95b23591c95803a6c5f9e481147212bda5e0aa83a3b |
| templates/layout.tmpl | 277227e57b055848e355098a3198a0e3604483fb8b288a447925abcb0237ae55 |
| ui_routes_test.go | 495936d31169777361a2d5b9757752f884e9f326584e4c98cfce7113372ee282 |
| app_routes_test.go | 6e6a7072b4191986530dd7c9b0fc6e36a765083be37766c711aa0f3e1b432211 |

Lead immediately restored user4567 to the known-reviewed83b frozen plain-number
assets while this source restoration completed. No new browser harness/matrix
was prepared; exact83b computed style/border/capture evidence above is reused
within unchanged CSS scope. Lead owns final v9 rebind/publication/acceptance.
Implementer performed no service, push/default merge or lifecycle actions.

## Exact plain count/history color matching and regression

User explicitly prioritized exact shared bar colors for plain numbers in both
themes and requested a regression. Final owning U10 amend
`7fa5afc5a2504262c49b1c866adb57acd1efad13` atop9fb adds only three scoped count
foreground aliases to `--history-ok/maintenance/outage`; no count background,
padding, display, badge/global semantic change. All existing history colors,
table border/corners and behavior remain. CSSv10 and three URL assertions.
Approved lead writing corrects only the contradicted appearance count contract.
Five-file final delta69+/14−; no application Go/JS/input/migration changes.

Old0600 retained at local ref
`2026-11-10-status-theme-responsive-preview-u10-before-plain-matching`.
Old range9fb→0600 versus new9fb→7fa5 is a substantive exact-count-color successor,
not patch-equivalence or merged history. Prior a927/83b/rejected3fd refs remain.

New existing-suite `TestStatusCountColorsMatchHistoryWithoutBadges` reads the
real HTTP-served stylesheet. It compares count foreground and bar background
token references, checks token presence in light/manual-dark/system-dark root
contexts, allows count color-only declarations, rejects unexpected count override
rules, and tolerates declaration whitespace/optional final semicolon. No fixed
hex mirror, CSS engine, framework or dependency. Actual cascade remains browser
acceptance. Negative old0600CSS: all3 statuses fail, exit1,0.084s, log
`u10-plain-regression-before.log`; fixedCSS passes exit0,0.090s in
`u10-plain-regression-after.log`. Final whitespace-normalized test included in
normal focused batch1.047s and preview batch3.769s, both pass; i18n/diff pass.
Hooks0.45s(gofmt0.04/i18n0.38), worktree/index clean and window released.

Final source SHA256 hashes unchanged by hooks:

| File | SHA256 |
| --- | --- |
| public/status.css | a3169c88268a04b41bb4c9e9bef814788028dbc5bcba545b9cba8af30a4e9716 |
| templates/layout.tmpl | 265e7ead53fe0897ac8bad3e6e169135b434b93071471778775b1ff50f273b8e |
| ui_routes_test.go | 6405548b016a9e0f8cabd78c5560ee80d56a51b36630586fcb915a5316867c8b |
| app_routes_test.go | a27af4ccdd4d96be096a566259aecd20d421408c30abcc46debcc2b0d5adeda3 |
| docs/reference/appearance.md | 0daad840fde6ccbbdd29ae2cd914b4bb1987df60e95d1ef6d8bb178524b004c1 |

Source completion reported promptly before browser preparation. Lead owns final
review/candidate/release, publication and4567 refresh. No browser/services/push/
default integration yet. Browser scope remains two captures and actual plain
count foreground==barfill/transparentbg/padding0/inline in H2 and small accordion
under light/manual+system dark, waiting existing real color transitions.

### R10 and final actual matching acceptance

R10 final source review7fa5 passed no findings/history/docs/test. Lead released
immutable18090. Existing script SHA256
`f8f5881ecba729bf25114e4413cd8c619d08948ab8cfc6c6d3fe51cceec7c108`
ran once2026-11-11 07:16:44–07:16:48UTC(4.2s), authoritative exit0, two groups
passed/two desktop PNGs. Evidence `browser-u10-plain-matching-7fa5afc/` and adjacent
`.log`. Errors/console/network empty; no harness correction, retry, app/Git/service
action, focus/contrast gate or scope expansion. Browser/runner finished.

18 actual H2+small-accordion samples/context match rendered bars exactly:
dark collapsed/expanded/System green134,239,172; yellow252,211,77; red239,68,68.
Light green25,135,84; yellow255,193,7; red220,53,69. Every sample has transparent
background, padding0, displayinline and preserved title/ARIA; separator/total plain
ink retained. Native color transitions finish before settled sampling. All retained
table/header1px borders,8px corners,2pxdivider and no-overflow checks pass. Immediate
result and two PNG paths sent to lead for visual acceptance/4567 refresh.

## Final integration refresh, 2026-11-11

User explicitly directed status/master integration. Fresh upstream advanced9fb
to`9ef71e50a68e9b5c8ceac199ce5d87e7d9dd2aa7` via one automated dependency commit:
modernc/libc1.80.2→1.81.0, cc/ccgo sums and matching ordinary package vendorHash.
Only go.mod/go.sum/nix/package.nix changed upstream; no application, assets,
schemas/migrations, routes or fixtures. Retain reviewed7fa at
`2026-11-10-status-theme-responsive-preview-u10-before-final-rebase`.

Normal conflict-free rebase yielded
`8e17ccb9728bed308bbe7d67126eb84dfdf8a81c` atop9ef. `range-diff` marks the single
UI commit unchanged. Old9fb→7fa and new9ef→8e17 binary/full-index patch bytes are
identical SHA256`0deb5f2a4edccd9982aae7e76cc1edea29c2ca9fbaa9925b999c4594a3c60900`;
stable patch ID`93d279174c22a25675d0d456a0f843c36c7488cc`. All five reviewed file
blobs and every public/templates asset are identical. Lead independently rebuilt
the final tree and saved R10 equivalence certificate
`u10-rebase-review-equivalence.json`; no new review or UI browser run is needed
for unchanged patch/assets. Accepted7fa preview remains unchanged. No migrations.

Rebase's ambient prepare-message hook printed missing Lefthook PATH; no bypass
flag was used. Nix resolves the declared tool and required pre-commit all-file
hooks ran successfully without source changes. Existing quick exec21881 joined
exit0; a fresh installed Luna/low watcher could not access that parent-owned
session, returned incomplete and launched no duplicate command. Parent fallback
joined it and ran the remaining ordinary batch as directed by lead.

`u10-final-rebase-go-checks.log`: full normal Go11.196s, full preview Go14.781s,
count regression0.091s, i18n health and hooks0.55s, all pass; total37.424s,
authoritative exit0. Worktree/index clean and patch equality rechecked after
format hooks. No VM or package deployment/service/lifecycle action.

Fresh fetch kept target9ef. SSH feature push used exact force-with-lease old7fa
and succeeded; remote proof feature8e17/master9ef. Session comparison captured
exact9ef→8e17. New head CI runs at report time: i18n43019893456 and
Integration43019893520, both in progress. All older branch runs were completed,
so no stale active run required cancellation. Lead owns CI continuation, short
merge claim/default mutation and final acceptance. Index/rebase/push window
explicitly released; no commands or watcher work remain executing here.

## Lead acceptance and user preview refresh

R8 independent source review passed without findings. Lead visually inspected
both browser PNGs; stronger red/yellow distinction and rounded desktop/mobile
surfaces accepted. Ordinary SSH feature publication verified a927; master stays9fb.
Onlyi18n workflow42900781621triggered andpassed. Comparisoncapturedexact9fb→a927.

At21:01UTC lead replaced only old registered4567service65d5b15f with new
a0554170-335b-4d1b-ab8b-91661343292b via native service stop/run under user's refresh
request. Frozenpreview-data-a9273d2 exactassets; HTTP200/publicCSSv6 hash matches
b1cca98a115da88a105f48e96215f7c6586913d6cf9049b539f366d6d1f207e9.
Preview http://aitherdev.int.vpsfree.cz:4567/?lang=en. No newdefaultmerge/deploy.

## Historical matching and approved count badges

Lead checked pre-sessione560historyCSS plus the exact referenced Bootstrap5.2
beta1stylesheet. Original status counts and bars matched green#198754,
yellow#ffc107,red#dc3545. Sessioncontrastforegroundchanges introduced mismatch.
Userexplicitlyselected matchingfilledcountbadges, emphasizing sharedmeaning;
permits better readablecolors. D11brief uses exactcurrenthistoryfillbackgrounds
with contrastingnumeralink, avoiding pale yellow plaintext, noglobaltextpalette
change. Mainagentwriting/humanizerpassed conciseappearanceparagraph. Border
only83bproofcompletedfirst3.7s2groups/2PNGnoerrors; no need refreshuserpreviewtwice.

## Final combined preview refresh

Leadacceptedactualtwo-themebadge/borderproofandvisuallyinspectedlight-phone+
darkdesktopPNGs. Currenthead3fd10ea793ff727a66a01ac9002a214214b19652 and frozen
13assetsservedbynewregistered4567service8a3c5616-cd92-4a0e-a3f7-fdaab7c11a07.
Olda055service stoppedonlyforrequestedrefresh; no othercleanup/lifecycle. Public
HTTP200/CSSv8hash26d823e635055304871588471737a93ad6a06a32efc381ff5daf36298e2d4237
matchesreviewedcandidate. Exactcompiledbinaryreuseproof retained. Newfeature
publishedwithforceleaseagainst83b, master9fbunchanged. Newpolishnotmerged.

## Lead exact-matching preview delivery

R10source reviewnofindings; leadinspectedbothlight/darkPNGs fromfirstpassing
computedRGBcheck. Numberforegrounds exactlyequalbarbackgrounds for3statuses/H2+
accordion inlight/manualdark/systemdark, transparentbg/inline/padding0. Oldbar
paletteunchanged. Regressionbeforeold0600FAIL/fixedPASS/quickchecksPASSretained.
Registered4567serviceda1562b3-b0c8-4d7b-8ab8-0ab2e84e62b0 servesexactfrozen7fa
assets/CSSv10SHAa3169c88268a04b41bb4c9e9bef814788028dbc5bcba545b9cba8af30a4e9716.
PublicHTTP/assetverified, priorc6e6servicereplacedonlyforrequestedrefresh.
Publishedforcelease0600→7fa, master9fbunchanged, comparisoncaptured. ExistingCI
42978279940observedbyb9c10c91, no newdefaultintegration/deployment/lifecycle.
