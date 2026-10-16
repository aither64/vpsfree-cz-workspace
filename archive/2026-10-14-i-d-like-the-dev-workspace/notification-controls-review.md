# Final affected review: global notification controls, sound and click focus

Retained reviewer0 report, recorded by lead from its completed report. One
Advisory; no Blocking or Important findings. The committed deliverable satisfies
its affected source-review gate after recording the Advisory disposition.
Browser/native sound/focus and final composition remain separate gates.

## Finding

Advisory — a cross-tab change can leave the new quick menu reporting stale
delivery state. Lanes: general/UI correctness and affected shared-state risk.
Eighth74d3f0d9530755882b33b89a53e93c7feae5898f, client lines271–275,430–438.

Two current-version documents: A says Enabled while B completes Disable. A's
cleanup/registration storage event correctly retires observations and sets
registered=false, but does not replace displayed status. observationRetired makes
menu-open/visible refresh return, so both surfaces may retain Enabled indefinitely
while Test is disabled. Publish existing honest incomplete/unconfirmed copy on
storage invalidation, preserve fences, and add storage-revocation/menu-open
regression. No automatic subscription repair, new persistence or old-tab protocol.
This presentation issue does not block existing cleanup or title observation.
Finding came from source flow; reviewer ran no reproduction test.

## Identity, scope and evidence

Retained independent reviewer0, GPT-6.1 Sol/xhigh/read_only; settings unchanged.
Reverified bound current/session, both absent DEV_SESSION identity markers and
live roster17/thread/settings. Applied mandatory-change-review and all four lane
references, workspace/runtime guidance and owning guides. Direct read-only
inspection; no nested agents, writes, tests/builds, network/provider/host/queue/
reservation/lifecycle operations.

Affected469757183ba9491d642b56e91658dc64e390647b ->
53f560fe3b898aa4544dae9376fcc7d6b1f33130.
Complete own832d9f1a6a21337dd44063ddf39f7a88cfc95450 -> same final.
Treeb68072c54f5ce069eba2dcd85ff78cabcd6cc647; clean at entry/final.
All25 manifest hashes, four exact Git patches, complete SHA/parent/messages,
series/stat and42 source blob/hash/worktree equalities match. First7 unchanged.
Affected12paths,+693/-97; whole42paths,+5953/-107. Server/store/transport,
attention/title observer, receipt helpers, modules/vendorHash/lock unchanged.
Earlier source conclusions retain unchanged boundaries; no confirmation rerun
of provider/processgroup or other unchanged lanes.

## Global controls and title independence

Shared index/session menu exposes existing explicit Enable/Disable and Play
sound; Test/detail remain full panel. Single per-document owner binds collections
directly to shared actions/state/rendering/busy guards, without hidden click
forwarding or duplicate cleanup. Index safely lacks full panel/Test and starts
no hidden Test polling. Load/menu-open/visible revisit observe and check bounded
worker readiness without permission/register/subscribe/Test/Disable/session-mute
mutations. Both surfaces block competing actions while an action owns the page.

Incomplete/server-cleanup states and saved-old-ID/current-digest obligations
remain, including local unsubscribe after server failure. Fully off requires
confirmed server removals and local absence. Provider-accepted push cannot be
recalled. Global off reuses registration/subscription removal, no pause flag.
Per-session preferences and title/reservation processing remain independent.
Unchanged session-attention observer/render/ACK continues even though presence
may return early. New actual-module contract exercises input, done, R2 and focused
ACK with delivery/sound off and no mute writes. No title regression found.

## Sound persistence and display

One strict IDBv1/sessions reserved singleton: browser-notification-sound identity,
boolean playSound, fixed at=Number.MAX_SAFE_INTEGER. Closed three-field reader
defaults only on absence; malformed present state unavailable. Ordinary update
rejects reserved identity. New pruner excludes it; fixed rank protects it under
exact deployed pruner while old pages remain open (old511 ordinary plus preference;
new512 plus preference). This protects the NEW saved choice, not old notification
semantics; no generic version/schema framework.

Open/transaction deadlines, transaction-completion resolution and overdue abort
where possible bound storage. UI displays committed/read choices, rereads uncertain
saves, guards stale reads and reports unsupported/unavailable/update limitation.
Menu and panel share committed state; revisit sees other tabs' saved choice.
Disable/re-enable preserves preference. One show helper reads immediately before
each native attempt, after status/receipt awaits, in all display branches. True
omits silent; false/corrupt/failed/stalled read requests silent:true. Never retry
rejected silent display audibly. Tags, payload, Test correlation/outcomes and
sender retry/expiry unchanged. Short storage deadline cannot block indefinitely.
No arbitrary private data or exception messages persisted.

Native silent capability and recorded options do not prove acoustic results;
browser/OS remain authoritative. soundReady is current-controller diagnostic
readiness, not OS proof. Mechanism and old-pruner protection are proportionate.

## Focus-only ninth

Independent53f560fe owns focus reuse/tests/guides. Strict safeRoute, same origin,
session slug and optional final slash; home distinct. Prefer target member,
otherwise existing matching view. Await exactly one focus; no navigate/reload/
member or section change/page message/worker ACK/new-tab retry. Rejected or
vanished client preserves promise failure; no duplicate. No-match keeps canonical
validated authenticated route and attentionIdentity. Existing-view focus is not
a fresh incarnation/authentication check; normal visible/focused page observation
owns that. Tests cover slash/query/hash, await/no navigation, member preference,
foreign/child/encoded/nonmatching/home boundaries, canonical open and failed/closed
client. Corrected user symptom is Firefox foreground without intended tab selection
in same window; actual cause is unproved. No-match opening is user-confirmed.

## Verification and documentation

Supplied eighth48 Node passes,5syntax, focused Go template PASS0.045s and diff;
ninth/final52 Node passes,0fail/cancel/skip,6628.63667ms,3syntax/diff. No checks
rerun by reviewer. Eighth Go/template files unchanged by ninth, not a new execution.
Meaningful tests cover format/default/commit/failure/deadline/abort/new+old prune,
all display paths/late soundoff/stall/no audible retry, shared controls/locks/
title independence and focus. Advisory cross-tab label case lacks coverage.

Browser fixture PREPARED/UNRUN: both-engine menu/keyboard/mobile/persistence/no-load
mutation, real worker takeover retaining tab/draft; Chromium-only synthetic push/
silent options/click listener. Untrusted synthetic focus may reject; no native
sound suppression, physical macOS selection or real click acceptance established.
No long/native/provider/host53f checks claimed.

Both owning guides accurately separate browser/global/session scope, title
independence, optional persistence, silent failure and focus/no-match. Main copy
pass reflected in source. Lasting behavior lives in runtime guides; individual
rollout/investigation evidence lives in session. No documentation/proportionality
finding beyond Advisory.

## Complete history, consolidation and migration

Exactly9 coherent owning commits, linear/no merges:
1.96717cdeb5f733391846a95d78c117068ce77de8 attention/Web Push, inseparable imports/modules/vendorHash.
2.bb9e6291bec10227c961c36559fba406938f1eaa bounded provider diagnostics.
3.6e1d9a191724d376cad2a71f234f0e4d1c01f36f descendant-exit observer.
4.867682c3df251fbe6941ff9a667539ae1af790ec menu/layout.
5.012f6184faa62b7d476555058f1473adcd908528 feedback/consolidated remedies.
6.4ed9af55127743b7564cb4dd01d10c9f7fee5120 status-row removal.
7.469757183ba9491d642b56e91658dc64e390647b automatic activation/folded remedy.
8.74d3f0d9530755882b33b89a53e93c7feae5898f global controls/sound.
9.53f560fe3b898aa4544dae9376fcc7d6b1f33130 independent focus reuse.

First7 consumed objects unchanged; eighth/ninth distinct postdeployment requests,
independently reviewable. No obsolete unapplied approach, fixup/follow-up series or
repeated runtime dependency/channel/generated stream. Dependency/module/vendorHash
only first owning commit; no further source consolidation needed. Protected initial
registration92b2576d, sensitive-session273a08c/ba8669b, admission3d60ced,
sharding69399c5 and integration832d9f1 ancestry remains supported baseline.

No migrations or persistent/private conversions across complete own range. Sound
adds optional IDBv1 content, no DB/object-store upgrade. Unconsumed two-field stage
replaced directly; no dual reader/transitional migration. Private notificationv1,
optional Test metadata, payloadv1, strict optional creation/old omitted receipts,
capable-reader pairing and upstream journal/capability fences retain lineage.
Consumed6e1/4ed/469 supported: preserve subscriptions, VAPID/private keys, outbox,
receipts, cleanup selectors and coordination; recover forward compatibly.

Current consumersbce984296ec29faa0cf756f632a26e30d77b6fba and
40172e5fbef65c60e89b5977bae023e724572e9e both select469 with matching identities.
No53f composition supplied/certified. Future consumer pin streams require one
final owning selection each, preserving consumed refs and protected baselines,
plus final mechanical composition/history/migration conclusions.

## Acceptance and limits

User now confirms macOS popup/sound after system settings; preserve as user
evidence. Old Linux rejection/provider/processgroup/fixture causes remain unknown
historical evidence, not explanation. New visual-only and existing-tab focus need
actual user/native confirmation. No-match open is user-confirmed/preserved.

Record Advisory disposition before finite browser check. No Blocking/Important
finding prevents it. No source publication, deployment, default merge, release,
reservation release or lifecycle approval. Keep reservation1956d2a0 and session open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/
