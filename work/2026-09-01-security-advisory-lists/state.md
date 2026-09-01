# 2026-09-01-security-advisory-lists

## Repositories

- `vpsadmin`
  - branch: `2026-09-01-security-advisory-lists`
  - worktree: `worktrees/2026-09-01-security-advisory-lists/vpsadmin`
  - base: `origin/master`
- `vpsf-status`
  - branch: `2026-09-01-security-advisory-lists`
  - worktree: `worktrees/2026-09-01-security-advisory-lists/vpsf-status`
  - base: `origin/master`
- `vpsfree-kb-contracts`
  - branch: `2026-09-01-security-advisory-lists`
  - worktree: `worktrees/2026-09-01-security-advisory-lists/vpsfree-kb-contracts`
  - base: `origin/master`
- `vpsfree-cz-configuration`
  - branch: `2026-09-01-security-advisory-lists`
  - worktree: `worktrees/2026-09-01-security-advisory-lists/vpsfree-cz-configuration`
  - base: `origin/master`

## Status

- Initiative session verified from `VPSFREE_DEV_SESSION_SLUG` and
  `bin/dev-session current`.
- Plan and compatibility decisions recorded.
- All repository worktrees and required hook frameworks are ready.
- All intended changes are committed and quick verification has passed.
- The mandatory standalone review completed without blockers. Its pagination
  finding was fixed and verified before long integration tests.
- Application, contract, and configuration branches are pushed. Local
  validation is complete except for the known status-host ISO prerequisite;
  current-head GitHub Actions are being monitored.

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

## Results

- vpsAdmin already limited its 30-day index list to five published advisories;
  the implementation adds the full-list link and effective-date API ordering.
- vpsf-status previously requested ten advisories and exposed the same partial
  list through HTML and JSON; the implementation now renders at most three and
  omits the field from JSON.
- The current KB contract has no advisory-specific page or capture bindings.
- vpsAdmin commits:
  - `5a94d2873` `api: interleave security advisory drafts by date`
  - `d6aa30f5c` `webui: link recent advisories to the full list`
  - `bb68d02f9` `api: paginate advisories by effective date`
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
  - vpsAdmin: `bb68d02f96ec8a2fdd2fe133a2a3ed90ae9142df`
  - vpsf-status: `587cd65bb02e6dddea7f6b6409e42a15f36ab4fb`
- vpsfree-kb-contracts commit `e37d95e` pins the vpsAdmin revision and its
  transitive vpsAdminOS revision `8e44a5124439b1f3048ffc56b1717614a5360358`.
- The complete KB contract check passed: 42 controls, 34 paths, 35 capture
  concepts, 90 page bindings, 4 managed pages, 12 runtime tests, and 120
  screenshot variants. No advisory-bound page or screenshot drift was
  reported, so no KB candidate, staging, or publication is required.
- Rebasing the configuration worktree onto current `origin/master` first
  required its Nix shell because the ambient pre-rebase hook could not load
  bundled gems. The shell rebase succeeded without conflicts.
- vpsfree-cz-configuration commits generated by `confctl` after dropping the
  superseded unpushed vpsAdmin pin:
  - `d64e03f7` `inputs: set vpsfStatus to ac33a9a2`
  - `d517f0dd` `inputs: set vpsadminServices to bb68d02f`
  - `73440264` `inputs: set vpsfStatus to 587cd65b`
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
- Current-head GitHub results so far: vpsAdmin RuboCop, i18n health, and
  topic-parallel API specs passed; the KB contract check passed. The vpsAdmin
  CI integration job, vpsf-status integration job, and KB managed-page runtime
  job remain queued without a self-hosted runner assigned. No current-head
  workflow has failed.

## Open questions

- None. The user approved the public vpsf-status JSON field removal and chose
  `created_at` as the stable effective date for drafts.

## Cleanup

- Pending. Keep feature branches after integration; remove worktrees only when
  the initiative is merged or abandoned.
