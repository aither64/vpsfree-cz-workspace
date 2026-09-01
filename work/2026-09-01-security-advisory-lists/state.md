# 2026-09-01-security-advisory-lists

## Repositories

- `vpsadmin`
  - branch: `2026-09-01-security-advisory-lists`
  - worktree: `worktrees/2026-09-01-security-advisory-lists/vpsadmin`
    (removed after merge)
  - base: `origin/master`
- `vpsf-status`
  - branch: `2026-09-01-security-advisory-lists`
  - worktree: `worktrees/2026-09-01-security-advisory-lists/vpsf-status`
    (removed after merge)
  - base: `origin/master`
- `vpsfree-kb-contracts`
  - branch: `2026-09-01-security-advisory-lists`
  - worktree: `worktrees/2026-09-01-security-advisory-lists/vpsfree-kb-contracts`
    (removed after merge)
  - base: `origin/master`
- `vpsfree-cz-configuration`
  - branch: `2026-09-01-security-advisory-lists`
  - worktree: `worktrees/2026-09-01-security-advisory-lists/vpsfree-cz-configuration`
    (removed after merge)
  - base: `origin/master`

## Status

- Initiative session verified from `VPSFREE_DEV_SESSION_SLUG` and
  `bin/dev-session current`.
- Plan and compatibility decisions recorded.
- All repository worktrees and required hook frameworks were prepared before
  implementation and integration.
- All intended changes are committed and quick verification has passed.
- The mandatory standalone review completed without blockers. Its pagination
  finding was fixed and verified before long integration tests.
- All four feature branches were rebased or regenerated on their current
  default branches, verified, and fast-forwarded into `master`.
- Local and remote feature branches are retained at the merged revisions.
- Feature and temporary integration worktrees have been removed.
- Default-branch GitHub Actions have no observed failures; self-hosted jobs
  that had not acquired a runner at cleanup time remain queued.

## Commands run

- `bin/dev-session current`
- Read workspace and applicable user-facing writing skill instructions.
- Inspected upstream repository code, tests, channel definitions, and current
  remote revisions while preparing the implementation plan.
- Created all four worktrees from their current `origin/master` refs with
  `bin/dev-session worktree add`.
- Installed vpsAdmin/configuration Overcommit hooks in their root Nix shells
  and vpsf-status Lefthook through `nix develop -c make hooks`.
- `nix develop .#api -c bundle exec rspec
  spec/api/resources/security_advisory_spec.rb:302`
- `nix develop .#api -c bundle exec rubocop
  lib/vpsadmin/api/resources/security_advisory.rb
  spec/api/resources/security_advisory_spec.rb`
- `nix develop .#webui -c lang/scripts/locales-update`
- vpsAdmin WebUI PHP syntax, gettext health, and Playwright JavaScript syntax
  checks.
- `nix develop -c go test ./...` in vpsf-status after each functional commit.
- `nix develop -c make i18n-health` in vpsf-status.
- `nix flake update vpsadmin` and `nix develop -c bin/check` in
  vpsfree-kb-contracts.
- Verified the official `actions/checkout` tags before editing the page runtime
  workflow; `v7` points to the latest `v7.0.1` release.
- `nix develop -c confctl ls 'cz.vpsfree/vpsadmin/*'` and
  `nix develop -c confctl ls 'cz.vpsfree/machines/prg/apu'`.
- Fresh-context mandatory change review of all four repository diffs and
  compatibility decisions.
- Focused effective-date pagination spec and RuboCop after the review fix.
- Re-ran `nix develop -c bin/check` after advancing the contract pin.
- `nix develop .#api -c bundle exec rspec
  spec/api/resources/security_advisory_spec.rb`.
- `./test-runner.sh test 'webui#security-advisories'` in vpsAdmin.
- `./test-runner.sh test status-page` in vpsf-status, followed by a focused
  advisory-example rerun while diagnosing the language redirect.
- `nix develop -c confctl build -y 'cz.vpsfree/vpsadmin/*'`.
- `nix develop -c confctl build -y
  'cz.vpsfree/machines/prg/apu'`.
- Fetched all four current default branches and rebased the feature branches.
- Used `git range-diff` to verify that the rebased vpsAdmin series is
  patch-identical to the reviewed series.
- Re-ran the complete vpsAdmin advisory API spec, focused RuboCop, WebUI PHP
  syntax, gettext health, and Playwright JavaScript syntax checks after the
  rebase and again from the temporary integration worktree.
- Re-ran `go test ./...` and `make i18n-health` from the vpsf-status
  integration worktree.
- Advanced the KB contract pin with `nix flake update vpsadmin`, amended its
  single pin commit, and re-ran `nix develop -c bin/check` from the integration
  worktree.
- Dropped superseded generated configuration pins while rebasing, then ran
  `confctl inputs channel set --commit` once for the final vpsAdmin revision
  and once for the final vpsf-status revision.
- Fast-forwarded all four feature tips from detached integration worktrees and
  pushed them to the corresponding `master` branches.
- Removed the initiative and temporary integration worktrees while retaining
  the local and remote feature branches.

## Results

- vpsAdmin already limited its 30-day index list to five published advisories;
  the implementation adds the full-list link and effective-date API ordering.
- vpsf-status previously requested ten advisories and exposed the same partial
  list through HTML and JSON; the implementation now renders at most three and
  omits the field from JSON.
- The current KB contract has no advisory-specific page or capture bindings.
- vpsAdmin commits:
  - `4d4b3cab4` `api: interleave security advisory drafts by date`
  - `594f7ca80` `webui: link recent advisories to the full list`
  - `ba1217fb2` `api: paginate advisories by effective date`
- Focused API ordering example passed, RuboCop found no offenses, PHP and
  JavaScript syntax checks passed, gettext catalogs are current, and all
  vpsAdmin pre-commit hooks passed.
- The initial API spec run exposed the ActiveRecord 8 requirement to wrap the
  constant SQL fragment in `Arel.sql`; the implementation was corrected before
  the passing focused run.
- The first vpsAdmin commit attempt ran outside the root Nix shell and hooks
  correctly rejected the missing tools. The same staged commit passed from
  `nix develop`; no hooks were bypassed.
- vpsf-status commits:
  - `6b8bde1` `Limit recent security advisories to three`
  - `ac33a9a` `Remove security advisories from public JSON`
  - `587cd65` `Test the localized advisory page directly`
- The full vpsf-status Go suite and localization health check passed, as did
  both Lefthook pre-commit runs.
- The vpsf-status fetch now requests three advisories and truncates any
  overlong response before fetching CVEs or updating the HTML state.
- The public JSON contract now explicitly excludes `security_advisories`; the
  populated JSON contract fixture verifies the field remains absent.
- The standalone reviewer reported no blocker. It identified that HaveAPI's
  inherited numeric-ID cursor could skip or repeat advisories when effective
  dates and IDs have different ordering. The follow-up derives a composite
  `(effective_date, created_at, id)` boundary from the visible cursor row and
  tests pagination in both directions. Its focused MariaDB spec, RuboCop, and
  all pre-commit hooks passed.
- Pushed application revisions:
  - vpsAdmin: `ba1217fb2757cf8624ac0d1fd89d9466377b6289`
  - vpsf-status: `587cd65bb02e6dddea7f6b6409e42a15f36ab4fb`
- vpsfree-kb-contracts commit `5dd94f1` pins the vpsAdmin revision and its
  transitive vpsAdminOS revision `8e44a5124439b1f3048ffc56b1717614a5360358`.
- The complete KB contract check passed: 42 controls, 34 paths, 35 capture
  concepts, 90 page bindings, 4 managed pages, 12 runtime tests, and 120
  screenshot variants. No advisory-bound page or screenshot drift was
  reported, so no KB candidate, staging, or publication is required.
- Rebasing the configuration worktree onto current `origin/master` first
  required its Nix shell because the ambient pre-rebase hook could not load
  bundled gems. The shell rebase succeeded without conflicts.
- vpsfree-cz-configuration commits generated by `confctl` after rebasing and
  dropping superseded pins:
  - `9534ae42` `inputs: set vpsadminServices to ba1217fb`
  - `74f2c58b` `inputs: set vpsfStatus to 587cd65b`
- Configuration inventory evaluation resolves the affected vpsAdmin service
  set and `cz.vpsfree/machines/prg/apu`; both generated commits passed
  Overcommit.
- The amended KB pin was force-pushed and the queued workflow for its stale
  commit was cancelled; completed stale checks were left intact.
- The complete vpsAdmin advisory API spec passed with 31 examples and no
  failures. The vpsAdmin three-machine WebUI test passed its Playwright
  advisory flow and the full script completed successfully.
- The first full vpsf-status VM run preserved five failures. Four were in
  pre-existing cluster-health examples: the rendered JSON showed
  `webui=down` after a WebUI 502 and `pool_status=false`, so normal JSON,
  metrics, ping-loss, and HTTP-recovery expectations timed out. Three other
  existing examples passed. The changed advisory example failed because the
  test fetched `/` without following its `/?lang=en` redirect and inspected
  only the `Found` body.
- The advisory integration test now requests `/?lang=en` directly. A focused
  VM rerun passed the advisory example in 18.98 seconds and the focused test
  script completed successfully. The temporary skips used to isolate that
  example were removed before commit. This lesson is recorded in
  `notes/vpsf-status/2026-09-01-status-page-language-redirect.md`.
- All 11 requested vpsAdmin configuration machines built successfully as
  generation `2026-09-01--13-00-18` using vpsAdmin `bb68d02f`.
- The `cz.vpsfree/machines/prg/apu` build remains unavailable in this local
  environment because `configs/carrier.nix` requires the absent
  `/srv/iso-images/systemrescue-11.01-amd64.iso`. This matches the existing
  durable note in
  `notes/vpsfree-cz-configuration/2026-06-04-build-machine-systemrescue-iso.md`;
  no placeholder was created.
- Stale queued or running GitHub Actions for superseded application/contract
  SHAs were cancelled; completed stale checks were retained.
- Before merge, the rebased vpsAdmin feature head had passed RuboCop, WebUI
  PHPUnit, i18n, client, and libnodectld workflows; topic-parallel API specs
  remained in progress and its self-hosted CI job remained queued. The
  vpsf-status feature integration workflow passed. The KB contract check
  passed while its managed-page runtime job remained queued. Default-branch
  pushes started new workflow runs with no observed failure at cleanup time.
- The mandatory review was not repeated after the final rebase: the only
  application branch whose base moved had a patch-identical `range-diff`, its
  complete affected spec passed, and the remaining changes only regenerated
  exact dependency and configuration pins. The existing review therefore
  still covers the merged code and design.
- Integration-worktree validation passed: 31 vpsAdmin advisory examples,
  focused RuboCop, PHP/gettext/JavaScript checks, the full vpsf-status Go and
  i18n suites, and the complete KB contract check.
- All 11 vpsAdmin service configurations built successfully as generation
  `2026-09-01--15-00-35` from vpsAdmin `ba1217fb`.
- The integration-worktree APU build remains blocked by the same absent
  `/srv/iso-images/systemrescue-11.01-amd64.iso` prerequisite. Evaluation
  reached that declared local file and did not reveal a channel-pin error.
- Final merged revisions on local feature refs, remote feature refs, and remote
  `master` refs are identical:
  - vpsAdmin: `ba1217fb2757cf8624ac0d1fd89d9466377b6289`
  - vpsf-status: `587cd65bb02e6dddea7f6b6409e42a15f36ab4fb`
  - vpsfree-kb-contracts: `5dd94f1609ecb0742360d6b0b2b8fa99c190a519`
  - vpsfree-cz-configuration: `74f2c58be77f022b4e28401345896128edbe90b9`

## Open questions

- None. The user approved the public vpsf-status JSON field removal and chose
  `created_at` as the stable effective date for drafts.

## Cleanup

- Complete. Feature and temporary integration worktrees, including generated
  worktree-local caches, were removed. Local and remote feature branches were
  retained at the merged revisions.
