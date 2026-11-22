# vpsAdminOS CI can hit GitHub archive rate limits

## Symptom

The CI `Build OS and populate binary cache` job fails quickly while fetching an
unchanged Linux source revision. Downstream tests are skipped.

The same failure can block a local test-runner invocation before its VM starts,
because both environments evaluate the identical fixed-output source fetch.

## Cause

Nix `fetchurl` downloads the pinned Linux archive from GitHub. GitHub returned
HTTP 429 for every built-in retry, so the Linux source derivation failed before
the kernel or changed ZFS code was compiled.

## Resolution

Inspect the failed log to confirm that the source revision and hash are
unchanged and that no compiler command ran. After establishing the HTTP 429 as
the root cause, rerun the failed workflow attempt so the responsible runner can
build and publish the kernel closure.

Observed in vpsAdminOS CI run `33641348420` for
`work/2026-09-02-vpsadminos-chattr-test`. Attempts 1 and 2 both failed on the
same archive before compilation, so the second failure was not rerun
immediately.

A local focused `kernel/vpsadminos#misc-attrs` run also received HTTP 429 for
the same archive. It did not compile the kernel or ZFS and did not execute any
test assertion. An equivalent codeload archive or a later retry can populate
the fixed-output source without changing the configured kernel revision.

For this occurrence, `nix store prefetch-file` against the equivalent codeload
URL returned the configured archive hash and populated the exact fixed-output
store path. The subsequent focused build and VM test succeeded without any
source or pin change. This is suitable as a local unblock; CI should still be
allowed to fetch the configured URL normally so its binary-cache publication
remains reproducible.
