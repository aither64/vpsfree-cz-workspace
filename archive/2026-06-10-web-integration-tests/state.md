---
lifecycle: complete
---
# 2026-06-10-web-integration-tests

## Repositories
- `web`
  - Bare repo: `repos/web.git`
  - Worktree: `worktrees/2026-06-10-web-integration-tests/web`
  - Branch: `2026-06-10-web-integration-tests`
  - Base: `origin/master` at `b6a55b7 registration: collect applicant time zone`
- Reference repositories inspected:
  - `vpsf-status` branches `2026-06-01-vpsf-status-integration-tests` and
    `2026-06-08-test-runner-resources`
  - `vpsfree-irc-bot` branches
    `2026-06-01-vpsfree-irc-bot-integration-tests` and
    `2026-06-08-test-runner-resources`
  - `vpsadmin` branch `2026-06-08-test-runner-resources` and `origin/master`
  - `vpsadminos` branch `2026-06-08-test-runner-resources`
  - `vpsfree-cz-configuration` `origin/master`

## Status
- Implemented integration and unit test harness in `web`.
- Replaced the obsolete production-facing Selenium/RSpec specs.
- Added a GitHub Actions workflow for the vpsAdminOS test-runner suite.
- Latest full integration run passed.

## Commands run
- `bin/dev-session current`
  - Active slug: `2026-06-10-web-integration-tests`
- `git --git-dir=repos/web.git fetch origin`
- `git --git-dir=repos/web.git worktree add -b 2026-06-10-web-integration-tests worktrees/2026-06-10-web-integration-tests/web origin/master`
- Inspected `web` structure and current tests with `find`, `rg`, `sed`, `nl`,
  and `git log`.
- Inspected example integration-test setup using `git show` on
  `vpsf-status` and `vpsfree-irc-bot`.
- Inspected vpsAdmin test services, Playwright, Mailpit, and registration
  support using `git show`/`git grep`.
- Inspected production web service configuration in `vpsfree-cz-configuration`.
- Verified `actions/checkout` releases from the official repository before
  using `actions/checkout@v6`; the releases page showed `v6.0.3` as latest on
  2026-06-10.
- `git add -N .github flake.nix flake.lock test-runner.sh tests`
  - Used so Nix flakes could see newly added files while the work remains
    uncommitted.
- `nix --extra-experimental-features 'nix-command flakes' flake lock`
- `./test-runner.sh ls`
  - Output: `web`
- `php -l lib/form.php`
  - Passed.
- `php -l tests/unit/registration_validator_test.php`
  - Passed.
- `php tests/unit/registration_validator_test.php`
  - Passed.
- `nix --extra-experimental-features 'nix-command flakes' build .#checks.x86_64-linux.validator-tests`
  - Passed.
- `nix --extra-experimental-features 'nix-command flakes' flake check --no-build`
  - Passed. Warnings: custom `tests`/`testsMeta` outputs are unknown to
    generic flake checking, and `apps.test-runner` lacks `meta`.
- `nix --extra-experimental-features 'nix-command flakes' build .#vpsfree-web`
  - Passed.
- `rm -rf /tmp/os-test-runner && ./test-runner.sh test -f web`
  - Final run passed at 2026-06-10 20:05:55 +0200 in 439.68 seconds.
- `nix --extra-experimental-features 'nix-command flakes' shell nixpkgs#nixfmt -c nixfmt flake.nix tests/suite/web.nix tests/all-tests.nix tests/make-test.nix default.nix php-packages.nix`
  - Applied after the final integration run; subsequent `flake check
    --no-build`, validator check build, and `.#vpsfree-web` build passed.

## Results
- `web` has no repository-local `AGENTS.md`.
- Previous tests were old Selenium/RSpec specs and have been removed:
  - `spec/registration_cs_spec.rb`
  - `spec/registration_en_spec.rb`
  - `Gemfile`
  - `Rakefile`
- The old tests targeted public `https://vpsfree.cz` and
  `https://vpsfree.org`. The Czech spec contained `binding.pry`, so it was not
  CI-ready.
- The site is PHP + server-side includes. Production configuration uses
  Nginx + PHP-FPM + `ssi on`, not Apache.
- Existing Nix/Composer files:
  - `default.nix`
  - `composer-env.nix`
  - `php-packages.nix`
  - `shell.nix`
  - `run-composer2nix.sh`
- vpsAdmin test services already provide:
  - disposable API/database/services VM;
  - Mailpit in the mailer container;
  - helper patterns for `wait_for_vpsadmin_api`, `api_ruby_json`, and Mailpit
    reads.
- vpsAdmin `origin/master` includes registration `time_zone` support; the older
  `2026-06-08-test-runner-resources` branch did not show that support in the
  inspected files.
- Current web page issues found during planning:
  - `cs/prihlaska/pravnicka-osoba/index.html` uses
    `entity_type=fyzicka`.
  - `en/registration/pravnicka-osoba/index.html` uses
    `entity_type=fyzicka`.
  - English static registration forms post to `/prihlaska/send.php` instead of
    `/registration/send.php`.
  - `RegistrationForm#printErrors` references an undefined `$error` variable in
    the API response error loop.
- Implemented test infrastructure:
  - `flake.nix`, `flake.lock`, and `test-runner.sh`;
  - RSpec-style vpsAdminOS test-runner suite in `tests/suite/web.nix`;
  - small runner helper extension in
    `tests/runner/extensions/vpsadmin_services.rb`;
  - Playwright tests under `tests/playwright/web`;
  - fast PHP validator test at `tests/unit/registration_validator_test.php`;
  - workflow `.github/workflows/integration-tests.yml`.
- The integration test uses two VMs:
  - `services`: vpsAdmin test cluster plus Mailpit, with a test-only
    vpsAdminOS hypervisor node so registration locations are available;
  - `web`: Nginx + PHP-FPM + SSI serving the packaged site.
- Browser tests use `cs.vpsfree.test` and `en.vpsfree.test` instead of the real
  production domains. Chromium has HSTS state for the production domains and
  upgrades them to HTTPS, which bypasses the test VM.
- Public page coverage includes standalone CS/EN HTML entry points, static
  registration pages, accepted pages with a harmless ID query, 404 pages, and
  Czech hardware survey pages. It excludes fragments, POST handlers, SSI
  include helpers, sitemap/robots documents, and QR image generator endpoints.
- Real registration submission coverage creates valid unique registrations for
  CS/EN and physical/company entities, verifies returned IDs, verifies
  `RegistrationRequest` rows in vpsAdmin, and checks Mailpit confirmation mail.
- Validation coverage checks required-field messages, representative invalid
  values, and accepted values through the `_mock=1` path.
- Product fixes made while implementing tests:
  - static company `entity_type` values are now `pravnicka`;
  - English static registration forms post to `/registration/send.php`;
  - static registration pages use an `id="entity_type"` hidden input so shared
    JavaScript resolves the selected entity consistently;
  - shared registration JavaScript no longer fetches/reapplies dynamic form
    state on static pages without `#form-placeholder`, avoiding field resets;
  - `RegistrationForm#printErrors` no longer references undefined `$error`;
  - `Validators` now declares properties explicitly, accepts an injectable MX
    resolver for deterministic tests, treats missing MX records as acceptable,
    and avoids PHP 8 arithmetic on invalid birth-year input;
  - `default.nix`/`php-packages.nix` accept an optional `src`, and packaging
    excludes local `result` symlinks.

## Open questions
- None currently.

## Decisions
- Include Czech `/hw/` and `/hw/ajeto.html` as standalone page routes.
- Exclude `/nastroje/qr.php` and `/nastroje/qrcodesk.php` from page-health
  tests because they are image generator endpoints, not HTML pages.
- Assert Mailpit confirmation mail for all real registration submissions in the
  final persistence example.
- Keep test scripts in the current RSpec-style test-runner structure with
  `describe`, `it`, and `expect`.

## Commits
- `51af20f` `Fix static registration form submission`
- `13a3015` `Add vpsAdminOS integration test suite`
- `d8df270` `Remove obsolete Selenium registration specs`
- `7f686dd` `Run web integration tests in GitHub Actions`
- Final `web` worktree status after commits: clean.

## Push and CI
- Pushed `2026-06-10-web-integration-tests` to
  `git@github.com:vpsfreecz/web.git`.
- GitHub Actions run:
  `https://github.com/vpsfreecz/web/actions/runs/27297296380`
- Result: passed in 10m52s.
- Completed steps: validator tests, integration tests, result evaluation, log
  summary, gcroot cleanup.
- Fast-forwarded `master` to `7f686dd` from a fresh temporary merge worktree
  and pushed `master` to `git@github.com:vpsfreecz/web.git`.
- Master push triggered GitHub Actions run
  `https://github.com/vpsfreecz/web/actions/runs/27300105330`.
  Watching was stopped before completion per user instruction.

## Cleanup
- Removed worktrees:
  - `worktrees/2026-06-10-web-integration-tests/web`
  - `worktrees/2026-06-10-web-integration-tests/web-merge-master`
- Removed transient `/tmp/os-test-runner`.
- Kept local and remote branch refs as required by workspace policy.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
