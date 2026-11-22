# vpsAdmin API example validation can block provider integration tests

Related initiative:
`work/2026-07-27-terraform-provider-vpsadmin-issue-11`

## Symptom

`nix develop -c make test-integration` can wait for
`http://api.vpsadmin.test/` until the 15-minute machine-command timeout and
then report only that `curl` never succeeded. HAProxy returns HTTP 503 because
the API backend never becomes healthy.

## Cause

Inspect the retained VM interactively with:

```sh
./test-runner.sh debug --state-dir=/tmp/provider-debug workflows
```

At the Pry prompt, start or query the `services` machine and read the API
journal:

```ruby
machines["services"].execute(
  "journalctl -b --no-pager -u vpsadmin-api.service -o cat -n 300"
)
```

With provider flake input `vpsadmin` at `52933ca65`, packaged HaveAPI 0.29.8
rejects `VpsAdmin::API::Resources::Location::Index` because its example
response contains undeclared `created_at` and `updated_at` fields. Puma exits
before serving the API, so no provider or OpenTofu operation runs.

The matching vpsAdmin correction is commit `e0407c301`, which removes those
fields (and corrects the related IP-address example). As of 2026-07-27, that
commit is on an unmerged vpsAdmin branch and is not an ancestor of
`52933ca65`.

## Workaround and verification

For diagnostic provider validation only, temporarily update the tested
checkout's lock to a revision containing the correction:

```sh
nix flake lock --override-input vpsadmin \
  github:vpsfreecz/vpsadmin/e0407c301c53112f6ebb92cc8005605561eef7bb \
./test-runner.sh test -t ci
```

`nix run --override-input ... .#test-runner` is insufficient: the test runner
reevaluates the repository in child `nix-instantiate`/`nix-build` processes,
which read the checkout's lock again.

Keep the temporary override explicit in test records and restore the committed
lock immediately afterward. In the related initiative, the override let the
API mount and the provider resolve the requested OS template and submit
`Vps.Create`. The suite then failed later when vpsAdmin rejected the request
because another setup transaction still held a resource lock. This proves the
original API-startup failure was removed, but is not a fully green integration
result.

Do not treat an override run as validation of the provider's pinned integration
environment; update the normal flake input only after the upstream correction
is merged.

## GitHub Actions evidence

Provider Integration Tests run `30280042039` reproduced the same failure
against the locked vpsAdmin revision `52933ca65`. The workflow waited 909.04
seconds for the API, received HTTP 503 responses throughout, never saw the API
description, and raised `OsVm::TimeoutError` before OpenTofu or the provider
ran.

Download and inspect the failed run's uploaded test-log artifact before
rerunning. The artifact contains machine consoles, shells, test-runner output,
and HAProxy evidence, but it does not contain the service VM's systemd journal.
It can establish that the API backend never became healthy, while the exact
HaveAPI exception still requires an interactive retained-VM journal or improved
workflow diagnostics.

## Confirmed resolution

The trigger was vpsAdmin's automated packaged-gem update from HaveAPI 0.29.6
to 0.29.8. The API Gemfile permits this with `~> 0.29.6`. HaveAPI 0.29.8
strictly validates documented example responses against their declared output
schemas.

Backport only vpsAdmin commit `9ad43e4ec` from
`2026-06-15-vpsadmin-events`. It corrects the Location and IP-address examples
without bringing in event work or changing the API contract. In the related
initiative, the isolated backport is `cba29b57c`.

The vpsAdmin API boot smoke spec passed all 5 examples under HaveAPI 0.29.8.
The provider's normal integration suite then passed all 8 workflow examples
without an input override, and the provider GitHub integration workflow passed
on the same combined revisions.
