# 2026-08-23-vpsadmin-outage-summary

## Repositories

- `vpsadmin`
  - branch: `2026-08-23-vpsadmin-outage-summary`
  - worktree:
    `worktrees/2026-08-23-vpsadmin-outage-summary/vpsadmin`
  - integration worktree:
    `worktrees/2026-08-23-vpsadmin-outage-summary/integrate-vpsadmin`
  - base: `b12f41859a9ae198224cd6ca63eddbcdd0371db8`
  - head: `66f58d7615f932ea3233c58b737678f90bd7bae7`
- `vpsfree-kb-contracts`
  - branch: `2026-08-23-vpsadmin-outage-summary`
  - worktree:
    `worktrees/2026-08-23-vpsadmin-outage-summary/vpsfree-kb-contracts`
  - integration worktree:
    `worktrees/2026-08-23-vpsadmin-outage-summary/integrate-vpsfree-kb-contracts`
  - base: `c1d0aca2b7848a29512811e157b0e8cb4c3184cc`
  - head: `85d7f97deb90e215b9a9d155ca978380e2f57319`
- `vpsfree-cz-configuration`
  - branch: `2026-08-23-vpsadmin-outage-summary`
  - worktree:
    `worktrees/2026-08-23-vpsadmin-outage-summary/vpsfree-cz-configuration`
  - integration worktree:
    `worktrees/2026-08-23-vpsadmin-outage-summary/integrate-vpsfree-cz-configuration`
  - base: `7cd45c867e3a9823f2e7d627c6e153cdc079489b`
  - head: `8fa2141aa8f275afa98900f3278faee3f7a67555`

## Status

All intended changes are committed, verified, and fast-forwarded to the three
default branches in dependency order. Remote feature branches are retained.
No deployment command was run.

## Commands run

- `bin/dev-session current`
- `bin/dev-session worktree add 2026-08-23-vpsadmin-outage-summary vpsadmin --as-is`
- Read the workspace and repository `AGENTS.md` instructions.
- Inspected outage WebUI forms/pages, language selection, API resource/model,
  outage fixtures/specs, adjacent security-advisory localization, and relevant
  git history with `rg`, `sed`, `git blame`, and `git log`.
- Verified the feature branch and `origin/master` both point to
  `b12f41859a9ae198224cd6ca63eddbcdd0371db8`.
- Fetched all affected repositories and added same-slug worktrees for
  `vpsfree-kb-contracts` and `vpsfree-cz-configuration` from current
  `origin/master`.
- The configuration worktree command returned exit 1 because its checkout hook
  ran outside the Nix shell and could not load bundled Overcommit gems. As
  documented in the workspace notes, the branch and clean worktree were still
  created successfully; hook-managed commands will run inside `nix develop`.
- Added localized outage-summary selection to both WebUI list renderers and
  added focused PHPUnit plus Playwright coverage.
- `php -l webui/forms/outage.forms.php`
- `php -l webui/tests/Regression/OutageLocalizationTest.php`
- `nix-instantiate --parse tests/suite/webui.nix`
- `nix develop .#webui -c composer install --working-dir=webui ...` failed
  because the shell hook changes the working directory to
  `~/.config/composer`; the documented absolute-path form succeeded.
- `nix develop .#webui -c composer --working-dir=.../webui test -- --filter
  OutageLocalizationTest`
- `nix develop .#webui -c composer --working-dir=.../webui test`
- `nix develop -c node --check ...` could not run because Node.js is not in the
  root shell; `nix shell nixpkgs#nodejs -c node --check ...` succeeded.
- `git diff --check`
- The first hook-managed vpsAdmin commit attempt stopped because the fresh
  worktree lacked `api/.gems`. `nix develop .#api -c bundle check` installed the
  declared API bundle; the unbypassed retry passed every pre-commit hook.
- Committed and pushed vpsAdmin as
  `66f58d7615f932ea3233c58b737678f90bd7bae7`.
- Pinned the vpsAdmin commit in `vpsfree-kb-contracts` with
  `nix flake update vpsadmin`.
- The first `nix develop -c bin/check` found that `contract/pages.yml` also
  enforces the vpsAdmin pin even though the canonical workflow omitted it.
  Updated that pin, corrected the workflow, recorded a durable workspace note,
  and reran the check successfully.
- Split the KB history into a mechanical contract-pin commit
  (`26431f108d137d1c4fbb9c82254f0ab4fbb15c79`) and the independently reviewable
  workflow correction (`85d7f97deb90e215b9a9d155ca978380e2f57319`).
- Force-pushed the unmerged KB feature branch with lease and cancelled both
  superseded workflow runs for the old branch head.
- Ran `nix develop -c confctl inputs channel set --commit vpsadmin vpsadmin
  66f58d7615f932ea3233c58b737678f90bd7bae7`.
- The generated configuration commit passed its pre-commit hook. An ambient
  `git push` was rejected by the pre-push hook because its gems were unavailable;
  the unbypassed `nix develop -c git push ...` succeeded.
- Committed and pushed configuration as
  `8fa2141aa8f275afa98900f3278faee3f7a67555`.
- Launched the exactly one standalone reviewer required by
  `skills/mandatory-change-review/SKILL.md` with fresh context and the complete
  three-repository review packet. Long local integration checks remain deferred
  until its result is addressed.
- The mandatory reviewer reported no blocking, important, or advisory findings.
  It confirmed the centralized locale/fallback behavior, retained escaping,
  unchanged all-language detail view, focused commit series, exact pins, and
  deployment safety.
- `./test-runner.sh test 'webui#support-pages'`
- `nix develop -c confctl build -y --tag vpsadmin`

## Results

- Both reported locations are rendered by `webui/forms/outage.forms.php`:
  `outage_list()` for the dedicated page and `outage_list_overview()` via
  `outage_list_recent()` for the index page.
- Each renderer hard-codes `$outage->en_summary`, so changing the WebUI/API
  language cannot affect the reason column.
- Outages are already stored in `outage_translations` and exposed by the API as
  per-language fields such as `en_summary` and `cs_summary`. Admin forms already
  create and edit these translations.
- The language switcher already maps the selected WebUI locale to API codes
  (`en`/`cs`) and works for logged-in users, guest cookies, and browser language
  detection. The defect is therefore confined to the two renderer expressions.
- Proposed fix: add an outage-localized text helper that selects the field using
  `webui_current_api_language($langs)`, tries English second, treats null/empty
  translations as absent, and returns an empty string only when neither value
  exists. Replace both direct `en_summary` accesses with this helper and retain
  `h()` escaping at the call sites.
- Do not change the outage detail/admin view, which intentionally shows all
  language variants.
- No gettext catalog update is needed because outage summaries are stored
  operator-authored content, not static interface strings.
- `OutageLocalizationTest`: 3 tests and 3 assertions passed.
- Full WebUI PHPUnit suite: 87 tests and 354 assertions passed.
- Both changed PHP files pass syntax checks, the Playwright file passes the
  Node.js syntax check, the Nix fixture parses, and the diff has no whitespace
  errors.
- vpsAdmin pre-commit hooks passed: migration specs, Nix formatting, API and
  WebUI i18n health, and PHP CS Fixer.
- The complete KB contract check passed: documentation and page contracts,
  annotations, managed-page sources, 60 Ruby test runs with 194 assertions,
  and the capture inventory.
- The configuration lock changes only `vpsadminServices` to the feature SHA.
  `vpsadminStaging` remains at `b12f41859a9ae198224cd6ca63eddbcdd0371db8`
  and `vpsadminProduction` remains at
  `c28b0b44735f1913193ecac6450da8623db5aabe`.
- Reviewer-noted residual gaps to close: the deferred `webui#support-pages`
  browser test and `confctl build -y --tag vpsadmin`; fallback/escaping remain
  unit/static coverage rather than browser assertions, guest locale detection
  remains in the existing language-selection unit suite, and no managed KB
  capture covers outage lists.
- `webui#support-pages` passed: its Playwright example completed successfully
  in 322.87 seconds and the test runner reported 1/1 successful scripts.
- The configuration build passed for all 17 selected machines, producing
  generation `2026-08-23--23-26-28` for the namespace containers, proxy, API,
  database, RabbitMQ, Redis, vpsAdmin, development WebUI, and both production
  WebUI roles. No unexpected kernel build occurred.
- Current-head vpsAdmin WebUI PHPUnit and i18n Actions are green; selected CI is
  complete but red because an unrelated VM teardown timed out. The KB `Check`
  and `Managed page runtime` workflows are green. No configuration
  feature-branch workflow was created.
- Inspected failed vpsAdmin CI run `32666845611` attempt 1 using both
  `gh run view --log-failed` and the downloaded full-log artifact. All 18 WebUI
  scripts passed, including `webui#support-pages` in 137.33 seconds. The only
  unexpected failure was `vps/autostart-monitoring`: its sole behavioral
  example passed in 192.53 seconds, then osvm timed out waiting for
  `poweroff -f` during VM teardown with an empty output buffer. The test runner
  terminated QEMU afterward. This is unrelated to the outage WebUI code,
  fixtures, or configuration pin.
- Reran the investigated failed GitHub Actions job as attempt 2 and launched
  the exact local `vps/autostart-monitoring` test. The local scheduler reported
  shared-host `/dev/shm` pressure from concurrent VM tests before starting it;
  any resource failure must be distinguished from an assertion failure.
- The exact local `vps/autostart-monitoring` target passed, including clean VM
  teardown: its sole behavioral example succeeded in 756.2 seconds and the
  test runner reported 1/1 successful scripts in 1549.42 seconds. This closes
  the only behavior/teardown gap from hosted attempt 1; hosted attempt 2 remains
  capacity-queued behind other long CI runs and is still being monitored.
- Refetched all three `origin/master` refs before integration. They remain at
  the recorded feature bases, so no rebase or dependent pin refresh is needed.
- Created detached integration worktrees from each fetched `origin/master`.
  The configuration post-checkout hook again lacked its gems in the ambient
  shell; `nix develop -c bundle check` succeeded in that worktree before any
  integration action.
- Fast-forwarded each detached integration worktree to its feature head without
  pushing. At the vpsAdmin integration tip, PHP and Node syntax, Nix parsing,
  focused PHPUnit (3 tests/3 assertions), and diff hygiene passed. At the KB
  integration tip, the complete `bin/check` passed again (60 Ruby tests/194
  assertions and the 120-image inventory). At the configuration integration
  tip, Nixfmt, RuboCop, every no-build flake check, and diff hygiene passed.
- Refetched `vpsadmin/master`, confirmed it remained the recorded base and an
  ancestor of the clean integration tip, and pushed the detached integration
  head as a fast-forward from `b12f41859a` to `66f58d761`.
- Default-branch WebUI PHPUnit and both i18n jobs passed. The selected
  integration CI is running and remains the gate before the KB fast-forward.
- Hosted feature attempt 2 completed successfully but selected no tests: after
  the same commit reached `master`, the push-event fallback diff used
  `origin/master` at the identical commit and reported `no changed files`.
  That skipped attempt is not counted as validation; attempt 1's passing
  behavior plus the clean exact local target remain the teardown evidence.
- vpsAdmin default-branch workflows all passed at `66f58d761`: CI, WebUI
  PHPUnit, i18n health, and API Migration Specs.
- Refetched `vpsfree-kb-contracts/master`, confirmed the reviewed base was
  unchanged, and fast-forwarded it from `c1d0aca` to `85d7f97`. Default-branch
  `Check` and `Managed page runtime` both passed.
- Refetched `vpsfree-cz-configuration/master`, confirmed the reviewed base was
  unchanged, and pushed the detached integration tip through the unbypassed
  Nix-shell pre-push hook. The default branch fast-forwarded from `7cd45c86` to
  `8fa2141a`; the repository created no workflow run for this commit.
- Final remote audit confirmed that each `master` and retained feature branch
  points to its intended head: vpsAdmin `66f58d761`, KB contracts `85d7f97`,
  and configuration `8fa2141a`. All six worktrees were clean before cleanup.

## Open questions

- None. Use an outage-specific helper to avoid changing the different
  anonymous-display semantics of security advisories.

## Cleanup

- Removed all six clean feature/integration worktrees and their empty initiative
  directory. Local and remote feature branch refs are retained as required.
