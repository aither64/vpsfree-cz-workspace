# Security Advisories State

## Initiative

- Slug: `2026-05-29-security-advisories`
- Branch: `2026-05-29-security-advisories`
- Started: 2026-05-29
- Current status: implementation is committed in the project worktrees and
  split dev-cluster support commits are committed in the coordination
  workspace. Remaining work is to rebase the vpsAdmin feature branch on
  current upstream, push unpushed branches, repair/verify the running bridge
  dev-cluster login, and monitor GitHub Actions to completion.

## Worktrees

| Repository | Worktree | Base |
| --- | --- | --- |
| `vpsadmin` | `worktrees/2026-05-29-security-advisories/vpsadmin` | `f2dc568ff` (`deps: update HaveAPI components to 0.28.4`) |
| `vpsadmin-go-client` | `worktrees/2026-05-29-security-advisories/vpsadmin-go-client` | `45a5170` (`Add commit message rules`) |
| `vpsf-status` | `worktrees/2026-05-29-security-advisories/vpsf-status` | `5f6db13` (`outage reports: rename planned outage helpers`) |
| `vpsfree-irc-bot` | `worktrees/2026-05-29-security-advisories/vpsfree-irc-bot` | `6db629e` (`Update GitHub checkout action to v6`) |
| `vpsfree-mail-templates` | `worktrees/2026-05-29-security-advisories/vpsfree-mail-templates` | `d35ad25` (`outage reports: label impact values`) |
| `vpsfree-cz-configuration` | `worktrees/2026-05-29-security-advisories/vpsfree-cz-configuration` | `a0e0f0ee` (`inputs: update vpsadminServices to f2dc568f`) |

## Commands Run

- `git --git-dir=repos/vpsadmin.git fetch --prune origin`
- `git --git-dir=repos/vpsfree-cz-configuration.git fetch --prune origin`
- `git --git-dir=repos/vpsfree-mail-templates.git fetch --prune origin`
- `git --git-dir=repos/vpsadmin.git worktree add -b 2026-05-29-security-advisories worktrees/2026-05-29-security-advisories/vpsadmin origin/master`
- `git --git-dir=repos/vpsfree-cz-configuration.git worktree add -b 2026-05-29-security-advisories worktrees/2026-05-29-security-advisories/vpsfree-cz-configuration origin/master`
- `git --git-dir=repos/vpsfree-mail-templates.git update-ref refs/heads/master refs/remotes/origin/master`
- `git --git-dir=repos/vpsfree-mail-templates.git symbolic-ref HEAD refs/heads/master`
- `git --git-dir=repos/vpsfree-mail-templates.git worktree add -b 2026-05-29-security-advisories worktrees/2026-05-29-security-advisories/vpsfree-mail-templates origin/master`
- `git -C repos/vpsf-status.git fetch --prune origin`
- `git -C repos/vpsf-status.git update-ref refs/heads/master refs/remotes/origin/master`
- `git -C repos/vpsf-status.git symbolic-ref HEAD refs/heads/master`
- `git --git-dir=repos/vpsf-status.git worktree add -b 2026-05-29-security-advisories worktrees/2026-05-29-security-advisories/vpsf-status master`
- `git -C repos/vpsfree-irc-bot.git fetch --prune origin`
- `git -C repos/vpsfree-irc-bot.git update-ref refs/heads/master refs/remotes/origin/master`
- `git -C repos/vpsfree-irc-bot.git symbolic-ref HEAD refs/heads/master`
- `git --git-dir=repos/vpsfree-irc-bot.git worktree add -b 2026-05-29-security-advisories worktrees/2026-05-29-security-advisories/vpsfree-irc-bot master`
- `git -C repos/vpsadmin-go-client.git fetch --prune origin`
- `git -C repos/vpsadmin-go-client.git update-ref refs/heads/master refs/remotes/origin/master`
- `git -C repos/vpsadmin-go-client.git symbolic-ref HEAD refs/heads/master`
- `git -C repos/vpsadmin-go-client.git worktree add -b 2026-05-29-security-advisories worktrees/2026-05-29-security-advisories/vpsadmin-go-client master`
- `git -C repos/vpsadmin-go-client.git worktree remove /home/aither/workspace/ai/vpsfree.cz/repos/vpsadmin-go-client.git/worktrees/2026-05-29-security-advisories/vpsadmin-go-client`
- `git --git-dir=repos/vpsadmin-go-client.git worktree add worktrees/2026-05-29-security-advisories/vpsadmin-go-client 2026-05-29-security-advisories`
- `git -C worktrees/2026-05-29-security-advisories/<repo> remote get-url origin`

## Repository Instructions Read

- `worktrees/2026-05-29-security-advisories/vpsadmin/AGENTS.md`
- `worktrees/2026-05-29-security-advisories/vpsfree-cz-configuration/AGENTS.md`
- `worktrees/2026-05-29-security-advisories/vpsfree-mail-templates/AGENTS.md`
- `worktrees/2026-05-29-security-advisories/vpsf-status/AGENTS.md`
- `worktrees/2026-05-29-security-advisories/vpsadmin-go-client/AGENTS.md`
- `vpsfree-irc-bot` has no repository-local `AGENTS.md`; commands and style
  will be inferred from `README.md`, `Gemfile`, `Rakefile`, specs, and flake
  files before edits.

## Notes

- `vpsadmin` had advanced before this initiative; the new worktree starts from
  current `origin/master` at `f2dc568ff`.
- `vpsfree-cz-configuration` already pins `vpsadminServices` to that vpsAdmin
  revision at `a0e0f0ee`.
- `vpsfree-mail-templates.git`, `vpsf-status.git`,
  `vpsfree-irc-bot.git`, and `vpsadmin-go-client.git` had bare `HEAD`
  pointing outside `refs/heads`. Local `master` refs were created from
  `origin/master` and bare `HEAD` was pointed to `refs/heads/master` before
  creating worktrees.
- The first `vpsadmin-go-client` worktree command used `git -C` and created the
  worktree path relative to the bare repository directory. That misplaced
  worktree was removed and recreated under the initiative worktree group using
  `--git-dir` from the workspace root.
- Before implementation, upstreams were fetched and feature worktrees were
  fast-forwarded/rebased to current upstreams where needed. Notable bases seen
  during the rebase pass: `vpsadmin` `21a1d0b11`, `vpsf-status` `b481a8c9`,
  `vpsfree-irc-bot` `5d54aac8`, `vpsfree-cz-configuration` `88e9f518`.
- `vpsadmin-go-client` generation needed a local vpsAdmin API server started
  from the `api/` directory, with the test database seeded using the spec seed
  helpers. Running Rack from the repository root failed because `config.ru` and
  relative paths were wrong.
- The generated Go client has broad drift from upstream, not only the new
  advisory resources. New resources include `SecurityAdvisory`,
  `SecurityAdvisoryUpdate`, `UserSecurityAdvisory`, `VpsSecurityAdvisory`, and
  `OutageSecurityAdvisory`.
- `vpsf-status/go.mod` currently has a temporary local replace:
  `github.com/vpsfreecz/vpsadmin-go-client => ../vpsadmin-go-client`. This is
  useful for local compilation, but it prevents Nix `buildGoModule` and the
  vpsf-status integration suite from building in the sandbox. Replace it with
  the released/pushed generated client pseudo-version before final integration
  validation and deployment.
- `vpsfree-cz-configuration` only enables the new IRC bot
  `security_advisories` setting for `#vpsfree` so far. Input/package pins for
  vpsAdmin, vpsf-status, and vpsfree-irc-bot must be updated after the feature
  branches are committed and available.
- The vpsAdmin Nix package source used by the VM test framework only sees
  files that are part of the Git source. For uncommitted cross-repo tests, a
  throwaway Git copy was needed so new files and ignored generated package
  locks were visible. See
  `notes/cross-project/2026-06-01-test-runner-flake-overrides.md`.

## Implementation Summary

- `vpsadmin`
  - Added core advisory migrations, models, API resources, transaction-chain
    mail support, built-in mail templates, focused API/model specs, web UI
    pages/forms/routes/index display, and outage-report cross-links.
  - Advisory states are `draft`, `published`, and `retracted`.
  - Node status states are `unknown`, `not_affected`, `vulnerable`, and
    `mitigated`.
  - Publishing is blocked until active nodes are all known
    `not_affected`/`mitigated`; mitigated nodes require `vulnerable_until` and
    `mitigated_since`.
  - Affected VPS/user rows are current-impact snapshots rebuilt at publish or
    explicitly by admins.
  - Mail send flags default to false for publish and update actions.
  - Migration/schema cleanup keeps the advisory feature in one core migration
    plus one outage_reports plugin migration for the outage/advisory join
    table.
  - `api/db/schema.rb` is kept core-only. Added a smoke spec that fails if
    plugin-created tables appear in the core schema or if the schema version
    is older than the latest core migration.
  - Split outage/advisory API coverage out of the core advisory resource spec
    into an outage_reports plugin spec. Extracted generic VPS/export fixture
    helpers from the outage_reports helper into a core spec helper.
- `vpsadmin-go-client`
  - Regenerated from the local vpsAdmin API schema and formatted with `gofmt`.
- `vpsf-status`
  - Added polling/rendering/JSON for recent public security advisories.
  - Added unit and route coverage plus a status-page integration fixture that
    creates a published mitigated advisory through vpsAdmin.
- `vpsfree-irc-bot`
  - Added a `security_advisories` plugin that announces new published
    advisories and advisory updates, with state persisted per server.
  - Added unit wiring/config sample and vpsAdmin-events integration coverage.
- `vpsfree-mail-templates`
  - Added English and Czech production templates for advisory announcements and
    updates.
- `vpsfree-cz-configuration`
  - Enabled the IRC bot advisory watcher on `#vpsfree`.

## Validation

- Verified all six worktrees are on branch
  `2026-05-29-security-advisories`.
- Verified all six worktree remotes use SSH URLs.
- Updated `plan.md` for the user's decision to implement advisories in
  vpsAdmin core rather than as a plugin.
- vpsAdmin syntax:
  - `ruby -c` for new/changed Ruby files.
  - `php -l` for new/changed web UI PHP files.
- vpsAdmin focused specs:
  - Temporary MariaDB under `/tmp`, `DATABASE_URL` with `encoding=utf8`,
    `RACK_ENV=test VPSADMIN_PLUGINS=all bundle exec rspec
    spec/models/security_advisory_spec.rb
    spec/api/resources/security_advisory_spec.rb`
  - Result after the encoding fix: 16 examples, 0 failures.
  - A failed intermediate run without `encoding=utf8` produced MariaDB
    `COLLATION 'utf8mb3_bin' is not valid for CHARACTER SET 'utf8mb4'` during
    API authentication; keep the encoding in future local DATABASE_URL runs.
  - Migration/schema follow-up on 2026-06-02:
    - `ruby -c` passed for the changed advisory specs, schema spec, and spec
      helpers.
    - Static schema precheck passed: no plugin tables in `api/db/schema.rb`
      and schema version equals latest core migration `20260601120000`.
    - `VPSADMIN_PLUGINS=none bundle exec rspec
      spec/smoke/core_schema_spec.rb
      spec/api/resources/security_advisory_spec.rb
      spec/models/security_advisory_spec.rb`: 21 examples, 0 failures.
    - An intermediate outage_reports plugin spec run failed because a helper
      did not accept Ruby 3 keyword attributes; fixed by accepting `**kwattrs`.
    - `VPSADMIN_PLUGINS=all bundle exec rspec
      spec/api/plugins/outage_reports/security_advisory_spec.rb`: 3 examples,
      0 failures.
    - `bundle exec rubocop` on changed API specs/helpers: no offenses.
    - `git diff --check`: passed.
- vpsAdmin CI/test metadata:
  - `ruby tests/ci-selection-test.rb`: 13 runs, 40 assertions, 0 failures.
  - Checked `rake -T`; `rake vpsadmin:gems` only rebuilds `libnodectld`,
    `nodectl`, and `nodectld`, which this feature did not touch. No vpsAdmin
    generated gem rebuild is needed for this change.
- `vpsadmin-go-client`:
  - `gofmt -w client`
  - `CGO_ENABLED=0 go test ./...` passed; rerun after final checks also
    passed.
- `vpsf-status`:
  - `CGO_ENABLED=0 go test ./...` passed; rerun after final checks also
    passed.
  - Plain `go test ./...` failed in this environment because cgo/gcc was not
    available.
  - Nix integration is pending until `go.mod` uses a released generated client
    instead of the sibling local replace.
- `vpsfree-irc-bot`:
  - `ruby -c lib/vpsfree-irc-bot/security_advisories.rb`
  - `ruby -c lib/vpsfree-irc-bot.rb`
  - `nix develop --command bash -lc 'bundle exec rspec'`: 39 examples,
    0 failures. Rerun after final checks also passed.
  - A direct
    `nix run --override-input vpsadmin path:/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-05-29-security-advisories/vpsadmin .#test-runner -- test vpsadmin-events`
    first failed because the runtime test-runner evaluation still used
    `flake.lock` and built a vpsAdmin package without the new advisory files.
  - A verified temp-source run passed after locking a throwaway IRC bot copy to
    a throwaway vpsAdmin Git copy that included ignored generated package
    locks:
    `nix run .#test-runner -- test --fresh vpsadmin-events`
    Result: 6 examples, 0 failures; total test script time 494.84 seconds.
- `vpsfree-mail-templates`:
  - `ruby -c` for new `meta.rb` files.
  - ERB compilation check for new English/Czech plain-text templates.
- `vpsfree-cz-configuration`:
  - `nix develop --command nixfmt --check
    cluster/cz.vpsfree/containers/int.vpsfbot/config.nix` passed.
- Cross-repository:
  - `git diff --check` passed in all six modified worktrees.

## Dev Cluster

- Started a vpsAdmin dev cluster for this initiative on 2026-06-01, first in
  local mode for initial smoke testing:
  `dev-clusters/vpsadmin/bin/devcluster start
  2026-05-29-security-advisories --topology single --network local`.
- The user needed standard HTTPS `:443`, so the local-mode cluster was stopped
  and restarted on the bridge network:
  `dev-clusters/vpsadmin/bin/devcluster start
  2026-05-29-security-advisories --topology single --network bridge`.
- The cluster is running and ready:
  `dev-clusters/vpsadmin/bin/devcluster status
  2026-05-29-security-advisories` reports `status: running`, `ready: yes`,
  `pid: 1487029`, `topology: single`, `network: bridge`.
- Bridge URLs use normal HTTPS on `172.16.106.53:443`:
  - Web UI: `https://webui.aitherdev.int.vpsfree.cz/`
  - API: `https://api.aitherdev.int.vpsfree.cz/`
  - Auth: `https://auth.aitherdev.int.vpsfree.cz/`
  - Console: `https://console.aitherdev.int.vpsfree.cz/`
  - Mailpit: `https://mailpit.aitherdev.int.vpsfree.cz/`
- Credentials:
  - Admin: `test-admin` / `testAdminPassword`
  - Users: `test-user1` / `testUser1Password`,
    `test-user2` / `testUser2Password`
  - Mailpit: `mailpit` / `mailpitPassword`
- Bridge SSH addresses:
  - services: `172.16.106.53`
  - node1: `172.16.106.41`
  - dns-primary: `172.16.106.61`
  - dns-secondary: `172.16.106.62`
- New vpsAdmin files were staged before starting the cluster so Nix flake
  source copying could see them. This is only for source visibility; nothing
  was committed.
- First start attempt failed during Nix evaluation because the updated
  vpsAdmin test-services module now defines Mailpit by default and the
  dev-cluster module also defines its own Mailpit service:
  `containers.mailer.systemd.services.mailpit.description` had conflicting
  values. Patched `dev-clusters/vpsadmin/nix/test.nix` to set
  `vpsadmin.test.mailpit.enable = false` and keep the dev-cluster Mailpit
  service as the exposed capture service.
- Verification:
  - Web UI loaded through
    `curl -k --resolve webui.aitherdev.int.vpsfree.cz:443:172.16.106.53
    https://webui.aitherdev.int.vpsfree.cz/` and returned an 8924-byte XHTML
    page.
  - Mailpit API loaded through `172.16.106.53:443` with basic auth and
    reported version `1.30.0`.
- Follow-up Web UI feedback implemented and deployed on 2026-06-01:
  - Removed `Security advisories` from the main top navigation.
  - Kept `Security advisories` in the index sidebar and added it to the
    cluster sidebar.
  - Suppressed the empty recent-advisories table on the index page when there
    are no advisories.
  - Rendered the security advisory page sidebar and added the admin
    `New security advisory` link there.
  - Added a VPS details sidebar link to security advisories filtered by that
    VPS, matching the existing outage link shape.
  - Allowed logged-in users to filter advisory summaries by VPS at the API
    layer, restricted by `security_advisory_vpses.user_id` so users only get
    results for their own VPSes.
- Follow-up validation:
  - PHP syntax passed for touched Web UI files.
  - `ruby -c api/lib/vpsadmin/api/resources/security_advisory.rb` passed.
  - `git diff --check` passed in `vpsadmin`.
  - Focused advisory API spec passed against a temporary MariaDB:
    `spec/api/resources/security_advisory_spec.rb`, 14 examples, 0 failures.
  - Deployed with
    `dev-clusters/vpsadmin/bin/devcluster update
    2026-05-29-security-advisories services`.
  - Verified the running bridge cluster still reports `ready: yes`.
  - Verified Web UI, API, and Mailpit respond on
    `https://*.aitherdev.int.vpsfree.cz/` through `172.16.106.53:443`.
  - Verified as `test-admin` that the main nav excludes security advisories,
    the cluster sidebar includes the advisory link, and the advisory list
    sidebar includes `New security advisory`.
- Second Web UI feedback round implemented and deployed on 2026-06-01:
  - Added field hints/placeholders to the new advisory form for CVEs, name,
    translated summary, description, and response.
  - Changed the new advisory submit label to `Create draft`.
  - Added node-status selection to the new advisory form.
  - Added a compact node-status bulk row to apply state/timestamps/note to all
    listed nodes client-side, with per-node edits below it.
  - Restricted advisory node status forms and publish validation to active
    hypervisor and storage nodes only.
  - Normalized `YYYY-MM-DD HH:MM` node timestamp inputs to ISO 8601 before
    sending them to the API.
  - Fixed advisory detail information rows to use rowspans for translated
    fields.
  - Hid `Your affected VPS` from admins and added admin affected user/VPS
    counters.
  - Fixed mail-template language seeding so `cs` is labeled `Česky`, including
    repair of records previously labeled only `cs`.
  - Kept built-in core advisory mail templates generic (`vpsAdmin`) so branded
    wording remains in `vpsfree-mail-templates`.
- Second feedback validation:
  - PHP syntax passed for `webui/forms/security_advisory.forms.php` and
    `webui/pages/page_security_advisory.php`.
  - Ruby syntax passed for touched API model/bootstrap files.
  - Focused advisory API/model specs passed against temporary MariaDB:
    `spec/api/resources/security_advisory_spec.rb` and
    `spec/models/security_advisory_spec.rb`, 17 examples, 0 failures.
  - Mail template model spec passed after the language-label regression:
    `spec/models/mail_templates_spec.rb`, 7 examples, 0 failures.
  - `git diff --check` passed in `vpsadmin`.
  - Deployed with
    `dev-clusters/vpsadmin/bin/devcluster update
    2026-05-29-security-advisories services`.
  - Verified `GET /v7.0/languages` returns `en/English` and `cs/Česky`.
  - Verified as `test-admin` that the new advisory form shows hints,
    `Create draft`, the node-status bulk row, and only the single active
    hypervisor node in this single-node dev cluster.
  - Created draft advisory `#3` through the Web UI form with node status saved;
    the detail page shows admin affected counters, no `Your affected VPS`
    section, rowspans on translated information fields, and the saved
    mitigated node status.
- Third Web UI feedback round implemented and deployed on 2026-06-01:
  - Reduced new-advisory text inputs and textareas from 70 to 60 columns.
  - Removed the remaining security-advisory form references to `vpsFree.cz`
    from placeholder/help text.
  - Rendered the embedded new-advisory node-status editor as a compact nested
    table inside one `colspan=3` form row, instead of expanding the outer
    advisory form table to five columns.
  - Moved the node-status bulk `Apply` button under `All nodes` on both the
    new advisory form and the standalone node-status editor.
  - Reduced node-status timestamp fields to size 15 and note fields to size 18.
- Third feedback validation:
  - `php -l webui/forms/security_advisory.forms.php` passed.
  - `git diff --check` passed in `vpsadmin`.
  - Verified advisory feature files have no `vpsFree.cz`, `vpsFree`, or
    `vpsfree` wording in `webui/forms/security_advisory.forms.php`,
    `webui/pages/page_security_advisory.php`, or `api/mail_templates`.
  - Deployed with
    `dev-clusters/vpsadmin/bin/devcluster update
    2026-05-29-security-advisories services`.
  - Verified the running bridge cluster reports `ready: yes`.
  - Verified as `test-admin` that the deployed new advisory form uses
    `size="60"`/`cols="60"`, embeds `security-advisory-node-table` in a
    `colspan="3"` row, and shows the bulk `Apply` button under `All nodes`.
  - Verified the deployed standalone node-status editor also shows `Apply`
    under `All nodes` with compact timestamp/note inputs.
- Fourth Web UI feedback round implemented and deployed on 2026-06-01:
  - Prefilled advisory node-status timestamp fields with the current local
    date/time for new statuses and bulk defaults.
  - Made `vulnerable_until` and `mitigated_since` optional for `unknown`,
    `not_affected`, and `vulnerable` node states; `not_affected` clears both
    timestamps before sending them to the API.
  - Added editable `published_at` fields to advisory create, publish, edit,
    and update flows, with current date/time defaults.
  - Limited recent/index advisory lists to published advisories.
  - Removed `State` and `Nodes` columns from the recent/index advisory list.
  - Displayed advisory summary, description, and response only in the logged-in
    user's current Web UI language, while anonymous users still see all
    translations.
- Fourth feedback validation:
  - PHP syntax passed for `webui/forms/security_advisory.forms.php` and
    `webui/pages/page_security_advisory.php`.
  - Ruby syntax passed for touched advisory API/model/spec files.
  - Focused advisory API/model specs passed against temporary MariaDB:
    `spec/api/resources/security_advisory_spec.rb` and
    `spec/models/security_advisory_spec.rb`, 17 examples, 0 failures.
  - `git diff --check` passed in `vpsadmin`.
  - Deployed with
    `dev-clusters/vpsadmin/bin/devcluster update
    2026-05-29-security-advisories services`.
  - Verified the running bridge cluster reports `ready: yes`.
  - Verified the deployed public index page renders the recent advisory table
    with `Published`, `CVEs`, `Name`, and `Summary`, and without `State` or
    `Nodes`.
- Fifth Web UI feedback round implemented and deployed on 2026-06-01:
  - Fixed recent/index advisory summaries by reading localized HaveAPI
    resource attributes directly instead of relying on `isset()` for magic
    properties.
  - Removed the language prefix from advisory detail summary, description, and
    response rows for logged-in users; anonymous users still see all
    translations with language labels.
- Fifth feedback validation:
  - `php -l webui/forms/security_advisory.forms.php` passed.
  - `git diff --check -- webui/forms/security_advisory.forms.php` passed.
  - Deployed with
    `dev-clusters/vpsadmin/bin/devcluster update
    2026-05-29-security-advisories services`.
  - Verified the anonymous index recent advisory row shows `English summary`
    in the `Summary` column.
  - Verified a fresh OAuth2 login as `test-admin` and confirmed advisory detail
    shows plain localized content without `English:` prefixes.
  - Verified anonymous advisory detail still shows both `English` and `Česky`
    prefixes.
- Sixth feedback round implemented on 2026-06-02:
  - Removed advisory `title` from the unreleased vpsAdmin advisory migration,
    schema, API params/output, model translation helpers, Web UI forms/details,
    and advisory specs.
  - Kept `summary` as the required localized public headline/list text.
  - Regenerated `vpsadmin-go-client` from a local vpsAdmin API server started
    from the edited worktree; generated advisory resources no longer expose
    `en_title`/`cs_title`.
  - Updated `vpsf-status` to remove `EnTitle`, the public `en_title` JSON
    field, and the separate status-page `Advisory` column.
  - Updated vpsf-status and vpsfree-irc-bot integration fixtures to stop
    creating translation `title` values.
- Sixth feedback validation:
  - vpsAdmin focused advisory specs passed against a temporary MariaDB:
    `spec/models/security_advisory_spec.rb` and
    `spec/api/resources/security_advisory_spec.rb`, 17 examples, 0 failures.
  - vpsAdmin syntax checks passed for touched Ruby/PHP advisory files.
  - `ruby tests/ci-selection-test.rb` passed: 13 runs, 40 assertions,
    0 failures.
  - Regenerated client was checked with `CGO_ENABLED=0 go test ./...` in
    `vpsadmin-go-client`.
  - `CGO_ENABLED=0 go test ./...` passed in `vpsf-status`.
  - `nix develop --command bash -lc 'bundle exec rspec'` passed in
    `vpsfree-irc-bot`: 39 examples, 0 failures.
  - `git diff --check` passed in all six feature worktrees.
  - Deployed vpsAdmin-side changes with
    `dev-clusters/vpsadmin/bin/devcluster update
    2026-05-29-security-advisories services`.
  - Verified the bridge dev cluster reports `ready: yes`.
  - Verified
    `https://api.aitherdev.int.vpsfree.cz/v7.0/security_advisories` returns
    advisory summary/description/response fields and no `en_title`/`cs_title`
    fields.
- Useful stop command:
  `dev-clusters/vpsadmin/bin/devcluster stop
  2026-05-29-security-advisories`.
- Dev-cluster vpsf-status integration implemented on 2026-06-02:
  - Added `status.aitherdev.int.vpsfree.cz` to the dev-cluster default
    domains and to `devcluster urls`.
  - Added config backfill so existing copied cluster configs pick up new
    default keys without losing local overrides.
  - Added a `vpsfStatus` flake input and optional local source wiring for
    `worktrees/<slug>/vpsf-status`.
  - Added optional local `worktrees/<slug>/vpsadmin-go-client` source wiring
    for local generated-client testing.
  - Enabled `vpsf-status` in the services VM, configured it against the
    dev-cluster API/Web UI/console URLs and selected topology nodes, and
    exposed it through nginx on `https://status.aitherdev.int.vpsfree.cz/`.
  - Extended `vpsf-status` package support so local Nix builds can copy a
    sibling generated client source for the current temporary Go module
    replacement.
  - Updated the `vpsf-status` vendor hash for the local generated client:
    `sha256-O4Exw5HSmC3nmha/M3kWo85M05J+MwSFJJRa1UYUsLE=`.
  - Added the persistent internal DNS CNAME to
    `vpsfree-cz-configuration/configs/internal-dns/zone.vpsfree.cz.`:
    `status.aitherdev.int` -> `frontend.aitherdev.int.vpsfree.cz.`.
- Dev-cluster vpsf-status validation:
  - `bash -n dev-clusters/vpsadmin/bin/devcluster` passed.
  - `jq -e . dev-clusters/vpsadmin/default-config.json` passed.
  - `dev-clusters/vpsadmin/bin/devcluster update
    2026-05-29-security-advisories services` passed; it reissued the dev
    certificate to include `status.aitherdev.int.vpsfree.cz`, built
    `vpsf-status-dev`, switched the services VM, and started
    `vpsf-status.service`.
  - `dev-clusters/vpsadmin/bin/devcluster status
    2026-05-29-security-advisories` reports `ready: yes`.
  - Direct SSH to services confirmed `vpsf-status.service` is `active` and
    `getent hosts status.aitherdev.int.vpsfree.cz` resolves to
    `172.16.106.53`.
  - The dev certificate SAN includes `status.aitherdev.int.vpsfree.cz`.
  - `curl -k --resolve
    status.aitherdev.int.vpsfree.cz:443:172.16.106.53
    https://status.aitherdev.int.vpsfree.cz/` returned HTTP 200.
  - `https://status.aitherdev.int.vpsfree.cz/json` includes
    `security_advisories`; it showed the published test advisory and
    `api`, `webui`, and `console` as operational.
  - `CGO_ENABLED=0 go test ./...` passed in `vpsf-status`.
  - `git diff --check` passed in the workspace,
    `vpsfree-cz-configuration`, and `vpsf-status`.
  - `nixfmt --check` passed for touched Nix files.
- Internal DNS validation:
  - `named-checkzone vpsfree.cz configs/internal-dns/zone.vpsfree.cz.`
    passed with the pre-existing `@fqdn@` check-names warning.
  - `nix develop -c confctl build -y -t internal-dns` passed and built
    generations for `cz.vpsfree/containers/brq/int.ns1` and
    `cz.vpsfree/containers/prg/int.ns1`.
  - Internal DNS was built but not deployed.
- `vpsfree-cz-configuration` was committed and pushed on 2026-06-02:
  - `dc4bccf3` `vpsadmin-config: enable security advisory IRC notifications`
  - `bb1c7c41` `dns: add aitherdev status alias`
  - Remote branch:
    `origin/2026-05-29-security-advisories`
  - Push had to be run inside `nix develop` because the installed Git hooks
    need the repository Bundler environment.
- vpsf-status / IRC bot follow-up implemented on 2026-06-02:
  - Removed the `Affected nodes` column from the recent security advisories
    table in `vpsf-status`.
  - Changed the status-page `No issues reported` banner so recent security
    advisories do not hide it; the banner now depends only on outage report
    state and notices.
  - Kept the separate `Unable to fetch security advisories from vpsAdmin`
    warning when advisory fetching fails.
  - Removed the affected-node-count line from new-advisory IRC announcements.
  - Updated `vpsf-status` route tests and the `vpsfree-irc-bot`
    vpsAdmin-events integration test expectations.
  - Validation passed:
    `CGO_ENABLED=0 go test ./...` in `vpsf-status`;
    `nix develop --command bash -lc 'bundle exec rspec'` in
    `vpsfree-irc-bot`; `ruby -c
    lib/vpsfree-irc-bot/security_advisories.rb`; `git diff --check` in both
    worktrees.
  - Deployed to the running bridge dev cluster with
    `dev-clusters/vpsadmin/bin/devcluster update
    2026-05-29-security-advisories services`.
- Adminer dev-cluster support:
  - Added `adminer.aitherdev.int.vpsfree.cz` to the vpsAdmin dev-cluster
    default domains and `devcluster urls`.
  - Added an Adminer service on the services VM behind nginx basic auth and
    documented the development database connection details.
  - Added the persistent internal DNS CNAME to
    `vpsfree-cz-configuration/configs/internal-dns/zone.vpsfree.cz.`:
    `adminer.aitherdev.int` -> `frontend.aitherdev.int.vpsfree.cz.`.
- Final committed feature worktrees before push:
  - `vpsadmin`: `2ecf36b73` `api: add security advisories`; branch is
    currently ahead 1 and behind upstream `origin/master` by 7 commits.
  - `vpsadmin-go-client`: `4c74d69`
    `Update client for security advisories`; already pushed to
    `origin/2026-05-29-security-advisories`.
  - `vpsf-status`: `775c7aa`
    `status: show recent security advisories`.
  - `vpsfree-irc-bot`: `cd206df`
    `bot: announce security advisories`.
  - `vpsfree-mail-templates`: `9797f7f`
    `security_advisory: add user mail templates`.
  - `vpsfree-cz-configuration`: `dc4bccf3`
    `vpsadmin-config: enable security advisory IRC notifications`,
    `bb1c7c41` `dns: add aitherdev status alias`, and `a10f6dd9`
    `dns: add aitherdev adminer alias`; pushed to
    `origin/2026-05-29-security-advisories`.
- Final focused validations before push:
  - `vpsadmin`: focused core advisory/schema/mail-template specs and the
    outage_reports advisory plugin spec passed against temporary MariaDB;
    targeted RuboCop on changed advisory/spec files passed.
  - `vpsadmin-go-client`: `go fmt ./...` and `CGO_ENABLED=0 go test ./...`
    passed.
  - `vpsf-status`: `CGO_ENABLED=0 go test ./...`,
    `nix build .#vpsf-status --no-link`, `lefthook run pre-commit
    --all-files` through `nix develop`, and a throwaway-lock
    `status-page` integration run passed.
  - `vpsfree-irc-bot`: repository specs passed with `bundle exec rspec`
    through `nix develop`; a throwaway-lock `vpsadmin-events` integration
    run passed.
  - `vpsfree-mail-templates`: Ruby syntax and ERB compilation checks passed
    for the new English and Czech advisory templates.
- Coordination workspace commits for this task:
  - `1e8a652` `docs: preserve generated confctl commit messages`.
  - `1c0df48` `dev-clusters: merge vpsadmin default config updates`.
  - `acf762d` `dev-clusters: add Adminer to vpsadmin cluster`.
  - `cb7fc42` `dev-clusters: add vpsf-status to vpsadmin cluster`.
  - `d5043e7` `dev-clusters: use configured API host for webui OAuth`.
  - `a50a1a7` `dev-clusters: disable duplicate vpsadmin Mailpit service`.
  - `9e528d5` `dev-clusters: keep webui sessions out of private tmp`.
- Dev-cluster login repair on 2026-06-02:
  - The Web UI OAuth callback was still failing after the API internal URL
    fix because PHP could not write sessions:
    `PHP Request Shutdown: Write failed: No space left on device (28)`.
  - The Web UI PHP-FPM private `/tmp` tmpfs was full of session files. Many
    session files were about 2.6 MiB because logged-in Web UI sessions store
    the API description.
  - Old session files were removed and PHP-FPM was restarted, which
    immediately restored login.
  - Added a dev-cluster Web UI override that stores sessions in
    `/run/vpsadmin-webui-sessions` and sets aggressive one-hour session GC.
  - Deployed with
    `dev-clusters/vpsadmin/bin/devcluster update
    2026-05-29-security-advisories services`.
  - Verified `/etc/vpsadmin/config.php` in the `webui` container contains the
    new `session.save_path` and GC settings, `/tmp` is empty, and the full
    OAuth login flow for `test-admin` redirects to `?page=cluster` with no
    token-exchange error.
  - Live check against
    `https://status.aitherdev.int.vpsfree.cz/` confirmed that recent security
    advisories are shown, `No issues reported` is still shown when there are
    no outage reports, and the `Affected nodes` column is absent.
- Top-level CVE resource revision implemented on 2026-06-02:
  - Added `SecurityAdvisoryCve` as a top-level vpsAdmin API resource with
    `index`, `show`, `create`, `update`, and `delete`.
  - Removed flattened `cves` and `cve_urls` from
    `SecurityAdvisory`/`SecurityAdvisoryUpdate` API output. The web UI still
    accepts a comma/whitespace-separated CVE text input and reconciles it to
    CVE rows through the new API resource.
  - Publishing now also requires at least one assigned CVE.
  - Regenerated `vpsadmin-go-client`; generated output now includes
    `ResourceSecurityAdvisoryCve` and `Client.SecurityAdvisoryCve`.
  - Updated `vpsf-status` to fetch CVE rows separately for each advisory and
    expose JSON `security_advisories.recent[].cves` as objects with
    `id`, `cve_id`, and `url`.
  - Updated `vpsfree-irc-bot` to fetch CVE rows independently for new-advisory
    and update messages.
  - Confirmed `vpsfree-mail-templates` did not need API-client changes because
    templates render the Ruby model helper `@a.cves`; changed Czech template
    label to `CVEs`.
  - Updated `vpsf-status/nix/package.nix` vendor hash for the regenerated Go
    client to
    `sha256-Gn+WmMpzOsJ1NN2x+wAzHCN/DQtKioCYCY1/xVnhusE=`.
- Adminer dev-cluster support implemented on 2026-06-02:
  - Added `adminer.aitherdev.int.vpsfree.cz` to the dev-cluster default
    domains and `devcluster urls`.
  - Added `adminer.service` to the services VM, serving `pkgs.adminer` through
    PHP on localhost and nginx HTTPS with dev-cluster basic auth.
  - Documented Adminer and the dev vpsAdmin database login in
    `dev-clusters/vpsadmin/README.md`.
  - Added the persistent internal DNS CNAME to
    `vpsfree-cz-configuration/configs/internal-dns/zone.vpsfree.cz.`:
    `adminer.aitherdev.int` -> `frontend.aitherdev.int.vpsfree.cz.`.
- 2026-06-02 validation and deployment after the CVE/Adminer revision:
  - `ruby tests/ci-selection-test.rb` in `vpsadmin`: 13 runs,
    40 assertions, 0 failures.
  - vpsAdmin focused specs through `nix develop`, against the temporary
    MariaDB socket at `/tmp/vpsadmin-vuln73-mariadb/mysql.sock`:
    `spec/api/resources/security_advisory_spec.rb` and
    `spec/models/security_advisory_spec.rb`, 20 examples, 0 failures.
  - `CGO_ENABLED=0 go test ./...` passed in `vpsadmin-go-client`.
  - `CGO_ENABLED=0 go test ./...` passed in `vpsf-status`.
  - Explicit Nix build of the local `vpsf-status` package with the sibling
    regenerated Go client source passed.
  - `nix develop --command bash -lc 'bundle exec rspec'` passed in
    `vpsfree-irc-bot`: 39 examples, 0 failures.
  - ERB syntax compilation passed for all new advisory templates in
    `vpsfree-mail-templates`.
  - `jq -e` passed for `dev-clusters/vpsadmin/default-config.json`;
    `bash -n` passed for `dev-clusters/vpsadmin/bin/devcluster`;
    `nixfmt` formatted `dev-clusters/vpsadmin/nix/test.nix`.
  - `named-checkzone vpsfree.cz configs/internal-dns/zone.vpsfree.cz.`
    passed with the pre-existing `@fqdn@` check-names warning.
  - `git diff --check` passed in all six feature worktrees and for the touched
    dev-cluster workspace files.
  - Deployed to the running bridge dev cluster with
    `dev-clusters/vpsadmin/bin/devcluster update
    2026-05-29-security-advisories services`. The update reissued the dev
    certificate for `adminer.aitherdev.int.vpsfree.cz`, switched the services
    VM, and started `adminer.service` and `vpsf-status.service`.
  - Live Adminer check:
    `curl -k -u adminer:adminerPassword --resolve
    adminer.aitherdev.int.vpsfree.cz:443:172.16.106.53
    https://adminer.aitherdev.int.vpsfree.cz/` returned the Adminer 5.4.2
    login page.
  - Live status-page check:
    `https://status.aitherdev.int.vpsfree.cz/` shows `No issues reported`
    before `Recent Security Advisories` and does not contain an
    `Affected nodes` column.
  - Live status JSON check confirmed
    `security_advisories.recent[].cves[]` is an object.
  - Live vpsAdmin API check:
    `https://api.aitherdev.int.vpsfree.cz/v7.0/security_advisory_cves`
    returned `status: true` and one visible CVE row.
  - The temporary local Rack API server used for Go client generation was
    stopped; nothing remains listening on `127.0.0.1:9292`.
- Dev-cluster Web UI 500 fixed on 2026-06-02:
  - Symptom: anonymous `https://webui.aitherdev.int.vpsfree.cz/` returned
    HTTP 500 after adding Adminer.
  - Cause: the Web UI used `http://api.vpsadmin.test` as `INT_API_URL`.
    That hostname did not have an explicit nginx vhost, so nginx routed it to
    the first vhost. After Adminer was added, the first vhost was the
    basic-auth-protected Adminer host, so the HaveAPI PHP client received a
    401 HTML page for its `OPTIONS /v7.0/` description request and failed to
    parse it as JSON.
  - Fix: changed the dev-cluster Web UI internal API URL to
    `http://api.aitherdev.int.vpsfree.cz`, which is explicitly mapped in the
    dev-cluster host table and nginx API vhost.
  - Validation: `nixfmt` and `git diff --check` passed for
    `dev-clusters/vpsadmin/nix/test.nix`; `devcluster update
    2026-05-29-security-advisories services` completed; the generated
    `/etc/vpsadmin/config.php` has
    `INT_API_URL = http://api.aitherdev.int.vpsfree.cz`; and
    `curl -k --resolve webui.aitherdev.int.vpsfree.cz:443:172.16.106.53
    https://webui.aitherdev.int.vpsfree.cz/` returned HTTP 200.
- `vpsfree-cz-configuration` Adminer DNS alias was committed and pushed on
  2026-06-02:
  - `a10f6dd9` `dns: add aitherdev adminer alias`
  - Remote branch: `origin/2026-05-29-security-advisories`
  - Validation before commit:
    `named-checkzone vpsfree.cz configs/internal-dns/zone.vpsfree.cz.` passed
    with the pre-existing `@fqdn@` check-names warning, and
    `nix develop --command confctl build -y -t internal-dns` built
    generations for `cz.vpsfree/containers/brq/int.ns1` and
    `cz.vpsfree/containers/prg/int.ns1`.
- Security advisory parameter descriptions moved to API metadata on
  2026-06-02:
  - Added descriptions to vpsAdmin API parameters for security advisory
    `name`, `published_at`, localized `summary`/`description`/`response`,
    publish `send_mail`, node status fields, advisory update fields, and
    `SecurityAdvisoryCve` fields.
  - Updated `webui/forms/security_advisory.forms.php` so the new/edit,
    publish, and update forms read help text from
    `getParameters('input')`. The WebUI keeps placeholders and the
    comma-separated CVE entry helper because that field is a UI aggregate over
    `SecurityAdvisoryCve` rows.
  - Added focused API-description coverage in
    `api/spec/api/resources/security_advisory_spec.rb` to assert that the
    advisory, publish, CVE, and advisory-update parameter descriptions are
    present in `OPTIONS /v7.0/`.
  - Validation:
    `ruby -c api/lib/vpsadmin/api/resources/security_advisory.rb`;
    `ruby -c api/lib/vpsadmin/api/resources/security_advisory_cve.rb`;
    `ruby -c api/lib/vpsadmin/api/resources/security_advisory_update.rb`;
    `php -l webui/forms/security_advisory.forms.php`;
    focused `nix develop ..#api -c bundle exec rspec
    spec/api/resources/security_advisory_spec.rb --format progress`
    against the temporary MariaDB socket at
    `/tmp/vpsadmin-vuln73-mariadb/mysql.sock`: 18 examples, 0 failures;
    `git diff --check`.
  - Deployed to the running bridge dev cluster with
    `dev-clusters/vpsadmin/bin/devcluster update
    2026-05-29-security-advisories services`.
  - Deployment recovery note: the first switch failed because the services VM
    root filesystem was full while relinking vpsAdmin database config. Ran
    `nix-collect-garbage -d` inside the services VM, freeing about 432 MiB,
    then reran the switch. RabbitMQ had an inconsistent empty local state with
    a stale `/var/lib/vpsadmin-rabbitmq/rabbitmq-initialized` stamp, so
    supervisor could not authenticate. Reset RabbitMQ local state, reran
    `vpsadmin-rabbitmq-setup.service`, and restarted supervisor.
  - Live validation after recovery:
    `systemctl --failed` in the services VM reported no failed units;
    `vpsadmin-api.service`, `vpsadmin-supervisor.service`,
    `container@webui.service`, and `vpsadmin-rabbitmq-setup.service` were
    active; `rabbitmqctl list_users` showed the expected `api`, `console`,
    `supervisor`, node, mailer, and admin users; API and WebUI returned HTTP
    200. `OPTIONS https://api.aitherdev.int.vpsfree.cz/v7.0/` returned the
    expected security advisory parameter descriptions.
  - Follow-up recovery: `container@mailer.service` was left inactive after
    the earlier RabbitMQ setup dependency failure, so the seeded mailer node
    was not updating its status. Started `container@mailer.service` manually.
    Inside the mailer container, `vpsadmin-nodectld.service`,
    `postfix.service`, and `mailpit.service` were active. RabbitMQ showed a
    running connection for `vpsadmin-mailer.lab`. The node 100 status row
    advanced from `2026-06-02 17:57:40` to `2026-06-02 17:58:40` UTC and
    `update_count` increased from 3 to 5. `systemctl --failed` reported no
    failed units and `container@mailer.service` was active.

## Cleanup

- Remove worktrees after merge or abandonment.
- Keep local and remote feature branches unless explicitly asked to delete them.
- Removed the throwaway temp sources used for the IRC bot VM integration run.
