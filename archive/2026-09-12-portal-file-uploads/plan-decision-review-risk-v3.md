## Findings

### Blocking — v2 recovery can retire a current or unproven proposal

At `7f0d1ab:portal/internal/web/server.go:1588-1617`, the action context uses a trimmed `PlanTurnID`, but the freshness check compares the transcript against the untrimmed value. A crafted recovery request with `"planTurnId":" plan "` therefore matches the durable `plan:plan:<digest>` attempt during reconciliation/discard, yet bypasses the current-plan guard and retires it.

The guard also permits retirement when `LatestTurnID` equals the source turn but `completedPlan` cannot prove the proposal. That is an unproven state, not proof of obsolescence.

This can remove a prepared request after Plan mode changed to Default but before send, causing the legitimate retry to fail at `server.go:1663-1675` and releasing the lifecycle guard prematurely.

Normalize the turn ID once and retire v2 only when a newer turn or a demonstrably different proposal proves the source obsolete. Preserve same-turn unproven states. Add tests for padded turn IDs and same-latest-turn transcripts lacking a qualifying plan.

### Important — recovered submitted receipts may never reach acknowledgement

At `7f0d1ab:portal/internal/web/static/app.js:2137-2151`, recovery starts before transcript observation. The attempt is marked in-flight, so acknowledgement excludes it. When recovery later returns a submitted receipt, `app.js:2596-2614` clears the in-flight marker but schedules no follow-up acknowledgement or refresh.

If no later App Server event occurs, the observed browser record and accepted provider-ledger entry remain until another refresh or session retirement. This violates the stated normal transcript-acknowledgement contract. Trigger acknowledgement after successful receipt recovery and cover the held-response ordering in the browser test.

No further findings in the requested commits. `DiscardPreparedSend` correctly serializes ledger access, checks exact message/context identity, refuses submitted states, restores memory on write failure, and durably releases the lifecycle blocker. Legacy `action=same` is rejected before reconciliation, and recovery itself does not send or change mode. The listed pin commits consistently select `ee9ab427` and `7f0d1abd`.

Residual gap: the shared worktrees advanced to rewritten runtime and downstream heads during review (`7f640a0`, `a6d257e`, `36db5db`, `d600271`). Those newer heads were not reviewed; this result applies only to the packet’s exact commits. The reported test passes were accepted as supplied, and full browser acceptance, package builds, publication, and deployment remain unverified.