# 2026-08-03-vpsadmin-ci-failure

## Goal

Find the root cause of GitHub Actions run 30748100208, job 91499932626,
and improve vpsAdmin test diagnostics so a recurrence preserves the server-side
evidence needed to identify the precise failure.

## Affected repositories

- `vpsadmin`

## Approach

1. Inspect both workflow attempts and the uploaded integration-test artifact.
2. Reconstruct the failed WebUI OAuth login and determine which conclusions the
   available application, database, and test evidence can support.
3. Keep WebUI HTTP failures test-fatal and preserve nested nginx/PHP-FPM logs
   so the next occurrence exposes the underlying server exception.
4. Run quick component checks, commit, and perform mandatory change review.
5. Run the targeted WebUI integration test, then push and monitor CI if local
   verification is successful.

## Compatibility and deployment

The change is confined to Playwright navigation synchronization and
integration-test log collection. It does not alter production API/WebUI
behavior, persistent state, database schemas, on-disk formats, or deployment
ordering. Mixed deployments and rollback are unaffected.

## Testing plan

- Ruby and JavaScript syntax checks plus repository hooks for all changed
  files.
- `./test-runner.sh test 'webui#auth'` after mandatory review.
- The original `./test-runner.sh test 'webui#transactions'` reproduction.
- GitHub Actions validation on the pushed feature branch.
