# Disposable native Files smoke receipt

Current status: **PREPARED `dd445cb0`, not executed**, expected runtime source
`dd445cb0627f93375f1378af6b59d30ef8b34875`. The lead reported this published
deployment-preservation successor atop live `76c9` archive fix: the Files patch
range-diff is `=` and all 14 task files, full JavaScript and renderer inputs are
byte-identical to smoke-tested `6a1bfad8287e98fe8f1c928e79e3e9e18d3b8062`.
This equivalence proof is lead-reported, not independently certified here.
Implementer2 changed only the temporary script's expected SHA from `6a1` to
`dd445cb0`; the existing HEAD/clean-assets guards, Files/settings scenarios,
history-restoration diagnosis and pinned command remain unchanged. Execution
awaits affected final review. No smoke/check run or application source edit was
performed for this preparation. The user authorized deployment only; this
receipt grants no integration approval.

Historical status: **SUCCESS / PASS, exit 0**, runtime source
`6a1bfad8287e98fe8f1c928e79e3e9e18d3b8062`. The corrected native Chromium
smoke passed under the lead's parent monitor, exec session `50509`, final chunk
`42d598`. Implementer2 inspected the matching JSON PASS result in
`/tmp/files-tab-verification-6a1bfad8-20261028/browser-smoke-final.log`.
All original Files scenarios and settings click scroll/viewport, URL hash,
Back-to-General and Forward-to-Automation checks passed. The exact pinned
store-path command below is unchanged; source and script were unchanged during
the run, and the lead reported no remaining operation. No duplicate execution
or log copy was performed. Final acceptance and session state remain lead-owned.

Preparation and diagnostic history: after the historical PASS below,
the lead reported this published successor atop deployed `2caa`, preserving
the deployed settings click fix, seven regression-test lines and asset version
65. The lead reported the Files JavaScript block and nine task files byte
identical to reviewed/tested `617235fc`; this receipt does not independently
certify that equivalence. Initially implementer2 changed only the temporary
script's expected SHA from `617235fce02ac7095d258c73575bb8a64696b6d1` to the
successor. The unchanged HEAD guard now rejects the old snapshot.

After affected final review passed, the reviewer requested actual Chromium
coverage for the preserved settings click fix. Implementer2 added a separate
minimal settings DOM route to the same disposable script/server. It extracts
the shipped session/settings tab handlers, hash-selection helpers and history
listeners unchanged from `app.js`, following the communication/presentation
browser tests' settings behavior. Prepared checks click General then Automation
inside an actually scrolled container, require stable window/container/tab-bar
scroll and tab-bar bounds, verify URL hashes and selected/hidden panels, then
use real browser Back/Forward to select General/Automation. The existing Files
fixture and scenarios remain unchanged. Output adds `settingsScenarios` only.

Quick syntax probe passed, exit 0:
`/nix/store/l07gdbxylzfl8pbx9pxy6fyg95w4hjwy-nodejs-24.19.0/bin/node --check /tmp/files-tab-browser-smoke-2026-10-28-implementer2/smoke.cjs`.
The pinned store paths and command below are unchanged. The lead owns the
parent-monitor execution and final evidence/state links.

The lead subsequently executed the extended successor smoke once, exit 1:
`/tmp/files-tab-verification-6a1bfad8-20261028/browser-smoke.log`, parent exec
session `19091`, chunk `a2e6ad`. Both native click stages passed. The failure was
at Back (`smoke.cjs:176`): the fixture incorrectly required unchanged scroll
during history traversal, beyond the click-fix contract.

An authorized isolated settings-only Chromium probe, exit 0, established the
cause without executing Files/full smoke. Evidence remains at
`/tmp/files-tab-browser-smoke-2026-10-28-implementer2/settings-history-probe.log`.
Under default `history.scrollRestoration = "auto"`, both clicks retained
container `scrollTop=40`, tab-bar top `99`. Back's `popstate` observed 40, then
native restoration/fragment scrolling moved to 179 before `hashchange`, with
tab-bar top -40; Forward retained 179. Hash, selected tab and visible panel were
correct throughout. Diagnostic-only `"manual"` kept 40 during Back/Forward,
isolating native history behavior from click automation and the shipped handler.
The final harness does **not** set manual restoration or alter browser behavior.

The lead confirmed the contract: preserve viewport/tab-bar scroll on native
clicks; correctly select tab/panel/hash on Back/Forward. The minimal correction
keeps all strict click position/viewport assertions and all history
selection/panel/hash assertions, while applying the position invariant only to
clicks. Native history scrolling remains an observed coverage limitation, not a
product regression finding or a new product promise. The corrected script's
pinned Node `--check` passed, exit 0, before the final successful execution
recorded above. Source, expected head and existing Files scenarios were unchanged.

Historical result, before the successor preparation:

Prepared by implementer2 for runtime source
`617235fce02ac7095d258c73575bb8a64696b6d1`. **EXECUTED / PASS, exit 0.**
After independent final review, the lead executed the command below under the
visibly reported parent-monitor fallback because native watcher launch tools
were unavailable. Lead-reported evidence: parent tool exec session `56326`
exited 0; call chunk `d71fb2` returned the JSON PASS result. Source and temporary
script stayed unchanged during the run; no operation remains. Implementer2
updated this receipt from the lead's result without duplicate execution.

Temporary directory: `/tmp/files-tab-browser-smoke-2026-10-28-implementer2/`.
It contains `smoke.cjs` and `shell.nix`; no persistent repository tests, source
changes, dependency trees or browser caches were added to tracking.

Exact command used for both historical PASS runs and prepared for `dd445cb0`
(explicit store paths, independent of Nix shell PATH activation; the script now
expects `dd445cb0` and includes the settings extension):

```sh
env \
  TMPDIR=/tmp/files-tab-browser-smoke-2026-10-28-implementer2 \
  XDG_CACHE_HOME=/tmp/files-tab-browser-smoke-2026-10-28-implementer2/cache \
  PLAYWRIGHT_MODULE=/nix/store/2xc3ahwfjaa3k3wpn4gslgws25swsyd7-playwright-core-1.59.1 \
  CHROMIUM_EXECUTABLE=/nix/store/789yhb4v2kq51jwl4acmmjvxs7mfrlhv-chromium-152.0.7977.75/bin/chromium \
  PATH=/nix/store/nly4cml071i82515r89rpdw38z55wjqd-git-2.54.0/bin:/run/current-system/sw/bin \
  /nix/store/l07gdbxylzfl8pbx9pxy6fyg95w4hjwy-nodejs-24.19.0/bin/node \
  /tmp/files-tab-browser-smoke-2026-10-28-implementer2/smoke.cjs
```

The shell pins runtime root nixpkgs
`a5cc6f2c37bf518436dc8d1c288ccd0c43c2f4c4`, supplying Node, Git,
`playwright-driver` and Chromium. The smoke refuses a different HEAD or
uncommitted changes to either exercised asset.

The first watcher attempt used `nix-shell --impure .../shell.nix --run 'node
.../smoke.cjs'` and failed with exit 127 before JavaScript ran. Evidence:
`/tmp/files-tab-verification-host-browser-617235fc-20261028/browser-smoke.log`
and `browser-smoke.result` (`elapsed_seconds=0`). A fresh shell probe resolved
the four exact package paths above; it did not reproduce the missing-Node PATH.
The original watcher's environment is not captured in those two logs, so its
specific PATH failure remains unproven. The corrected command removes shell
activation from interpreter lookup. A quick probe with these exact environment
and Node/Git/Playwright/Chromium paths exited 0: Node v24.19.0, Git 2.54.0,
Playwright module loaded, Chromium executable exists. No browser was launched.
The Node wrapper resolves internally to
`/nix/store/3307vfpkpybyzf4w7mcn1pavnylsvb35-nodejs-slim-24.19.0/bin/node`.
`shell.nix` also exports `NODE_EXECUTABLE` for explicit interpreter use.

It follows the existing Files contract test's extraction convention, retaining
the shipped client, Files block, read scopes and source renderer in a real DOM.
Files scenarios passed on both historical `617235fc` and `6a1bfad8` runs:
root-only collapsed defaults, native summary expansion,
direct children without prefetch, child/root Load more, native collapse abort
with deliberately late success ignored, cached reopening, selected markdown DOM
retained through paging, collapse and root replacement, and absence of recursive
endpoint calls. All recorded requests used the correct directory/file shapes.

Limits: controlled request promises, no backend or transport cancellation, full
portal/template/CSS, raw editor, hide/queue/409 coverage or live session fixture.
The settings fixture uses minimal scrollable DOM/CSS and two categories; it
exercises real Chromium navigation with shipped handlers, not the entire portal
layout, additional settings categories, keyboard controls or settings writes.
Existing contracts and broader verification own these areas.

The lead owns the shared state update; it was already dirty during preparation.
Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-28-files-tab-limit-diagnosis/>.
