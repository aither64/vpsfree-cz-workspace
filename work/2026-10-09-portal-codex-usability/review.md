# Independent review

Reviewer `/root/final_review`, GPT-6 Astra/xhigh/read_only, installed default
lead_reviewed catalog role. Threadless initiative has no retained roster.
Risk high; lanes general, architecture/repetition, scope/proportionality,
risk/compatibility. Initial heads and complete eight-commit inventory are in
[review-packet.md](review-packet.md). No live reset consumed.

No Blocking findings. Four Important findings:

1. General/risk: stale tabs could overwrite another unresolved reset attempt or
   remove its record. Fixed with an origin-scoped Web Lock across authoritative
   reload, check, persist, RPC and removal; storage events update other tabs.
   Coordination unavailable fails closed. Five mocked controller tests pass,
   including stale two-tab use, contention, uncertain outcome and same-key retry.
2. General/architecture: failed automatic history repair lost its retry on hiding
   during backoff. Both browser integrations now resume that retry after showing;
   manual older-page failure still waits for Retry. Provider regression passes;
   portal real-browser fixture updated and pending execution.
3. General: compact limits dialog omitted allowance windows and reset times.
   Shared window renderer now fills both sidebar and dialog. Narrow-viewport
   browser regression prepared.
4. General: layout fixture required a div in a button/select collection.
   Mode visibility now checked separately.

Reviewer found the eight-commit series coherent, no obsolete unmerged approaches
or redundant pin updates, and **no migrations**. Account origin checks, live
identity verification, cache invalidation, optional protocol fields and native
text paste fit the documented boundaries. Long checks and deployment were pending.

A focused affected-lane rerun is required for the new cross-tab coordination
design. Narrow history/window/layout fixes receive direct inspection and checks.

## Additional verification correction

CI at runtime 901af601 failed only TestBrowserClientShipsMessageAndLifecycleInteractions:
a string assertion expected a literal 1000 instead of refreshPolicy.indexProgressMs.
The assertion now checks the shared policy and passes locally. Raw failed logs
are in /tmp/portal-old-runtime-ci.log; the new exact head must pass CI.

## Focused rerun

The same independent Astra/xhigh reviewer inspected runtime 26640fb5 / account
commit 3ec36265 in all four affected lanes. No findings. Authoritative reload,
persistence, RPC and removal remain under one origin lock; pending attempts
block new Use, missing locks fail closed and contention sends no request.
Five mocked controller tests passed independently. No server contract or migrations.
Real cross-page browser lock/storage events and stalled-request behavior remain
verification limits; a pending attempt survives page closure for explicit retry.

## Real-browser follow-up

The complete seven-case browser suite passes across the initial batch and
focused corrections. Lifecycle, repository review, settings and history paging
passed at 26640fb5. Question and usability passed at 496c0995; presentation
passed in Chromium and Firefox at 675504f6. Changes after reviewed 26640fb5
are confined to three browser fixtures, directly inspected and checked under
the skill's narrow-fix policy. Two actual browser pages now exercise native
Web Lock contention and shared-storage updates; no redemption is sent on
contention. The mocked lost response reload retries the identical UUID once.
Native Ctrl+V text, binary file attachment and mixed paste also pass.

Obsolete test expectations addressed the old ten-second grace and earlier
archival metadata/menu layout. Each failed attempt's logs were inspected
before rerunning; no application change was needed. Corrections were folded
into their owning unmerged commits. Final series remains eight focused
commits with no migrations or obsolete approaches.
