# vpsf-status integration tests

## Goal

Add vpsAdminOS test-runner based integration tests to `vpsf-status` and run
them from GitHub Actions on push.

The tests boot a local one-node vpsAdmin cluster, run the packaged
`vpsf-status` service in a separate VM, and verify JSON, Prometheus metrics,
node reachability transitions, vpsAdmin reachability transitions, and outage
reports.

## Affected repositories

- `vpsf-status`: implementation, tests, flake wiring, NixOS module capability,
  Makefile target, and GitHub workflow.

Reference-only repositories:

- `vpsadmin`: vpsAdmin service VM, one-node test cluster, seed data, and plugin
  model shape for outage reports.
- `vpsadminos`: test runner, test framework, and GitHub Actions helper actions.
- `terraform-provider-vpsadmin`, `confctl`, `vpsfree-irc-bot`: examples of
  external test-runner wiring and vpsAdmin integration-test helpers.

No edits were made outside `vpsf-status`.

## Worktree

- Branch: `2026-06-01-vpsf-status-integration-tests`
- Worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-01-vpsf-status-integration-tests/vpsf-status`
- Base: `origin/master` at `c6fab24`

## Implemented changes

1. Flake wiring
   - Added `vpsadmin`, `vpsadminos`, and aligned `nixpkgs` inputs.
   - Exposed `packages.x86_64-linux.test-runner` and
     `apps.x86_64-linux.test-runner`.
   - Exposed `tests` and `testsMeta` through the vpsAdminOS test framework for
     `x86_64-linux`.
   - Passed the vpsAdminOS path, vpsAdmin path, vpsf-status NixOS module, and
     packaged vpsf-status derivation into suites.

2. Local test runner entry points
   - Added `test-runner.sh`.
   - Added `make test-integration`, which runs `./test-runner.sh test -t ci`.

3. Integration test tree
   - Added `tests/all-tests.nix`, `tests/make-test.nix`, `tests/README.md`,
     `tests/runner/extensions/vpsadmin_services.rb`, and
     `tests/suite/status-page.nix`.
   - Kept the vpsAdmin helper local to `vpsf-status`; it only provides API
     readiness and Ruby fixture helpers needed by this suite.
   - Loaded vpsAdmin outage_reports plugin models in the helper so direct Ruby
     fixture creation can use `Outage`, `OutageTranslation`, and
     `OutageEntity`.

4. NixOS module fix
   - Added `CAP_NET_RAW` to the service's ambient and bounding capability sets
     so the packaged service can perform ICMP ping checks as the system user.

5. GitHub workflow
   - Added `.github/workflows/integration-tests.yml`.
   - The workflow runs on `push` for workflow, flake, Go, Nix, assets, tests,
     Makefile, and test-runner wrapper changes.
   - It uses a self-hosted runner and vpsAdminOS helper actions to determine
     test parallelism, evaluate results, summarize logs, and upload logs on
     failure.

## Test topology

The `status-page` suite starts:

- `services`: vpsAdmin services VM serving `api.vpsadmin.test`,
  `webui.vpsadmin.test`, and `console.vpsadmin.test`.
- `node`: vpsAdminOS node VM from the vpsAdmin one-node cluster fixture.
- `status`: NixOS VM running the packaged `vpsf-status` service with the repo's
  NixOS module.

The suite uses a dedicated socket multicast port (`22131`) for all machines so
it does not collide with other locally running vpsAdminOS test-runner suites
that use the default socket network port.

The status config uses the vpsAdmin seed data:

- API URL: `http://api.vpsadmin.test`
- Web UI URL: `http://webui.vpsadmin.test`
- Console URL: `http://console.vpsadmin.test/console.js`
- Node ID: `101`
- Node name: `vpsadmin-node1.lab`
- Node IP: `192.168.10.11`
- Empty external web services, nameservers, and DNS resolvers.

## Covered behavior

- Baseline JSON contains operational vpsAdmin services and the expected node.
- Baseline metrics contain `vpsfstatus_up 1` and expected vpsAdmin/node gauges.
- Dropping ICMP from the status VM to the node changes node ping status to down
  and later back to responding.
- Stopping `nodectld`, aging the node status row, and restarting `nodectld`
  changes vpsAdmin/node status down and back up.
- Blocking HTTP from the status VM to vpsAdmin services changes API, web UI,
  console, and node vpsAdmin status down and later back up.
- Creating announced and resolved outage reports in vpsAdmin makes them appear
  under `outage_reports.announced` and `outage_reports.recent`.

## Compatibility and deployment analysis

- Runtime API/JSON/metrics contracts are not intentionally changed.
- No database schemas, migrations, persisted state formats, generated clients,
  or external service protocols are changed.
- The test suite creates only ephemeral VM state.
- The GitHub workflow affects CI only and requires a self-hosted runner capable
  of running vpsAdminOS QEMU tests.
- The `CAP_NET_RAW` service capability change is backward compatible for
  deployments: it broadens the service sandbox only enough to allow the ping
  behavior already configured in vpsf-status.
- No coordinated vpsAdminOS node rollout is required.

## Validation

Run:

- `./test-runner.sh ls`
- `./test-runner.sh ls -t ci`
- `nix develop --command go test ./...`
- `nix build .#vpsf-status --no-link`
- `./test-runner.sh test status-page`

Not run:

- Full `./test-runner.sh test -t ci` after the final description-only cleanup.
  `ls -t ci` selects `status-page`, and `status-page` was run directly.

## Remaining review points

- Whether path-filtered push CI is preferred over unconditional push CI.
- Whether rendered HTML checks should be added in a later suite.
