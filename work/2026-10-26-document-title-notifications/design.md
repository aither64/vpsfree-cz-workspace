# Document title attention: accepted implementation brief

Updated 2026-10-26 after the user said “Implement the plan”. The accepted scope
is the bounded title correction, aitherdev deployment through the matching
workspace/configuration selections, verification, integration into the three
repositories' master branches, and machine release. The lead records the exact
approval and coordinates those operations. This document does not report them
as already executed.

Design owner: architect0 (retained Astra/xhigh, workspace_write). Lead owns
plan/state. Implementer0 owns the runtime package; implementer1 owns the dependent
workspace/configuration pins. The investigation evidence below is preserved:
that investigation performed no application edits, builds, commits, deployment,
other-session inspection or conversation reads.

## Finding and confidence

**Confirmed regression:** the installed browser title controller stops reading
attention while its document is hidden. A response that finishes after switching
to another browser tab cannot add a new title marker. Returning to the session
focused immediately acknowledges that event, so the marker can remain absent
throughout. An existing marker survives hiding, but does not refresh.

**Separately confirmed expected behavior:** the Codex tab's amber dot represents
current idle/blocking state. The title represents an unread event. Reading an
event clears the title without clearing the dot or answering a question. This
alone explains a mismatch in a focused session, including another portal section.

Confidence is high for both source behavior and the synthetic reproduction.
The affected browser tab's visibility/focus, loaded asset generation, IndexedDB
read status, network responses and server attention baseline were not inspected.
The report cannot establish which condition applied to the user's exact tab.

## Verified provenance

- `dev-session current` returned `2026-10-26-document-title-notifications`;
  both environment identity variables matched that slug and
  `/home/aither/workspace/ai/vpsfree.cz`.
- Selected profile and running `workspace-portal@vpsfree-cz.service` executable
  (PID 2017250 at inspection):
  `/nix/store/vq113xqpwhz09sc7myd9zciyqvn1lsvv-dev-workspace-0.2.0`.
- Its derivation is
  `/nix/store/m723id7qwyfm1gq4mbbi65h11p83cxbk-dev-workspace-0.2.0.drv`;
  `nix derivation show` identifies source
  `/nix/store/xzh3s2660hw9p1klfh26ck93l9msjy3w-source`.
- Installed `AGENTS.md`, notification guide, `attention.go`, `notifications.go`,
  `static/app.js`, `static/session-attention.js` and attention store were
  byte-compared to canonical bare repository refs. They all match the locally
  available `origin/master` at
  `7e6d7c9cdb3388ab7abc720c034c15c21afbd686`. This is file parity, not a claim
  that the entire derivation source equals that commit. No remote fetch was needed.
- Local `master` is older:
  `52dcd471186ef874c5c93f4133744195d4815454`. Its title controller continues
  background polling. Hidden suppression entered in
  `752f914e084a95a475be77eb77513d83d6498a84`,
  `portal: retire paused read cycles and recover on tab resume`.
- Installed codex-web input is
  `8b60554bc10c2a6bcbf9732a8b77ad959c317036`, matching locally available
  codex-web `origin/master`; local codex-web `master` is
  `57972192e30fe52ab33b867c8fe4d171f59a7fd5`. Title policy is owned by
  dev-workspace, not codex-web. No Codex-version change is needed for this fix.
- Installed session template loads `app.js?v=61`,
  `session-attention-store.js?v=4`, `session-attention.js?v=2`.
  Already open pages can retain earlier JavaScript; the running binary alone
  cannot identify code executing in the reported tab.

## Exact semantics and interfaces

Source references below are relative to the immutable source directory above.

| Surface | Input and behavior |
| --- | --- |
| Codex rail dot | `portal/internal/web/static/app.js:4202`, `updateCodexWaitingIndicator`: fresh selected-conversation activity, interactive page, state timestamp, and either idle with no active thread/other team work, or waiting with a blocking prompt. No unread-event/acknowledgement dependency. |
| Codex header badge | Same file, `status.textContent = threadStatus`: raw thread status such as `idle` or `active`; not an unread notification. |
| Browser title | `portal/internal/web/static/session-attention.js:3`: unseen `done` event becomes `✓`; input/approval becomes `?`; reservation count is independent. |
| Server attention | `portal/internal/web/attention.go:62` and `:165`: successful lead completion with all ready members idle, or a real blocking native prompt with valid thread/turn/item identity. No natural-language question detection. |
| Attention HTTP | `portal/internal/web/notifications.go:477`: `GET /api/sessions/<slug>/attention` supplies identity, root, revision, freshness and event. Stale/ineligible baselines expose no event. |

An ordinary final assistant message asking “shall I implement this plan?” leaves
the turn completed/idle. It is not a native blocking request. Its eligible unread
marker is **`✓`**, not `?`. A native blocking input/approval prompt uses **`?`**.
Optional asynchronous questions also are not blocking requests. A finished plan
or prose question does not become a pending input RPC merely because it needs a
human decision.

`session-attention.js:24,41` acknowledges only an observed matching event when
the document is visible and focused, on any session section. Seen event IDs are
stored in origin-scoped IndexedDB and shared across matching tabs. Visiting
Repositories or Settings can therefore acknowledge the event without viewing
the conversation. Becoming unfocused again does not restore an acknowledged
marker. Notification permission and delivery mute do not disable title attention.

Installed hidden behavior is at `:22,69,116`: refresh refuses a hidden document;
visibility change to hidden aborts the current cycle and clears its timer.
Worker messages still call the same guarded refresh, and BroadcastChannel updates
are also visibility gated. Thus Web Push is not a fallback for hidden title
updates. Visible but unfocused windows continue polling and retain unseen markers.
On visible focused return the fetched event is acknowledged before final render.

Initial browser load is distinct from an observer baseline:

- A hidden initial page makes no attention read in the installed controller.
- A visible unfocused load can show a persisted unread event; a focused load
  acknowledges it.
- On first server observation of an already completed lead turn, the reducer
  establishes a baseline and does not invent a completion. An observed later
  successful turn can create `done` once all ready members are idle.
- A continuity gap over 90 seconds likewise does not discover old completion.
  Already persisted, still relevant events survive the gap without redelivery.
  Pending blocking input may produce a title event at baseline without a push.
- Any stale/unclassified required member observation prevents fresh attention.
  HTTP failure clears the current displayed event until a successful read;
  neither condition proves the conversation dot must also be absent.

These rules are documented in `docs/browser-notifications.md` and covered by
the existing `TestAttentionBaselineDeferredCompletionAndNewerTurn` and
`TestAttentionRestartGapPreservesKnownEventsWithoutDiscoveringOldCompletion`
source tests. Those Go tests were inspected, not rerun in this investigation.

## Bounded reproduction

Disposable fixture: [title-probe.cjs](title-probe.cjs). It evaluates unmodified
installed JavaScript and the exact older local-master source in Node VM contexts
with synthetic focus, timers, API responses and in-memory read state. It does
not contact the portal or native App Server. The Node executable is the exact
Node 24.19.0 dependency from the installed package's derivation.

From the workspace root:

```sh
/nix/store/viadyk3hg56ib6vky4cm3sb2y3n305aw-nodejs-24.19.0/bin/node work/2026-10-26-document-title-notifications/title-probe.cjs
```

Result: exit 0, under one second.

| Scenario | Result |
| --- | --- |
| Installed: visible page, hide, completion, poll/worker hint | Plain title; zero new HTTP reads; event remains unread. |
| Older local master: same sequence | `✓ fixture`; background reads occur; event remains unread. |
| Both: focused return | Plain title; event acknowledged. |
| Installed: visible unfocused completion | `✓ fixture`; unread. |
| Installed: visible unfocused native input | `? fixture`; unread. |
| Installed: initial hidden load | Plain title; zero HTTP reads. |

The existing test `50 attention documents stop hidden HTTP and storage work and
retire old results on resume` explicitly asserts the suppression, but only checks
that an already cached marker survives hiding. It misses new hidden events.
The probe materially strengthens the diagnosis by exercising that missing
transition and comparing the older implementation. No broad suite is necessary
to deliver this investigation; it does not establish real-browser timer latency.

## Accepted correction and invariants

Restore background attention refresh as a narrow exception to hidden-page
polling suppression. Retain the existing five-second polling cadence and one
current read cycle per document. A hidden document may GET attention, reconcile
the identity-scoped store and render its title. No new event stream, worker
infrastructure or server schema is needed. Browser timer throttling still
applies; a suspended browser cannot promise immediate updates.

- Remove visibility from attention-cycle admission and validity. Keep the
  running-cycle identity, generation, stopped and changed-session fences.
- On visibility change retire/abort the prior cycle and immediately start a new
  cycle in either visible or hidden state. Hiding must not clear the only timer
  without arranging its successor. Showing must not wait for an obsolete
  transport. Old bodies, errors, finalizers and storage continuations cannot
  update or release the successor cycle.
- Focus events acknowledge eligible observed attention and request refresh
  without creating concurrent reads. `pagehide` stops and retires all work;
  `pageshow` resumes only when the session identity remains valid.
- Acknowledgement requires visible **and** focused at entry and inside the
  asynchronous store callback. Hidden/unfocused observation never marks a new
  event read or starts a presence POST. Already dispatched presence requests
  retain their ordinary outcome. Same-session focused acknowledgement still
  applies to every portal section.
- Matching BroadcastChannel acknowledgement is reconciled while hidden so
  another tab's read clears the title. It must not itself acknowledge new
  attention. Worker hints use the same bounded attention refresh path.
- Check visibility immediately before starting coordination reads. Keep hidden
  coordination polling paused and retain its last known reservation count;
  refresh it on visible return. Cancel a prior visible coordination read on
  hide without allowing its late result to change the new cycle.
- Check rendered session identity and root before storage, acknowledgement,
  presence or settings use. Replacement requires reload. Keep monotonic stored
  revisions and existing failure/read-status behavior.
- Preserve server event semantics, mute/permission independence and the Codex
  dot. Ordinary final prose questions yield eligible unread `✓`; native blocking
  input/approval yields `?`. No prose classification, idle-dot mirroring or
  synthetic completion from an initial idle baseline.

## Implementation packages and boundaries

Current inspected runtime baseline remains locally available `origin/master`
`7e6d7c9cdb3388ab7abc720c034c15c21afbd686`. Owners recheck their actual feature
bases and applicable repository instructions before editing. Route substantive
deviations through the lead.

**Implementer0 — dev-workspace runtime, no dependency on pin preparation.**
Own the controller, regression tests and related technical documentation:

- `portal/internal/web/static/session-attention.js` and the title asset query
  version in `portal/internal/web/templates/session.html`.
- `portal/internal/web/attention_browser_test.cjs`: replace blanket hidden-zero
  work assertions with bounded attention-only reads and new-event title checks;
  retain generation, cancellation and replacement coverage.
- `portal/internal/web/firefox_tabs_acceptance.cjs`, with only necessary fixture
  changes in `firefox_tabs_test.go`: narrow the exception in
  `assertBackgroundUnchanged`, `settledBackground` and read-budget final lane
  checks. Permit bounded attention; still forbid hidden transcript, pending,
  SSE and coordination traffic. Discarded/pagehide documents remain quiet.
  Supply valid attention snapshots for title checks, rather than merely counting
  failed reads. Reuse this fixture and runner, without new test infrastructure.
- `docs/browser-notifications.md` and `docs/workspace-portal.md`: explain the
  attention exception and correct the blanket zero-hidden-traffic claim.

Acceptance is the invariant and test matrix below. Deliver one focused runtime
change with quick-check evidence and published exact head for downstream pins.
No codex-web, server reducer, protocol or native Codex update belongs here.

**Implementer1 — workspace and vpsfree-cz-configuration selections.**
Can inspect instructions, channel mapping and composition independently; exact
pin changes depend on implementer0's published head. Own only the two feature
worktrees' input selection/lock changes and their required checks. In workspace,
update `inputs.vpsfree-dev-workspace.inputs.dev-workspace.url` and generate the
composed lock with `nix flake update vpsfree-dev-workspace/dev-workspace`.
Preserve extension revision/hash, siblings and follows paths. In configuration,
use its existing confctl channel/role mapping for `devWorkspace` and the ordinary
exact-revision `channel set --commit` workflow; do not hand-edit channel-owned
locks. Keep only the final runtime selection in each logical pin stream.

Acceptance: both effective runtime selections equal the accepted runtime head;
semantic lock diffs contain only intended/transitive changes; extension and
unrelated selections remain intact; run
`bin/check-dev-workspace-deployment --workspace-root PATH --configuration-root PATH`
against final locks. No system-installed copy of the workspace application.
Serialize Git operations within each owned repository. Lead owns shared tracking.

**Lead — review, rollout, integration and release.** Coordinate the final
reviewed heads, required checks, aitherdev claim and user-profile application
deployment alongside configuration's matching host contract. Integrate the
approved dev-workspace, workspace and vpsfree-cz-configuration master targets
after verified deployment, then release the exact owned machine claim with
fresh remote lineage evidence. Use the mandatory installed coordination guides
and keep repository merge claims short; no claims while awaiting tests/review.
Finishing this work leaves the session open.

## Acceptance and verification

The focused browser matrix must prove:

1. New `done` and blocking input events update hidden titles to `✓`/`?` and stay
   unread, including a hidden initial load. Cached markers survive hiding and
   clear when new work/request resolution supersedes them.
2. Visible-unfocused observation stays unread. Focused return clears the title
   on Codex, Settings or Repositories; the idle/blocking dot remains independent.
   Matching cross-tab acknowledgement clears a hidden title without new reads
   being acknowledged. Mute/permission-off does not disable title attention.
3. Hidden cycles issue only bounded attention reads, with no presence POST,
   coordination reads or heavy conversation polling. At most one current cycle
   runs, and hide/show leaves a live successor timer.
4. Pagehide/discard stops work; pageshow restores it. Old-generation body, error,
   finalizer and async storage results cannot change successor state. Session or
   root replacement prevents writes and requires reload.

Quick commands in the runtime feature worktree, using its Nix environment:

```sh
nix develop --no-update-lock-file -c node --check portal/internal/web/static/session-attention.js
nix develop --no-update-lock-file -c node --test portal/internal/web/attention_browser_test.cjs
nix develop --no-update-lock-file -c node --check portal/internal/web/firefox_tabs_acceptance.cjs
```

Check any other changed JavaScript likewise. If a focused Go fixture check is
needed, use `go -C portal test -mod=readonly ./internal/web` with its targeted
`-run` expression inside Nix; on this host set
`DEV_WORKSPACES_CODEX_PROVIDERS` to an absent disposable catalog path. Do not
expand into server changes to accommodate a browser-only regression.

Commit all intended deliverables and pass quick checks before independent final
review. The review covers full branch history, final diff and the explicit
**no migrations** conclusion. Longer verification then reuses existing checks:
the package check includes Go/Node tests and attention syntax/contracts;
`session-creation` and `session-archive-lifecycle` are existing required VM
acceptance checks, with the latter explicitly required before deployment.
Follow existing CI/package requirements and the lead's configuration validation;
do not create a new build campaign.

For actual tab visibility use existing `TestFirefoxTabs`, with
`PORTAL_FIREFOX_TABS_TEST=1`, exact `FIREFOX_BINARY`/`GECKODRIVER_BINARY`, Nix Node
and an isolated headful/Xvfb display. Extend its existing synthetic fixture to
verify background title updates plus the narrow read-budget exception. This
tests browser behavior, not real model/backend performance. Delegate long or
uncertain runs to the monitor utility. After deployment verify served asset
generation, portal health/conversation continuity and the hidden-title/focused-
clearing behavior; the lead owns any required disposable runtime smoke checks.

## Compatibility, deployment and recovery

No persisted-format, IndexedDB schema, API, Codex protocol, native version,
database, generated client, CLI, Terraform or Nix module change is needed.
Mixed old/new pages remain compatible: old hidden tabs retain the limitation
until reloaded, while updated pages consume the same attention endpoint and
seen IDs. The correction preserves acknowledgement, delivery mute and event
identity. No coordinated machine update is required.

There are no migrations. Existing persisted events and seen IDs remain usable
by old and new pages. Increased hidden traffic is limited to the existing small
attention GET and its browser-store reconciliation; all heavy hidden polling
stays paused. Runtime/config pins must select the same exact runtime while the
application continues to come from the workspace user profile.

The lead owns the authorized rollout/integration sequence and records exact
system/profile store paths, source/input graph, deployed/final heads and fresh
remote ancestry before machine release. Reload replaces already executing
browser code. Recover with a capable forward package if necessary; no event-store
reset or state migration is warranted. Failed/uncertain deployment retains its
machine claim until effects and integrated lineage are reconciled.

Session remains open after handoff, integration and machine release:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-26-document-title-notifications/

## Final implementation reconciliation

The accepted design is implemented at runtime d2099c62656bc2a36c306918a92832ba1e1a0cc0
and deployed with matching consumers. The necessary native Firefox fixture
correction is documented in runtime-fixture-followup.md; it changes no product
behavior or interface and preserves durable retry assertions. Original and
affected final reviews passed without findings, exact builds/native acceptance/
feature and master CI passed, live served-source/continuity verified, all three
remote master integrations proved and aitherdev released. See state.md and
rollout.md for final paths/lineage; session remains open.
