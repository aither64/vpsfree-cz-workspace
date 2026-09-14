**Blocking — a claimed answer can be sent to a replacement offer with the same ID.**

Repository: `codex-web`, commit `1a0ed38060db44bc3849d7adec481519d78dfa90`.
References: [finishResponse](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-portal-review-fixes/codex-web/codex/client.go:1453), [writeOn](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-portal-review-fixes/codex-web/codex/client.go:706), [claim](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-portal-review-fixes/codex-web/codex/client.go:1404).

The token is checked when claiming the request, but the claim can wait for `writeMu`. During that wait, `handleResolved` can remove the offer and the reader can admit a different question with the same JSON-RPC ID on the same connection. `writeOn` only checks the connection and generation, so it sends the old answer to the replacement request. The token comparison after writing only prevents deletion of the replacement; it cannot undo delivery.

Confirmed with a deterministic temporary Go overlay test, without changing the project tree: claim the first offer while holding `writeMu`; send `serverRequest/resolved`; reissue that ID with changed questions/options; wait for the new token; release `writeMu`. `RespondPrompt` returned success, and the server received answer `First` even though the replacement offered only `Second`. The focused test failed in 0.019 seconds. Command: `nix develop --command go test -mod=readonly -overlay /tmp/portal-general-review-9poc4owz/overlay.json ./codex -run TestReviewReissuedOfferWhileAnswerWaitsForWrite -count=1`.

Revalidate the exact claimed offer at write admission and serialize that admission with offer retirement/replacement. Reject an expired claim as definitely unsent. Add this post-claim replacement regression for user answers and ensure automatic responses and approvals use the same protection.

**Blocking — the runtime series bundles independently reviewable behaviors.**

Repository: `dev-workspace`, commits `9d71b418d7d409abc6fb56bdefc4e9ecf1126b8d` and `94e3114c6fef510ca21d29efd1741faa848a4147`.
References: [repository history observation and loading](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-portal-review-fixes/dev-workspace/portal/internal/web/static/repository-review.js:166), [read and timing helpers](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-portal-review-fixes/dev-workspace/portal/internal/web/static/app.js:299), [answer recovery](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-portal-review-fixes/dev-workspace/portal/internal/web/static/app.js:626).

`9d71b41` combines exact/lazy file rendering with automatic repository history refresh and stale head observation. The packet's renderer/content lifecycle rationale explains coupling within the file renderer, but history refresh neither consumes the Git range contract nor requires file collapse. It can be reviewed, tested and reverted separately. `94e3114` likewise combines page read/timing recovery with question response recovery and its provider dependency. A shared read-scope helper establishes an ordering dependency, not an indivisible behavior change.

Split automatic repository histories from file rendering, and read/timing recovery from question response recovery. Keep supporting tests with each behavior; keep the required provider pins with their consuming response change. The dedicated archival-settings, provider-contract, reviewer-model and downstream-pin commits have coherent purposes. This finding is Blocking under the General lane's explicit commit-series rule.

**Important — refreshing a failed snooze cannot retry it when the offer is unchanged.**

Repository: `dev-workspace`, commit `94e3114c6fef510ca21d29efd1741faa848a4147`.
References: [failure latch](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-portal-review-fixes/dev-workspace/portal/internal/web/static/app.js:2634), [token-only reset](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-portal-review-fixes/dev-workspace/portal/internal/web/static/app.js:2569), [Refresh question handler](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-portal-review-fixes/dev-workspace/portal/internal/web/static/app.js:2792).

After a temporary HTTP failure before snooze delivery, `snoozeFailed` remains true and every further snooze attempt exits immediately. Following the inline instruction to refresh only reloads the prompt. If the App Server connection and offer remain valid, the same token returns, so the failure latch never clears. Automatic resolution therefore continues while the user answers, with no working inline recovery path short of reloading the document or replacing the offer.

Allow an explicit refresh/retry to clear the failed state for the authoritatively restored offer and attempt its token-bound snooze again. Add coverage for a failed HTTP snooze followed by restoration of the same token, alongside changed-token recovery.

Reviewed all four exact base/head ranges in `packet.md`, their commit messages, local repository rules, relevant provider/runtime code and tests, and the organization/workspace pin changes. The OAuth2 regression fixture, Git count validation, 2000/2001 boundaries and secret-draft exclusion have focused coverage. No additional findings in the organization or workspace changes. Organization flake evaluation is now reported passing by the coordinator.

Residual validation: committed browser acceptance has not run, and packaged/profile deployment, Firefox navigation cancellation, hidden-tab restoration and isolated live App Server acceptance remain pending. These are required follow-up checks after reconciliation, not results established by this review. The temporary reproduction initially encountered existing inconsistent vendor contents; `-mod=readonly` allowed the focused test without modifying vendor data. No project files or long/live tests were changed or run.
