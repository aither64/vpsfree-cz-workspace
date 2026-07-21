# 2026-07-21-system-install-failure

## Goal

Investigate the unexpected `system/install` failure in vpsadminos CI run
29815572098, identify the root cause from the complete job artifacts, and make
the test synchronize on the actual pool initialization contract.

## Affected repositories

- `vpsadminos`: system installation integration test only.

## Approach

1. Download and inspect the complete failed-job artifact, including the test
   runner transcript and installed-machine diagnostics.
2. Compare the failed assertion timing with the pool runit service and osctld
   initialization sequence.
3. Replace the intermediate ZFS-property polling with the pool service's
   completion/readiness check, then assert the finished state directly.
4. Run quick discovery/evaluation and formatting/hook checks, commit the fix,
   obtain the mandatory standalone change review, and run the targeted
   `system/install` integration test.

## Compatibility and deployment

This is a test-only synchronization change. It does not change persisted data,
database schemas, APIs, generated clients, protocols, NixOS module options, or
runtime behavior. There are no mixed-version, deployment-ordering, coordinated
node-update, or rollback constraints. Old and new vpsAdminOS systems remain
compatible; only CI waits for the documented one-shot service completion signal
before inspecting initialized pool state.

## Testing plan

- Confirm `system/install` test discovery/evaluation.
- Run the repository's mandatory overcommit hooks.
- Run `./test-runner.sh test system/install` after standalone change review.
