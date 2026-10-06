# vpsfree-irc-bot integration tests

## Goal

Add integration tests for `vpsfree-irc-bot` that verify:

- the bot can connect to a real IRC server and post messages to a channel;
- the bot can connect to a local vpsAdmin API instance;
- vpsAdmin-originated events are announced on IRC with the expected text;
- lighter IRC-only checks do not boot the vpsAdmin services VM.

## Affected repositories

- `vpsfree-irc-bot`: primary implementation repository.

Reference repositories inspected for test-framework patterns:

- `vpsadminos`: upstream VM test framework and runner.
- `vpsadmin`: vpsAdmin services VM and examples of service-heavy tests.
- `confctl`: compact external consumer of the vpsAdminOS test framework.
- `terraform-provider-vpsadmin`: external consumer that imports vpsAdmin test
  machines and adds vpsAdmin API helper extensions.

No changes are planned in the reference repositories.

## Current findings

`vpsfree-irc-bot` has no local `AGENTS.md`, no test-runner integration, and no
Nix package output. It currently has a Nix dev shell and RSpec/RuboCop tooling.
The existing GitHub workflow runs only `nix develop -c bundle exec rspec`.

The bot's vpsAdmin-facing features are:

- `WebEventLog`, which polls `api.news_log.list(since: ...)` and posts
  `News from vpsAdmin: ...` to configured IRC channels.
- `OutageReports`, which polls `api.outage.list`, `api.outage_update.list`,
  reads `api.system_config.show('webui', 'base_url')`, and posts outage
  reports, updates, and reminders.
- `Cluster`, which uses `api.node.public_status` for the `status` command.

The vpsAdmin services VM is already reusable from `vpsadmin`:

- `tests/configs/nixos/vpsadmin-services.nix` boots MariaDB, RabbitMQ, Redis,
  API, supervisor, webui, Mailpit, console router, and related services.
- The config enables the `newslog` and `outage_reports` plugins.
- It provides a socket-network address, test hosts such as
  `api.vpsadmin.test`, test credentials, and an `/etc/haveapi-client.yml`
  suitable for vpsAdmin CLI/API access.

The vpsAdminOS framework is consumed by downstream repos using this shape:

- add `vpsadminos` as a flake input;
- expose `tests`, `testsMeta`, and `apps.test-runner`;
- add a small `test-runner.sh` wrapper around `nix run .#test-runner`;
- add `tests/all-tests.nix`, `tests/make-test.nix`, and `tests/suite/*.nix`;
- load local Ruby test-runner extensions from `tests/runner/extensions`.

Nixpkgs includes `ngircd` and the NixOS module `services.ngircd`, which is a
good fit for a small local IRC server.

## Proposed implementation

1. Add flake inputs and test-runner outputs to `vpsfree-irc-bot`.

   Follow the established downstream pattern from `vpsadmin`, `confctl`, and
   `terraform-provider-vpsadmin`: add `vpsadmin` and `vpsadminos` inputs, use
   `vpsadminos.lib.testFramework.mkTests` and `mkTestsMeta`, and expose
   `apps.${system}.test-runner`. Prefer aligning `nixpkgs` with the
   `vpsadminos` input for test evaluation, matching the vpsAdmin/provider
   repos, unless review prefers keeping the bot's current standalone
   `nixos-unstable` input for development.

2. Add a Nix package for the bot.

   Build the bot from the existing `Gemfile.lock`/`gemset.nix` with
   `bundlerEnv`, install `bin/vpsfree-irc-bot`, and wrap it with the local
   `lib/` path. Use this package inside VM tests instead of running from the
   source checkout with mutable bundler state.

3. Add test framework files.

   Add:

   - `test-runner.sh`;
   - `tests/all-tests.nix`;
   - `tests/make-test.nix`;
   - `tests/README.md`;
   - `tests/runner/extensions/irc_bot.rb`;
   - `tests/configs/nixos/irc-bot.nix` and small shared helpers as needed.

   The local extension should provide raw IRC helpers that can register a test
   client, join a channel, respond to PING, and wait for matching `PRIVMSG`
   lines. This verifies the server actually receives the bot's output.

4. Add a lightweight IRC-only suite.

   `tests/suite/irc-basic.nix` should boot a single small NixOS VM with:

   - `services.ngircd` enabled on localhost or a socket-network address;
   - the packaged bot running as a systemd service;
   - a generated bot config for a test channel;
   - all vpsAdmin-dependent bot channel lists empty.

   It should verify the bot joins IRC and responds to a simple command such as
   `!ping` with `pong`. This suite should carry tags such as `ci`, `irc`, and
   `light`, and must not import or start vpsAdmin services.

5. Add the vpsAdmin-backed event suite.

   `tests/suite/vpsadmin-events.nix` should boot:

   - the `services` machine from `vpsadmin/tests/configs/nixos/vpsadmin-services.nix`;
   - an IRC/bot NixOS machine using `ngircd` and the packaged bot.

   The machines should use socket networking. The bot machine should resolve
   `api.vpsadmin.test` to the services VM and should run with a HaveAPI client
   config for the test vpsAdmin instance.

   Initial examples:

   - wait for vpsAdmin API and IRC readiness;
   - start the bot after vpsAdmin is reachable;
   - create a `NewsLog` row or use the vpsAdmin API to publish a news item;
   - wait for `News from vpsAdmin: ...` on IRC;
   - create or update an announced outage fixture;
   - wait for the outage announcement/update lines on IRC.

   Prefer deterministic fixture text and database/API setup through the
   services VM, using a minimal local `VpsadminServicesMachine` helper based on
   the Terraform provider's extension.

6. Keep polling tests fast without changing production defaults.

   The bot currently polls news every 60 seconds and outages every 60/30
   seconds. Add a default-preserving test knob, most likely environment
   variables read at class load time, so the VM service can run with short
   polling intervals such as 2 seconds. Production defaults remain unchanged.

7. Wire validation and optional CI.

   Local validation commands:

   - `nix develop -c bundle exec rspec`;
   - `nix develop -c bundle exec rubocop`;
   - `./test-runner.sh ls`;
   - `./test-runner.sh test irc-basic`;
   - `./test-runner.sh test vpsadmin-events`.

   The bot repository currently runs on GitHub-hosted Ubuntu for RSpec. The VM
   integration workflow may need a self-hosted runner like vpsAdmin uses. Add
   the local test-runner first; add CI after measuring runtime and confirming
   runner availability.

## Compatibility and deployment

This work is test and packaging infrastructure only. It does not intentionally
change persisted bot state, vpsAdmin database schemas, public API contracts, or
IRC protocol behavior.

Runtime behavior should remain compatible:

- bot poll intervals keep the existing defaults unless a test explicitly sets
  the new environment variables;
- generated bot configs for tests should not affect deployment config in
  `vpsfree-cz-configuration`;
- flake input changes affect development/test evaluation, not deployed systems,
  unless downstream configuration later chooses to consume the new package
  output.

The tests intentionally exercise mixed components: current bot code against the
current vpsAdmin services VM from the `vpsadmin` flake input. If the existing
`haveapi-client` dependency is no longer compatible with current vpsAdmin, the
integration test should expose that and the follow-up fix should be handled in
the bot repository.

## Open review points

- Whether to align the bot's `nixpkgs` input with `vpsadminos/nixpkgs`, as
  downstream integration-test consumers do, or keep a separate bot dev-shell
  `nixpkgs` input and add a test-only nixpkgs input.
- Whether the first vpsAdmin-backed suite should include both news-log and
  outage-report coverage immediately, or land news-log first and add outage
  coverage as the next focused change.
- Whether to add GitHub Actions integration in this branch or wait until the
  local VM test runtime and runner requirements are known.

## Implementation outcome

The implementation includes the full local test-runner integration and the
GitHub Actions workflow in `vpsfree-irc-bot`.

Implemented pieces:

- flake package output for the bot;
- `apps.test-runner`, `tests`, and `testsMeta` outputs;
- `test-runner.sh`;
- shared test framework files under `tests/`;
- IRC host-forward and raw IRC client helpers;
- vpsAdmin services helper methods for API readiness and database fixtures;
- `irc-basic`, a lightweight IRC-only suite;
- `vpsadmin-events`, a vpsAdmin-backed suite;
- push workflow for ci-tagged integration tests.

The lightweight suite covers bot commands that do not need external services:
help, command-specific help, channel/private ping, uptime/counters, archive
URLs and argument validation, lastlog, greetings, mute/unmute state, and
rank/top/karma behavior.

The vpsAdmin-backed suite covers the bot's vpsAdmin connection and event
posting behavior:

- `!status` through `Cluster`;
- news-log polling and IRC announcement;
- announced outage polling and IRC announcement;
- `!outage` response;
- outage update polling and IRC announcement.

Outage URL is not optional. The vpsAdmin fixture configures
`webui/base_url = http://webui.vpsadmin.test`, and the tests assert that the
bot posts the generated outage URL for new outages, `!outage`, and outage
updates.

## Compatibility update

No vpsAdmin database schema, API contract, generated client, or deployed
configuration changes are introduced.

Runtime behavior changes are intentionally narrow:

- optional integrations are only loaded when their config is present;
- API-backed plugins still require `api_url`;
- outage reports still require the vpsAdmin WebUI base URL;
- test-only environment variables can shorten polling intervals, while
  production defaults remain 60 seconds for checks and 30 seconds for outage
  reminders;
- multi-line messages are sent as individual IRC lines, which fixes outage
  announcements on real IRC servers.

Deployment and rollback do not require ordering between components. Rolling
back the bot code restores previous optional-plugin loading and message-send
behavior without changing persisted state.
