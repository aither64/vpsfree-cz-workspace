# Mandatory review packet: codex-web

## Review assignment

- Reviewer: retained `reviewer0`, model GPT-6 Sol, reasoning effort xhigh,
  read-only access.
- Risk: high. The change adds an authenticated transcript paging API over
  persisted Codex rollout data, cursor continuity rules, bounded metadata
  caching, and browser state reconciliation for live conversations.
- Lanes: general, architecture and repetition, scope and proportionality, and
  risk and compatibility.
- Canonical procedure: `~/.codex/skills/mandatory-change-review/SKILL.md` and
  every selected lane reference under its `references/` directory.

## Repository and history

- Repository: `worktrees/2026-09-29-portal-performance/codex-web`.
- Feature branch: `2026-09-29-portal-performance`.
- Initial base: `e92dd887c888d5a9f50c70febc714f875cb44378`.
- Review head: `f16fcff6fa9a5476545c98b50ecf1c2db04bf602`.
- Complete base-to-head series:
  1. `0fad2e12e4156f512f1642222e065cabc0da72a7` — `codex: page transcripts without loading full turns`
  2. `f16fcff6fa9a5476545c98b50ecf1c2db04bf602` — `browser: page mounted conversations incrementally`
- The worktree is clean. There are no schema or data migrations.
- The first commit was pushed for early CI feedback; GitHub Actions Check run
  `36598475658` passed. The second commit is not pushed. Neither commit is on a
  default branch or deployed.

## Intended behavior

- Add an optional authorized `/thread/page` route that returns at most 100
  transcript entries, newest first by page, with opaque continuation cursors.
- Read only the bounded rollout regions required for a page instead of loading
  and parsing an entire large rollout on every refresh.
- Cache derived rollout metadata for at most 60 seconds, serve bounded fresh
  reads while rebuilding due metadata in the background, and invalidate on
  supported append-writer changes.
- Keep the existing `/thread` contract for mixed-version clients and explicitly
  return `501 transcript_paging_unavailable` when paging is unsupported.
- Make the generic mounted conversation load the newest page independently of
  pending prompts and queue reconciliation, retain loaded older entries, repair
  gaps or active-turn updates, preserve stable DOM nodes and scroll position,
  and acknowledge durable sends against all retained entries.
- Fall back to `/thread` only for a missing page route or the explicit 501
  capability response. Authorization, server, timeout, cursor, abort, and
  malformed-response failures must not weaken into fallback.
- Expose the same page reader, history model, and entry-key helpers to custom
  consumers so the workspace portal does not duplicate the reconciliation
  rules.

## Acceptance criteria

- A large conversation renders the newest page without waiting for full-history
  parsing, pending requests, or queue reconciliation.
- **Load older** appends history without duplicate entries or losing already
  rendered nodes; cursor expiry/reset recovers through a fresh newest page and
  gap repair.
- Live refreshes preserve previously loaded history and do not treat absence
  from a bounded newest page as deletion or failed send acknowledgement.
- Paging authorization is no weaker than the existing thread read, cursors are
  bounded and retryable, and malformed or cross-thread pages fail closed.
- Existing clients and servers continue to interoperate through the legacy
  route and explicit capability fallback.
- Metadata freshness never exceeds the documented 60-second bound under the
  supported append-writer model; authoritative checks remain server-side.
- The deployed portal later meets a 2-second p95 usable-render target for 30
  normal loads and 30 loads overlapping a dry-run archive scan. That live gate
  is intentionally not part of this pre-push quick review.

## Compatibility, deployment, and recovery

- API addition is optional and backward compatible. Old clients retain
  `/thread`; new clients use strict fallback only when paging is absent.
- No persisted format, database schema, Codex protocol write, or migration is
  introduced. Cursor tokens are ephemeral and may be rejected after rollout
  replacement or incompatible metadata change.
- The page parser is checked against the pinned Codex 0.155.0 protocol corpus.
  Mixed-version operation and failure behavior are review targets.
- Deployment will occur only after the downstream pin chain is committed,
  reviewed, built, and pushed. The user-profile package is switched through
  `workspace-host`; no system configuration pin is changed.
- Profile rollback is not a valid recovery path because the current workspace
  has forward-only team registration state. Recovery must use a newer package
  that retains current readers and site composition while disabling or fixing
  the new paging path.

## Consumers and adjacent work

- Generic consumer: `conversation/assets/conversation.js` in this repository.
- Downstream custom consumer under implementation:
  `worktrees/2026-09-29-portal-performance/dev-workspace/portal/internal/web/static/app.js`.
  It imports `createTranscriptHistory`, `readTranscriptPage`, and
  `transcriptEntryKey` instead of maintaining a duplicate model.
- Downstream exact source pins are deliberately uncommitted until this review
  is reconciled and the final feature head is pushed.

## Explicit non-goals

- Do not change the legacy `/thread` payload size or remove it.
- Do not expose conversation contents, weaken existing read authorization, or
  make cursors durable across arbitrary rollout rewrites.
- Do not identify or repair unrelated historic transition-lock holders.
- Do not merge a feature branch, change a default branch, deploy, archive the
  session, or change vpsFree.cz system configuration in this review.

## Verification evidence

- `node --check conversation/assets/conversation.js`
- `node --check test/paging_browser_contract_test.cjs`
- `node --test test/paging_browser_contract_test.cjs test/conversation_browser_contract_test.cjs test/uploads_browser_contract_test.cjs test/sync_browser_contract_test.cjs`
  passed 47 tests.
- `TMPDIR=/tmp/codex-web-test go test -mod=readonly ./...` passed all packages.
  The short temporary path avoids the Unix-socket path-length failure caused by
  Nix's long temporary directory.
- `git diff --check` passed.
- The initial unqualified `go test ./...` selected stale repository vendor mode;
  no vendor files were changed. The locked `-mod=readonly` result above is the
  applicable source check.

## Reviewer deliverable

Start with findings ordered by Blocking, Important, then Advisory, with file,
line, and commit references where possible. Explicitly assess authorization and
data exposure, cursor and rollout mutation behavior, metadata freshness and CPU
trade-offs, live reconciliation and durable-send correctness, mixed-version
fallback, cross-project helper reuse, commit scope, and test gaps. If there are
no findings, say so clearly and still list residual risks and verification
gaps. This is an incremental pre-push review; final branch-readiness history and
migration conclusions will be requested separately after the full pin chain and
live acceptance are complete.
