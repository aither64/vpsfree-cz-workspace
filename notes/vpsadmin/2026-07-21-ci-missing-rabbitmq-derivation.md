# CI evaluation can fail after a Nix store derivation disappears

## Symptom

The serialized vpsAdmin `CI` workflow completed 116 of 117 integration tests,
but `client/snapshot-download` was reported as an unexpected failure. Its
archived `test-runner.log` failed during Nix evaluation of
`environment.etc.dbus-1.source` because the RabbitMQ 4.2.5 derivation store
path did not exist.

## Cause

The Nix store path needed to evaluate the services VM disappeared on the
self-hosted runner. The test VM was never built and the snapshot-download test
script did not run. This is runner/store state, not an application assertion
or a failure in the authentication-token change under test.

## Verification

Workflow run `29781749917` had 116 successful tests and this one pre-test
evaluation failure. The downloaded `vpsadmin-test-logs-29781749917` artifact
contained `unexpected_failure` in `test-result.txt` and the missing derivation
error in the test's `test-runner.log`.

When this recurs, inspect the archived per-test log before rerunning. A green
rerun does not by itself identify this failure as unrelated.

Related initiative:
`work/2026-07-20-security-advisory-review/`.
