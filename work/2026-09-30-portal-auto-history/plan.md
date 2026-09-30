# 2026-09-30-portal-auto-history

## Goal

Replace the portal's persistent Load older transcript button with automatic, user-initiated upward history loading. Preserve the visible-message anchor, prevent request cascades, retain centered loading/error/retry feedback, add focused browser coverage, review the complete change, and prepare an aitherdev deployment without merging the feature branch unless separately authorized.

## Affected repositories

- `dev-workspace`: portal transcript template, browser behavior, styling,
  focused browser coverage, and the portal behavior guide.

## Approach

- Remove the normal `Load older` control. Keep the history control row only for
  transient loading, compatibility, error, and retry feedback, centered above
  the transcript.
- Start one older-page read when user-originated upward navigation reaches
  within 200 pixels of the transcript top. Cover wheel, touch, scrollbar, and
  keyboard input, including upward input when the viewport is already at the
  top and cannot scroll.
- Reuse the existing page cursor, timeout, hidden-document, legacy-server, and
  in-flight request guards. Preserve the current visible-message anchor while
  prepending.
- Require further upward user navigation before loading another page.
  Programmatic scroll restoration, resize, rendering, and filter changes must
  not create a request cascade.
- Stop automatic retries after an error. Keep a centered `Retry` action that
  repeats the failed older-page or continuity-repair read.

## Decisions

- Automatic loading fully replaces the normal button, as selected by the user.
- The near-top threshold is 200 pixels. The page size remains 100 items.
- The existing history row remains the accessible status region. Loading copy
  is `Loading earlier messages…`; existing reconnect, unavailable-server, and
  continuity-repair messages remain intact.
- This is a bounded portal edit and goes directly to the ready implementation
  member. No separate architecture brief is needed.
- The previous portal-performance initiative is complete. This follow-up uses a
  new branch and does not inherit its default-branch merge authorization.

## Compatibility and deployment

- No API, schema, cursor, persisted-state, protocol, or package-input change is
  required. The browser continues to use the existing optional transcript-page
  endpoint and legacy fallback.
- Browser and server assets ship in the same user-profile package generation.
  Rolling back selects the previous UI and does not need data conversion or
  cleanup because the change creates no state.
- Build and deploy the reviewed feature branch through the aitherdev workspace
  user profile. Do not change `vpsfree-cz-configuration` for this application
  iteration.
- Keep the feature branch unmerged until the user explicitly authorizes
  integration into `dev-workspace` `master`.

## Documentation

- Update `docs/workspace-portal.md` so the current transcript history behavior,
  loading feedback, and retry semantics no longer describe a manual button.
- No KB change is useful: this is operator-facing workspace tooling rather than
  member-facing vpsFree.cz product documentation.

## Testing plan

- Extend the live Playwright paging test to prove that initial and programmatic
  scrolling do not fetch older pages, upward user input fetches exactly one
  page, and the visible anchor shifts by less than the existing tolerance.
- Cover request de-duplication, no recursive page cascade, history exhaustion,
  upward keyboard input at a non-scrollable top, read failure, and successful
  explicit retry.
- Run JavaScript syntax and focused portal browser checks before review. After
  mandatory independent review, run the broader package verification, CI, and
  an aitherdev smoke test against a long conversation.
