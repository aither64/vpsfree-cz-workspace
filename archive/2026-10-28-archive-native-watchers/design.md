# Design and verification brief

## Implementation

Keep QuiesceExplicitArchive as the managed entry and delegate its current body to
an unexported helper accepting an interruption function. The managed entry passes
Client.Interrupt, retaining retry cancellation and uncertainty checks. Only
QuiesceNativeDescendants passes the embedded native client interruption method,
after its existing loaded metadata and parent-chain ownership proof. Validate
fresh child ID, CWD and recorded parent before child mutations; preserve repeated
parent discovery, parent-first quiescence and deepest-first retirement. Wrap child
quiesce/retire errors with identity and stage. Do not widen the policy resolver or
change public APIs. No generic retries or UI redesign.

Keep held prompt capture and goal pause before interruption; wait for idle using
existing code. Repeating after an interrupted/lost reply uses fresh active-turn
state and retained evidence. Native utilities intentionally lack retry ownership.
Managed root/member path stays unchanged. Current-state invariants belong in
session-archive-recovery.md; no migration or new on-disk state.

## Tests and acceptance

Use a command fixture with production configured client, ordinary root manifest,
retained roster, materialized rollouts and active native child missing from roster.
Prove red before callback change, green afterward. Cover child under root/member,
queue/goal order, concurrent child spawning, foreign same-CWD identity, managed
retry cancellation and uncertainty, lost interrupt reply/retry. Reuse focused
fixtures rather than build a new harness. Test metadata identity drift before
mutation. Run gofmt and git diff --check plus focused Go tests in nix develop.

After all intended changes including pins are committed, mandatory final review
covers general, architecture, scope and compatibility lanes, full branch history
and no migrations. Then run package and session-archive-lifecycle derivations,
composed default/deployment contracts and aitherdev build. Independent watchers own
long commands, logs and terminal status; lead diagnoses failures and accepts work.

## Deployment and recovery

Publish exact runtime source and match workspace nested override with configuration
devWorkspace channel. Build before machine acquisition, preserve selected profile
until checks pass. Use ordinary confctl system deploy and guarded user-profile
switch with exact ownership environment. Verify health, paths and conversation
continuity. Resume the target archive using its existing receipt/current identity;
never edit evidence or delete checkouts manually. Complete archive and tracking
sync independently. Default-branch merge needs separate explicit user direction.
