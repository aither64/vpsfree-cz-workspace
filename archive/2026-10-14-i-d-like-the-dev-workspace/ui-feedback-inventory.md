# UI feedback frozen inventory

Frozen runtime head: `867682c3df251fbe6941ff9a667539ae1af790ec`; clean registered worktree.
Parent/deployed source: `6e1d9a191724d376cad2a71f234f0e4d1c01f36f` (preserved unchanged).
Integrated branch base: `832d9f1a6a21337dd44063ddf39f7a88cfc95450`.
The UI fix is one new coherent fourth commit; no existing commit was amended.
Publication and long/browser checks are held for the lead's final deliverable
review and delivery-scope decision.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/>

## Result and scope

Browser notifications is reached through the existing native workspace menu,
with the same separate-page navigation as Operations and Automatic archival.
The index no longer renders or initializes browser-level notification controls;
its per-session creation checkbox remains. The standalone page and session
Settings use the same existing controls with scoped flex wrapping and gaps.
The native popover's focus, dismissal and keyboard behavior is reused unchanged.

Owned application/test paths (seven):

- `portal/internal/web/notifications_browser_test.cjs`.
- `portal/internal/web/notifications_test.go`.
- `portal/internal/web/server.go`.
- `portal/internal/web/static/style.css`.
- `portal/internal/web/templates/index.html`.
- `portal/internal/web/templates/notifications.html`.
- `portal/internal/web/templates/session.html`.

There is no browser-notifications.js overlap. Sender, transport, worker, shared
store, attention reducer and notification persistence are unchanged. Module
files and vendorHash are unchanged. `ui-feedback-freeze.json` contains independent
Git-byte comparisons and SHA256s. The new GET route uses the existing guarded
handler, render path and security-header/CSP wrapper, rendering only the reused
public panel and display label; it exposes no private state or external data.

Only the existing Browser notifications and Back to workspace labels/title are
newly placed. The lead directly approved the exact
`ui-feedback-visible-copy.patch` using the writing and Humanizer skills.
The existing descriptions/buttons are unchanged. No durable feature-doc rewrite
was useful for this navigation/layout correction; the panel explains its
unchanged behavior and the existing notification guide remains accurate.

## Quick evidence

Cached declared runtime environment, Node24.19.0 and Go1.26.6; no Nix daemon.
All commands and output are retained in new ui-feedback-*.log/status files:

- `gofmt -w portal/internal/web/notifications_test.go`: PASS.
- `node --check portal/internal/web/notifications_browser_test.cjs`: PASS.
- `node portal/internal/web/attention_browser_test.cjs`: PASS, 15 named tests,
  no failures/skips (0.315s command).
- `go -C portal test -mod=readonly -count=1 ./internal/web -run
  '^(TestNotificationsPageIsSeparateFromIndex|TestAutomaticArchivalPageIsSeparateFromIndex|TestOperationsNavigationDoesNotReadOrEmbedStatus)$'`:
  PASS, three tests, package0.100s (26.929s including compilation).
- `git diff --check`: PASS.

Go used GOMODCACHE=/tmp/session-webpush-mod,
GOCACHE=/tmp/session-portal-go-cache and GOPROXY=off. No dependency acquisition.
The Go regression checks real template navigation boundaries and retains the
new-session preference. The CJS source prepares desktop/mobile control spacing,
menu keyboard/focus navigation, initialized hidden Settings and no-load permission,
worker-registration or subscription mutation assertions. Its syntax passed;
actual browser execution has NOT run and awaits final review.

No declared hook framework is present in the runtime repository. core.hooksPath
is unset and the normal Git hook directory has sample hooks only. No hook bypass
was used. The normal commit used the <=80-column body file
`/tmp/session-ui-feedback-commit-message.txt`; retained copy
`ui-feedback-commit-message.txt`. Commit log/status record success.

## Future browser command (lead only, after review)

From the registered runtime worktree:

```sh
source /home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace/runtime-dev-env.sh
export GOMODCACHE=/tmp/session-webpush-mod GOCACHE=/tmp/session-portal-go-cache GOPROXY=off
export NODE_PATH=/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules
export PLAYWRIGHT_BROWSERS_PATH=/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers
PORTAL_BROWSER_TEST=1 go -C portal test -mod=readonly -count=1 -v ./internal/web -run '^TestNotificationsBrowser$'
```

Run under the lead's fresh watcher/fallback as required; member socket restrictions
remain outside the product. This fixture uses synthetic subscription/delivery
for template/CSP/worker plumbing and UI contracts. It is not provider acceptance
or macOS/physical display proof. No browser/provider/native operation was started.

## Whole-branch history and migration provenance

`ui-feedback-series.txt` lists all four owning commits over the integrated base:
feature96717cde, provider diagnosticsbb9e6291, processgroup test6e1d9a19,
then this new UI867682c3. `ui-feedback-change.patch/stat` is only the UI delta;
`ui-feedback-whole-branch.patch/stat` captures the complete branch. The earlier
published/deployed source6e1 remains intact. All prior review/evidence/probe
packets remain untouched; no stale live fixture was relabeled for this head.

This UI change introduces no persistent format, schema, endpoint mutation,
worker protocol or migration. The prior feature's initial private notification
store version1 and optional creation flag remain as reviewed; old omitted
receipts remain supported, newly flagged receipts require the capable bundled
helper and forward-only transition pairing. No prior state or migration was
rewritten. Provider diagnostics and processgroup-test commits add no persisted
formats. The integrated upstream capability journal remains upstream supported
lineage, distinct from feature notification state. Original provider/processgroup
failure causes remain unproved. No host, queue, reservation, lifecycle, package
transition, deployment, publication or pin operation occurred for this UI task.

Lead owns state/artifact registration, affected final review, delivery investigation,
publication and downstream composition. No source readiness beyond quick-checked,
committed UI is claimed here.
