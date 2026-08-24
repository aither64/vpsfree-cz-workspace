# 2026-08-23-vpsadmin-outage-summary

## Goal

Make outage reasons on the vpsAdmin WebUI overview and dedicated outage list
follow the selected language, verify the behavior, pin the exact result in the
KB contract and production configuration, and fast-forward the verified
changes into each repository's default branch.

## Affected repositories

- `vpsadmin`: WebUI outage list rendering and regression coverage.
- `vpsfree-kb-contracts`: exact vpsAdmin revision pin and visible-WebUI
  contract verification.
- `vpsfree-cz-configuration`: exact vpsAdmin revision pin in the `vpsadmin`
  services channel.

## Approach

1. Select the outage summary field using the active WebUI/API language, with
   English fallback for missing or empty selected translations.
2. Use the helper in both list renderers while retaining HTML escaping and the
   existing all-language outage detail view.
3. Add focused PHPUnit coverage and exercise both affected pages in the
   existing Playwright support-pages scenario.
4. Commit and push vpsAdmin, pin its exact SHA in both downstream repositories,
   and run the documentation contract and configuration evaluation.
5. Run the mandatory fresh-agent review after quick verification and before
   long browser/configuration checks.
6. After current-head CI and local verification pass, integrate `vpsadmin`,
   `vpsfree-kb-contracts`, and `vpsfree-cz-configuration` into `master` in that
   order using fresh worktrees and fast-forward-only merges.

## Compatibility and deployment

- The application change is WebUI-only. The outage schema and API already expose
  per-language `en_summary`, `cs_summary`, description, and update fields.
- Persisted outage data and API contracts remain unchanged.
- Old and new WebUI versions can run against the same API and database during
  a rolling deployment.
- Fall back to English for incomplete legacy translations, preserving the
  current visible behavior instead of rendering an empty reason.
- Rollback is safe because the proposed change does not write or transform
  state.
- No vpsAdminOS or coordinated node update is required.
- The configuration pin changes desired state but this initiative will not run
  `confctl deploy`. No production KB page or media write is needed.

## Testing plan

- Add a focused WebUI PHPUnit regression for choosing the current language and
  falling back to English when the chosen summary is empty or unavailable.
- Extend the existing outage Playwright coverage with distinct English and
  Czech fixture summaries, switch the UI to Czech, and assert the Czech reason
  on both the overview and `outage&action=list` page.
- Run the targeted PHPUnit regression and the relevant WebUI browser script;
  run the WebUI hook/lint checks before committing an implementation.
- Pin the exact vpsAdmin commit in `vpsfree-kb-contracts` and run
  `nix develop -c bin/check`; existing contracts contain no outage-report list
  capture, so no screenshot or page candidate change is expected.
- Pin only `vpsadminServices` with
  `confctl inputs channel set --commit vpsadmin vpsadmin REV`, verify the other
  vpsAdmin inputs are unchanged, and build all `vpsadmin`-tagged consumers.
- Monitor feature and default-branch GitHub Actions, inspecting logs and
  artifacts for failures before accepting reruns.
