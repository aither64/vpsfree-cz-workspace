---
lifecycle: active
---

# 2026-09-03-webui-vps-ipv6

## Repositories

- `vpsadmin`
  - branch: `2026-09-03-webui-vps-ipv6`
  - worktree: `worktrees/2026-09-03-webui-vps-ipv6/vpsadmin`
  - base: `origin/master` at `cbd0fa16434947a4273610389d84216bcde35e72`
  - integrated `master`: `1acc1955f0e7b4f2b67a18674d02a6da8e9e8da4`
- `vpsfree-kb-contracts`
  - branch: `2026-09-03-webui-vps-ipv6`
  - worktree: `worktrees/2026-09-03-webui-vps-ipv6/vpsfree-kb-contracts`
  - base: `origin/master` at `46466e83c2293f47bfef3fe516a3b51c2de14c70`
  - integrated `master`: `e5ed479f9d4058556dcf225b4c16afd5b9f0051a`
- `vpsfree-cz-configuration`
  - branch: `2026-09-03-webui-vps-ipv6`
  - worktree: `worktrees/2026-09-03-webui-vps-ipv6/vpsfree-cz-configuration`
  - base: `origin/master` at `57d7c12a2da78d334d338a0e56dd7438376a6973`
  - final integration base: `origin/master` at
    `1139d11d9254cd86ec328a34a760589d4f7ce82c`
  - integrated `master`: `248e2fc614bb3bc29c0a9c9f910330ade0b3cb80`

## Status

The vpsAdmin fix, documentation-landmark remediation, focused KB capture
contract, and consolidated `vpsadminServices` configuration pin are integrated
into all three default branches in provider-first order. Checksummed schema-5
Czech and English KB release candidates are prepared locally without publishing
them. Mandatory review and reruns passed at `xhigh`, all four affected
service-host configurations build on the final configuration base, and quick
default-branch workflows are green. The user explicitly chose not to wait for
the remaining long CI runs; they remain active on the exact integrated heads.
Deployment and production KB publication remain out of scope.

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
- On 2026-09-04, the user authorized a `vpsadmin` channel update in
  vpsfree-cz-configuration followed by default-branch integration. Re-read the
  configuration repository guidance and the mandatory-change-review workflow.
- Fetched all three project remotes over SSH. vpsAdmin and vpsfree-kb-contracts
  default branches still match the reviewed feature bases; configuration
  `origin/master` advanced to `57d7c12a` before its worktree was created.
- Added the configuration worktree from current `origin/master`. The helper
  returned nonzero after successfully creating it because the ambient shell
  lacked its Bundler-managed Overcommit gems. Installed Overcommit and signed
  both custom hook types inside `nix develop`; no hook was bypassed.
- Ran `confctl inputs channel set --commit` for channel and role `vpsadmin` at
  exact revision `d18fe2671abb47deda06ba54b17d5fe68d789478` in the configuration
  Nix shell, producing commit
  `8a1666f8f3b14cde8335e7a25e1a1a70becab5a6`.
- Ran the complete configuration Overcommit suite, confirmed the exact channel
  pin, and evaluated the inventory of 17 `vpsadmin`-tagged machines. Held the
  longer configuration build until mandatory review completes.
- Started expanded mandatory change review at high risk and maximum effort with
  fresh General, Architecture, Scope, and Risk/compatibility lanes. Read and
  applied the WebUI change workflow and bilingual user-facing-writing guidance
  after the General lane identified an affected-page annotation gap.
- Added stable documentation IDs to the existing “Manage host addresses” and
  “Add host addresses” WebUI links. The focused test, all 88 WebUI unit tests,
  PHP syntax checks, and the complete vpsAdmin Overcommit suite passed.
- Committed and pushed vpsAdmin remediation revision
  `1acc1955f0e7b4f2b67a18674d02a6da8e9e8da4`.
- Fetched all 114 accessible Czech and 77 English production KB pages, applied
  the required user-facing-writing guidance to the two affected instructions,
  and prepared checksummed schema-5 release manifests. No staging or production
  write has occurred.
- Added the two host-address controls and their semantic path to the contract,
  refreshed the full page/discovery inventory to match the production fetch,
  and preserved the independent vpsAdminOS lock closure. `bin/check` and the
  candidate-aware KB annotation checker passed.
- Amended and force-pushed the consolidated vpsfree-kb-contracts revision as
  `1f7c2bf9dd0d71d8c1aafbd73eda362678af7009`.
- Generated a fresh one-step configuration channel update from current
  `origin/master` to final vpsAdmin revision `1acc1955` using
  `confctl inputs channel set --commit`. Amended the unpushed configuration
  commit to that exact generated lock and changelog as `0e8c2a6e`; all
  configuration hooks passed.
- The user required `xhigh` reasoning for all review work. Updated and pushed
  the workspace rule in commit `6fb7e15`; the pre-existing unrelated
  session-detection edit in `AGENTS.md` remains unstaged and untouched.
- Ran the remediation review with fresh General, Architecture, Scope, and
  Risk/compatibility reviewers using `gpt-5.6-sol` at the workspace-required
  `xhigh` effort. Architecture reported no findings. General required the
  unrelated production inventory refresh to be split from the feature commit;
  General and Risk required the English page's reciprocal `<page>` marker;
  Scope requested only a tracking-language correction.
- Added the missing English `<page>manuals:vps:ip_addresses</page>` marker,
  regenerated both schema-5 manifests, and reran the candidate-aware annotation
  checker successfully. The English release manifest now has SHA-256
  `5b8a1c7e973b0e480ae5e02f6057723eae06f0a3be9c3f74a76fc2c3f25ee93d`.
- Rewrote the unmerged vpsfree-kb-contracts history into focused feature commit
  `9732c49` and independent production-inventory refresh commit `e5ed479`, then
  force-pushed the feature branch with an explicit lease against its previous
  remote head `1f7c2bf`.
- Reran the affected General, Scope, and Risk/compatibility lanes using fresh
  `gpt-5.6-sol` reviewers at exact `xhigh` reasoning effort. The Architecture
  lane was not rerun because the fixes changed page-pairing metadata, tracking,
  and commit boundaries without changing the already reviewed design or final
  contract tree.
- Ran `confctl build -y` separately for `cz.vpsfree/vpsadmin/int.api1`,
  `int.api2`, `int.webui1`, and `int.webui2`; all four builds completed and
  resolved vpsAdmin revision `1acc1955`. An initial non-interactive attempt
  stopped before building when `confctl` requested confirmation; the documented
  `--yes` option was used for the successful builds.
- Pushed configuration feature revision
  `0e8c2a6e02ff6f4dd93d786498da5fc66a532682`. The repository has no feature
  branch workflow runs. Removed only the two Nix-shell helper files
  `.bin/rubocop` and `.bundle/config` that were recreated during validation.
- Checked the global KB staging service read-only. It remains owned by
  `2026-08-18-vpsadmin-password-reset` with that initiative's pending release,
  so this initiative did not claim, reset, stage, or otherwise modify it.
- Dry-ran and then performed an exact path-scoped `git clean` of this
  initiative's untracked `kb-sources` and unchanged `kb-candidates` copies.
  The two tracked public candidates and all release/review metadata remain.
- The final vpsfree-kb-contracts feature-head workflows passed: Check run
  `33852215844` and Managed page runtime run `33852215930` on `e5ed479`.
  vpsAdmin WebUI PHPUnit and i18n health passed on `1acc1955`; broad
  integration run `33849770155` remained healthy in `Run tests`. The user
  explicitly instructed the session not to wait for that long run before
  integrating the reviewed commits.
- Created fresh detached integration worktrees from each fetched default
  branch, fast-forwarded them with `git merge --ff-only`, and preserved the
  provider-first order. The vpsAdmin integration tree passed the complete
  Overcommit suite before `master` was pushed to `1acc1955`. The contract
  integration tree passed complete `bin/check` before `master` was pushed to
  `e5ed479`.
- Configuration `origin/master` advanced during the CI wait through unrelated
  automated nixpkgs, vpsAdminOS, and llm-agents input updates. Rebased the
  one-commit feature branch inside its required Nix hook environment onto
  `1139d11d`, producing `248e2fc`; its diff remained only the three
  `vpsadminServices` lock fields. Force-pushed the rewritten feature branch
  with an explicit lease against `0e8c2a6e`.
- Reran the full configuration Overcommit suite and all four focused
  `confctl build -y` commands after that rebase, both in the feature worktree
  and again in the fresh detached integration worktree. Fast-forwarded and
  pushed configuration `master` to `248e2fc`, then removed all three temporary
  integration worktrees without force.

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
- Pre-remediation vpsfree-kb-contracts checks passed: 42 controls, 34 paths,
  35 capture concepts, 3 semantic selectors; all four Ruby test groups passed
  (60 runs, 194 assertions total); and the inventory contains 60 concepts and
  120 variants.
- The pre-remediation contract diff contained eight intended files: pin
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
- The `vpsadmin` channel maps role `vpsadmin` only to `vpsadminServices`; the
  `vpsadminStaging` and `vpsadminProduction` node inputs are separate and were
  not changed.
- The consolidated generated configuration commit updates only the
  `vpsadminServices` revision, NAR hash, and timestamp from `cbd0fa16` to final
  vpsAdmin commit `1acc1955`. Its generated changelog contains both the IPv6
  capability fix and the invisible documentation landmarks.
- The configuration pre-commit hook passed Nixfmt. Commit-message hooks passed
  with only the accepted generated-changelog width warning. The Nix shell's
  untracked `.bin/rubocop` and `.bundle/config` helper files were inspected and
  removed; the configuration worktree is clean.
- Architecture and Risk reviewers found no Blocking, Important, or Advisory
  issue in the committed API, contract, or configuration series. They confirmed
  the output-policy ownership, exact pins, unchanged assignment authorization,
  additive mixed-version behavior, and provider-first merge order.
- The General reviewer found one Blocking documentation-contract gap: the
  affected Czech and English IP-address pages tell members to use “Manage host
  addresses” and then “Add host addresses”, but those existing actions have no
  WebUI landmarks or semantic page binding. The gap must be corrected and the
  affected lanes rerun before the configuration build or any merge.
- Reviewer read-only Nix commands temporarily recreated `.bin/rubocop` and
  `.bundle/config` in the shared configuration worktree. Reviewers coordinated
  ownership and removed the exact generated files; tracked content was never
  modified. Cleanliness will be rechecked after all lanes finish.
- The complete production fetch found five Czech pages that had already been
  removed since the last inventory and four unchanged Guix discoveries whose
  paragraph numbers moved by one. The contract now records the current page set
  and preserves the existing reasons for those Guix discoveries.
- The remediated contract contains 44 controls and 35 paths. Its full
  `bin/check` run passed, including 60 Ruby test runs with 194 assertions and
  validation of all 120 screenshot variants. The candidate-aware checker
  reports 92 bindings and 9 explicit exceptions.
- The first `xhigh` remediation review confirmed that the API authorization,
  public capability classification, provider-first ordering, dependency pins,
  and compatibility design remain sound. Its actionable findings were confined
  to commit separation, the English language-pair marker, and tracking
  accuracy; all three were corrected before the long configuration build.
- The General, Scope, and Risk/compatibility reruns reported no Blocking,
  Important, or Advisory findings. They independently confirmed the focused
  commit split, reciprocal page markers and regenerated hashes, exact provider
  pins, unchanged authorization, additive mixed-version behavior, and accurate
  tracking. The unchanged residual gaps are visibility-only browser coverage,
  no direct positive `remote_console_server` assertion, and staging verification
  before any future production KB promotion.
- The four configuration builds produced successful generations for both API
  and both WebUI service hosts. They built the API, supervisor, database,
  console-router, and WebUI packages at exact source revision `1acc1955`; no
  deployment was attempted.
- All three remote default branches resolve to their intended integrated heads:
  vpsAdmin `1acc1955`, vpsfree-kb-contracts `e5ed479`, and
  vpsfree-cz-configuration `248e2fc`. The final configuration channel reports
  role `vpsadmin`, input `vpsadminServices`, revision `1acc1955`.
- On the integrated vpsAdmin head, WebUI PHPUnit run `33862002052`, RuboCop run
  `33862002042`, and i18n health run `33862002062` passed. API Specs run
  `33862002041` and CI run `33862002066` remained active at handoff. On the
  integrated contract head, Check run `33862106524` passed and Managed page
  runtime run `33862106472` remained active. The earlier feature-head broad
  vpsAdmin run `33849770155` also remained active; the user explicitly chose
  not to wait for these long runs.

## Open questions

None.

## Cleanup

- All three feature worktrees are clean. Keep them while the exact-head CI runs
  remain active; remove them and finalize only after no CI handoff remains.
- The transient full KB source/candidate fetch, including private production
  snapshots, has been removed. The two tracked public candidates are preserved.
- The temporary detached integration worktrees and their parent directory were
  removed cleanly. Feature branches remain locally and remotely as required.
- The initiative is not yet eligible for finalization or archival because the
  user chose not to wait for the active default-branch CI runs.
