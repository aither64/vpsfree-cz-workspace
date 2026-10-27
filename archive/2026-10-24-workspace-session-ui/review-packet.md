# Final review packet

## Requested result and scope

Implement four portal issues: consistent accessible settings switches; New output
based on content visible under the active filters/disclosure state; repeated
Send/Steer and Queue next submissions while earlier delivery is pending; silence
routine queued-message reads while retaining shared refresh deadlines/grace and
real errors. User approved implementation; no default-branch integration or
runtime deployment is approved.

Session: `2026-10-24-workspace-session-ui` in
`/home/aither/workspace/ai/vpsfree.cz`; see `plan.md`, `state.md`, `design.md`.
Repository/worktree:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-workspace-session-ui/dev-workspace`.
Branch: `2026-10-24-workspace-session-ui`, target `origin/master`.
Initial base: `b3a6eb2fc0b41cf0cb965bf4c39991815d9df734`.
Fresh fetch before assignment confirms `origin/master` remains the initial base;
the feature is ahead by exactly five commits, behind by zero.

Final committed head: `5293cf5b3d6752e804223833a1bb9d484e55b759`.
The worktree/index are clean. [Complete final diff](final.diff) and
[complete commit messages](final-history.txt) are saved alongside this packet.

Complete series, oldest first:

1. `439e33a596ab334c539271cb7ebac9e508acb564` settings switches.
2. `4b3817f4f39e73e6012a5b3a57f7c61769a48b03` visible unread and asset cache refs.
3. `74a55c8ba75c784683ee8d6fa386f6a9e3f52960` repeated composer submission buffer.
4. `dedf61d843796ddb1b6d7f3bf690ddf295bab12f` quiet queue reads and dedicated test.
5. `5293cf5b3d6752e804223833a1bb9d484e55b759` final guide reconciliation.

Each behavior is independently reviewable; final guide is one coherent prose
update. Capacity/orphan/retry fixes were made before the owning initial composer
commit, so no obsolete fixup commits remain. No dependency/channel/generated
update streams. No migrations; none merged, released, deployed or externally
consumed. New browser tab-local dispatch metadata is versioned separately from
existing delivery attempts; specifically review mixed-version/reload semantics.

## Quick verification completed before review

All commands below ran in repository `nix develop`:

- 71/71 existing attention browser cases for settings; notification JS syntax,
  gofmt of updated assertion and diff checks.
- `node --check portal/internal/web/static/app.js`, composer and paging live
  browser test scripts (authored browser tests not executed yet).
- From `portal/internal/web`: `node composer_handoff_contract_test.cjs`,
  `node paging_browser_test.cjs`, `node submission_notice_contract_test.cjs`,
  `node --test read_cycle_browser_test.cjs` (17/17).
- Pinned conversation asset imported from
  `/nix/store/549mbnzpbcs81ccvvv4wrh9xmjrxg86n-source/conversation/assets/conversation.js`;
  shared `refresh_presentation_contract_test.cjs` and awaited dedicated
  `queue_refresh_presentation_test.cjs` complete successfully.
- Final syntax/composer/paging/submission rerun after capacity/orphan/readback
  cleanup; `git diff --check base..HEAD` passes.

Regressions cover full buffer/rejected 21st/no orphan/reload recovery, failed
ordered capture cleanup only for provably fresh never-dispatched IDs, unknown
no discard/overtake, failed input edit/new ID/same attachments, confirmed save
retry with no extra HTTP, visible filter/disclosure projection and history.
No package, real browser, native integration or deployment checks run yet.

## Review policy

Risk: high, because browser persistence/uncertain message delivery must preserve
IDs and attachments across retry, late HTTP results and reload. Lanes: general,
architecture/repetition, scope/proportionality, risk/compatibility. Read the
mandatory-change-review skill and all four lane references. Retained independent
reviewer0: `gpt-6.1-sol`, saved `xhigh`; no override/fallback. Do not edit source
or spawn nested reviewers. Final review only after all code committed/quick
checks pass, before any long verification.

## Boundaries and consumers

Portal owns browser presentation/dispatch. `codex-web` is pinned at
`11ec57d2203fc735696fe75a837d47da55a5c6af` via Go and flake input, unchanged.
Existing message/queue endpoints, native FIFO, retries and exact-ID receipts
remain the provider contract. No new protocol, server state migration, settings
save-handler redesign, host/module configuration or runtime package selection.
Local operator is trusted per repository AGENTS; remote clients remain untrusted.
Preserve ordinary concurrency, identity, authorization and recovery checks.

Browser buffer is per tab/conversation, max 20 including active. Original action,
IDs and attachment IDs retained; dispatch one request at a time; model completion
need not precede another send. Reload pauses remaining intent. Uncertain outcome
fences later dispatch, cannot be discarded as unsent. Definitely unsent input can
be edited/discarded; confirmed delivery retries local status saving without HTTP.
Native concurrent steer consumption/execution order is not promised across other
clients/queued turns. No live runtime/settings/lifecycle mutations were performed.

## Acceptance inspection and documentation

Lead applied user-facing-writing directly to unchanged settings labels/new UI
labels and `docs/workspace-portal.md`. README already links that guide. Feature
explanations and recovery semantics stay in the project guide; temporary test
and rollout evidence stays in this session. No rollout executed/prepared.

Review all four behaviors, failure/reload/draft/attachment identity and filter
state, ensure no stale helper/timer or disproportionate new machinery, and
explicitly conclude whole-branch history, no migrations (if verified), obsolete
follow-up dispositions and repeated dependency/generated update streams.

## Source/operation inventory

Lead confirmed no diff in `flake.nix`, `flake.lock`, `portal/go.mod`,
`portal/go.sum`, `libexec/` or `nix/`; SSH origin is
`git@github.com:aither64/dev-workspace.git`. No hook framework is declared,
`core.hooksPath` unset, and no executable non-sample hook was found. All feature
commits ran from repository Nix environment with message files. No branch
publication/deployment yet; all history remains unmerged and unapplied.

Reviewer remains fully read-only under saved instructions, including session
files. Its final report will be delivered to lead and preserved verbatim by the
lead; it will not write `review.md` itself.
