## Blocking

- Plan implementation idempotency is keyed only by plan content, not by plan turn. The browser deliberately treats identical plans from different turns as distinct decisions, but it searches durable attempts using only `"Implement the plan."` plus `plan:<digest>` ([app.js:508](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-file-uploads/dev-workspace/portal/internal/web/static/app.js:508), [app.js:2715](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-file-uploads/dev-workspace/portal/internal/web/static/app.js:2715), commit `d2cdeabd`). The server constructs the same turn-independent context and reconciles it before validating `planTurnId` ([server.go:1570](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-file-uploads/dev-workspace/portal/internal/web/server.go:1570), commit `031e3a34`); accepted attempts immediately return their old receipt ([client.go:3750](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-file-uploads/codex-web/codex/client.go:3750), commit `c0fbae9d`). Consequently, if acknowledgement of plan A remains pending and a later turn B produces identical plan text, the UI shows B as intended but reuses A’s client ID; the server returns A’s receipt and never sends B’s implementation request. This violates the explicit later-identical-turn behavior and can silently discard an approved implementation. Bind new attempts and reconciliation to turn plus digest, while retaining an explicit compatibility path for genuinely pre-upgrade attempts, and add a regression covering an accepted unresolved attempt followed by an identical plan in a later turn.

## Important

None.

## Advisory

None.