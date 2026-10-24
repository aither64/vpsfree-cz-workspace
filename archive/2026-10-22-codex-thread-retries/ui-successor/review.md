# Presentation milestone: independent final review

Reviewer0 to lead, 2026-10-23. Saved by lead from the retained reviewer's report.
The reviewer remained read-only. This records the complete findings, disposition,
source/history/compatibility conclusions and verification limits; the exact
reported source inventories are also in review-packet.md and owner receipts.

## Findings and disposition

Blocking: none. Important: exactly P1 below. Advisory: none. All four assigned
lanes are complete for A f8629067 / B39497062. A has no findings. This is not a
clean presentation approval while P1 is unresolved. Resolve it or record an
explicit Important-finding decision before focused capture.

### P1: activity-only footer changes do not preserve bottom-follow

Important; general / architecture, actual consumer integration. B39497062,
portal/internal/web/static/app.js2756–2758 and4299–4304; static/style.css272;
retry_activity_browser_test.cjs112,137. A renderer: retry_activity.js107–123
at f8629067.

B mounts the independent activity renderer but neither observes footer size or
visibility nor receives a layout notification. Its ResizeObserver observes only
the fixed transcript viewport. A independently changes hidden state, text and
controls, altering scrollHeight without resizing the observed box. Overflow
anchoring is explicitly disabled.

A long conversation following its bottom with activity:null can receive a
scheduled activity-only read or a taller notice with uncertainty, reason or
wrapped controls. ScrollTop remains at the old bottom, leaving notice/actions
below the viewport until another transcript render, resize or manual scroll.
The fixture manually scrolls before capacity and later captures, concealing this
transition. This is source-derived, not an empirically reproduced browser failure;
reviewer tests/capture were prohibited. Sent early as message
6d8ba512-a955-4d6b-857b-268e10f63fd4.

Requested remedy: B's transcript owner observes footer layout changes or consumes
an explicit notification and applies the existing follow flag. Follow when
appropriate, preserving a scrolled-up message anchor and composer focus/selection.
Assert idle-to-visible and height growth without manual scrolling or unrelated
transcript updates, plus the scrolled-up case. Keep it within presentation
ownership; no backend/scheduling change is needed.

Lead remedy disposition and exact follow-up verification: review-findings.md.
The lead calls this same finding I1; P1 and I1 are one finding.

## Identity, independence and exact sources

dev-session current returned2026-10-22-codex-thread-retries from tracking. Both
environment markers were absent, consistent with the trusted session/workspace
binding. Live roster verified reviewer0 ready, review purpose, gpt-6.1-sol/xhigh,
read_only, thread01a162d6-4bf1-7142-bb04-7b871eb2d1af. No settings override,
fallback, authored implementation or nested review.

Read RELEASED packet, accepted design.md14–392 and acceptance.md, applicable
workspace routes, both repo AGENTS, mandatory-change-review skill and all four
full lane references. Inspected committed diffs/history, adjacent actual
consumers, tests, owning documentation and saved quick evidence.

| Repository | Base | Reviewed head | Reviewed tree |
| --- | --- | --- | --- |
| A | ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5 | f86290673d752c77b56c70228c3d26aced75e177 | 0ed8092438d2f0a70838828573bbfd187b73393f |
| B | bf6d4b0c49600c15e17fe71248807ef43424e932 | 39497062e0da98a70386355384fa922c0eaa0168 | 28a9d72044dc3ffa7eb4f817cbb2c4d6c9614d18 |

Deployed predecessors: Aac62eeeb9d8b1fa7b8ed8fb95ba8160acb7efa1c and
B7b8c646974df72e0df3e576d10f09d79823ae004. Independently confirmed exact heads,
trees, initially clean source, bases, fresh SSH feature refs and verified final
bundles. Conclusions bind those commits, not later moving sources.

## API, authorization and presentation

A's focused optional RetryActivityProvider, Target.RetryActivity and capability
leave the required client and legacy RetryProvider intact. Actual Handler
resolution verifies opaque conversation, trusted native thread/directory,
exact origin, bounded decoding and common mutation lock. Providers receive only
the resolved thread. Token-only POST rejects extra routing/options/message
fields, missing/malformed identity and trailing bodies. Tokens grant no authority.

DTO validation bounds safe integers, qualities, nullable unknown metrics,
phase/outcome/action combinations, ASCII identities and UTF-8 reason bytes.
Provider errors map to fixed typed409/503, without arbitrary diagnostics.
Reasons use textContent. No browser socket/thread/native-option authority.

The adapter uses intended routes/token-only bodies. Renderer coalesces reads,
aborts/retires stale reads, ignores destroyed responses, suspends hidden-page
timers and observes after uncertain/stale writes without repeat POST or Send
fallback. Now requires a scheduled token; Stop never toggles preferences or
Interrupts. Exact conversation/chain dismissal persists on reload; storage
failure preserves same-page dismissal. New conversations/chains are independent.

Counts distinguish confirmed starts and one uncertain submission, with honest
partial/unavailable labels. Countdown and active exact elapsed use server
observation plus monotonic browser time; terminal/partial duration does not
invent more time. Countdown is outside polite announcements. Named buttons,
switches, keyboard controls and responsive wrapping are present. Actual visual,
accessibility and geometry execution remains pending; P1 concerns geometry.

B's footer/message-list are inside the real scroll owner. Incremental and full
renderers mutate only transcript-entries; dates/messages/disclosures/anchors use
that list, scrolling remains transcript. Filter/history/live-update preserves
footer. Composer/Send/Queue/plan ownership is unchanged. P1 remains.

Settings has exactly two whole-session switches, booleans+expectedRevision.
Reads retire stale requests; writes serialize; uncertainty triggers observation,
not duplicate mutation. Archived/inactive/unavailable state disables controls;
missing policy/activity endpoints hide optional UI. Real B resolver has no new
activity provider/policy backend yet; controlled fixtures expose presentation
capabilities. This matches the deferred backend milestone, not backend readiness.

## Delivery contracts, ownership and proportionality

A deployed-to-final ten paths concern presentation/API/docs/tests, with no
codex/native/ledger change. B fourteen paths are five aligned dependency files
plus presentation/docs/tests; no production server, managed-client, policy,
controller, lock or sidecar delta.

Incident2 receipt-first prepared-plan recovery, exact positive nonqueued proof,
immutable tuple, old-epoch exclusion, bounded HTTP SH wait and fresh authority
checks remain. Independent patch IDs confirm retention and both incident fixes
unchanged. B pre-presentation product tree differs from deployed7b8c in only
five dependency files. Prior unchanged delivery/lock review conclusions remain
applicable; they do not substitute for review of this UI/API.

Protected Pending, accepted-only retirement and >64 replay lineage remain in
retention patch4850f62fbfc3bb6569f25a5a4f946bcebce73a7f. Optional metadata adds
no Send/Queue/Implement precondition. Sender/plan receipt logic is unchanged.
No new manual refusal found.

A owns DTO/errors/adapter/notice; B owns Settings, runtime policy and layout.
Go/JS validation is an intentional transport boundary, justified by actual
consumer. Scope is proportionate: no speculative framework, native normalization,
reset/resume workaround or policy schema.

## Complete histories and update streams

A full series: df00fa36c820fc7a62ee5b8dd6e1745940ff8e15,
6c828759440705c632e1902fa8309ccac446b050,
c1f415ad5602c23e6443cced73cb59267a796f05,
ac62eeeb9d8b1fa7b8ed8fb95ba8160acb7efa1c,
f86290673d752c77b56c70228c3d26aced75e177. Prior four exact; ac62 direct parent.
Native verification/legacy embedding support are supported boundaries, not
abandoned UI iterations. No A dependency stream.

B full series:7262c24e4fbe9dbf8604e73590f9b5ef3d5dce99,
b3c7187c6e26e269994433716a0ee719d0a7edf7,
aafaf4195d695c4641ce4f9342d56a1786f237c3,
67b354e814162533f6d19342e4e4513540be70fd,
6dba4c398ba2bf54896734ab88eb449cffcd237f,
6435f157fbb0a7e5084a48a3966f2b531d906036,
b8967dfe58b83c8b82c3fd7980b4d2b58dab589c,
39497062e0da98a70386355384fa922c0eaa0168.

Original core/capability/runtime exact. Independently computed patch IDs:

- f856549e→6dba4c39 retention:4850f62fbfc3bb6569f25a5a4f946bcebce73a7f.
- 9fe56d2b→6435f157 plan:cbc1224fe9709472c635142d9ac1f772583697a9.
- 7b8c6469→b8967dfe runtime:4bd691213eac0f4b2b9c561c41600cbe5490520c.

Sole A stream67b354e8 consolidates a708f401 and preconsolidationc4cee3bf. Candidate
c4cee3bf tree equals final39497062. No redundant pins, obsolete fixups, abandoned
approaches or transitional migrations remain. Commit purposes/tests/docs coherent.

Go/Nix/vendor consistently select Af862; NAR
sha256-jOEXFTr55N88YbPakjlMw/7wsH8ZKr51Ag+Z1QaM25A=, module
h1:5iVFEW9ghXtccbfhFB2swLC+UqZYIqEPaRfNOh1bsMM=, vendor
sha256-x0Qrgfvcn74v0E6zJ7JKgwBnOGuJNUNTZQz0JdFIqcU=. Independent full lock
comparison changes only codex-web; all other nodes/edges/follows equal.

Deployed7b8c exact ref/bundle preserved, nonancestor after consolidation. Retained
patch equality establishes supported lineage, not literal merge or equivalence
of this substantive successor. Prior c1f/ed2 provenance remains. W/C outside
this milestone, no composition approval here.

## Migrations and documentation

No database migrations. Deployed retry1/generic3 unchanged and supported. No
ledger rewrite, identity regeneration/conversion/reset, policy sidecar or native
protocol change. No transitional branch-only migration.

New persistence is browser-local codex-web.retry-activity.dismissed markers keyed
exact conversation+chain, containing no routing/prompts/options/action credentials.
Old clients ignore them; no backend authority or migration.

A README/reference explain optional contract, token/auth distinction, metrics,
host scrolling, stale errors and dismissal. B portal/recovery guides condition
controls on availability and preserve schedule/cancellation/native/admission
warnings. Lasting contracts in owning repos; preview/rollout in session records.
Placement/adequacy acceptable subject P1; no KB publication.

## Evidence and remaining gates

Owner evidence, no reviewer execution:

- A tested tree exact; Go0.106s, retry race1.119s, Node102/0fail/0skip.
- B shipped HTTP/import+PlanDelivery/contention5.965s; fixture compile0.042s;
  syntax/paging/read-cycle17/0fail.
- Packets match SHA2566672e61c…fd6e1 and977f30c6…cd; B quick/syntax hashes match.
- Paging assertion now requires stronger already-deployed guard, no relaxation;
  original unsupported invocation/stale assertion evidence retained.
- Actual HTTPS/CSP/assets fixture has controlled data, frozen time, root/member,
  desktop/mobile. Unrun; manual-scroll coverage gap is P1.
- capture.sh checks exact B/clean, enters locked shell/portal, selects one240s
  subtest/dedicated screenshots. Must update after corrected final head.

No tests/builds/native/browser/CIwait/live-state/edits/claims/deployment/integration/
release/lifecycle performed. No screenshot/backend/package/native/WC/live usability
or deployment readiness certified. After P1 direct verification, actual-template
capture and explicit user visual acceptance precede backend expansion. Later
completed backend needs affected final review. Retain reviewer for material
related followups.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/
