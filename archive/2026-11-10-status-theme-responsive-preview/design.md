# vpsf-status themes, responsive layout and standalone preview

Status: **ACCEPTED FOR IMPLEMENTATION** — D1 accepted; P1/P2 released by lead
after user direction to proceed, 2026-11-10. D2 refreshes the implementation base.
Owner: architect0 (retained GPT-6 Astra/xhigh, workspace_write).
Lead owns scope acceptance, package release, plan/state and user communication.
Architect work is limited to this brief; implementers own application changes.
The D3 addendum below supersedes the original visible theme/language controls
and adds only the user's original light-history palette and dark-logo corrections.
D4 refines the settings trigger and header wrapping and records the theme-click
acceptance requirement; all other accepted contracts remain in force.

## Scope and evidence

Change only vpsf-status presentation and an opt-in development preview. Keep Go
rendering, routes and status calculations. Web/WebUI are visual references only.
Session identity/environment matched; the live roster was read. D1 inspected local
remote-default refs without fetching. Lead fetched the implementation base below;
architect inspected its manifest and base diff. Neither establishes deployed state.

| Source | Exact revision | Commit date |
| --- | --- | --- |
| vpsf-status implementation base, fetched `origin/master` | `e560b43b01b7b387f1cd7a40a635d27f3b7fba2b` | 2026-11-10 |
| web `origin/master` | `7fec3e3ccc5a1aa41bad7f06f83d01fa6cd15fe9` | 2026-11-09 |
| vpsadmin-webui `origin/main` | `88ac13b89d6421c914cd57e18153de1fee6fc7b7` | 2026-11-09 |

D1 status evidence was read at `018b700f06cf216a125a70ac9bfedddaabf07b92`
(2026-10-24). Its complete diff to the implementation base changes only `go.mod`,
`go.sum`, `flake.lock` and `nix/package.nix`; rendering, fixtures and app interfaces
are unchanged. Worktree: `worktrees/2026-11-10-status-theme-responsive-preview/vpsf-status`.
Targeted evidence at the recorded revisions:

- Status `main.go`, `app.go`, `index.go`: Go `html/template`; `/`, `/entity`,
  `/group`, `/about`, `/json`, `/metrics`, `/static/`; cached locale-specific index
  bodies with a request-time shell. Entity and group pages share `entity.tmpl`.
- `templates/{layout,index_header,index_shell,status,entity,history_bar,about,loading}.tmpl`:
  Bootstrap 5.2.0-beta1 CSS/JS and Bootstrap Icons 1.8.3 via jsDelivr; custom CSS
  and popover positioning are inline. Headers repeat in index, entity and about.
- `localization.go`, `i18n/README.md`: English/Czech; `?lang=` overrides browser
  `Accept-Language`, with localized navigation. Source catalog is
  `internal/i18n/catalog/messages.go`; editable Czech is `i18n/cs.toml`;
  `*.active.toml` is generated/embedded. Use `make i18n-update` and `i18n-health`.
- `status.go`, `test_helpers_test.go`, `history.go`: `openConfig` creates state
  without probes; `initialize` starts probes. Tests already build a real application
  with synthetic operational state, a fixed clock and temporary SQLite history.
- `go.mod`, `flake.nix`, `Makefile`, `nix/package.nix`, `config-sample.json`:
  existing Go toolchain/dependency graph and assets; sample config targets real
  services and is unsuitable as a synthetic preview. Reads beyond UI entry points
  established preview startup/state isolation and packaging dependencies.
- Web `css/{bootstrap.min,style_own}.css`, `cs/hlavicka.html`: navy
  `#16273f`/`#1f3959`, white text, orange `#f6914b`.
- WebUI `src/styles/index.css`, `src/app/theme.tsx`,
  `src/components/layout/PublicThemeSwitcher.tsx`: navy/orange palette, semantic
  tokens, System/Light/Dark preference and explicit `data-theme` overrides.

## Accepted appearance and behavior

Use restrained navy surfaces and orange links/accents, preserving the familiar
status-page information order. Light is white panels on pale blue-gray; dark is
navy panels with brighter secondary text and visible control boundaries.

| Token | Light | Dark |
| --- | --- | --- |
| Page / panel / raised surface | `#f3f6fb` / `#ffffff` / `#e8eef7` | `#111f33` / `#1f3959` / `#294565` |
| Primary / secondary text | `#16273f` / `#475569` | `#f8fafc` / `#c3cede` |
| Link / control border | `#9a450b` / `#68768a` | `#ffb16c` / `#7186a2` |
| Success text / background | `#166534` / `#eaf7ef` | `#86efac` / `#163b2b` |
| Warning text / background | `#854d0e` / `#fff4df` | `#fcd34d` / `#493510` |
| Failure text / background | `#b91c1c` / `#fff0f0` | `#fca5a5` / `#4b232b` |
| Information text / background | `#1d4ed8` / `#edf4ff` | `#93c5fd` / `#1b3658` |

Target WCAG AA: normal text ≥4.5:1; meaningful icons/control boundaries ≥3:1;
visible focus. Keep status labels/icons as well as color.
Calculated sRGB samples: light body 15.04:1; dark body 11.23:1; dark secondary on
raised surface 6.19:1; dark link there 5.51:1; semantic pairs ≥5.85:1 light and
≥6.79:1 dark. Dark control border on panel is 3.15:1; recheck each actual surface.
For comparison, current warning yellow on white is 1.63:1. WebUI's dark danger
token against its danger-row token is 2.49:1; this is a token calculation, not a
claim about every rendered WebUI component. Verify computed styles in the preview.

Put a labelled native theme dropdown beside the language control in a shared
header: **System / Light / Dark**. Localize its label/options in both catalogs.
Retain the brand and page title, back navigation on detail/about, and timestamp
on the overview. Controls should have approximately 44px touch height and remain
visible without a hamburger menu. Confirm the existing logo works on both themes.

Default to System. Store explicit `light`/`dark` in origin-local
`localStorage["vpsf-status.theme"]`; System removes the override. Invalid values
fall back to System. A small guarded inline script before styles sets the root
`data-theme` for first paint. CSS media queries handle System, including OS changes;
manual choices override them. Set matching `color-scheme` for native controls.
Storage failures must not break rendering or in-page switching. A storage listener
can synchronize other tabs. Without JS, follow system CSS and hide the inactive
manual control. Theme is browser-only: no cookie, query parameter or cache variant.

Keep Bootstrap at its existing version for this change; 5.2 does not provide the
5.3 theme switch contract. Add a small local stylesheet overriding all used
surfaces, tables, text utilities, badges, alerts, accordions, pagination, dropdowns
and popovers. Use semantic variables, opaque popovers and clearly visible focus;
do not merely darken the body. Give new local assets versioned URLs for the
existing 24-hour static cache. No typography or icon framework is required.

## Responsive layout

- Desktop: retain compact status tables and hierarchy; allow long names to wrap.
- Tablet (roughly 768–991px): let header groups wrap; keep controls together and
  put the timestamp on its own line when needed. Reduce excessive inner padding.
- Phone (<768px): stack outage/advisory and probe-event rows into readable entries
  with real localized field labels; preserve table header associations, all data,
  links and event coverage grouping. Keep small node/DNS matrices tabular where
  they fit. Wrap long hostnames/messages; never clip important status or links.
- Current seven-column incidents and six/seven-column event logs have no responsive
  wrappers. Avoid page-wide overflow; local horizontal scrolling is a fallback
  for genuinely tabular content, not the primary incident-reading experience.
- The default 90-day history grid has a 358px minimum (90×2px + 89×2px gaps).
  Contain overflow within the history track; preserve every day. On coarse pointers,
  use larger day targets and horizontal scrolling with the recent end initially
  visible. Verify tap/focus opening, reachable links and dismissal of popovers.
- Preserve readable text at 200% zoom, footer wrapping, and keyboard navigation.

## Standalone preview and released execution packages

Use a preview-only Go build entry (`preview` build tag; normal `main.go` excluded
only for that tag). Reuse `application.routes`, templates, localization and view
builders. Seed synthetic status and a disposable SQLite directory; never call
`Status.initialize` or use production config/state. Freeze the clock for captures.
Default to loopback; label the preview synthetic. Include healthy, maintenance,
down/degraded, loading/fetch-failure, notice, advisory, long-text, entity/group,
history/popover and paginated-event examples. No exhaustive monitoring simulation.

Dependencies: repository Nix dev shell and current locked Go module graph
(Go, embedded `modernc.org/sqlite`, go-i18n and client/metrics dependencies),
`templates/`, `public/`, and a writable disposable history directory. No database
server, credentials, ICMP privilege, vpsAdmin service or VM is needed. Browser
network access to existing jsDelivr CSS/JS/icon fonts remains required; this is
backend-independent, not a promised offline bundle. Preview launch must use
`dev-session service run` under the lead's released preview scope.

| Released package / owner | Files and dependencies | Acceptance and evidence |
| --- | --- | --- |
| P1 UI — implementer0 | Templates; new `public/status.css` and `public/theme.js`; `app.go` only for shared-header parsing; catalogs/generated translations; focused rendering tests. Accepted appearance/behavior brief is the dependency. | Both themes and locales on all HTML routes; responsive examples and keyboard/touch checks; exact diff/head, screenshots and check results. |
| P2 preview — implementer1 | `main.go` build tag; new preview-tagged entry/fixtures/tests; README preview instructions. Reuses current app interfaces, no `app.go` edits. Independent of P1 implementation. | Synthetic routes/history work without outbound probes; normal CLI/build remains unchanged; startup/dependency instructions and exact check evidence. |

Both packages are **released by lead** under these unchanged interfaces. Lead owns
acceptance and Git windows; architect0 and assigned peers resolve routine technical
clarification directly. UI/preview checks join after both.
JSON/metrics, API clients, schema, protocols, NixOS options and production pins
stay unchanged. Old code ignores the new browser preference. Deploy app/templates/
assets together if later authorized; rollback needs no conversion. Preview history
never enters production. No coordinated node updates are needed.

Quick checks after implementation: `go test ./...`, `make i18n-health`, focused
preview-tag tests/build and normal build, plus route rendering in English/Czech.
Use registered preview browser checks at 320/390/768/1024/1440px: both palettes,
system changes/manual persistence, first paint, blocked storage, zoom, long text,
no body overflow, popover edges, keyboard/touch controls and computed contrast.
Commit and pass quick checks before mandatory final review. No devcluster is needed
to judge this UI; `./test-runner.sh test status-page` remains a later service check
if warranted. Long/uncertain builds and tests require a verification watcher.

Verified here: source structure, fixture construction seam and sampled color
arithmetic. D2 found no source-interface change invalidating either package;
dependency compatibility still requires the planned implementation checks.
Preview compilation/startup, browser rendering/accessibility, logo treatment and
runtime network isolation remain untested here. No design blocker was found.

## D3 — compact settings, original light history palette, official dark logo

User-directed follow-up, 2026-11-10; D3 accepted and full U2 released by lead to
implementer0. Inspected head: `9958b0375eb4d7c655cdc505a76e46ec95301cd4`.
Scope is these three visual changes only; preserve the existing layout, status
semantics, preview fixtures and history-popover behavior (including the guarded
delayed dismissal). No backend, routing, preference-key or persistence migration.

- **Light history:** restore the entire original light history palette following
  the user's clarification, “fwiw i liked all the colors of history bars in the
  original theme”. Base is `e560b43b01b7b387f1cd7a40a635d27f3b7fba2b`:
  `templates/layout.tmpl:21–23` gives OK `#198754`, maintenance `#ffc107`,
  outage `#dc3545`. Include original warning/outage/unknown/coverage fills as
  applicable; implementer0 supplies the exact complete mapping from that base,
  without inventing missing states. Keep independently accessible semantic text
  colors and all dark-theme colors unchanged. No new architect investigation.
- **Dark logo:** copy official `web:obrazky/vpsFree-bile.png` from revision
  `7fec3e3ccc5a1aa41bad7f06f83d01fa6cd15fe9`, blob
  `41a78b8dc4f2ee76d847453b7d2da85ae4f037f6`, to `public/vpsfree-dark.png`.
  The English website's `en/hlavicka.html:50` uses this asset. Inspected PNG is
  transparent RGBA, 173×50, with white lettering/outline and orange “vps”; it is
  a verified repository asset, not a claim about the currently deployed website.
  Keep existing `public/vpsfree.png` in light mode. Use CSS-selected images in
  the same brand slot (preserve intrinsic proportions); dark removes the current
  white image background/padding. No inversion, recoloring or remote hotlink.
  Reuse explicit-theme/system media selectors so logo and palette agree before
  first paint and without JS. Expose only one accessible brand name; hidden image
  must not duplicate it. Check sharpness at intended size, without enlarging the
  smaller asset beyond its intrinsic size merely to match the old image width.
- **One settings control:** replace visible theme/language widgets with one native
  `<details>` and a 44×44px `<summary>` showing a three-dots icon and localized
  accessible Settings name. Keep back navigation and timestamp in their current
  roles. Use an opaque, right-aligned panel constrained to the viewport; no nested
  dropdown and no ARIA `menu` role for these ordinary form controls.
- Inside, use a labelled fieldset with three native radios styled as icon choices
  (system/display, sun, moon), each with localized accessible name, selected mark
  and focus indication. Native radios retain Tab/arrow/Space behavior. Keep the
  panel open after theme changes. Preserve first-paint bootstrap, System following
  the OS, `vpsf-status.theme` semantics, invalid/blocked storage behavior and tab
  synchronization; update selection for every theme change, including storage.
- Add a labelled language `<select>` whose options use `.Locale.SwitchLinks`:
  `value=.URL`, visible `.Label`, selected `.Active`. Navigate to the selected URL
  on committed change; reuse those server-generated URLs verbatim, preserving
  entity/group IDs, pagination, preview scenario and other current query values.
  Do not reconstruct URLs in JS or submit a language-only form. Native select
  keyboard handling must remain intact.
- Progressive enhancement: native details and existing localized language links
  work without JS. Theme radios and language select start hidden; reveal after
  their handlers/selection are installed, then hide the fallback link list.
  Without JS, only language links show inside settings and system CSS selects
  theme/logo. With JS, close on outside pointer or focus leaving the details;
  Escape closes and returns focus to summary. Summary can toggle with Enter/Space.
  No focus trap; outside interaction retains its destination focus. Preserve
  native select interaction and existing history Escape/outside behavior.

U2 owner implementer0: `templates/index_header.tmpl`, `templates/layout.tmpl`,
`public/{status.css,theme.js,vpsfree-dark.png}`, relevant catalogs/generated
translations and focused route/UI tests. Existing app interfaces suffice; no
`app.go` change is needed. Lead owns final localized prose, release and acceptance;
architect0 remains the routine technical contact. Full U2, including all original
light history colors, menu and logo, is released under these contracts. No blocker.
Source inspection stayed within eight targeted application/reference files;
no HTTP requests, builds, service actions or application edits by architect.

Acceptance: bump CSS URL from `v=1` to `v=2`, JS from `v=2` to `v=3` for the
24-hour asset cache; new logo path is distinct. Quick checks cover template render,
fresh translations and normal/preview tests affected by markup. Browser checks:
all light history fills match the recorded original mapping (OK `rgb(25,135,84)`)
with semantic text/dark unchanged; official
dark logo without white plate in System/manual modes; one compact trigger at
320/390px and desktop, no overflow; open/close/focus, native radio/select keys,
persisted/cross-tab/blocked-storage theme, language query preservation, no-JS
language links and first-paint logo/theme. Capture light/dark header + open panel.
Visual result and browser behavior remain implementation acceptance checks,
not verified by this source-only addendum. No wider UI redesign is authorized.

## D4 — smaller gear, working theme clicks, timestamp in the header row

User-directed refinement, 2026-11-10. U3 is already released by lead to
implementer0; this addendum reconciles its sufficient direct brief, without
additional scope. Architect0 checked identity/retained settings and only the
existing brief, header/CSS and recorded narrow-panel evidence. Implementer0 owns
actual-browser/event diagnosis and the fix; implementer2 owns assigned browser
acceptance. No root cause is inferred by this design update.

- Replace the three-dots glyph with existing Bootstrap Icons `bi-gear`, sized
  about 16px. Use a compact approximately 32×32px summary on fine-pointer desktop;
  retain a 44×44px hit area for coarse pointers. Preserve the localized Settings
  accessible name, native details semantics and visible keyboard focus.
- Put brand, Rendered-at timestamp and actions on one header row whenever their
  contents fit. Remove the unconditional full-row timestamp requirement. Keep
  actions at the inline end; allow wrapping only when available width requires
  it. On narrow screens timestamp may use its own line. No clipping, truncation,
  forced tiny text or fixed desktop breakpoint that wastes otherwise ample room.
  Keep existing Back navigation and the right anchoring of its settings panel.
- Clicking the actual system/sun/moon glyph or its choice label must select that
  theme immediately and leave the panel open. Native radio keyboard behavior,
  selected indication, storage/cross-tab updates and first-paint behavior remain
  unchanged. Outside/focus-exit and Escape dismissal still work; user clicks
  inside theme choices must not be mistaken for a request to dismiss the panel.
- Preserve the existing language select/query behavior, no-JS language fallback,
  official logos, light-history palette, dark colors and history-popover behavior.
  Recheck the six established narrow Back-panel cases: entity/group/about at
  320px and 390px, with the panel wholly within the viewport and no body overflow.

U3 boundaries remain header template, local CSS/theme JS, necessary cache URL
bumps and focused tests under implementer0; lead owns acceptance and prose.
Minimum evidence: affected quick checks, actual glyph-click theme changes with
panel remaining open in desktop/touch browser checks, compact gear/focus sizing,
one-row desktop header when it fits, narrow wrapping and the six Back-panel cases.
Reuse unaffected passing evidence. No new assets, dependencies or backend changes.

## C7 — separate app inputs from the cached integration OS composition

**Withdrawn by user direction, 2026-11-10:** retain the original status input graph
and wait for matching upstream kernel-cache publication before rerunning tests.
The following proposal is historical, not an active implementation instruction.
Implementer0 restores its owned uncommitted input changes; CI visibility
diagnostics remain independently allowed. No U5 graph evaluation or rerun.

Sufficient correction brief, revised 2026-11-10 after user feedback to remove
the permanent nested revision override, based on final app head
`2d448fd21e8ea5ec3b2a1322bb170d35617470ce` and C5/C6 in `c1-ci-stage.md`.
Owner: implementer0, package U5; lead accepts release/check scheduling. Scope is
`flake.nix`, Nix-generated `flake.lock`, `.github/workflows/integration-tests.yml`
and a short existing test-documentation note if needed. No application, kernel,
VM topology, test-assertion, Go dependency or vendor-hash change.

### Settled input and package interfaces

Replace root nixpkgs follows with its own updateable app input. Restore the
OS's upstream locked composition in the generated lock, with no nested override:

```nix
inputs = {
  vpsadmin.url = "github:vpsfreecz/vpsadmin";
  vpsadminos.follows = "vpsadmin/vpsadminos";
  nixpkgs.url = "github:NixOS/nixpkgs/nixos-26.05";
};
```

Keep vpsAdmin source `3f9b68adb97b7f43df929a85fc172d9d11e15211` and OS/test-runner
source `837baf04054c6ee0e71d288b8870ac42a6990c38`. Root nixpkgs locks to current
`ac588ef1c914865dad517b337ea0eb9694a4021c`; packages, overlays and devShells retain
that input and Go 1.26. Both mkTests and mkTestsMeta set
`pkgsPath = vpsadminos.inputs.nixpkgs.outPath;`. Keep suiteArgs supplying the modern
`self.packages.${system}.vpsf-status` and current module to the older VM package
composition. vpsAdmin's own nixpkgs already follows its OS input, so both align.
Root input name stays `nixpkgs`: the existing forward-only app dependency updater
continues updating that independent input without changing the OS package set.
Future intentional OS updates use the upstream composition and ordinary cache
verification; there is no extra revision literal in flake.nix to maintain.

After editing declarations, generate the lock from the last passing run's complete
lock at `018b700f06cf216a125a70ac9bfedddaabf07b92`. That lock already has the same
vpsAdmin/OS source revisions and upstream ee48 package composition. In the own
app worktree, use a temporary reference file; do not hand-edit JSON:

```sh
reference_lock=$(mktemp)
git show 018b700f06cf216a125a70ac9bfedddaabf07b92:flake.lock > "$reference_lock"
nix flake lock --reference-lock-file "$reference_lock" \
  --override-flake github:NixOS/nixpkgs/nixos-26.05 \
    github:NixOS/nixpkgs/ac588ef1c914865dad517b337ea0eb9694a4021c
```

The one-time full-ref mapping keeps the new root at exact ac588ef while preserving
its updateable nixos-26.05 original URL. A no-build/no-write metadata probe using
this reference lock verified the complete result: every baseline locked identity
retained, only modern ac588ef added, and OS nixpkgs original remains nixos-26.05
with ee48 locked. Root hash stays `sha256-XuAV2cUwaod3Bt4XFVqiXz3v1w2ex16W6Sv4S7EWres=`.
Probe fixture/evidence: `/tmp/2026-11-10-status-theme-responsive-preview-c7-input-probe/`.
Actual application lock generation remains U5's check. Removing the old declaration
alone preserved its exact-revision original in the candidate lock; an attempted
nested OS refresh selected current staging and changed unrelated inputs, so neither
is the recipe. Inspect semantic paths, not unstable node suffixes, and confirm no
other source/hash changes versus final 2d448fd. Verify ordinary evaluation with
--no-update-lock-file and without the mapping. No registry subsystem is added.

### Diagnostics and verification gate

Add runner `--verbose`, capture stderr with `2>&1 | tee test.log`, retain pipefail.
Change the existing full-log upload condition to `failure() || cancelled()` and
include `test.log` alongside per-test logs/text. Preserve current timeouts,
assertions, cleanup and result evaluation. Cancellation upload is best effort
within Actions cancellation handling, not a guarantee after runner loss. Verify
official current action refs under the workflow procedure; no new log framework.

Before any full test run, evaluate the complete selected status-page testJson
derivation using the pinned runner's actual evaluation expression and capture its
input graph. Disable import-from-derivation builds; if evaluation needs an
unrealized generated input, report that exact prerequisite instead of building
it implicitly. Metadata/test listing alone is insufficient. Confirm both plain
and builtin-ZFS kernel out/dev identities and query their configured trusted
cache narinfos; require matching available substitutes before full execution.
No kernel build exception is established by C6. Cache absence or differing OS
source/inputs blocks rerun and returns to lead with exact evidence.

Quick acceptance: semantic lock diff/source preservation; ordinary no-update
evaluation; root Go/package identity remains modern; tests/testsMeta share the
restored OS input and unchanged suite/resources; complete config/kernel/cache
evidence; workflow syntax and focused Go/package checks appropriate to the input
change. Lead schedules evaluation/long checks and independent committed review;
then one faithful full three-VM/seven-example CI run, with detailed logs, on the
reviewed final head. No duplicated local run or weakened merge condition.

Compatibility: this changes build-input composition, not API, storage, schema,
UI behavior or runtime settings. The modern app carries its Nix runtime closure
into older test VMs; actual mixed-closure operation still requires integration.
No production OS change/deployment is included. Recovery is a coherent revert of
this input/workflow patch, which restores the known cache problem rather than
solving it; no data rollback/migration is needed. Restored kernel cache availability
and full-suite success remain unverified dependencies, not promised outcomes.

## K1 — populate kernel caches after upstream input updates

Sufficient brief, 2026-11-10; implementer3 owns
`vpsadminos/.github/workflows/kernels.yml` and an optional short paragraph in
existing `docs/os/kernel-zfs-development.md`. Base/source is own registered
checkout `650170d699e3033c5279b911a2ef0a355439613c` (origin/staging).
Today's 10:16 UTC commit updates only flake.lock, nixpkgs c56a87d8e → ac588ef1c.
No kernel version/config/source, flake input, test, updater or deployment change.
Lead accepts package release and publication; no OS staging merge is approved.

The workflow currently watches only itself and os/packages/linux/** on staging
push/PR, plus daily 03:05 UTC. Add flake.nix and flake.lock to both path lists.
Preserve existing branch filters, schedule, all-version matrix, build command,
cache-copy and generation publication. Current `lib.kernelVersions` contains seven
versions, including stable 6.12.113, unstable 6.18.49 and retained 6.12.95. Running
the existing matrix covers the user's “at least latest stable” without a new
selection mechanism; input changes may therefore rebuild multiple kernel versions.

**Automated updates need an additional completion trigger.** The existing
`flake-update.yml` (“Update flake inputs”) checks out with GITHUB_TOKEN and pushes
with its default credentials. GitHub suppresses recursive push workflow runs
from this token, so paths alone would miss today's update mechanism. Add
`workflow_run` for that exact workflow, type completed, branch staging. In detect,
allow this event only on success, same repository and head_branch staging; other
existing events retain their behavior. No PAT, updater edit or dispatch subsystem.

For workflow_run, checkout trusted `refs/heads/staging` after completion: its
event head_sha is the updater's starting revision and can precede the pushed lock.
For existing events retain normal checkout ref selection. Detect exports the
resolved `git rev-parse HEAD` as an additional output, and every build checkout
uses that exact SHA, keeping matrix detection and compilation on one graph.
Preserve the existing branch/profile naming semantics. Completion can also follow
a no-change successful updater; rebuilding existing targets then reuses substitutes.
GitHub requires workflow_run configuration on the default branch; read-only API
confirmed staging is default. This does not become operational merely by pushing
our feature branch, and no run is requested by this design package.

Existing output coverage is sufficient: flake.nix kernelCiQemuSystems applies
kernelCacheToplevelModule to each ci-toplevel-kernel-VERSION target. It explicitly
links builtin-ZFS `boot.kernelPackage.dev` and plain
`boot.kernelForBuiltinsConfig.dev` into the toplevel. The boot closure retains
builtin out; nixpkgs ac588ef's standard multiple-outputs hook propagates each dev
to out, and these kernel derivations do not override that hook. Copying the closure
therefore retains both variants' out/dev outputs. Keep those existing targets;
no new output is needed. This builds current OS-source/input identities, not the
old status OS837baf with a downstream-overridden toolchain. It complements U5;
it does not establish cache coverage for the original status input graph.
The user withdrew U5's graph change and chose to wait for matching kernel-cache
publication before rerunning status tests; verify those exact outputs first.

Official release APIs checked during K1: actions/checkout v7.0.1 and
cachix/install-nix-action v31.11.3. Their action manifests use Node24 and composite
execution respectively. Use latest compatible refs in the touched workflow;
checkout's previous v6 already uses the same runtime generation. Preserve inputs
and review any compatibility requirement rather than adding unrelated upgrades.

Quick acceptance: YAML/actionlint; assert both input paths in push/PR filters;
successful same-repository staging completion accepted, failed/cancelled/other
branches rejected; existing nightly and kernel-path events retained; exact SHA
flows detect→build. No-build `nix eval --json .#lib.kernelVersions` and
`nix eval --raw .#lib.availableKernels.stableKernelVersion` must show stable in
the matrix and unchanged target-name conversion. Disable IFD builds. Source/static
coverage is enough for this trigger-only change; do not compile kernels or run VM
tests merely to validate YAML. Independent committed review remains required.

Publication boundary: ordinary feature push does not match the staging push
filter. A PR targeting staging does match and runs self-hosted kernel builds plus
existing cache SSH/profile writes; lead must account for this before creating it.
No cache credentials/policy, production activation or automatic kernel rollout
changes. Runtime/state/API compatibility is unchanged. Reverting this workflow
patch restores the old triggers; already published immutable store paths remain
valid and need no deletion. Actual Actions event delivery and cache publication
remain unexecuted verification, not claimed success.

## C8 / U7 — ordinary nested vpsAdminOS dependency refresh

Sufficient bounded brief, 2026-11-10. C7 remains withdrawn: retain original
flake.nix declarations and follows relationships, with no split, override or new
input. Implementer0 owns only the Nix-generated vpsf-status `flake.lock` and a
minimal existing test-doc note if useful, after lead accepts U5 completion and
releases U7. UI and K1 remain separately owned. Current status head at inspection
is `c4e11ec3f933de75f782b95bb3034ca31e3034d5`; use lead's final integrated base.

In the own status worktree run the ordinary command:

```sh
nix flake update vpsadmin/vpsadminos
```

No manual JSON, global update, reference-lock reconstruction or flake declaration
change. Verify the resulting exact OS is `650170d699e3033c5279b911a2ef0a355439613c`;
if upstream advanced, report the new identity before treating it as this brief.
A no-build metadata probe and actual ordinary update of an isolated fixture lock
both produced the same graph. Evidence is in
`/tmp/2026-11-10-status-theme-responsive-preview-c8-input-probe/`.

Expected semantic delta from the original status lock:

- vpsAdminOS: `837baf04054c6ee0e71d288b8870ac42a6990c38` →
  `650170d699e3033c5279b911a2ef0a355439613c`.
- Its impermanence: `7b1d382faf603b6d264f58627330f9faa5cba149` →
  `fa627f4c8b8e92f58f58a73d99ee4e1304e64eb2`.
- Its nixpkgsUnstable: `f13ff45afd1bb73e640eaa08a7066dbed07e3238` →
  `f4a03c008967841f2a0b3cb7c436fc6fc31671f6`.
- vpsAdmin stays `3f9b68adb97b7f43df929a85fc172d9d11e15211`; shared/root stable
  nixpkgs stays `ac588ef1c914865dad517b337ea0eb9694a4021c`, preserving Go 1.26.
  All other pins and follows remain unchanged. These two transitive changes
  belong to the selected upstream OS composition; do not independently freeze them.

The upstream default test kernel changes from 6.12.95 to 6.12.113. This is an
explicit test-baseline effect of the dependency refresh, not a kernel-source edit
or production rollout. Status suite, imported vpsAdmin cluster configs and current
test base contain no kernel version/config override. Expected current stable
outputs, already published by run `42803793083`, job `129787930399`:

| Variant | out | dev |
| --- | --- | --- |
| Builtin ZFS | `b043pwyanxjfz22hbiibv5wipqqcl932-linux-6.12.113` | `5kahy705jlci2fhhwmjr3hjn1cad8264-linux-6.12.113-dev` |
| Plain configuration kernel | `6fknvi25ssxff96569ykjd0pnnvsyi5n-linux-6.12.113` | `8jpmywdph9hpjd7irr5jnfai8ir95r99-linux-6.12.113-dev` |

All are /nix/store paths. Toplevel
`84j4bizm2y0slcl96xqaxjwacqyllwsh-vpsadminos-system-vpsadminos-26.05.git.650170d`
references both devs; each dev references its out. All four narinfo requests
returned HTTP 200 at cache.vpsadminos.org. Matching the actual status config to
these identities is still an acceptance prerequisite, not yet established by
source inspection alone.

Focused interface review: mkTests/mkTestsMeta arguments, makeTestLib, makeTest,
testFramework.sourcePath and packaged test-runner remain available. The consumed
Ruby overlay and test-runner/nix/lib.nix are unchanged. machine_class_for hook,
timeout class and shell method signatures used by the status extension remain.
New test JSON adds shell transport/rootDisk handling with its matching new runner;
the status wrapper does not construct those fields. No concrete interface break
was found. Old vpsAdmin services/node components with this newer OS still require
full-config evaluation and integration; no broader compatibility claim is made.

Acceptance sequence: semantic lock diff and unchanged flake.nix; ordinary
no-update evaluation of app/package and selected test metadata; then complete
status-page testJson derivation/input graph with IFD builds disabled, confirming
both kernel variants match the four cached paths above. Preserve all three VMs,
seven examples, resources, timeouts and assertions. If a missing option/API,
unrealized IFD prerequisite or different kernel identity appears, stop and report
the concrete blocker before expanding source scope or running the suite.
Lead schedules the bounded evaluation and exact-head independent review; then
one faithful full status CI run with existing detailed logs. No kernel build or
duplicate full test invocation is authorized by this design brief.

Runtime API/schema/data/UI remain unchanged; no production OS deployment or data
migration. App package inputs remain stable, though source/version identity can
change on the new commit. Recovery is a coherent revert of this lock-only update;
it restores the known old cache mismatch. Recreate isolated test state for the
new OS/runner rather than resuming C5's interrupted preparation. Unchanged UI/Go
evidence can be reused within its scope; it does not replace full integration.

## D11 — count/history color consistency (proposed, not released)

Bounded source-only assessment at status head `83b8893455a4042862597c140494f05ed004ca26`.
`templates/status.tmpl:3` shares the count spans between 1.5rem h2 headings and
normal-size accordion buttons; `public/status.css` supplies page/panel/expanded
backgrounds. With the linked Bootstrap defaults, button counts are 1rem, not
large text. No browser verification was run. Light counts currently differ from
all three history fills; dark green/yellow already match and dark red differs.

Exact fill colors as numeral ink are not readable across these contexts:
light yellow `#ffc107` has 1.40–1.63:1 contrast against the three light surfaces;
dark red `#ef4444` has 4.40:1 on page, 3.12:1 on panel and 2.62:1 on expanded
accordion. Light green/red are 4.53:1 on white but 3.88:1 on expanded background.
These calculated ratios do not support a blanket count-foreground alias to the
history variables. Keep original light bars and the accepted dark red unchanged.

Recommended optional follow-up: compact filled count badges, scoped only to
`.status-counts > .text-success`, `.text-warning` and `.text-danger`. Their
backgrounds use existing `--history-ok/maintenance/outage` respectively, so the
status color matches the bars exactly. Use white numerals on light green/red
(4.53:1), `#16273f` on light yellow (9.23:1), and `#111111` on all dark fills
(minimum 5.02:1 on red). Small inline padding and slight corner rounding suffice;
keep slashes/total plain, inherited type size, existing titles/ARIA and conditional
counts. Do not change global semantic text colors, other badges or history fills.
If count badges are unwanted, retain the current readable shades and explain
the distinction; exact matching numeral ink would require changing accepted fills.

Lead owns whether to release this follow-up; implementer2's current border work
is unchanged. If released, CSS plus its existing asset-cache reference are the
expected files; no data/API/storage changes. Quick acceptance checks the three
fill aliases and foreground contrast; browser acceptance covers h2 plus collapsed
and expanded accordion counts in both themes, narrow wrapping and existing
accessible labels. Reverting those scoped CSS rules restores current rendering.
