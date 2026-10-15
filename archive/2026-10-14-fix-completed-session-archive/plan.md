# 2026-10-14-fix-completed-session-archive

## Goal

Implement the approved completed-session archive fix, deploy the exact reviewed
runtime to aitherdev using vpsfree-cz-configuration and the workspace user profile,
then explicitly archive `2026-10-05-network-ipv4-left-counter`.

## Affected repositories

- dev-workspace: Ruby lifecycle conversion and regression tests.
- workspace: direct nested runtime revision and generated composed lock.
- vpsfree-cz-configuration: confctl-managed dev-workspace/devWorkspace pin.
Use this initiative's dedicated feature branch/worktrees in all three.

## Approach

Allow every validated lifecycle to transition to archived for explicit archival.
Replace the actual lifecycle header value and preserve all body content/newlines.
Keep strict complete/abandoned conversion and automatic archival behavior.
Add focused conversion, archive/revive and interrupted retry tests; run quick
checks, commit and independently review the final deliverable before long checks.
Publish the reviewed runtime, compose matching source locks, build outside claims,
then activate system followed by application profile under coordinator ownership.
Finally retry the original ordinary explicit archive, retaining branch refs,
conversations and private worktree recovery.

## Decisions

The user selected deployment followed by the original archive in the planning
question, then directed implementation of that plan. This authorizes aitherdev
system/profile activation and archival of the named original session. It does not
authorize default-branch integration of this fix or closure of this fix initiative.
No existing session binding was present, so a separate initiative was created.
Do not change the original valid complete state to active as a workaround.

## Compatibility and deployment

No database/schema, API, protocol, CLI, manifest, journal, observation or cluster
format changes. Existing schema-3 explicit journals and schema-4 revival retain
their current contract; strict older complete/abandoned journals keep saved policy.
The corrected helper remains compatible with old valid tracking. Mixed packages
share existing formats, but the older executor still has this refusal for fresh
completed-to-archived attempts. Application selection remains forward-only;
recover the original admitted candidate or a reviewed successor, preserving
coordinator artifacts/ownership. System activation precedes matching profile
activation and requires no reboot. No production vpsAdmin deployment or migration.

## Documentation

Use an implementation comment for the non-obvious explicit transition rule.
Existing runtime archive/recovery docs describe the intended behavior correctly;
check them against implementation without duplicating rollout status into them.
Keep exact source heads, verification, approvals, operations and original archive
acceptance in this session's state and rollout artifacts. Investigation evidence
is in work/2026-10-14-archive-complete-investigation and its reusable note.

## Testing plan

Focused Ruby: valid source lifecycle matrix targeting archived, matching-target
idempotence, LF/CRLF and unchanged body, invalid header rejection, preserved strict
policy. Explicit archive/revive completed and abandoned fixtures retain local
contents/index and branch heads. Inject an interruption for completed input and
resume the same operation. Run mandatory independent review after quick checks
and committed changes. Then run packaged verification, composed deployment
contract, exact-source CI and aitherdev build through fresh utility watchers.
Deployment acceptance includes package/system identities, portal and Codex/tmux
continuity, actual-state pure conversion and complete original archive outcome.
