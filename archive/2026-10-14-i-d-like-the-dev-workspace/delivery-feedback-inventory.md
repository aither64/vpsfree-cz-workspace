# Delivery feedback and status-row removal: frozen source inventory

Final clean runtime head: `a5e41580d6dbeae9cbb468c707c22106f159066c`.
Fifth delivery commit: `43c6461e3f5ce900f72df7b2aa9593584884b04e`.
Sixth status-row removal: `a5e41580d6dbeae9cbb468c707c22106f159066c`.
UI base: `867682c3df251fbe6941ff9a667539ae1af790ec`; deployed6e1 remains intact.
Publication, long/native/browser checks, provider operations and downstream pins
are held for lead-owned committed affected final review.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/>

## Scope and result

The successful existing /test reply adds its exact queued event descriptor.
The browser retains one pending descriptor and one latest outcome in optional
fields of its existing attention record. Matching requires identity, event ID,
revision and expiry. Worker receipt is distinct from display API resolution or
rejection and matching browser-record present/absent/unavailable. Safe browser
error-name categories replace arbitrary error text. Exact repeated explicit tests
have fresh test-only tags; duplicate deliveries coalesce. Closing older entries
is bounded to32 and restricted to same-identity test metadata. Session tags,
focus acknowledgement and Reservations behavior are unchanged.

The page resumes its saved descriptor after reopening, polls local results and
the existing registration-wide provider status until expiry+10s, and stops on
completion/pagehide/Disable/replacement. A last provider result is explicitly
uncorrelated. Storage access and diagnostic notification reads have deadlines;
storage failure cannot prevent the worker's display attempt. Existing worker
updates/capabilities are checked honestly, without unregistering, resubscribing,
resetting keys or silently activating a waiting update.

The dedicated notification page loads shared store before client. Store/client
query versions2 and worker import2 prevent old cached helpers silently supplying
new features. The index panel/client is not restored; the existing native menu,
shared control spacing, hidden Settings and no-load subscription/permission
mutation contracts remain. The sixth commit only removes the user-requested
session-attention-status paragraph and changes the existing browser assertion
to count0. Every status write already tolerates absence; observer/title/presence
and persistent reservations are untouched.

The Firefox/macOS non-display cause remains unproved. These changes improve
correlated diagnosis; no provider acceptance, worker receipt or display API
resolution establishes physical screen appearance or click success.

## Owned paths and exact deltas

- `docs/browser-notifications-operations.md`.
- `docs/browser-notifications.md`.
- `portal/internal/web/attention_browser_test.cjs`.
- `portal/internal/web/notifications.go`.
- `portal/internal/web/notifications_browser_test.cjs`.
- `portal/internal/web/notifications_test.go`.
- `portal/internal/web/static/browser-notifications.js`.
- `portal/internal/web/static/notification-worker.js`.
- `portal/internal/web/static/session-attention-store.js`.
- `portal/internal/web/templates/notifications.html`.
- `portal/internal/web/templates/session.html`.

Fifth:11paths,525insertions/21deletions; sixth:2paths,1insertion/2deletions.
`delivery-feedback-change.patch/stat` covers UIbase->fifth;
`delivery-feedback-status-removal.patch/stat` covers fifth->sixth;
`delivery-feedback-combined.patch/stat` covers both assigned changes.
`delivery-feedback-freeze.json` binds full source identities, final path hashes
and10 protected unchanged blobs (store, transport, reducer, title observer,
menu/style, production processgroup, modules and vendorHash owner).

The sender/observer implementations in notifications.go are byte-unchanged;
that file's entire patch is only a local response descriptor and reply assembly.
No private server snapshot field was added. No additional endpoint, transport,
provider allowlist, SSRF guard, mute, lease, expiry/retry or cleanup behavior
changed. Existing two-selector subscription cleanup remains intact.

## Documentation and copy

Owning docs: docs/browser-notifications.md and browser-notifications-operations.md.
They distinguish queue/provider/receipt/display/record/physical appearance/click,
explain exact correlation, bounded local persistence, updates and unknown older
components. The feature guide correctly says display is attempted for every
push. Browser-local persistence prose is separate from server outbox/presence.

The lead directly applied writing/Humanizer to
`delivery-feedback-copy-review.patch`, approved it with four exact edits, and
those edits are preserved in `delivery-feedback-copy-final.patch`. No new visible
strings were added afterward; the last Enable-stop change only cancels an old
wait. The sixth removal adds no copy. Existing UI867 labels and copy stay intact.

## Quick verification and exact evidence applicability

Cached declared runtime env only: Node24.19.0, Go1.26.6,
GOMODCACHE=/tmp/session-webpush-mod, GOCACHE=/tmp/session-portal-go-cache,
GOPROXY=off and absent disposable provider catalog. No Nix daemon/dependency fetch.

Fifth source, tested before committing the identical source tree:

- `node portal/internal/web/attention_browser_test.cjs`:22namedPASS,
  original15retained; no failures/skips. Initial final command2.001s, followed
  by affected22-test rerun for the explicit Enable-stop refinement, PASS.
  `delivery-feedback-node-final.log/status` and `node-enable-stop.log/status`.
- `go -C portal test -mod=readonly -count=1 -v ./internal/web -run
  '^(TestAttention|TestNotifications|TestAutomaticArchivalPageIsSeparateFromIndex|TestOperationsNavigationDoesNotReadOrEmbedStatus|TestSessionPageUsesPersistentSidebarAndSectionPanels|TestSessionStylesUseMatchingPerResponseNonce)'`:
  22top-levelPASS, package0.511s/command7.246s, and1intentional real-browser skip.
  `delivery-feedback-go-final.log/status`.
- Node syntax for client, worker, shared store, unit module and actual-browser
  fixture:PASS; diff checkPASS. Per-file syntax logs/status and
  `delivery-feedback-quick-results.json` preserve commands/durations.

Final sixth source, tested before committing its identical two-line delta:

- Exact three Go template regressions (NotificationsPageIsSeparateFromIndex,
  SessionPageUsesPersistentSidebarAndSectionPanels and
  SessionStylesUseMatchingPerResponseNonce):PASS, package0.095s.
- Changed browser CJS syntax and diff check:PASS.
- `delivery-feedback-status-removal-{go,syntax,diff}.log/status`.

Meaningful actual-module contracts cover pre-display receipt vs final display,
resolved/rejected/safe errors, absent/unavailable browser records, no-tab push,
failed/stalled storage still attempting display, duplicate/reordered/other-tab
correlation, fresh tags, session ACK isolation, queue advancement/provider scope,
reload, pagehide, expiry, Disable, replacement and old server/helper/worker limits.
Go binds reply fields to the exact outbox event and checks descriptor privacy,
plus existing origin/payload/transport/SSRF/cleanup contracts. No test merely
mirrors the CSS implementation.

## Prepared browser verification, UNRUN

The existing actual-template CJS retains menu/focus/mobile+desktop spacing,
hidden Settings initialization and no-load mutation checks. It additionally
uses a correlated exact Test descriptor, synthetic push to the real worker with
zero tabs, persisted post-display resolution and reopen via the dedicated page.
Display errors/storage/update limits are covered in the quick actual-module
harness. Old proof/probe/fixture artifacts were not overwritten.

After committed affected final review and finding reconciliation, the lead may
run the exact final-head fixture via a fresh watcher/fallback from the registered
runtime worktree:

```sh
source /home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace/runtime-dev-env.sh
export GOMODCACHE=/tmp/session-webpush-mod GOCACHE=/tmp/session-portal-go-cache GOPROXY=off
export NODE_PATH=/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules
export PLAYWRIGHT_BROWSERS_PATH=/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers
PORTAL_BROWSER_TEST=1 go -C portal test -mod=readonly -count=1 -v ./internal/web -run '^TestNotificationsBrowser$'
```

No actual browser/provider/native/display/SSH/HTTPS/credentials/host operation
has run for this packet. Future native probes must read the exact post-display
outcome; old pre-display records alone are insufficient acceptance. Physical
Firefox/macOS and real click/authentication evidence remain required from the
user/authorized lead; Linux synthetic fixtures cannot provide it.

## Complete history and persistent lineage

`delivery-feedback-fifth-series.txt` preserves the requested5commitseries;
`delivery-feedback-final-series.txt` and `whole-branch.patch/stat` cover all6
owning commits over integrated832d9f1. Original feature96717cde, providerbb9e6291,
processgroup6e1d9a19 and UI867682c3 are unchanged. The already consumed6e1 and
all old source/probe/review/evidence packets remain preserved. New fifth and
sixth commits are coherent separate changes; no obsolete intermediate pin or
source commit was introduced, and nothing was published or amended.

There is no new server format, migration, dependency or vendorHash change.
The /test success reply is additive; old clients ignore its descriptor. Existing
IndexedDB v1/object store is unchanged: testPending/testOutcome are optional,
closed bounded field sets. Old records/workers/clients provide unknown detailed
results; new worker still accepts version1queued payloads. No old browser record
is rewritten as a migration. Server private notificationv1 and optional creation
flag remain as previously reviewed: omitted receipts supported, flagged receipts
need the capable bundled helper under forward-only transition pairing. Existing
subscription keys, VAPID, outbox, cleanup selectors and deletion obligations
retain their formats. Upstream capability-journal lineage remains protected
upstream behavior, distinct from feature notification metadata. Provider and
processgroup original failure causes remain unproved.

Normal Git commits used separate <=80-column message files with git commit -F.
No hook bypass; no declared runtime hook framework and core.hooksPath remains
unset (normal directory contains samples only). Commit log/status/message files
are retained. Lead owns state/artifact registration, committed affected review,
publication, downstream pins and authorized activation/execution. No queue,
reservation, lifecycle, host, package transition or integration action occurred.
