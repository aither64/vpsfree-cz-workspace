# 2026-11-10-status-theme-responsive-preview

## Goal

I'd like to extend vpsf-status, so that:

- contains light/dark themes (auto detection + manual switch).. not sure how to handle this, it could be near language switch, but perhaps in a drop down menu? leaving that up to you
- the current theme is light, so you have to introduce the dark theme. use colors/inspiration from vpsfree.cz and the new dark theme from vpsadmin-webui (although this one is not perfect, it has insufficient contrast and is thus hard to read).
- make the design responsive to support smaller screens (tablets and phones)
- I'll need to see it in a preview server... we do have it integrated into vpsadmin dev cluster, but it is rather heavy, so maybe it'd be worth to run it standalone

Look it over and suggest a solution.

## Affected repositories

- `vpsf-status`: intended implementation, styling and standalone preview.
- `web` and `vpsadmin-webui`: read-only visual references from canonical bare repositories.
- `vpsfree-cz-configuration`: user-requested status channel update after status CI/merge.
- `vpsadminos`: user-requested kernel cache build trigger on Nixpkgs input changes, at least latest stable kernel.
- Coordination workspace: this session's plan, state and proposed design only.

## Approach

User directed implementation after the proposal: "proceed with implementation".
Architect `architect0` owns `design.md`; implementer0 owns themes/responsive UI
(P1), implementer1 owns the opt-in synthetic preview and its documentation (P2).
Implementer2 prepares browser-verification tooling (B1), with browser execution
assigned after dependencies pass. User subsequently approved vpsf-status/master integration conditional on passing CI and requested its configuration channel update; no deployment authorized.

The accepted brief is [design.md](design.md); P1/P2 are released on the refreshed
vpsf-status base `e560b43b01b7b387f1cd7a40a635d27f3b7fba2b`. Reference-to-current
changes are dependency-only and did not invalidate the design's source interfaces.

## Decisions

### User visual feedback after preview

User requested three refinements: restore the entire original history palette in light
mode; use branding suited to the dark header (check vpsfree.org if necessary);
replace the large visible controls by a single settings/overflow icon opening a
dropdown with theme icons and a language select. This supersedes the initial
two-visible-controls recommendation. Preserve the accepted responsive layout,
contrast for text, browser preference, localization and monitoring boundaries.
Architect0 owns bounded D3 brief/asset evidence; implementer0 will own complete
U2 application edits/checks/commit/refinements. User preview remains port4567.

### User click regression and compact header follow-up

U3 addresses a reproduced held-mouse gesture failure missed by previous fast-click
coverage: summary loses focus on theme label mousedown; deferred focusout closes
the menu before mouseup/radio activation. Use the native radio as full-tile pointer
target, retaining labels/keyboard focus/default behavior, rather than introducing
another focus manager. Replace dots with a16px gear glyph/32px fine-pointer trigger
(44px coarse hit area). Keep timestamp on the header row whenever contents fit,
wrapping only when narrow. B4 must use actual glyph/tile pointer down/up held across
frames, ordinary clicks, touch, and header/menu geometry; prior faster checks do
not refute the user's observed defect. No changes to logo/palette/backend.

### U4: phone gear first row and real hit-target titles

User wants gear at top beside logo/Status on iPhone, not grouped with a wrapped
timestamp, and mouse-over theme titles. Bounded direct small-edit brief: phone
320/375/390/430 gear first row/top right while timestamp wraps independently;
desktop1024/1440 timestamp stays inline. Put reused localized theme title on actual
full-tile native radio pointer target, not only covered label. Preserve full-tile
held-click fix, focus/keyboard/noJS, gear sizing and contained Back-page popup.
Implementer0 owns complete U4; implementer2 B5 verifies actualhit titles/phone row/
desktoprow/heldgesture with ~3screens, no broad repeated browser audit.

- Preserve the existing light appearance while introducing an accessible dark palette.
- Recommend explicit System/Light/Dark choices and responsive header/content layout.
- Prefer a standalone preview if existing architecture permits representative data
  without the vpsAdmin development cluster; distinguish verified feasibility from
  an untested launch recipe.
- User confirmed sample data is suitable for the first visual preview.
- Retain the saved Full-team roster and settings. Parallel application edits use
  disjoint file boundaries and lead-coordinated index/commit windows. Implementer3
  remains unassigned; reviewer0 will receive the completed final branch.

## Compatibility and deployment

Aim for frontend-only behavior and a browser-local preference, with no API,
database, protocol or deployment-configuration changes. Confirm this in source.
No production deployment or session lifecycle action is authorized. Status integration is conditionally approved by the latest user turn; configuration integration requires its own explicit direction.
Future temporary previews must use `dev-session service run`.

## Documentation

Readers: user evaluating the proposed UX and implementers taking a subsequent
implementation package. Keep proposal/evidence in this session's `design.md` and
current phase/results in `state.md`. Lasting feature/preview documentation belongs
in vpsf-status if implementation proceeds.

## Testing plan

This pass uses source inspection only; no builds or tests are necessary to state
the proposal. Design will identify quick checks and browser acceptance for both
themes, system/manual preference, localization, contrast, narrow screens and
representative status data. Implementation requires committed changes, passing
quick checks and mandatory independent final review before longer checks.

## Delivery acceptance and channel update

User accepted the UI: "ok, good enough. if it passes CI then it can be merged. update vpsf-status channel in vpsfree-cz-configuration." Final status head2d448fd is independently reviewed and browser accepted. The exact CI must pass before the status/master merge. Prepare a clean target and active hooks outside the short repository claim; prove remote master and release immediately.

C2 is a bounded direct lead brief owned by implementer1: inspect existing vpsf-status channel/role→vpsfStatus input, prepare Nix/Overcommit, update the published channel through `confctl inputs channel update --commit vpsf-status vpsf-status` after confirmed status merge, retain useful generated changelog, verify isolated lock/input mapping and consumers, quick checks, publish feature with evidence. No handwritten functional configuration, machine build/deploy or state changes. Routine channel bump needs no new permanent documentation. Existing status supported state, APIs and rollback remain compatible; no migrations.

### U5 integration input/cache correction

User directed canceling abnormal94min CI and running locally. Local full-suite verbose logs proved Nix preparation beforeVMs; inherited OS package set drift made exact kernels unavailable in normal caches. Accepted C7 design isolates modern appGo1.26/rootNixpkgs from OS-pinned test composition, aligns tests/testsMeta, retains unchangedOS/vpsAdmin/suite/assertions and adds verbose/cancel-log diagnostics. Implementer0 owns U5 flake/lock/workflow/testREADME, evaluation-only kernelcache gate, quick checks, committed review before fullrerun. No forcedkernelbuild or weakened CImergecondition.

### U6 language buttons

User requests two side-by-side language buttons instead of native select. Bounded direct lead brief assigned implementer2: native SwitchLinks anchors styled as buttons sharedJS/noJS, selected-current indication/accessibility, verbatim route/query URLs and existingAbout exception. Preserve gear/themes/history/storage/focus; reuse labels. Own header/CSS/languageJS/layoutcacheversions/routes/appearancedocs only. U5/U6 disjoint source edits; commit/index orderU5thenU6. Minimal focused route/browser nativeclick/keyboard/noJS/entitypage2 checks, no broadmatrixrepeat. Finalreview coversboth newpackages before fullintegration.

### K1 requested upstream cache trigger

User: "what would improve this is if nixpkgs update in vpsadminos (there was once today) would trigger the build, at least the latest stable kernel". Prepare minimal existing kernelworkflow trigger/matrix correction in own vpsAdminOS branch from currentstaging. No kernelversion/source, cachecredentials, productiondeployment or staging/masterintegration implied. Architect design follows currentC7revision; implementation owner assigned after sufficientbrief. Verify latest imported actions as required, workflow/evaluation-only checks first, independentcommittedreview before publishing/checks. No blindkernelfullbuild; actual upstream build/publication requires approvedintegration/execution boundary.
