# Mandatory review packet: dev-workspace

## Review identity

- Repository: `dev-workspace`
- Worktree: `worktrees/2026-09-30-portal-auto-history/dev-workspace`
- Remote default branch: `origin/master`
- Exact refreshed base: `d20bb64c45db1d803fc3b7a8c2956049860d72dd`
- Exact feature head: `7c133c562ac51076c1f45af46e180f8bfbabe836`
- Reviewer: retained `reviewer0`, saved `gpt-6-sol` with xhigh effort and
  read-only access
- Risk: medium. This changes interactive browser behavior and package rollout,
  but has no persistent data, API, schema, protocol, authorization, or secret
  handling impact and is recoverable with a newer reverting package.

## Required lanes

- General review
- Architecture and repetition review
- Scope and proportionality review
- Risk and compatibility review

The review must use the canonical mandatory-change-review workflow and the
corresponding lane references. Report each finding as Blocking, Important, or
Advisory with file and line evidence, or explicitly report no findings for a
lane.

## Requested behavior

- Remove the persistent normal-state `Load older` button.
- Automatically request exactly one older page when deliberate upward wheel,
  touch, keyboard, or native scrollbar navigation reaches within 200 pixels of
  the transcript top, including upward input at an already non-scrollable top.
- Require another user input before another page request. Rendering, anchor
  restoration, resize handling, filter changes, and other programmatic motion
  must not cascade requests.
- Preserve the currently visible message anchor while prepending history and
  while the centered status/error control changes state.
- Keep existing paging capability, cursor, timeout, hidden-document,
  unavailable-server, continuity-repair, and in-flight serialization behavior.
- Preserve an older-page or repair failure across unrelated newest refreshes;
  explicit centered Retry must repeat the failed operation without automatic
  retries.
- Update durable portal behavior documentation and focused browser coverage.

## Design and boundaries

- Accepted plan: `work/2026-09-30-portal-auto-history/plan.md`
- Architect brief: `work/2026-09-30-portal-auto-history/design.md`
- Application documentation: `docs/workspace-portal.md`
- Affected application files:
  - `portal/internal/web/static/app.js`
  - `portal/internal/web/static/style.css`
  - `portal/internal/web/templates/session.html`
  - `portal/internal/web/paging_browser_live_test.cjs`
  - `docs/workspace-portal.md`
- No `codex-web`, `vpsfree-cz-configuration`, dependency, lockfile, generated
  output, endpoint, server contract, or package-input change is in scope.

## Complete history and final diff

`origin/master..HEAD` contains exactly one commit:

```text
7c133c5 portal: load older transcript pages on upward input
```

The final diff contains 362 insertions and 45 deletions across the five files
listed above. Test-fixture corrections discovered during focused verification
were amended into the owning unpushed commit. No superseded committed approach,
fixup commit, compatibility shim for an abandoned iteration, or unused
transition remains.

The initial all-lane review found a Blocking queued-repair timer race and an
Important deferred-threshold coverage gap. Both are amended into the same
commit: retryable failures cancel pending repair timers, timer callbacks recheck
typed failure/error and live repair state, the race has a concurrent newest-gap
regression, and native wheel coverage now starts at 260 pixels and crosses the
200-pixel threshold. The same reviewer must confirm these resolutions against
the complete amended branch.

There are no migrations. Therefore there is no migration lineage, unapplied
intermediate migration, released schema state, deployed schema state, or
external migration consumer to preserve.

## Compatibility and deployment

- Browser and server assets deploy atomically in the same user-profile package.
- The existing optional transcript page endpoint and legacy fallback are
  unchanged, so mixed server/browser API compatibility does not change.
- No persisted state is written. Older or newer packages can read all existing
  state because the feature creates none.
- Workspace package switches are forward-only. Recovery means building and
  switching to a newer package revision that restores the previous UI, not
  switching back to an older generation.
- The reviewed feature branch will be built and deployed through the aitherdev
  workspace user profile after review. No configuration-repository integration
  is needed. Default-branch integration is not authorized in this initiative.

## Verification evidence

Passing quick checks at the exact head:

```text
node --check portal/internal/web/static/app.js
node --check portal/internal/web/paging_browser_live_test.cjs
node portal/internal/web/paging_browser_test.cjs
git diff --check
PORTAL_BROWSER_TEST=1 CGO_ENABLED=0 GOWORK=off GOFLAGS=-mod=mod \
  go test ./internal/web \
  -run 'TestQuestionBrowser/paging_browser_live_test.cjs' -count=1 -v
```

The live Chromium check passes automatic paging, explicit retry, anchor
stability, exhaustion, keyboard, touch, native scrollbar, duplicate-request,
and independent newest/older read-lane scenarios. Playwright's default hidden
scrollbar argument is disabled only for this test so the real scrollbar thumb
can be exercised.

Longer package verification, remote CI, package build, deployment, and live
aitherdev smoke testing intentionally remain after findings are reconciled.

## Required conclusions

- Review the complete base-to-head history and final diff, not only selected
  snippets.
- Explicitly conclude whether obsolete branch history remains.
- Explicitly conclude that there are no migrations or migration-lineage risks.
- Reconcile implementation and documentation against the plan and architect
  brief, including the one-shot input gate, status-row anchor stability,
  persistent typed failure, legacy fallback, forward-only package transition,
  and recovery wording.
