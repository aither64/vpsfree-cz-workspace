# 2026-08-31-vpsadmin-notifications

## Repositories

- Session slug and feature branch: `2026-08-31-vpsadmin-notifications`.
- Worktree group:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-08-31-vpsadmin-notifications/`.
- `vpsadmin`: base `7b455cad1c0c`, head `f2f7c6a9a104`.
- `vpsfree-notification-templates`: base `04921d75ab53`, head
  `c38e56c945d1`.
- `vpsfree-cz-configuration`: rebased base `66ab5d69`, head `5aeb332c`.
- All three feature branches are pushed and all `origin` remotes use SSH.

## Implemented

### vpsAdmin

- Commit `64694866c` defines the declarative template format, restricted
  metadata parser and converted core/plugin data.
- Commit `3ca403080` adds the Nix packaging/checking helpers, flake outputs and
  reusable GitHub Actions workflow.
- Commit `ea956e5ed` adds database reconciliation, the Rake task and NixOS
  lifecycle integration.
- Commit `f2f7c6a9a` removes the standalone mail-template uploader.
- The metadata DSL is parsed through `Ripper`; repository metadata is never
  evaluated as Ruby. Only documented calls with literal strings, symbols and
  booleans are accepted.
- Validation covers the existing database limits, blank values, normalized
  two-letter languages and case-insensitive file collisions before packaging.
- Moved 52 API and 14 plugin templates to
  `<name>/email/<language>.(subject|text|html).erb`. Subjects were extracted
  from metadata and empty language declarations were removed.
- The effective package layers core templates, only configured plugins and an
  optional deployment source. Whole templates use first-wins precedence for
  core/plugin collisions; the deployment source overrides both.
- A one-shot service reconciles the effective package transactionally after
  database setup and before the API and supervisor. It serializes concurrent
  starts, repairs drift without writing unchanged records, and preserves rows
  not found in the managed package.
- The default-install task and database-setup option were renamed, with a Nix
  renamed-option alias. Existing mail-template API endpoints remain.
- No event models, event payloads, transports or protocols were added.

### Template repository

- Commit `c38e56c` moves all 69 templates below `templates/`, introduces the
  `email/` level, extracts localized subject files and preserves four body
  symlinks.
- Removed the repository-local Gemfile, Rakefile, lock file and checker. The
  thin flake calls vpsAdmin's helper and the workflow calls vpsAdmin's reusable
  workflow at exact revision `f2f7c6a9a10437892929fdf99b968e1010aa19b0`.
- The flake lock pins the same vpsAdmin revision. README and repository
  guidance describe the restricted, data-only provider contract.

### Production configuration

- Commit `7d8c10a9` adds the template flake/channel only to `int.api1` and sets
  `vpsadmin.api.notificationTemplates.source` to its default package. The
  template flake's vpsAdmin input follows `vpsadminServices`.
- Commit `b928eea5` updates the vpsfbot webhook allowlist for the repository
  rename.
- Confctl-generated commit `ecaf616d` pins `vpsadminServices` to
  `f2f7c6a9a10437892929fdf99b968e1010aa19b0`.
- Confctl-generated commit `5aeb332c` pins
  `vpsfreeNotificationTemplates` to
  `c38e56c945d1fb0df41a26b6c9127368eb592373`.
- Staging and production application channels were not changed. No deployment
  or merge was performed.

## Verification completed

### vpsAdmin

- Focused parser/importer specs: 31 examples, 0 failures, including restricted
  metadata execution, persistence constraints and real two-connection
  concurrency coverage.
- RuboCop passed for all changed parser/importer code. All four commits passed
  the repository's Overcommit hooks in the full Nix shell; no hook was
  bypassed. `git diff --check` passed.
- `ruby tests/ci-selection-test.rb` passed with 16 runs and 55 assertions.
- Targeted Nix builds passed for the default and effective template checks.
  The core checker reported 52 templates/160 files. The effective fixture
  reported 58 templates/178 files, included its explicitly enabled outage
  plugin, excluded the disabled payments plugin and applied the custom
  override.
- A full `nix flake check --no-build` is still blocked by the pre-existing
  `overlays.list` output, which modern Nix expects to be an overlay function.
  The new targeted checks pass independently.
- Converted metadata, subjects and body bytes were compared with
  `origin/master`; only intentionally empty language blocks differ.

### Template repository

- `nix flake check --print-build-logs` and `nix run .#check` passed against the
  final vpsAdmin pin: 69 templates and 337 files.
- Converted metadata, subjects, body bytes and symlink targets were compared
  with `origin/master`; only two semantically empty language blocks were
  removed.
- The repository declares no hook framework. `git diff --check` passed.
- The reusable workflow's imported action versions were checked against their
  official latest releases: `actions/checkout` v7 and
  `DeterminateSystems/determinate-nix-action` v3.22.2.

### Production configuration

- Every commit passed the declared Overcommit Nixfmt hook; no hook was
  bypassed. Lock changes were made and committed by `confctl inputs channel
  set --commit`.
- Resolved channels report vpsAdmin `f2f7c6a9` and templates `c38e56c9`; the
  template input's vpsAdmin edge follows `vpsadminServices`.
- `confctl build -y cz.vpsfree/vpsadmin/int.api1` passed, generation
  `2026-09-01--12-09-04`.
- `confctl build -y cz.vpsfree/vpsadmin/int.api2` passed, generation
  `2026-09-01--12-10-55`.
- `confctl build -y cz.vpsfree/containers/int.vpsfbot` passed, generation
  `2026-09-01--12-12-10`.
- The API1 generation has `vpsadmin-notification-templates.service` ordered
  after database setup and before the API/supervisor. It reconciles a
  75-template effective package and uses that immutable package path as the
  source identity. API2 has neither the template input nor the reconciliation
  unit.
- The configuration push first failed because the ambient shell did not have
  Overcommit's pinned gems. Re-running the push inside `nix develop` passed the
  mandatory pre-push hook. Generated `.bin/` and `.bundle/` files were then
  removed.

## Mandatory change review

The standalone fresh-context review completed before the long configuration
builds. It found three Blocking issues and one Important issue:

- external `meta.rb` was evaluated with `instance_eval` under the API service
  account;
- checker validation did not cover persistence constraints and normalized
  language collisions;
- the initial vpsAdmin commit combined the parser/data, tooling and lifecycle
  layers;
- effective packaging included packaged but disabled plugins.

All findings were accepted and resolved before the final branch rewrite. The
restricted parser no longer executes metadata, the checker validates database
constraints, enabled plugins are explicit, and vpsAdmin now has four
dependency-ordered commits. Focused tests and all long builds passed after the
fixes.

## Notable findings

- Nix store inputs are read-only, so overlay assembly makes build-directory
  copies writable before applying a custom source.
- The checker initially inherited an ASCII process locale in the Nix sandbox.
  All Ruby source/template reads now request UTF-8 explicitly.
- A repeatable-read transaction can retain an empty snapshot while waiting for
  another importer. Locking reads serialize before content queries, and a real
  two-connection regression spec covers the race.
- Whole plugin template directories use first-wins precedence, matching the old
  core-before-plugin behavior; copying individual files would mix colliding
  templates incorrectly.
- Entering the configuration dev shell first generated an unlocked default
  input. It was restored before commits, and final lock updates were made only
  by `confctl`.

## GitHub Actions

- Template current-head run `33495547655` at `c38e56c945d1` passed.
- vpsAdmin current-head RuboCop, WebUI PHPUnit, client and i18n workflows at
  `f2f7c6a9a104` passed. API-spec run `33495403486` also passed all core/full
  shards and its topic-coverage check.
- Current-head CI run `33495403375` is still running the full `tag=ci`
  integration suite because the change touches `packages/**` and `nixos/**`.
  A comparable successful branch run took about 7.5 hours, so this does not
  block handoff for review.
- Superseded in-progress vpsAdmin CI run `33490826983` at `c2f38a63951f` was
  cancelled after the force-push. No current-head runs were cancelled.
- The configuration repository has no workflow runs for this branch.

## Remaining work

- Observe current-head CI run `33495403375` to completion and inspect its logs
  if it fails.
- Merge and deployment remain with the user.
