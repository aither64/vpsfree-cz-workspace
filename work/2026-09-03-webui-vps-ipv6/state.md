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

The vpsAdmin fix and its focused KB capture contract are implemented, committed,
and pushed. Mandatory high-risk change review is complete and all findings are
resolved. Quick checks, the corrected bilingual contract captures, the focused
vpsAdmin browser integration test, and all GitHub Actions pass. No
implementation work remains. Merge, deployment, KB publication, and initiative
finalization remain outside this implementation request.

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
- Pinned that exact vpsAdmin revision in vpsfree-kb-contracts while preserving
  its independently advanced vpsAdminOS revision
  `6bdf458fd9105379860234ff33d352e55844f08f` and associated lock closure.
- Ran the contract's JavaScript syntax check and `bin/check` before capture.
- Started the dedicated `screenshots` development cluster using local
  networking because another session's active
  `2026-08-18-vpsadmin-password-reset` cluster occupied the bridge service
  address. The other cluster was not modified.
- Captured and registered the four affected Czech/English route and interface
  checkpoints one at a time, ran strict `bin/validate` and `bin/check`, visually
  inspected all four screenshots, and stopped the cluster cleanly.
- Reset only this initiative's ephemeral devcluster state after a cross-revision
  restart exposed a stale node container without a matching services database
  row. Verified both sides were empty before the successful recapture.
- Ran mandatory change review at high risk and maximum effort with General,
  Architecture, Scope, and Risk/compatibility lanes using fresh
  `gpt-5.6-sol` reviewers.
- Amended the unpushed vpsfree-kb-contracts change to focused revision
  `c7f0baedec7b19f587aefc7c2999f9be3f554754`.
- Ran `./test-runner.sh test 'webui#vps-user-core'` after mandatory review and
  pushed the corrected vpsfree-kb-contracts branch after confirming its base
  still matched current `origin/master`.
- Monitored GitHub Actions for both pushed revisions. The requests-plugin
  override is a full-suite trigger, so vpsAdmin CI selected all `tag=ci`
  integration tests instead of only the focused browser scenario.

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
- Reviewers found no issue with the Location authorization fix, shared output
  constants, or anonymous capability exposure. The General, Architecture, and
  Risk lanes independently identified one blocking contract problem: the
  initial `nix flake update vpsadmin` had regressed the contract-owned
  vpsAdminOS test framework from `6bdf458f` to `8e44a512`, where managed-page
  retry helpers are absent. The base lock closure and all page-runtime refs were
  restored while retaining the new vpsAdmin pin.
- The Scope lane also found ten unrelated PNG/hash changes from a full
  networking recapture. Those artifacts were restored to the base revision;
  only the interface-address screenshot changes remain because the route
  selector's closed appearance is byte-identical.
- The reviewers noted two non-blocking residuals: the unchanged authenticated
  `remote_console_server` output is not asserted directly, and the positive
  WebUI contract checks field availability without submitting an allocation.
  Existing browser/API coverage constrains both paths sufficiently for this
  additive fix. Remediation restored existing ownership and removed excess
  scope without adding a new design, so no review-lane rerun was required.
- The Czech and English focused runs passed the positive assertions. The
  interface-address form grew from 204 to 230 pixels and visibly contains the
  public IPv6 selector in both languages. The route selector's IPv6 option is
  covered by the browser assertion because a closed select displays only the
  IPv4 default.
- Three capture clients reported complete results and then exited normally or
  idled in the known Playwright close phase. Exact result files were verified
  before interrupting only the two close-hung clients. `bin/validate --update`
  was run immediately after every checkpoint so no result was overwritten.
- Final vpsfree-kb-contracts checks passed: 42 controls, 34 paths, 35 capture
  concepts, 3 semantic selectors; all four Ruby test groups passed (60 runs,
  194 assertions total); and the inventory contains 60 concepts and 120
  variants.
- The final contract diff against its base contains eight intended files: pin
  metadata, two positive scenario assertions, two inventory entries, and the
  two changed bilingual interface screenshots. vpsAdminOS, page-runtime, and
  unrelated screenshot content are unchanged from the base.
- vpsAdmin GitHub Actions on `d18fe267` passed: RuboCop, i18n health, API Specs,
  and the full `tag=ci` integration suite. CI run `33798687992` completed
  successfully; its test step took 3 hours 55 minutes 19 seconds and evaluation,
  summary, and cleanup also passed.
- The post-review `webui#vps-user-core` integration passed on its first attempt:
  the Playwright example succeeded in 2,080.94 seconds, the selected script in
  2,478.0 seconds, and the complete 1/1 test in 2,777.61 seconds. The runner
  used cached kernels; no unexpected local kernel compilation occurred.
- vpsfree-kb-contracts GitHub Actions on `c7f0baed` passed: Check run
  `33813611074` completed in 5 minutes 50 seconds, and Managed page runtime run
  `33813610967` completed in 27 minutes 20 seconds.

## Open questions

None.

## Cleanup

- Both worktrees are clean and active and must remain until any separately
  authorized merge is complete.
- The initiative is not eligible for finalization or archival.
