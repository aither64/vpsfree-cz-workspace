# 2026-08-10-vpsfconf-daily-update

## Goal

Find and fix the root cause of the failing `Daily update` GitHub Actions
workflow in `vpsfree-cz-configuration`.

## Affected repositories

- `vpsfree-cz-configuration`: workflow and/or hook integration fix.

## Approach

1. Inspect the first failing run and subsequent failures, including job logs.
2. Reproduce the hook failure locally from the current `master` state.
3. Fix the workflow at the narrowest reliable integration point.
4. Verify hook installation, the input-update commit path, and workflow syntax.
5. Push the feature branch and validate it using GitHub Actions.

## Compatibility and deployment

The workflow is development automation and does not change runtime NixOS
configuration, persisted state, schemas, APIs, or protocols. Old and new
workflow versions do not coexist on deployed hosts. Rollback is a git revert;
no deployment ordering or operator migration is required.

## Testing plan

- Reproduce the reported Overcommit signature failure locally.
- Install/sign the declared hooks through the repository development shell.
- Exercise a representative generated commit after changing the development
  shell input, or an equivalent isolated hook-signature regression test.
- Run the repository's mandatory hook checks for the final change.
- Run the mandatory fresh-context change review.
- Trigger or otherwise validate the daily workflow on the pushed branch and
  inspect its logs.

## 2026-08-21 recurrence

The workflow began failing again on 2026-08-14 in the package dependency
update step. Resume the initiative with this approach:

1. Compare the first and latest failures with the last successful run.
2. Reproduce the package-only Bundler environment leaking into the repository
   hook process.
3. Scope the temporary Bundler configuration to package generation only.
4. Verify workflow syntax, hook execution, and Bundler environment isolation.
5. Run the mandatory fresh-context review, fast-forward the fix into `master`,
   and trigger and inspect the complete hosted daily update workflow.

The compatibility and deployment analysis above is unchanged: this remains an
automation-only fix with no runtime, state, schema, API, or rollout impact.
