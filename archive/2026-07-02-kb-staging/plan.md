# 2026-07-02-kb-staging

## Goal

Enable a safe KB article draft workflow for Codex-authored user
documentation:

- drafts are created under an agreed DokuWiki namespace on
  `kb.vpsfree.cz` or `kb.vpsfree.org`;
- draft writes happen only after a local preview and explicit approval;
- published pages can be refined from drafts later;
- `vpsfree-irc-bot` does not announce draft page changes on IRC;
- production configuration can deploy the updated bot behavior.

## Affected repositories

- Workspace coordination repository:
  `/home/aither/workspace/ai/vpsfree.cz`
  - Document the KB draft workflow for future Codex sessions.
  - Existing `AGENTS.md` already contains DokuWiki token and write-approval
    rules; extend that section, or add a companion durable note if that is
    clearer once the current local `AGENTS.md` changes are reviewed.
- `vpsfree-irc-bot`
  - Worktree:
    `worktrees/2026-07-02-kb-staging/vpsfree-irc-bot`
  - Branch: `2026-07-02-kb-staging`
  - Implement general DokuWiki page include/exclude filtering.
- `vpsfree-cz-configuration`
  - Worktree:
    `worktrees/2026-07-02-kb-staging/vpsfree-cz-configuration`
  - Branch: `2026-07-02-kb-staging`
  - Pin/deploy the updated bot revision and configure the KB draft namespace
    to be excluded from IRC announcements.

## Approach

1. Use the draft namespace for KB staging.
   - Decision: use `drafts:` on both wikis unless the user explicitly requests
     another draft namespace for a future article.
   - Bot exclusion pattern would then be `drafts:*`.
   - If language-specific namespaces are later preferred, use explicit prefixes
     as `cs:drafts:*` and `en:drafts:*`.

2. Document the Codex KB drafting workflow in the workspace.
   - Add future-facing instructions near the existing DokuWiki section:
     prepare a local preview file first, authenticate/read-check the target
     wiki, write only to the approved draft namespace after explicit approval,
     and publish/move to the final namespace only after another approval.
   - State that draft pages are intentionally hidden from IRC announcements by
     the configured bot filters.
   - Do not record API tokens, page write responses containing sensitive data,
     or full token-bearing commands.

3. Implement filtering in `vpsfree-irc-bot`.
   - Add DokuWiki wiki config keys for page filters, for example:
     `include_pages` and `exclude_pages`.
   - Treat patterns as shell-style globs via `File.fnmatch?`, matched against
     DokuWiki page IDs such as `namespace:page`.
   - Default behavior remains unchanged:
     no include/exclude config means every page is eligible.
   - Filtering happens before expensive per-page calls, so ignored pages do not
     fetch versions, diffs, maintainers, or send announcements.
   - Update `dist/config.yml.sample` with documented example settings.
   - Add focused specs for:
     - no filters preserving current behavior;
     - `exclude_pages: ["drafts:*"]` suppressing create/change/delete notices;
     - include and exclude precedence, with excludes winning when both match.

4. Update `vpsfree-cz-configuration`.
   - After the bot branch is reviewed and pushed, update
     `packages/vpsfree-irc-bot/default.nix` to the new Git revision and hash.
   - Add the configured `exclude_pages` pattern to both KB entries in
     `cluster/cz.vpsfree/containers/int.vpsfbot/config.nix`.
   - Keep the deploy change separate from the bot functional change.

5. Review before longer tests.
   - Once intended changes are committed and quick checks pass, run the
     mandatory change review with a standalone agent before any longer
     integration test or deployment validation.

## Compatibility and deployment

- Bot compatibility:
  - Existing configurations without filters continue to announce all DokuWiki
    changes.
  - New filter keys are optional and consumed only by the updated bot.
  - The runtime config format is additive; rollback to the old bot would fail
    only if the old bot rejects unknown settings. The current bot stores wiki
    options and directly reads known keys, so extra keys should be harmless.
- KB behavior:
  - DokuWiki page storage and ACLs are unchanged.
  - Draft namespace choice affects editor workflow and bot filtering only.
  - Rollback does not affect existing draft pages; it would only resume IRC
    announcements for draft page updates if the filter is removed or the old
    bot is deployed without filtering.
- Deployment order:
  - Deploy the new bot package and matching `exclude_pages` config together in
    `vpsfree-cz-configuration`.
  - No coordinated vpsAdminOS node update is required; this is limited to the
    `int.vpsfbot` service/container and workspace documentation.
- Security:
  - No DokuWiki API token is committed or written into notes.
  - Any future draft page write still requires local preview plus direct user
    approval before calling `core.savePage`.

## Testing plan

- `vpsfree-irc-bot`:
  - Enter `nix develop`.
  - Ensure hooks/gems are available before commit.
  - Run `bundle exec rspec`.
  - Run `bundle exec rubocop` if Ruby files changed.
  - Consider `./test-runner.sh test suite/irc-basic` if filtering touches
    runtime plugin wiring beyond the DokuWiki unit tests.
- `vpsfree-cz-configuration`:
  - Enter `nix develop`.
  - Use a prefetch/build command to update and verify the bot package hash.
  - Run `nixfmt`/Overcommit hooks for touched Nix files.
  - Evaluate the affected service with
    `confctl build "cz.vpsfree/containers/int.vpsfbot"`.
  - Optional dry-run:
    `confctl deploy "cz.vpsfree/containers/int.vpsfbot" dry-activate`.
- Workspace docs:
  - Review rendered Markdown/plain text for clarity.
  - Verify no token values or write-capable API command transcripts are
    recorded.
