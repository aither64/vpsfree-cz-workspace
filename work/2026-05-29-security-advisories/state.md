# Security Advisories State

## Initiative

- Slug: `2026-05-29-security-advisories`
- Branch: `2026-05-29-security-advisories`
- Started: 2026-05-29
- Current status: clean outage/advisory link API is implemented and committed
  locally in `vpsadmin`; the generated Go client is updated and committed
  locally in `vpsadmin-go-client`. The feature branch histories were cleaned up
  on 2026-06-04 after creating local backup branches named
  `backup/2026-05-29-security-advisories-pre-cleanup` in all task repos.
  Current heads after the 2026-06-04 default-branch refresh: `vpsadmin`
  `597848686`, `vpsadmin-go-client` `1d9240f`, `vpsf-status` `ee9afa9`,
  `vpsfree-irc-bot` `a7393bb`, `vpsfree-mail-templates` `22e7393`, and
  `vpsfree-cz-configuration` `a25d799c`.
  `./test-runner.sh test 'webui#security-advisories'` passed on
  2026-06-04 after the cleanup. All task worktrees were fetched from their
  default branches again on 2026-06-04; only `vpsfree-cz-configuration` needed
  rebasing, now at `9dcd51bf`. The running dev cluster was updated
  successfully after the rebase.

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
- GitHub Actions run `26882093251` for vpsAdmin failed in
  `webui#vps-admin-ops` because `nodectld` crashed repeatedly during setup.
  The concrete exception was `NoMethodError: undefined method 'empty?' for nil`
  in `NodeCtld::PoolStatus#update`. The failure was a startup race: the remote
  control socket was accepting `nodectl refresh` after `Daemon#init` started
  remote control but before `PoolStatus#init` populated `@pools`. Since
  `nodectld` sets `Thread.abort_on_exception = true`, the remote command
  thread exception terminated the daemon and the test eventually timed out
  waiting for node 102 runtime status.
- Local vpsAdmin commits after the clean outage/advisory link API follow-up:
  `33c9e0cf2` (`outage_reports: expose advisory links as resource`) on top of
  `bb36cedf8` (`outage_reports: improve advisory links`).
- Local `vpsadmin-go-client` commit after regeneration:
  `f3b308f` (`Update client for outage advisory links`).

## Implementation Summary

### 2026-06-04 WebUI Playwright Coverage

- Continued on existing `vpsadmin` branch
  `2026-05-29-security-advisories` per user request.
- Committed the Playwright coverage in `vpsadmin` as `022411302`
  (`webui: add security advisory browser coverage`).
- Added dedicated Playwright security advisory browser coverage:
  `tests/playwright/webui/specs/security-advisories.spec.cjs`.
- Added advisory page helper:
  `tests/playwright/webui/lib/pages/security-advisory.cjs`.
- Extended `tests/suite/webui.nix` to seed deterministic advisory fixtures:
  affected published, unaffected published, draft hidden, node status data, and
  deterministic UI-create values.
- Added `webui#security-advisories` script metadata and CI routing/tags in
  `tests/suite/webui.nix`, `tests/ci-tags.nix`, `tests/ci-selection.yml`, and
  `tests/ci-selection-test.rb`.
- Updated the shared Playwright auth helper to wait up to 60 seconds for the
  post-login WebUI redirect; local VM startup made the previous 20-second
  assertion flaky.
- Fixed advisory detail markup in `webui/forms/security_advisory.forms.php` by
  clearing stale XTemplate form context before rendering the updates table.
  Without this, the browser treated update delete forms as nested/invalid after
  the related-outage link form, so the delete form was absent from the DOM.
- Changed advisory confirm-form helper to register a one-shot dialog accept
  handler before clicking instead of waiting indefinitely for a dialog event.

Validation for this continuation:

- `nix shell nixpkgs#nodejs -c node --check
  tests/playwright/webui/specs/security-advisories.spec.cjs`
- `nix shell nixpkgs#nodejs -c node --check
  tests/playwright/webui/lib/pages/security-advisory.cjs`
- `nix shell nixpkgs#nodejs -c node --check
  tests/playwright/webui/lib/pages/auth.cjs`
- `php -l webui/forms/security_advisory.forms.php`
- `nix-instantiate --parse tests/suite/webui.nix >/tmp/webui-nix-parse.out`
- `ruby tests/ci-selection-test.rb`: 15 runs, 54 assertions, 0 failures,
  0 errors.
- `git diff --check`
- `./test-runner.sh test 'webui#security-advisories'`: passed on the final run,
  1 test script successful in 842.7 seconds.
- Commit hooks passed during commit `022411302`: Nixfmt, PhpCsFixer,
  RuboCop, SingleLineSubject, TrailingPeriod, and TextWidth.

Integration issues fixed during this continuation:

- Initial advisory test attempts exposed list-page heading assumptions and a
  missing update delete form caused by invalid nested forms.
- Update form state options did not include `published`; test now posts a
  normal update without selecting a non-existent state.
- A previous helper implementation could hang waiting for a dialog event; it
  now accepts a dialog if present and proceeds to the normal page assertions.
- Related outage row assertions now match rendered labels (`Unplanned outage`,
  `Performance`) and assert the date column format.

### 2026-06-04 Default-Branch Refresh And Dev Deploy

- Fetched `origin` with pruning for all task worktrees:
  `vpsadmin`, `vpsadmin-go-client`, `vpsf-status`, `vpsfree-irc-bot`,
  `vpsfree-mail-templates`, and `vpsfree-cz-configuration`.
- Compared each worktree against `origin/master`.
  - `vpsadmin`: `13 0`, no upstream commits missing, still at `022411302`.
  - `vpsadmin-go-client`: `3 0`, no upstream commits missing, still at
    `f3b308f`.
  - `vpsf-status`: `5 0`, no upstream commits missing, still at `e967791`.
  - `vpsfree-irc-bot`: `4 0`, no upstream commits missing, still at
    `48337bb`.
  - `vpsfree-mail-templates`: `3 0`, no upstream commits missing, still at
    `21e9c06`.
  - `vpsfree-cz-configuration`: initially `3 7`, then rebased cleanly onto
    current `origin/master`; post-rebase comparison is `3 0`, head
    `9dcd51bf`.
- `vpsfree-cz-configuration` still has local untracked tool directories
  `.bin/` and `.bundle/`; they were left untouched.
- Post-rebase check:
  - `git diff --check` passed in `vpsfree-cz-configuration`.
- Deployed the refreshed worktrees to the running dev cluster:
  - `dev-clusters/vpsadmin/bin/devcluster update
    2026-05-29-security-advisories services` completed successfully.
  - `devcluster status 2026-05-29-security-advisories` reports running,
    topology `single`, network `bridge`, and `ready: yes`.
  - HTTP probes returned 200 for:
    `https://webui.aitherdev.int.vpsfree.cz/`,
    `https://api.aitherdev.int.vpsfree.cz/v7.0/`, and
    `https://status.aitherdev.int.vpsfree.cz/`.
  - Services VM has no failed systemd units. Confirmed active:
    `rabbitmq.service`, `vpsadmin-api.service`,
    `vpsadmin-console-router.service`, `vpsadmin-supervisor.service`,
    `vpsadmin-scheduler.service`, `container@webui.service`, and
    `vpsf-status.service`.
  - Services VM root filesystem is tight but usable: 4.8 GiB size, 4.1 GiB
    used, 420 MiB available, 91% used.
  - `node1` at `172.16.106.41` has `nodectld` running, and `nodectl status`
    reports `State: running`.

### 2026-06-04 Feature Branch History Cleanup

- Created local backup branches before rewriting:
  `backup/2026-05-29-security-advisories-pre-cleanup`.
  - `vpsadmin`: backup `022411302`, rewritten head `25bb83266`.
  - `vpsadmin-go-client`: backup `f3b308f`, rewritten head `1d9240f`.
  - `vpsf-status`: backup `e967791`, rewritten head `0e67673`.
  - `vpsfree-irc-bot`: backup `48337bb`, rewritten head `a7393bb`.
  - `vpsfree-mail-templates`: backup `21e9c06`, rewritten head `22e7393`.
  - `vpsfree-cz-configuration`: backup and head both `9dcd51bf`; no cleanup
    was applied there per user preference.
- Rewrote `vpsadmin` history while preserving the final tree:
  - Squashed advisory update-shape simplification into the main advisory
    feature commit.
  - Squashed the outage metric regression spec into the outage metric fix.
  - Squashed the MySQL charset follow-up and the order-dependent
    `add_route_spec` fixture isolation into the local-MariaDB CI commit.
  - Kept plugin migration helper fix, nodectld startup-race fix, and generated
    nodectld gem rebuild separate.
  - Combined outage/advisory linking commits, including direct join-resource
    use, reliable linked-advisory filtering, and the WebUI form-context fix.
  - Split shared Playwright login timeout into
    `207194501` (`tests: allow slower WebUI login redirects`).
  - Kept advisory Playwright coverage as `25bb83266`
    (`webui: add security advisory browser coverage`).
- Rewrote related repositories while preserving final trees:
  - `vpsadmin-go-client`: one generated-client commit `1d9240f`.
  - `vpsf-status`: one feature commit `0e67673`.
  - `vpsfree-irc-bot`: one feature commit `a7393bb`.
  - `vpsfree-mail-templates`: advisory templates commit `67142f4` plus outage
    report advisory-CVE template commit `22e7393`.
- Tree comparisons against the backup branches returned no differences in all
  rewritten repos.
- Commit hooks passed during rewritten commits:
  - `vpsadmin`: Overcommit Nixfmt, PhpCsFixer, RuboCop, SingleLineSubject,
    TrailingPeriod, and TextWidth.
  - `vpsf-status`: Lefthook `gofmt`.

### 2026-06-04 Push And GitHub Workflow Watch

- Force-pushed cleaned task branches:
  - `vpsadmin-go-client` `1d9240f`.
  - `vpsf-status` `0e67673`.
  - `vpsfree-irc-bot` `a7393bb`.
  - `vpsfree-mail-templates` `22e7393`.
  - `vpsfree-cz-configuration` `9dcd51bf`.
  - `vpsadmin` first `792a5d7d0`, then `f2528f112`, then final
    `25bb83266` after API Specs CI fixes were autosquashed.
- First `vpsadmin` API Specs run on `792a5d7d0` failed endpoint coverage
  because `api/spec/api/covered_endpoints.yml` still used stale nested
  `outage.security_advisory` endpoint names and missed
  `outage_security_advisory#show`.
- Fixed the coverage manifest, verified locally with:
  `nix develop .#api -c 'bundle exec rspec spec/api/endpoint_coverage_spec.rb
  spec/api/plugins/outage_reports/security_advisory_spec.rb --format progress'`.
- Second `vpsadmin` API Specs run on `f2528f112` passed coverage but failed
  `API specs (full) - engine` in
  `spec/models/transaction_chains/network_interface/add_route_spec.rb` with
  `Validation failed: Ip addr has already been taken`.
- Reproduced the engine shard locally with seed `31437`, then isolated
  `add_route_spec` route IPs in an example-local private VPS network and
  autosquashed that into `ce4dccac0` (`ci: run API specs with local MariaDB`).
- Local verification after the fixture fix:
  - `bundle exec rspec
    spec/models/transaction_chains/network_interface/add_route_spec.rb --seed
    31437 --format progress`: 1 example, 0 failures.
  - Engine shard equivalent:
    `find spec/models -name "*_spec.rb" | sort >
    tmp/rspec-files-engine-local.txt; xargs -a
    tmp/rspec-files-engine-local.txt bundle exec rspec --seed 31437 --format
    progress`: 735 examples, 0 failures, 3 pending.
- GitHub workflow status for current pushed heads:
  - `vpsf-status` Integration Tests `26937152802`: success.
  - `vpsfree-irc-bot` RSpec `26937153609`: success.
  - `vpsfree-irc-bot` Integration Tests `26937153620`: success.
  - `vpsadmin` RuboCop `26939004328`: success.
  - `vpsadmin` Webui PHPUnit `26939004322`: success.
  - `vpsadmin` libnodectld Specs `26939004310`: success.
  - `vpsadmin` API Specs `26939004324`: success.
  - `vpsadmin` CI `26939004499`: in progress at last update, still in
    `Run tests`.
  - `vpsfree-irc-bot`: Overcommit RuboCop, SingleLineSubject,
    TrailingPeriod, and TextWidth.
- After the final `vpsadmin` force-push, older CI runs on the same feature
  branch remained in progress at obsolete SHAs:
  - `26937799253` at `f2528f112`.
  - `26937202106` at `792a5d7d0`.
  `gh run cancel` was attempted for both after the user refreshed `gh`
  credentials, but GitHub still returned HTTP 403 `Resource not accessible by
  personal access token`. No workflows on other branches were touched.
- Local reproduction of the selector for the final force-push diff from
  `f2528f112` to `25bb83266` produced `mode=skip`, because only
  `api/spec/models/transaction_chains/network_interface/add_route_spec.rb`
  changed between those trees. The current GitHub CI run is nevertheless in
  its integration `Run tests` step, probably because the runner could not use
  the forced-out previous SHA and fell back to a broader branch-vs-master
  selection.
- `vpsadmin` CI run `26939004499` later failed only in the integration `webui`
  group. The dedicated `webui#security-advisories` script passed, but later
  VPS scripts failed during container creation with osctld reporting
  `error: user not found` for `ct create --user "2"`.
- Root cause: `prepare_webui_storage_runtime` created raw osctl containers for
  the storage browser fixtures without using the database fixture's user
  namespace map. osctl created users named after container IDs `16` through
  `27`; after nodectld restarted, it saw API VPS rows with
  `user_namespace_map_id=2` and cached map `2` as already present, so later
  WebUI VPS create flows skipped `osctl user new 2` and failed at
  `ct create --user 2`.
- Fixed `tests/suite/webui.nix` so storage fixture JSON includes
  `userNamespaceMapId`, `uidMap`, and `gidMap` for each fixture VPS. The
  storage runtime setup now creates the matching osctl user with the map data
  and passes `--user "$userns_map_id"` to `osctl ct new`.
- Committed the fix as vpsAdmin `3bd7a190e`:
  `tests: create WebUI storage fixtures with user namespaces`.
- No `vpsfree-cz-configuration` input bump was made for this test-only
  vpsAdmin fix. The running dev cluster builds vpsAdmin from the local
  `worktrees/2026-05-29-security-advisories/vpsadmin` path via
  `dev-clusters/vpsadmin/bin/devcluster` flake input overrides, so a cluster
  update picks up the new commit without changing `vpsadminServices`.
- Local verification for the WebUI fixture fix:
  - `nix-instantiate --parse tests/suite/webui.nix`.
  - `git diff --check`.
  - `./test-runner.sh test -f 'webui#storage-backup-export'`: passed. The
    Playwright example reported 2 tests passed in 4.9 minutes; the script
    finished in 759.33 seconds and the outer `webui` test in 1192.86 seconds.
- Pushed vpsAdmin `3bd7a190e` to
  `origin/2026-05-29-security-advisories`.
- GitHub Actions after push:
  - New vpsAdmin CI run `26949629281` queued for `3bd7a190e`.
  - Older vpsAdmin CI run `26937202106` was still in progress at old SHA
    `792a5d7d0` on the same branch. A second `gh run cancel` attempt still
    returned HTTP 403 `Resource not accessible by personal access token`, so
    it was left running. No workflows on other branches were touched.
  - `gh api -X POST .../actions/runs/26937202106/force-cancel` also returned
    HTTP 403 with `X-Accepted-GitHub-Permissions: actions=write`.
  - Listing self-hosted runners also returned HTTP 403 with
    `X-Accepted-GitHub-Permissions: administration=read`.
  - The branch-head run `26949629281` remains queued in GitHub metadata while
    the obsolete same-branch run `26937202106` remains `in_progress` with no
    runner name and no update since 2026-06-04 07:33 UTC.
- Deployed the new vpsAdmin worktree to the running dev cluster with
  `dev-clusters/vpsadmin/bin/devcluster update
  2026-05-29-security-advisories services`; it completed successfully.
- Post-deploy checks:
  - `devcluster status 2026-05-29-security-advisories`: running, topology
    `single`, network `bridge`, `ready: yes`.
  - Services VM has no failed systemd units.
  - `rabbitmq.service`, `vpsadmin-api.service`,
    `vpsadmin-console-router.service`, `vpsadmin-supervisor.service`,
    `vpsadmin-scheduler.service`, `container@webui.service`, and
    `vpsf-status.service` are active.
  - Services root filesystem is tight but usable: 4.8 GiB size, 4.2 GiB used,
    287 MiB available, 94% used.
  - `node1` `nodectl status` reports `State: running`.
  - HTTP probes returned 200 for
    `https://webui.aitherdev.int.vpsfree.cz/`,
    `https://api.aitherdev.int.vpsfree.cz/v7.0/`, and
    `https://status.aitherdev.int.vpsfree.cz/`.
- Validation after cleanup:
  - `vpsadmin`: `php -l webui/forms/security_advisory.forms.php`;
    `node --check` for touched Playwright JS files;
    `ruby tests/ci-selection-test.rb`; `git diff --check`.
  - `vpsadmin-go-client`: `CGO_ENABLED=0 go test ./...`; `git diff --check`.
  - `vpsf-status`: `CGO_ENABLED=0 go test ./...`; `git diff --check`.
  - `vpsfree-irc-bot`: `nix develop -c bundle exec rspec`;
    `git diff --check`.
  - `vpsfree-mail-templates`: ERB parse check through `nix develop`;
    `git diff --check`.
  - `vpsfree-cz-configuration`: `git diff --check`.
  - `./test-runner.sh test 'webui#security-advisories'`: passed; the example
    succeeded in 147.37 seconds, the script in 473.33 seconds, and the outer
    `webui` test in 737.14 seconds.

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
  - Replaced the temporary nested `/outages/:id/security_advisories` API with
    top-level `outage_security_advisory#index/show/create/delete`, backed by
    the `OutageSecurityAdvisory` join model. WebUI outage and advisory pages
    now create/delete join rows directly, so advisory details can always render
    the unlink action from the link row.
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
- vpsAdmin clean outage/advisory link API follow-up on 2026-06-03:
  - `ruby -c` for changed outage advisory Ruby files and plugin spec passed.
  - `php -l` for changed outage/advisory WebUI PHP files passed.
  - `git diff --check` passed.
  - `nix develop .#api -c bash -lc 'bundle exec rspec
    spec/api/plugins/outage_reports/security_advisory_spec.rb'`: 6 examples,
    0 failures.
  - `nix develop .#api -c bash -lc 'bundle exec rspec
    spec/api/plugins/outage_reports/outage_spec.rb
    spec/api/plugins/outage_reports/security_advisory_spec.rb'`: 61 examples,
    0 failures.
  - `nix develop -c bundle exec overcommit --run pre_commit`: Nixfmt,
    RuboCop, and PhpCsFixer passed.
  - Commit hooks passed during commit `33c9e0cf2`.
  - Integration tests were not run per user request.
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
  - Follow-up for GitHub Actions run `26882093251`:
    - `nix develop .#libnodectld --command bundle exec rspec
      spec/nodectld/pool_status_spec.rb`: 2 examples, 0 failures.
    - `nix develop .#libnodectld --command bundle exec rspec`: 389 examples,
      0 failures.
    - `nix-instantiate --parse tests/suite/storage/remote-common.nix` passed.
    - `nix develop .#libnodectld --command bundle exec ruby -c
      lib/nodectld/pool_status.rb`: syntax OK.
    - `nix develop .#libnodectld --command bundle exec ruby -c
      spec/nodectld/pool_status_spec.rb`: syntax OK.
    - `nix develop --command rake vpsadmin:gems` rebuilt and pushed
      `libnodectld`, `nodectl`, and `nodectld`
      `4.1.0.build20260603174938`.
    - `nix build --impure --expr 'let flake = builtins.getFlake
      "path:/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-05-29-security-advisories/vpsadmin";
      system = "x86_64-linux"; pkgs = import flake.inputs.nixpkgs {
      inherit system; overlays = [ flake.overlays.default ]; }; in [
      pkgs.libnodectld pkgs.nodectl pkgs.nodectld ]' --no-link` passed.
    - `bundle exec rubocop` is not available in the `.#libnodectld` bundle or
      as a standalone command in that dev shell; Overcommit RuboCop hooks ran
      successfully during commits instead.
- `vpsadmin-go-client`:
  - `gofmt -w client`
  - `CGO_ENABLED=0 go test ./...` passed; rerun after final checks also
    passed.
  - For the outage/advisory link API follow-up, regenerated against a temporary
    local vpsAdmin API server at `http://127.0.0.1:19292`; the server and
    persistent test DB were stopped afterwards.
  - `go fmt ./...` passed.
  - `CGO_ENABLED=0 go test ./...` passed.
- `vpsf-status`:
  - `CGO_ENABLED=0 go test ./...` passed; rerun after final checks also
    passed.
  - Plain `go test ./...` failed in this environment because cgo/gcc was not
    available.
  - For the outage/advisory link API follow-up, `CGO_ENABLED=0 go test ./...`
    passed with no source changes.
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
  - `vpsadmin`: `d4f9347e5` `api: add security advisories`; rebased onto
    `origin/master` at `d832189df`.
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
  - `vpsadmin`: after rebasing, focused core
    advisory/schema/mail-template specs passed against temporary MariaDB:
    28 examples, 0 failures. The outage_reports advisory plugin spec passed:
    3 examples, 0 failures. Targeted RuboCop on changed advisory/spec files
    passed before the rebase.
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
- `vpsf-status` CI lock correction on 2026-06-02:
  - GitHub Actions integration run `26849211273` failed while creating
    security advisory fixtures because the test VM was still locked to an
    older upstream `vpsadmin` revision without the `SecurityAdvisory` model.
  - Updated `flake.lock` to pin the `vpsadmin` input to the pushed feature
    commit `d4f9347e5d02dd9b4da5934e0ae9f4e18a38d71d`.
  - Committed and pushed `8429038`:
    `status: test security advisories against feature API`.
  - Validation before push: `CGO_ENABLED=0 go test ./...`, `nix build
    .#vpsf-status --no-link`, and
    `nix develop --command lefthook run pre-commit --all-files` passed.
    The commit was amended inside `nix develop` so the repository Git hook
    could run with `lefthook` available in `PATH`.
- GitHub Actions follow-up fixes on 2026-06-02:
  - `vpsadmin` API Specs failed in run `26849230234` because outage metrics
    still called dynamic translated summary methods such as `cs_summary`.
    After plugin tables were removed from the core schema, those methods are
    no longer reliable in schema-built plugin specs.
  - Fixed outage metrics to preload `outage_translations` and read summaries
    from the association, emitting an empty label for languages without a
    translation. Committed and pushed `2be7c47f0`
    `api: read outage metric summaries from translations`.
  - Added regression coverage for the empty untranslated label and pushed
    `ae25ee388` `api: cover untranslated outage metric labels`.
  - Focused validation:
    `ruby -c plugins/outage_reports/api/lib/vpsadmin/api/plugins/outage_reports/metrics.rb`;
    `nix develop .#api --command bundle exec rubocop
    ../plugins/outage_reports/api/lib/vpsadmin/api/plugins/outage_reports/metrics.rb
    spec/lib/vpsadmin/api/plugins/outage_reports/metrics_spec.rb`;
    `nix develop .#api --command bundle exec rspec
    spec/lib/vpsadmin/api/plugins/outage_reports/metrics_spec.rb --format
    progress` with `VPSADMIN_PLUGINS=all` and the temporary MariaDB socket.
  - A later API Specs run `26849986086` failed before running specs because
    the `routes` topic could not pull `mariadb:latest` from Docker Hub. The
    token available locally could not rerun the failed workflow, so the small
    regression-test commit above was used to trigger a fresh run.
  - The next API Specs run `26850575631` hit the same Docker Hub pull timeout.
    Removed the workflow-level MariaDB Docker services and let API Specs use
    the repository's local MariaDB fallback from `tools/test_db.rb`, adding
    `mariadb-server` to the workflow package list. Committed and pushed
    `bcf95b723` `ci: run API specs with local MariaDB`.
  - API Specs run `26851113030` then reached the specs but failed because the
    local MariaDB database was created with the server default `utf8mb4`
    charset, while the schema still declares `utf8mb3` collations. Updated the
    local test database URL and MySQL database creation helpers to set
    `utf8mb3`/`utf8mb3_unicode_ci` explicitly. Committed and pushed
    `3018becf4` `ci: preserve MySQL charset in API specs`.
  - Validation before pushing `3018becf4`: `ruby -c tools/test_db.rb`;
    `ruby -c api/spec/support/db_setup.rb`;
    `nix develop .#api --command bash -lc 'bundle exec rubocop
    ../tools/test_db.rb spec/support/db_setup.rb'`; auto-DB smoke
    `VPSADMIN_PLUGINS=none bundle exec rspec
    spec/smoke/core_schema_spec.rb --format progress` with 2 examples,
    0 failures; focused auto-DB smoke `VPSADMIN_PLUGINS=none bundle exec
    rspec spec/smoke/auth_smoke_spec.rb spec/smoke/stability_spec.rb --format
    progress` with 5 examples, 0 failures.
  - GitHub Actions after pushing `3018becf4`: API Specs run `26851584495`,
    libnodectld Specs run `26851584493`, CI run `26851584492`, and RuboCop
    run `26851584494` started. Older vpsAdmin CI runs `26849986084` and
    `26849230214` were still in progress and are being monitored even though
    they predate the current branch head.
  - Final vpsAdmin workflow results on 2026-06-03:
    - Current branch head `3018becf4` passed all workflows:
      API Specs `26851584495`, RuboCop `26851584494`, libnodectld Specs
      `26851584493`, and CI `26851584492`.
    - Superseded CI run `26849230214` for initial commit `d4f9347e5` passed
      after 3h51m.
    - Superseded CI run `26849986084` for commit `2be7c47f0` failed after
      3h08m in the WebUI VPS Playwright group: VPS create transaction chains
      failed at progress 0 in `vps-user-ops`, `vps-admin-ops`,
      `vps-user-core`, `vps-lifecycle`, and `vps-admin-core`. The same CI
      workflow passed on the current branch head, so no remaining head failure
      was left to fix.
  - `vpsfree-irc-bot` integration run `26849211188` failed because the test VM
    was locked to a vpsAdmin revision without `SecurityAdvisory` models.
    Updated `flake.lock` to vpsAdmin `2be7c47f0`, committed and pushed
    `7e76325` `bot: test advisory events against feature API`.
  - IRC bot validation: `nix develop --command bundle exec rspec` passed
    `39 examples, 0 failures`; `./test-runner.sh test -f vpsadmin-events`
    passed all 6 examples, including both security-advisory examples, in
    487.18 seconds.
  - `vpsf-status` was also aligned to vpsAdmin `2be7c47f0`, committed and
    pushed `5ed2ba1` `status: align vpsadmin feature input`.
  - Status-page validation: `CGO_ENABLED=0 go test ./...`, `nix build
    .#vpsf-status --no-link`, and
    `nix develop --command lefthook run pre-commit --all-files` passed.
  - Final cross-repository workflow status on 2026-06-03:
    - `vpsf-status` latest integration run `26850459760` passed.
    - `vpsfree-irc-bot` latest RSpec run `26850464628` and integration run
      `26850464621` passed.
    - All affected worktrees were clean except `vpsfree-cz-configuration`,
      which still had the known local untracked `.bin/` and `.bundle/`
      directories.
- Dev cluster authentication failure on 2026-06-03:
  - Symptom: browser login reported the webui OAuth callback error
    `vpsAdmin was unable to obtain access token from the authorization
    server`. A previous curl reproduction for `test-user1` left an
    `oauth2_authorizations` row with `user_session_id = NULL`, consistent
    with callback/token state not being persisted.
  - Root cause: after adding `vpsf-status` to the dev cluster, its built-in
    vpsAdmin webui HTTP probe used `HEAD /` every 5 seconds. The PHP webui
    starts a session at the top of `public/index.php` and stores the full API
    description in `$_SESSION`, so anonymous probes created 2.6 MiB session
    files. `/run/vpsadmin-webui-sessions` grew to 1.6 GiB with 728 files and
    filled the webui container `/run` tmpfs to 100%, preventing reliable
    OAuth state/PKCE verifier writes.
  - Immediate recovery: removed generated session files from
    `/run/vpsadmin-webui-sessions` in the webui container. `/run` dropped
    from 100% used to 1% used.
  - Superseded workaround: briefly extended `vpsf-status` with separate check
    URLs and configured the dev cluster to probe the webui favicon. This was
    removed before commit, because the index page is the important service
    check.
  - Durable fix: dev-cluster `vpsf-status` probes the webui index page every
    30 seconds, matching production. The webui container has a dedicated
    systemd timer that prunes PHP session files older than 60 minutes from
    `/run/vpsadmin-webui-sessions`, matching the configured PHP session
    lifetime.
  - Final validation: deployed with
    `dev-clusters/vpsadmin/bin/devcluster update
    2026-05-29-security-advisories services`. `vpsf-status` config has
    `check_interval = 30` and no separate webui check URL. HAProxy logs show
    `HEAD /` every 30 seconds and no new favicon probes after the switch. The
    webui container has `vpsadmin-webui-prune-sessions.timer` active; a
    synthetic two-hour-old `sess_*` file was deleted by
    `vpsadmin-webui-prune-sessions.service`; the first scheduled timer run
    also completed successfully. `/run` was 26 MiB used out of 1.6 GiB with
    11 session files. Fresh OAuth logins passed for `test-admin`
    (`?page=cluster`) and `test-user1` (`?page=`).
- Security advisory update text simplification on 2026-06-03:
  - Simplified advisory updates from `summary`, `description`, and `response`
    to `summary` plus optional `message`. Main advisory text fields remain
    `summary`, `description`, and `response`.
  - Updated vpsAdmin API resources, model translation helpers, built-in mail
    templates, WebUI forms/detail rendering, and specs. Update create/edit now
    requires per-language summaries and accepts optional per-language messages.
  - Added admin WebUI actions to edit and delete advisory updates. Delete has
    confirmation and update translation rows are deleted with the update.
  - Fixed direct admin update deletion coverage to assert no orphaned
    `security_advisory_translations` remain. Changed
    `SecurityAdvisory` update cleanup to `dependent: :destroy` so update
    callbacks are honored if an advisory is destroyed later.
  - Fixed `vpsadmin:plugins:status` and `vpsadmin:plugins:rollback`
    compatibility with ActiveRecord 8 while testing the dev-cluster migration
    path. `status` now uses `connection.pool.schema_migration`; rollback no
    longer references a stale undefined variable.
  - Updated `vpsfree-mail-templates` advisory update templates to render only
    optional update message text after the summary.
  - Updated the IRC bot integration fixture to create update translations with
    `message` instead of `description`/`response`; runtime bot code did not
    need a change because update announcements use the summary.
  - Regenerated `vpsadmin-go-client` from the local vpsAdmin API using the
    HaveAPI 0.28 generator. The generated update resource now exposes
    `en_message`/`cs_message` and show/update/delete actions. The new
    generated action files are staged so Nix flake source filtering can see
    them during local dev-cluster builds.
  - Updated `vpsf-status` Nix package hash for the regenerated local Go
    client; no status-page source change was needed for this text-field
    simplification.
  - Validation:
    - `ruby -c` for changed Ruby files in advisory update resources/models,
      plugin migration helpers, and advisory specs.
    - `php -l` for changed WebUI security advisory page/forms.
    - ERB compilation for vpsAdmin built-in advisory update templates and
      production `vpsfree-mail-templates` advisory update templates.
    - `VPSADMIN_PLUGINS=none bundle exec rspec
      spec/api/resources/security_advisory_spec.rb`: 17 examples, 0 failures.
    - `bundle exec rubocop` on changed advisory and plugin task Ruby files:
      no offenses.
    - `CGO_ENABLED=0 go test ./...` in `vpsadmin-go-client` and
      `vpsf-status`: passed.
    - `nix build --impure --expr ...` for `vpsf-status` with sibling local
      generated client: passed after the package hash update.
    - `nix develop --command bundle exec rspec` in `vpsfree-irc-bot`:
      39 examples, 0 failures.
    - `nix-instantiate --parse tests/suite/vpsadmin-events.nix`: passed.
    - After pushing the advisory update `message` field change, GitHub
      integration failed in `vpsfree-irc-bot` because its `vpsadmin` flake
      input was still pinned to `2be7c47f0`, whose
      `SecurityAdvisoryTranslation` schema did not have `message`.
      Updated the lock to vpsAdmin `c0aef236e` and reran
      `./test-runner.sh test -f vpsadmin-events`: 6 examples, 0 failures.
    - `git diff --check` passed in `vpsadmin`, `vpsadmin-go-client`,
      `vpsf-status`, `vpsfree-mail-templates`, and `vpsfree-irc-bot`.
  - Dev cluster migration/deploy:
    - Stopped vpsAdmin API/scheduler/supervisor/status services on the
      services VM and rolled back the old deployed advisory schema. The
      outage/advisory plugin join table was dropped manually because the old
      plugin rollback/status task was not ActiveRecord 8-compatible; then the
      core migration `20260601120000` was reverted with
      `db:migrate:down VERSION=20260601120000`.
    - Re-ran `dev-clusters/vpsadmin/bin/devcluster update
      2026-05-29-security-advisories services`. The first switch applied the
      new migration successfully, but exited non-zero because a temporary
      HaveAPI generator worktree caused a new `/mnt/haveapi` mount in the
      already-running VM. Removed and pruned that support worktree, then
      re-ran the services update to remove the stale mount.
    - Ran one final services update after the plugin task helper fix.
    - Final dev-cluster checks: no failed systemd units; `vpsadmin-api`,
      `vpsadmin-database-setup`, `vpsf-status`, `container@webui`, and
      `nginx` active; `vpsadmin-devcluster-seed` inactive as expected for a
      completed oneshot.
    - Dev database has schema migration rows `20260601120000` and
      `20260601121000-outage_reports`. `security_advisory_translations` has
      `summary`, `description`, `response`, and `message`, and no longer has
      the old `title` column.
    - `vpsadmin:plugins:status PLUGIN=outage_reports` works on the services
      VM and shows `20260601121000 Add outage security advisories` as up.
    - HTTP smoke checks returned 200 for
      `https://webui.aitherdev.int.vpsfree.cz/`,
      `https://status.aitherdev.int.vpsfree.cz/`, and
      `https://api.aitherdev.int.vpsfree.cz/v7.0/`.
    - API `OPTIONS /v7.0/security_advisory_updates` exposes `en_summary` and
      `en_message`, with no `en_description` or `en_response`.
  - Removed the temporary HaveAPI generator worktree after client generation
    and deployment; only the bare `repos/haveapi.git` remains.
  - Upstream/rebase and push status:
    - Fetched affected upstream repositories on 2026-06-03. All affected
      feature branches contain their `origin/master` heads; no additional
      rebase was needed after the final IRC bot lockfile commit. Earlier in
      the same push cycle, vpsAdmin was rebased onto moved `origin/master`
      and force-pushed.
    - Pushed vpsAdmin `2026-05-29-security-advisories` at `c0aef236e`.
    - Pushed vpsadmin-go-client at `7df45c3`.
    - Pushed vpsf-status at `c860b3e`.
    - Pushed vpsfree-mail-templates at `f143a3f`.
    - Pushed vpsfree-irc-bot at `48337bb`.
  - GitHub workflow status after push:
    - vpsAdmin API Specs, RuboCop, Webui PHPUnit, and libnodectld Specs are
      green for `c0aef236e`.
    - vpsf-status Integration Tests are green for `c860b3e`.
    - vpsfree-irc-bot RSpec and Integration Tests are running for `48337bb`.
    - vpsAdmin CI is still running for `c0aef236e`.

- 2026-06-03 outage/security advisory link follow-up:
  - Implemented WebUI changes:
    - Outage detail now shows linked advisory CVEs above `Handled by`, including
      advisory names and admin unlink controls.
    - Outage `Link security advisory` form now supports selecting multiple
      advisories and skips already linked advisories.
    - Security advisory detail now has an admin `Link outage` form accepting an
      outage ID, unlink controls, and related outage type/impact columns.
  - Implemented outage mail changes:
    - Outage mail chain now passes `security_advisory_cves` and `webui_url`.
    - vpsAdmin built-in outage announcement templates and
      `vpsfree-mail-templates` outage announcement templates now include linked
      CVEs/advisory names and the vpsAdmin outage detail URL.
  - Validation:
    - `php -l` passed for changed WebUI outage/security advisory files.
    - `ruby -c` passed for changed outage mail chain, plugin metadata, and spec
      files.
    - ERB compilation passed for changed vpsAdmin built-in and
      `vpsfree-mail-templates` outage announcement templates.
    - `nix develop .#api --command bundle exec rubocop` passed on changed Ruby
      files.
    - `nix develop .#api --command bundle exec rspec
      spec/models/transaction_chains/plugins/outage_reports/update_spec.rb
      spec/api/plugins/outage_reports/security_advisory_spec.rb --format
      progress`: 6 examples, 0 failures.
    - `git diff --check` passed in `vpsadmin` and `vpsfree-mail-templates`.
  - Dev cluster deployment:
    - Ran `dev-clusters/vpsadmin/bin/devcluster update
      2026-05-29-security-advisories services`; it completed successfully.
    - `devcluster status` reports the bridge cluster running and ready.
    - Direct service checks show no failed systemd units and
      `vpsadmin-api.service`, `container@webui.service`,
      `vpsadmin-supervisor.service`, and `vpsf-status.service` active.
    - HTTP checks returned 200 for `https://webui.aitherdev.int.vpsfree.cz/`
      and `https://api.aitherdev.int.vpsfree.cz/v7.0/`.
    - Deployed API rollback-only smoke script created two advisory links,
      unlinked both, verified link counts, and rolled back.
    - Deployed mail template database check confirmed
      `outage_report_user_announce` and `outage_report_generic_announce`
      include CVE text and outage detail links.

- 2026-06-03 advisory/outage WebUI action follow-up:
  - Planned and implemented a WebUI-only follow-up after admin testing:
    - Local vpsAdmin commit after squash: `bb36cedf8`
      (`outage_reports: improve advisory links`).
    - Security advisory `Related outages` rows now use the standard details
      icon instead of a text `Show` link.
    - Admins can unlink related outages from the advisory detail table with the
      same inline unlink action used on outage details.
    - Transaction log concern rendering now handles `SecurityAdvisory` in both
      PHP and the live JavaScript sidebar updater, linking to advisory details.
  - Validation:
    - `php -l webui/forms/security_advisory.forms.php` passed.
    - `php -l webui/lib/functions.lib.php` passed.
    - `nix shell nixpkgs#nodejs --command node --check
      webui/public/js/transaction-chains.js` passed. The repository's
      `.#webui` shell does not include `node`.
    - `git diff --check` passed in `vpsadmin` and for this state file.
    - Deployed with `dev-clusters/vpsadmin/bin/devcluster update
      2026-05-29-security-advisories services`. The switch initially failed
      because the services VM root filesystem was full while recreating
      vpsAdmin config symlinks. Ran `nix-collect-garbage -d` inside the VM,
      restarted the failed vpsAdmin units, restarted RabbitMQ after it lost
      its user/vhost process state, reran/verified RabbitMQ user provisioning,
      restored the initialized marker, and cleared failed units.
    - Final dev-cluster checks: cluster running/ready; no failed systemd units;
      `rabbitmq`, `vpsadmin-api`, `vpsadmin-console-router`,
      `vpsadmin-supervisor`, `vpsadmin-scheduler`, `container@webui`, and
      `vpsf-status` active; root filesystem 85% used with about 700 MiB free.
    - HTTP checks returned 200 for
      `https://webui.aitherdev.int.vpsfree.cz/` and
      `https://api.aitherdev.int.vpsfree.cz/v7.0/`.
    - Rendered advisory detail page
      `?page=security_advisory&action=show&id=1` shows the related outage
      details icon linking to `?page=outage&action=show&id=1`, with no text
      `Show` link.
    - Verified `transaction_concern_class("SecurityAdvisory")` and
      `transaction_concern_link("SecurityAdvisory", 1)` output the readable
      label and advisory detail link. The served `transaction-chains.js`
      contains the same `SecurityAdvisory` mapping for live sidebar updates.

- 2026-06-04 post-push default-branch refresh and squash review:
  - Fetched `origin` with pruning for all six task repositories.
  - Default branches advanced in `vpsadmin` and `vpsfree-cz-configuration`.
    Created local backups before rebasing:
    - `vpsadmin`:
      `backup/2026-05-29-security-advisories-pre-default-rebase-20260604-122953`
      at `3bd7a190e`.
    - `vpsfree-cz-configuration`:
      `backup/2026-05-29-security-advisories-pre-default-rebase-20260604-122953`
      at `9dcd51bf`.
  - `vpsadmin` rebase initially stopped because the Overcommit hook
    configuration signature was stale after fetching the new default branch.
    Ran `nix develop --command overcommit --sign`, then rebased cleanly onto
    `origin/master`; new local head is `597848686`.
  - `vpsfree-cz-configuration` rebased cleanly onto `origin/master`; new local
    head is `e8e90c94`. Existing untracked `.bin/` and `.bundle/` directories
    remain untouched.
  - `vpsadmin-go-client`, `vpsf-status`, `vpsfree-irc-bot`, and
    `vpsfree-mail-templates` were already based on current `origin/master` and
    were not rebased.
  - `git diff --check origin/master..HEAD` passed in `vpsadmin` and
    `vpsfree-cz-configuration`.
  - Squash review notes:
    - Keep `tests: allow slower WebUI login redirects` separate; it is the
      shared Playwright login helper change split out from the advisory browser
      coverage.
    - Consider moving the XTemplate form-context clearing hunk from
      `outage_reports: improve advisory links` into the original advisory UI
      commit if the history is rewritten.
    - Consider squashing `api: read outage metric summaries from translations`
      into the initial advisory API commit if treating it as fallout from the
      new plugin schema tests; otherwise it is also defensible as a small
      standalone outage metrics fix.
    - Keep `nodectld: avoid pool status startup race` and
      `packages: update nodectld gems` separate, because the gem rebuild is
      intentionally isolated.
    - No squash needed in `vpsfree-cz-configuration` per user preference.
  - Merged the feature branches into default branches using temporary detached
    worktrees under `worktrees/2026-05-29-security-advisories-merge` and
    fast-forward-only merges, then pushed:
    - `vpsadmin` `master` to `597848686`. The default branch later advanced to
      `21fe7e24e` by another upstream commit; `597848686` remains an ancestor.
    - `vpsadmin-go-client` `master` to `1d9240f`.
    - `vpsf-status` `master` to `0e67673`, then force-updated to
      `ee9afa9` after fixing the generated-client dependency described below.
    - `vpsfree-irc-bot` `master` to `a7393bb`.
    - `vpsfree-mail-templates` `master` to `22e7393`.
    - `vpsfree-cz-configuration` `master` to `e8e90c94`.
    - Follow-up after review: `vpsfree-cz-configuration` `master` to
      `a25d799c`, including:
      - `517faac2`: update the `vpsadmin` channel's `vpsadminServices` input
        to exact vpsAdmin revision
        `5978486864a57fdc94aaa7fae6a74813e76c3d63`.
      - `34db3522`: update the `vpsf-status` channel's `vpsfStatus` input to
        amended vpsf-status revision
        `ee9afa95a77c09efbf366bcf09d17857f54ea48d`.
      - `a25d799c`: update the packaged `vpsfree-irc-bot` source to
        `a7393bbe514958ad76ccd5ba86406b0270511297`.
  - `git diff --check origin/master..HEAD` passed in all six merge worktrees
    before pushing.
  - Push notes:
    - `vpsadmin` push needed `nix develop --command overcommit --sign` in the
      temporary worktree, then `nix develop --command git push origin
      HEAD:master`, because the ambient shell failed the Overcommit signature
      check.
    - `vpsfree-cz-configuration` push needed `nix develop --command git push
      origin HEAD:master`, because the ambient shell could not load the
      repository's Overcommit bundle.
    - The follow-up `vpsadminServices` pin was created by
      `confctl inputs channel set --commit vpsadmin vpsadmin
      5978486864a57fdc94aaa7fae6a74813e76c3d63` after signing the updated
      Overcommit pre-commit plugin signature. A locally created manual commit
      with misformatted changelog markers was reset before rerunning
      `confctl`; only the `confctl`-created commit was pushed.
    - `vpsf-status` initially still depended on old generated client commit
      `4c74d697`, which existed only on a local backup branch after cleanup.
      Updated `go.mod`/`go.sum` to merged generated client `1d9240f`, updated
      the normal `nix/package.nix` vendor hash, amended the vpsf-status feature
      commit, and force-pushed `vpsf-status` `master` and feature branch to
      `ee9afa9`.
    - The follow-up `vpsfStatus` configuration pin was created by
      `confctl inputs channel set --commit vpsf-status vpsf-status
      ee9afa95a77c09efbf366bcf09d17857f54ea48d`.
    - `vpsfree-irc-bot` has no `confctl` channel; it is packaged from
      `packages/vpsfree-irc-bot/default.nix`. Updated that package source to
      `a7393bbe514958ad76ccd5ba86406b0270511297` with prefetched hash
      `sha256-IZD80aV9Dq8mgPxqqJKA6fpuJ8hQyEoSRyn0uyIny1A=`.
    - GitHub printed existing Dependabot vulnerability notices for
      `vpsfree-irc-bot` and `vpsfree-cz-configuration`.
  - Removed the temporary merge worktrees. The configuration temporary worktree
    was force-removed after confirming only `.bin/` and `.bundle/` were
    untracked.
  - GitHub workflow state immediately after pushing:
    - `vpsadmin`: CI queued for new default head `21fe7e24e`; CI queued and
      API Specs running for the security-advisory merge head `597848686`;
      RuboCop and Webui PHPUnit already green for `597848686`.
    - `vpsf-status`: Integration Tests queued for `0e67673`; dependency graph
      update green.
    - `vpsfree-irc-bot`: RSpec green and Integration Tests queued for
      `a7393bb`.
    - `vpsadmin-go-client`, `vpsfree-mail-templates`, and
      `vpsfree-cz-configuration` had no new relevant push workflow run visible
      in `gh run list` at that point.
  - Later CI poll: vpsAdmin API Specs for `597848686` completed successfully;
    vpsAdmin selected CI for `597848686` and `21fe7e24e`, vpsf-status
    Integration Tests for `0e67673`, and vpsfree-irc-bot Integration Tests for
    `a7393bb` remained queued.
  - Dependency/pin validation after follow-up:
    - `vpsf-status`: `nix develop --command go test ./...` passed after
      updating `vpsadmin-go-client` to
      `v0.0.0-20260604065514-1d9240f3d27b`.
    - `vpsf-status`: `nix build .#vpsf-status` passed after updating the
      normal package vendor hash to
      `sha256-D8wImkdUvapGiudMcbvtGwkPOjbQHGKEGPGY7A4yFa4=`.
    - `vpsfree-cz-configuration`: `confctl build -y
      cz.vpsfree/containers/int.vpsfbot` passed with the updated IRC bot
      package pin.
    - `vpsfree-cz-configuration`: `confctl build -y
      cz.vpsfree/machines/prg/apu` failed before building vpsf-status because
      the local path `/srv/iso-images/systemrescue-11.01-amd64.iso` does not
      exist.
  - Current workflow state after dependency/pin follow-up:
    - Cancelled obsolete `vpsadmin` CI run `26952316519` for `21fe7e24e`.
    - Cancelled obsolete `vpsf-status` Integration Tests run `26952254108` for
      old commit `0e67673`.
    - `vpsadmin` selected CI run `26952238132` for `597848686` is queued.
    - `vpsf-status` Integration Tests run `26953358104` for amended commit
      `ee9afa9` is queued.
    - `vpsfree-irc-bot` Integration Tests run `26952260074` for `a7393bb` is
      queued.
  - Final deployment-pin correction on 2026-06-04:
    - Dev-cluster update was skipped per user request. The attempted build
      exposed that `vpsf-status`'s local `vpsadminGoClientSource` package path
      still used the old vendor hash. Updated that second vendor hash to
      `sha256-1+51I1kIJMVq5gBcrh7oPvFJiUgdcbUnjqb0y40SoRo=`.
    - Updated `vpsf-status` `flake.lock` so its `vpsadmin` input points at the
      deployed vpsAdmin revision
      `5978486864a57fdc94aaa7fae6a74813e76c3d63`, not stale `2be7c47`.
    - Amended and force-pushed `vpsf-status` `master` and
      `2026-05-29-security-advisories` to
      `a376224b97490353daae4e141667d8fcc1050c34`. Backed up the prior remote
      heads as
      `backup/2026-05-29-security-advisories-vpsf-status-ee9afa95` and
      `backup/2026-05-29-security-advisories-vpsf-status-5cd4deb8`.
    - Rebuilt `vpsfree-cz-configuration` history so the old `ee9afa9` and
      `5cd4deb8` pins are not left in `master`. Final config branch head is
      `a3202987f078b0e286f3b7ee72f4aef97ac7e8db`, with commits:
      `583f7945` (`vpsadminServices` -> `59784868`),
      `18c85306` (`vpsfStatus` -> `a376224b`), and `a3202987`
      (`vpsfree-irc-bot` package -> `a7393bb`). Backed up the old config head
      as `backup/2026-05-29-security-advisories-config-a25d799c`.
    - Updated the remote `vpsadmin` feature branch to match deployed
      `master` at `5978486864a57fdc94aaa7fae6a74813e76c3d63`; backed up the
      old feature ref as
      `backup/2026-05-29-security-advisories-vpsadmin-3bd7a190`.
    - Verification after the correction:
      - `vpsf-status`: `nix build .#vpsf-status --no-link` passed.
      - `vpsf-status`: replacement-source package build with local
        `vpsadmin-go-client` source passed.
      - `vpsfree-cz-configuration`: `confctl build -y
        cz.vpsfree/containers/int.vpsfbot` passed.
      - `vpsfree-cz-configuration`: `git diff --check` passed.
    - Cancelled obsolete queued `vpsf-status` Integration Tests runs
      `26954220422` and `26954221875` for `5cd4deb8`. Current runs to watch:
      `vpsadmin` master CI `26952238132`, `vpsadmin` feature branch runs
      `26954838456`/`26954838896`/`26954838511`/`26954838484`/`26954838471`,
      `vpsf-status` master/feature Integration Tests
      `26954599759`/`26954601255`, and `vpsfree-irc-bot` master Integration
      Tests `26952260074`.
    - CI snapshot after polling:
      - `vpsadmin` feature branch: RuboCop `26954838484`, Webui PHPUnit
        `26954838471`, and libnodectld Specs `26954838511` passed for
        `597848686`; API Specs `26954838896` and CI `26954838456` remained
        queued.
      - `vpsadmin` master selected CI `26952238132` remained in progress in
        the `Run tests` step for `597848686`.
      - `vpsf-status` master/feature Integration Tests
        `26954599759`/`26954601255` remained queued for `a376224b`.
      - `vpsfree-irc-bot` master RSpec `26952260134` passed and Integration
        Tests `26952260074` remained queued for `a7393bb`.
  - Follow-up bug investigation on 2026-06-04:
    - Confirmed the reported API hole in
      `security_advisory.node_status#create`: the action copied the nested
      `security_advisory_id` route parameter directly into
      `SecurityAdvisoryNodeStatus.create!`, so a missing advisory id could be
      stored when no database foreign key existed.
    - Updated the create action to load the parent advisory first and create
      the node status through the resolved advisory object.
    - Added model-level association presence validations for advisory child
      rows so raw-id writes cannot create orphan CVE, node status, update,
      affected user/VPS, translation, or outage link records.
    - Added API regression coverage for missing advisory ids on node status,
      CVE, update, and outage-link creates, plus model coverage for internal
      raw child rows.
    - Committed in `vpsadmin` as `aba00ba43`:
      `api: reject orphan security advisory children`.
    - Pushed `vpsadmin` branch `2026-05-29-security-advisories` to
      `origin` at `aba00ba4312a6f6760f6988b0888cf3bc1b62713`.
    - Fast-forwarded and pushed `vpsadmin` `master` to
      `aba00ba4312a6f6760f6988b0888cf3bc1b62713` from a temporary merge
      worktree, then removed the temporary worktree.
    - Master push triggered GitHub Actions runs: CI `26959294329` queued,
      RuboCop `26959294375` in progress, and API Specs `26959295281` queued
      at the time of merge.
    - Verification:
      - `nix develop .#api --command bundle exec rspec
        spec/api/resources/security_advisory_spec.rb
        spec/api/plugins/outage_reports/security_advisory_spec.rb
        spec/models/security_advisory_spec.rb` passed with 31 examples.
      - `nix develop .#api --command bundle exec rubocop ...` passed on the
        touched API/model/spec files.
      - `git diff --check` passed.
  - Follow-up staged publication timestamp coverage on 2026-06-04:
    - Confirmed current API create/update behavior persists `published_at` on
      drafts with focused RSpec:
      `nix develop .#api --command bundle exec rspec
      spec/api/resources/security_advisory_spec.rb -e
      'allows admins to create and update drafts'` passed.
    - Added WebUI browser assertions that staged `published_at` is visible
      after draft creation, editable before publishing, preserved as the
      publish-form default, and still visible after publishing and later
      advisory/update forms.
    - Committed locally in `vpsadmin` as
      `ad03f5cade060bfdf77f5f3a7b19a235406f20b3`:
      `tests: cover staged advisory publication time`.
    - Pushed to `vpsadmin` `master` at
      `ad03f5cade060bfdf77f5f3a7b19a235406f20b3`; remote feature branch
      `2026-05-29-security-advisories` remains at parent `aba00ba43`.
    - Master push triggered GitHub Actions CI run `26964211206`, queued at
      the time of push verification.
    - Verification:
      - `nix shell nixpkgs#nodejs -c node --check
        tests/playwright/webui/specs/security-advisories.spec.cjs` passed.
      - `git diff --check` passed.
      - `./test-runner.sh test 'webui#security-advisories'` passed in
        798.82 seconds.

## Cleanup

- Removed the `worktrees/2026-05-29-security-advisories` worktrees for
  `vpsadmin`, `vpsadmin-go-client`, `vpsf-status`,
  `vpsfree-cz-configuration`, `vpsfree-irc-bot`, and
  `vpsfree-mail-templates`, then removed the empty initiative worktree
  directory.
- Preserved local and remote feature branches as requested by the workspace
  policy.
- Removed the throwaway temp sources used for the IRC bot VM integration run.
- Stopped the running vpsAdmin dev cluster for slug
  `2026-05-29-security-advisories` with
  `dev-clusters/vpsadmin/bin/devcluster stop 2026-05-29-security-advisories`.
  Follow-up status reported `status: stopped`.
