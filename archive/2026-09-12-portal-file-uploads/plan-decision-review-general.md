# General review: current plan decisions

Reviewed the committed follow-up series described in
`plan-decision-review-packet.md`:

- codex-web
  `4a4c77b4acc2bbaef44e2327c37d9c984e091867..c0fbae9d4828bb05fdf5f17f9b85a66eaf98c612`
- dev-workspace
  `14871f50bb6f57542d3452de32924357ff629037..d2cdeabd6c43423491eead1b4cca7f8d2e866946`
- vpsfree-dev-workspace
  `6063618bcf1fc3eefe57187a22ccc3b1bf0b22b6..58c2dde52958a8e11fcb6decc2287b5e0a4dec11`
- workspace
  `96ec50e609a48372fc4ab5300e34dc12f6ba9733..545bf2df04e2844ecfa9ffa33a7e611f1d0ff6f4`
- vpsfree-cz-configuration
  `c79a68ea6ef80dcaaef95cf17950fa87afbe976d..15abf6b9ce8431537b8a16b538dd765357d00db9`

The review used gpt-5.6-sol with xhigh reasoning effort and inspected the exact
commit series, repository guidance, follow-up plan/state, implementation,
focused tests, documentation and downstream pin graph.

## Findings

No Blocking, Important or Advisory findings.

The provider records `latestTurnId` from the first descending history page's
actual newest raw turn after restoring display order, so an empty latest turn
still invalidates older rendered plans. A missing turn identity fails closed.
The runtime's shared plan selector requires that exact turn, a completed plan
item and nonempty text, and both same-session and new-session implementation use
it under the existing message lock. Validated creation retries retain their
captured goal and settings without rereading the source.

The extracted `ReconcileSend` path preserves `Send`'s existing accepted and
submitting behavior. It returns accepted receipts or reconciles history under
the existing per-thread lock, while absent and prepared attempts cannot resume
a thread, start a turn or change settings. The same-session handler performs
that recovery before freshness validation, then subjects any still-prepared or
new request to the current-plan and collaboration-mode checks.

The browser hides the existing composer node rather than rebuilding it, so its
draft, upload controller, attachments and settings remain mounted. The plan
state class hides only the redundant waiting strip; delivery receipts and the
queue remain outside the hidden form. Focus moves between the composer and
decision controls, async digest renders are generation-guarded, and page-local
dismissal includes both turn and content identities.

## Commit series and verification

The two provider commits separate transcript metadata from the independent
non-submitting recovery API. Dev-workspace keeps the provider pin, server
freshness/retry behavior and browser presentation in three focused commits.
Each downstream repository contains one pin-only commit. Every reviewed commit
is the direct descendant expected by the packet, commit subjects and bodies
match repository rules, and no fixup or superseded design commit remains in the
ranges. The generated configuration message is unchanged.

The lock graph consistently selects provider `c0fbae9`, runtime `d2cdeab`,
organization package `58c2dde` and workspace package `545bf2d`; no unrelated
committed change appears in the ranges. `git diff --check` passed for all five
ranges. Reviewer `GOWORK=off GOFLAGS=-mod=mod go mod tidy -diff` produced no
module-file change. The packet's provider/runtime full Go suites, browser
contract and JavaScript syntax check were already green and were not repeated.

## Residual validation gaps

- The prepared real-browser fixture has not run yet. It should verify the
  complete form replacement, draft/upload preservation, waiting-strip removal,
  queue and receipt visibility, focus restoration, dialog cancellation and
  desktop/narrow layout in Firefox.
- The plan-turn and recovery tests use controlled App Server fixtures. A live
  Codex 0.154.0 check should confirm that an empty, failed, interrupted or newer
  ordinary turn is exposed as the latest turn, and that accepted/submitting
  implementation attempts recover without another submission.
- Exact-head Nix package/configuration builds, mixed cached-asset checks, live
  smoke testing and deployment are intentionally later phases. This lane
  inspected their pins but did not execute those longer checks.
