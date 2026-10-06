# Verification evidence

> Historical evidence for the superseded restrictive implementation. This does
> not review or verify the approved whole-content replacement.


Configuration feature head `7cce4271be0bcd81a42c6784e12dff326e5d041f`,
base `b164a3b786cb82878f00f8ebd2a7825ee5254c15`.

## Quick checks and review

- Full configuration RSpec suite: 206 examples, 0 failures.
- Targeted RuboCop: 9 files, no offenses; mandatory Overcommit hooks passed.
- Whole-branch independent review and accepted focused corrections:
  [implementation-review.md](implementation-review.md).
- Lead offline original-input dry-run after remediation: 9/9, one unsaved
  incident candidate per report, exact expected event time and assignment; no
  stored records, live mailbox access or notifications. Originals remain external.

## Isolated database verification

Fresh Luna/low watcher ran the prepared combined verification at the final head.
It built the configuration-pinned API package
`a65a4dfeb92a59df4a80a737a20bcbf8558793ff` and MariaDB 11.4.12, then started
a private disposable Unix-socket-only database. It loaded the exact pinned
schema declarations for IPs, assignments and incident reports, and the actual
API historical assignment lookup and Result interface. Minimal ActiveRecord
models isolate persistence/active-resource behavior from the wider API boot.

All nine original reports passed both dry-run no-save and normal-parser save/
reload checks. Assignment IDs and event times match, including Provider.tools
.114000 and Custom Visuals .439254 fractions. The schema-loaded detected_at
column has precision 6; all nine times survived database roundtrip exactly.
Actual SQL highest-ID/inclusive-boundary selection, omission of prior-owner
logs, cross-assignment aggregate rejection and A/B/A rejection all passed.
Rejected/dry-run cases left zero incident records. No notification Handler or
mail transaction chain was invoked. The owned DB process stopped; private
artifacts remain outside version control.

The combined operation exited 1 after 42 seconds because the next exported Nix
shellHook referenced unset PS1 under `set -u`, before configuration build began.
Lead inspected the script, initialized PS1 in a separate build wrapper, and
strict-shell source/bundle-check smoke verification passed. Original failure
evidence is retained in untracked integration-verification.log/.status. This
wrapper issue does not invalidate completed database assertions.

## Configuration build

A new catalog-policy Luna/low watcher ran the remaining build once:
`confctl build --yes 'cz.vpsfree/vpsadmin/int.api1'` in the prepared Nix
environment at the exact final feature head. Exit 0 in 92 seconds, all 110
derivations completed and generation `2026-10-02--19-07-01` built.
Evidence: untracked api-build.log/.status. No kernel build, deployment,
cancellation or running operation remains.

Final pre-push fetch confirmed unchanged base b164a3b. Feature pushed over SSH
at exact head 7cce4271; portal comparison captures exact base/head. GitHub lists no
feature runs; repository workflow is scheduled/manual daily-update only.

## Limits

These are offline/disposable checks, not production or mailbox verification.
They do not test API model callbacks/notifications or the deployed database's
actual column precision. Actual deployed revisions and the production mail-task
owner must be identified for an authorized rollout. No schema/pin changes or
node coordination are needed. Mail deletion before parsing, partial-persistence/
notification recovery and rollback limits remain as documented in the owning
API README. Feature remains unmerged and undeployed.
