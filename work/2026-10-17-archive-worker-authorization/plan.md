# 2026-10-17-archive-worker-authorization

## Goal

Fix the deterministic portal archive authorization regression reported for
2026-10-14-ubuntu-container-build and require packaged end-to-end lifecycle
acceptance before releases. User approved implementation of the proposed plan,
including deployment and normal retry of the reported archive. No default-branch
integration is authorized.

## Affected repositories

- dev-workspace: authorization dispatch, regressions, real packaged VM/browser
  acceptance, CI gate and lifecycle documentation.
- workspace: nested runtime selection only.
- vpsfree-cz-configuration: matching devWorkspace channel selection only.

## Approach

Move the receipt-bound worker authorization call from delete to archive. Retain
all existing lifecycle/recovery checks and formats. Add fast CLI positive and
negative regressions and an automated VM test that runs the shipped portal,
systemd worker, CLI and native App Server together. Archive and revive disposable
sessions without model turns; check data restoration, interruption/retry,
portal restart and deferred tracking sync. Run the packaged check on every push
and pull request and before deployment.

## Decisions

User selected the focused fix plus release gate over a broad lifecycle redesign.
Lead owns design and code in this threadless initiative; no persistent roster
exists. Fresh independent review and verification utility follow installed site
policy. Preserve reported session receipts; never repair them by hand.

## Compatibility and deployment

No API, CLI, database, journal, recovery or module-option format changes. Old and
new recovery records remain readable. Existing package-generation fences and
forward-only profile recovery remain. Publish feature branches, align exact
runtime pins, verify before coordinated system/profile activation, and keep the
machine reservation through final review. No fleet/node updates. Deployment does
not imply master integration approval.

## Documentation

Maintainers/operators: update dev-workspace archive recovery and development
verification guidance. Session plan/state/design and rollout records retain
incident evidence and exact heads; reusable lesson records the testing gap.

## Testing plan

Fast CLI regression must fail on the original dispatch. Validate receipt/session/
workspace/attempt mismatches and archive-worker rejection for delete/revive.
Quick syntax and focused checks precede committed mandatory independent review.
Then run real packaged browser archive/revive, restart, interruption/retry and
pending-tracking scenarios in the VM plus package/CI checks under fresh watchers.
Finally run disposable deployed acceptance before retrying the reported archive.
