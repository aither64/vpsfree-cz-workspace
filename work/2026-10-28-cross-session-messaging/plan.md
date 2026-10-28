# Cross-session lead communication

Implement the conversation's approved plan in dev-workspace, deploy matching
host configuration through vpsfree-cz-configuration and the composed workspace
user profile. User authorized implementation and deployment; no default-branch
integration is authorized. User subsequently authorized normal tracking.

Existing leads communicate only after explicit user approval of a session pair.
Approval in either chat or the portal is sufficient for both directions, until
revocation or archive/delete. No new roles; no transitive or fork-inherited grants.
Messages are deliberately composed text, not permission to read peer transcripts,
modify their teams/worktrees, merge or deploy. Natural-language consent is lead
policy; the backend enforces the recorded pair grant and native caller identity.

Provide CLI and MCP operations allow/revoke/list/send/reply/history and a portal
Communication panel. Steer active leads, start eligible idle leads and hold work
while stopped, recovery-held or waiting for user input/approval. Preserve model,
effort and collaboration mode. Stable IDs and submission reconciliation prevent
duplicate delivery; uncertain outcomes remain visible. Revalidate grants under
locks at dispatch. Persist private versioned grants/messages outside Git.

Compatibility: additive private state, no roster migration or Codex upgrade.
New state and daemon tool startup need package capability checks. Old packages
must not manage unsupported state. Archived history survives; revival needs new
approval. Existing recovery and provider/lifecycle holds remain authoritative.
Application recovery is forward-only. System activation precedes profile switch.

Documentation belongs in dev-workspace's portal/session guide and communication
reference; site workflow exception belongs in workspace team guidance. Deployment
uses existing configuration operations documentation; per-rollout evidence here.

Acceptance: approve A-B from A, exchange both ways without approval in B, hold
while B stopped, resume explicitly, revoke from B, reject later sends. Cover
identity, grant lifetime, retry/restart/race and browser authorization cases.
Quick checks precede final independent review; packaged/native checks follow.

Projects: dev-workspace implementation, workspace guidance and runtime selection,
vpsfree-cz-configuration dev-workspace channel and aitherdev deployment.
