# 2026-06-10-web-integration-tests

## Goal
Add maintainable automated coverage for the `web` repository:

- run Playwright browser tests against a disposable vpsAdmin test cluster;
- verify Czech and English public pages render through the same SSI/PHP stack
  used by production;
- verify registration form dynamic loading, static form entry points, real
  submission to vpsAdmin, returned registration IDs, and form validation
  messages;
- replace the old Selenium/RSpec specs with the new test structure;
- add a GitHub Actions workflow that runs the integration suite on the
  self-hosted runner using the vpsAdminOS test runner.

## Affected repositories
- `web`
  - Primary implementation target.
  - Worktree: `worktrees/2026-06-10-web-integration-tests/web`
  - Branch: `2026-06-10-web-integration-tests`
- `vpsadmin` and `vpsadminos`
  - Used as flake inputs and test framework dependencies only.
  - No repository changes expected.

## Approach
1. Replace the old test harness
   - Remove or retire `spec/registration_{cs,en}_spec.rb`, `Gemfile`, and
     `Rakefile` if they are only used by the obsolete Selenium/RSpec tests.
   - The current specs target public production domains, one Czech spec still
     contains `binding.pry`, and they cannot run in CI as reliable integration
     tests.

2. Add Nix/test-runner integration like `vpsf-status` and `vpsfree-irc-bot`
   - Add a `flake.nix` with inputs:
     - `vpsadmin.url = "github:vpsfreecz/vpsadmin"`
     - `vpsadminos.follows = "vpsadmin/vpsadminos"`
     - `nixpkgs.follows = "vpsadminos/nixpkgs"`
   - Export `packages.${system}.vpsfree-web`, `apps.${system}.test-runner`,
     `tests`, and `testsMeta`.
   - Reuse the existing `default.nix`, `composer-env.nix`, and
     `php-packages.nix` to build the web tree with Composer dependencies.
   - Add `test-runner.sh`, `tests/all-tests.nix`, `tests/make-test.nix`,
     `tests/README.md`, and `tests/suite/web.nix`.

3. Build a disposable two-machine integration test
   - `services`: vpsAdmin services VM from
     `vpsadmin/tests/configs/nixos/vpsadmin-services.nix`.
     - Provides `api.vpsadmin.test`, database, scheduler, mailer container,
       and Mailpit.
     - Runs Playwright, following the vpsAdmin webui browser-test pattern.
   - `web`: lightweight NixOS VM running the packaged site through Nginx and
     PHP-FPM.
     - Configure virtual hosts `vpsfree.cz` -> `cs/` and `vpsfree.org` ->
       `en/`.
     - Enable SSI and PHP handling the same way production does in
       `vpsfree-cz-configuration/modules/services/vpsfree-web.nix`.
     - Write a test `config.php` with:
       - `API_URL = "http://api.vpsadmin.test"`
       - `ENVIRONMENT_ID = 1`
     - Expose shared aliases `/css`, `/js`, `/obrazky`, and `/download`.
   - Use a socket network so `services` can resolve `vpsfree.cz` and
     `vpsfree.org` to the web VM, and the web VM can resolve
     `api.vpsadmin.test` to the services VM.

4. Add a small runner extension
   - Add `tests/runner/extensions/vpsadmin_services.rb`, adapted from existing
     vpsAdmin/vpsf-status helpers.
   - Keep only the needed helpers:
     - wait for vpsAdmin API;
     - run API-side Ruby snippets and parse JSON;
     - wait for/clear/read Mailpit messages.

5. Add Playwright tests under `tests/playwright/web`
   - Use CommonJS files and a local `playwright.config.cjs`, matching the
     existing vpsAdmin webui test style.
   - Use Nix-provided `pkgs.playwright-test` and
     `pkgs.playwright-driver.browsers-chromium`; no npm install in CI.
   - Intercept or ignore external third-party requests so analytics, maps, and
     external links do not make tests flaky.

6. Public page coverage
   - Maintain a route manifest for public standalone pages in both language
     roots.
   - Include localized page entry points such as `/`, `/faq/`, `/parametry/`,
     `/parameters/`, `/prihlaska/`, `/registration/`, static registration
     pages, accepted pages with an explicit test ID query, 404 pages, and
     Czech-only hardware survey pages.
   - Exclude partials and handlers that are not standalone pages:
     `hlavicka.html`, `paticka.html`, `analytics.html`, `template.html`,
     `form.php`, `spolecne.php`, `send.php`, `osoba.php`, accepted-page
     `id.php`, sitemap/robots documents, QR image generator endpoints under
     `cs/nastroje`, and vendor PHP files under `cs/nastroje/phpqrcode`.
   - For each route, assert:
     - HTTP 2xx;
     - no same-origin failed assets;
     - no raw SSI directives left in the response;
     - no visible PHP fatal/warning output;
     - meaningful body content is present.

7. Registration browser coverage
   - Dynamic forms:
     - `/prihlaska/` and `/registration/`;
     - select `fyzicka` and `pravnicka`;
     - assert the AJAX-loaded form appears, required fields exist, action path
       is locale-correct, and time zone defaults when browser Intl supplies
       one.
   - Static forms:
     - `/prihlaska/fyzicka-osoba/`
     - `/prihlaska/pravnicka-osoba/`
     - `/registration/fyzicka-osoba/`
     - `/registration/pravnicka-osoba/`
     - assert form action and `entity_type` are correct.
   - Real submissions:
     - submit valid unique data for both languages and both entity types;
     - select real test-cluster location/template/currency/time zone options;
     - assert redirect to `/prihlaska/prijata/?<id>` or
       `/registration/accepted/?<id>`;
     - assert the accepted page displays the same numeric registration ID;
     - query vpsAdmin from the test script and assert the
       `RegistrationRequest` row contains the expected login, e-mail, language,
       org fields where applicable, and time zone;
     - assert Mailpit receives the expected registration mail when the vpsAdmin
       workflow sends one.
   - Validation coverage:
     - Use the existing `_mock=1` path for browser validation tests that should
       pass local PHP validation without creating API rows.
     - Cover required fields and representative invalid values for login, name,
       e-mail, birth year, address, city, ZIP/postal code, country, org name,
       org ID, distribution, location, currency, and time zone.
     - Assert both the `.error` field class and localized error text.
     - Keep a small number of accepted-value browser tests to verify the
       rendered form accepts non-ASCII names/cities and English postal/address
       formats.

8. Add focused fast unit tests if still useful after the browser suite shape is
   clear
   - Prefer a small PHP CLI test for `Validators` rather than adding PHPUnit.
   - If testing mail-domain rejection deterministically, refactor the validator
     to allow an injectable MX lookup while preserving the default
     `dns_get_record` behavior.
   - Run these from a flake `checks` output and from the workflow before the VM
     integration suite.

9. Fix defects exposed by the tests
   - The current static company forms have `entity_type=fyzicka`; they should
     be `pravnicka`.
   - The current English static forms post to `/prihlaska/send.php`; they
     should post to `/registration/send.php`.
   - Review API-error rendering in `RegistrationForm#printErrors`; it currently
     contains an unused/undefined `$error` reference in the API response loop.

## Compatibility and deployment
- Production behavior change should be limited to registration bug fixes found
  while making tests pass.
- No database schema, API protocol, persisted state, or deployment ordering
  changes are planned in `web`.
- The integration test creates registration requests only in the disposable
  vpsAdmin VM; no production API or database is touched.
- The test VM should mirror the existing production deployment model from
  `vpsfree-cz-configuration`: Nginx + PHP-FPM + SSI, not the older README
  Apache example.
- The web repository will gain a flake and lock file. That affects CI and local
  development only; production pinning remains controlled by configuration
  repositories.
- The test flake must use a vpsAdmin revision that supports registration
  `time_zone`, because current `web` already sends that field.
- Rollback impact is low: reverting this branch removes tests and any small
  registration-form fixes, and no new persistent format remains.

## Testing plan
- Local/static checks:
  - `nix flake check` once flake checks exist.
  - PHP unit validator script if added.
- Test-runner discovery:
  - `./test-runner.sh ls`
- Integration suite:
  - `./test-runner.sh test -f web`
  - `./test-runner.sh test -t ci`
- CI:
  - Add `.github/workflows/integration-tests.yml`.
  - Match the self-hosted workflow structure used by `vpsf-status` and
    `vpsfree-irc-bot`: reset per-user Nix gcroots, run
    `./test-runner.sh test -f --jobs auto -t ci --state-dir /tmp/os-test-runner`,
    evaluate/summarise/upload logs with vpsAdminOS actions, and clean gcroots.
  - Before implementing the workflow, verify current upstream versions for
    external GitHub actions as required by the workspace policy.
