# GitHub archive rate limits in vpsAdminOS CI

## Symptom

The `Build OS and populate binary cache` job failed while building the
top-level closure. A fixed-output Linux source derivation exhausted all four
download attempts with HTTP 429 responses from GitHub.

## Cause

GitHub rate-limited the unauthenticated archive URL for the pinned Linux
revision. The failure happened before livepatch or test jobs ran and was
unrelated to the feature diff.

## Response

Inspect the failed job with `gh run view RUN_ID --log-failed` before rerunning.
When the log shows only repeated HTTP 429 responses for an unchanged pinned
archive, rerunning the failed jobs is appropriate after the transient limit has
had a chance to clear.

## Verification

The first two attempts of vpsAdminOS Actions run `32566122706` failed with the
same HTTP 429 response. A third attempt after a four-minute backoff passed the
top-level build and all downstream jobs. The full result is recorded in
`work/2026-08-22-multiple-kernel-scopes/state.md`.

Related initiative:
`work/2026-08-22-multiple-kernel-scopes/`
