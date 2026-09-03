---
lifecycle: active
---

# 2026-09-03-webui-vps-ipv6

## Repositories

- `vpsadmin`
  - branch: `2026-09-03-webui-vps-ipv6`
  - worktree: `worktrees/2026-09-03-webui-vps-ipv6/vpsadmin`
  - base: `origin/master` at `cbd0fa16434947a4273610389d84216bcde35e72`
- `vpsfree-kb-contracts`
  - branch: `2026-09-03-webui-vps-ipv6`
  - worktree: `worktrees/2026-09-03-webui-vps-ipv6/vpsfree-kb-contracts`
  - base: `origin/master` at `46466e83c2293f47bfef3fe516a3b51c2de14c70`

## Status

The vpsAdmin fix and its KB capture contract are implemented and committed.
The vpsAdmin feature branch is pushed. Mandatory change review is next, before
the long vpsAdmin browser integration test.

## Commands run

- Inspected the Location resource, WebUI consumers, API specs, requests-plugin
  overrides, repository history, historical Codex sessions, and KB contract.
- Fetched workspace, vpsAdmin, and vpsfree-kb-contracts upstream `master` refs.
- Created both initiative worktrees with `bin/dev-session worktree add` from
  current `origin/master`.
- Ran focused API specs with `VPSADMIN_PLUGINS=all` and
  `VPSADMIN_PLUGINS=none`, RuboCop for all changed Ruby files, Ruby syntax
  checks, `git diff --check`, and a Node syntax check for the changed
  Playwright helper.
- Verified the custom Overcommit hook was unchanged, signed it for the fresh
  worktree, and ran all declared pre-commit and commit-message hooks in the
  root vpsAdmin Nix shell.
- Committed and pushed vpsAdmin revision
  `d18fe2671abb47deda06ba54b17d5fe68d789478`.
- Pinned that exact vpsAdmin revision in vpsfree-kb-contracts with its
  transitive vpsAdminOS revision
  `8e44a5124439b1f3048ffc56b1717614a5360358`.
- Ran the contract's JavaScript syntax check and `bin/check` before capture.
- Started the dedicated `screenshots` development cluster using local
  networking because another session's active
  `2026-08-18-vpsadmin-password-reset` cluster occupied the bridge service
  address. The other cluster was not modified.
- Captured the full networking scenario in Czech and English, ran
  `bin/validate --update`, strict `bin/validate`, and `bin/check`, generated
  both networking contact sheets, inspected the sheets and the four directly
  affected form screenshots, and stopped the cluster cleanly.
- Committed vpsfree-kb-contracts revision
  `abf07adc6e6a2e050a8167555eded366dbee6261`.

## Results

- `has_ipv6` is required by ordinary-member route and interface-address forms,
  but the non-admin Location output whitelist removes it.
- `Location#domain` is read directly only by administrator-only WebUI cluster
  pages. Member-visible Node names are derived separately; the user chose to
  keep the raw Location field restricted.
- The responsible pre-workspace worker was session
  `019e557f-e037-7682-bba1-964135736018`, overseen by parent session
  `019e548d-3620-7b71-a99a-6f8e85cc9810`.
- `bin/dev-session current` returned a false negative from tool execution:
  the tmux Codex frontend has the correct initiative environment, while the
  long-lived external app-server that launches tool shells does not. Use the
  explicit slug with session helpers.
- The Location and VPS API specs passed: 29 examples with the requests plugin
  enabled and 16 examples with core-only authorization, with zero failures.
  The plugin-specific examples were expected pending in each opposite mode.
- The focused RuboCop and Ruby/JavaScript syntax checks passed, as did all
  vpsAdmin hooks: Nixfmt, MigrationSpecs, VpsadminWebuiI18n,
  VpsadminApiI18n, PhpCsFixer, RuboCop, SingleLineSubject, TextWidth, and
  TrailingPeriod.
- A root `nix develop --command node` attempt failed because that shell does
  not include Node.js; `nix shell nixpkgs#nodejs --command node --check` is the
  appropriate focused syntax-check environment and passed.
- Running `git commit` outside the Nix shell demonstrated the already
  documented missing-hook-tool failure. Retrying through `nix develop`
  executed the full hook suite successfully; no hook was bypassed.
- The first contract check after `nix flake update vpsadmin` caught the
  transitive vpsAdminOS provenance mismatch. The page registry and all five
  page-runtime action refs now use the lock's exact vpsAdminOS revision. The
  action implementations were compared with current official `staging` and
  have not changed since that revision.
- The Czech and English scenario runs each passed the positive assertions and
  captured eight checkpoints. The interface-address form grew from 204 to 230
  pixels and visibly contains the public IPv6 selector in both languages. The
  route selector's IPv6 option is covered by the browser assertion because a
  closed select displays only the IPv4 default.
- Both capture clients reported complete results; two close phases then idled
  in `epoll`, matching the existing Playwright-close note. Exact result files
  were verified before interrupting only the clients. Strict validation passed
  after registering each result.
- Final vpsfree-kb-contracts checks passed: 42 controls, 34 paths, 35 capture
  concepts, 3 semantic selectors; all four Ruby test groups passed (60 runs,
  194 assertions total); and the inventory contains 60 concepts and 120
  variants.

## Open questions

None.

## Cleanup

- Both worktrees are active and must remain until review, CI, integration, and
  any separately authorized merge are complete.
- The initiative is not eligible for finalization or archival.
