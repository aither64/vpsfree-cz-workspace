# P6 workflow central hookup

Current package: P6-CENTRAL-FRONTEND-HOOKUP, implementer4. Lead released the
sole app.js production source window after helper d681233e, TEAM bd329bb9 and
P3 workflow6b64c744. P2 owns all typed views, templates, routes and authority;
P7 owns packaging and metadata. This artifact is not a template or server patch.

## Frozen carriers

P2 and P6 directly confirmed the accepted carrier contract:

- `body.dataset.sessionBackend` is authoritative `pi` or `codex`, independently
  of descriptor availability. Only the server normalizes recognized legacy data.
- `body.dataset.piWorkflow` is ordinary JSON, quoted/escaped by html/template,
  with exactly `{backend,basePath,member,namespace}`. No trusted-HTML bypass.
- `basePath` is `/api/sessions/<canonical-slug>`, `member` is the explicit
  selected retained address (default lead), and namespace binds durable backend,
  workspace, session, member and conversation incarnations across generations.
  No native path/ID or generation enters browser storage identity.

Pi freezes the independent data-conversation-scope carrier for the page. The P6
namespace must equal that exact scope, and the descriptor must match the current
page session and selected member.
Missing, malformed, mismatched or unavailable data leaves workflow controls held.
An unknown backend does not grant workflows or select Codex listeners. Explicit
Codex preserves its existing controls and ignores Pi descriptor content.

## Actual app.js hookup

`createPiWorkflowPage` owns one mount, validates the page scope before import and
again before mounting, and cancels obsolete imports/mounts on replacement or
teardown. It calls the committed `mountPiWorkflows` with the same raw scoped fetch,
`optionalQuestionStorage`, `conversationAssets.createQuestionCard`, the existing
roots and a layout-only composer callback. It adds no request wrapper or timer.

The roots remain `#optional-questions`, `#plan-actions`, `#codex-mode`, and
`#codex-mode-status`. Optional question cards stay outside the blocking `#pending`
composer lane. Exact Plan bytes come from the domain helper. The composer keeps
its existing legacy focus target and can also focus the helper's action row.

The explicit Codex backend gate controls legacy createAsyncQuestions construction,
Plan listener/form registration, Markdown Plan rendering, mode notice/catalog
construction and mode/settings updates. Legacy Plan retry admission and transcript
mode enrichment cannot operate the Pi-owned controls. Unrelated provider/model
settings updates continue. Legacy team-stat refresh also requires explicit Codex
and its actual team panel, so a Pi nonlead selector cannot trigger that read. No
legacy listener is attached and then hidden to simulate isolation.

`mountPageWorkflows` starts after roots, storage and composer exist. Current
conversation sync apply and connected-edge callbacks call default automatic
refresh, which reads no-store and updates the controller without clearing mode
uncertainty. The helper owns its explicit Refresh action and settlement fence.
The onChange callback changes layout only and cannot trigger a refresh loop.

Pagehide destroys the mount and invalidates the frozen page scope. A changed
namespace/member/session/thread similarly requires a fresh authoritative page;
pageshow cannot revive the retired binding. No durable identity is derived from
transcript text, NativeID or runtime generation. Same-scope stream reconnect
does not remount or submit saved intents.

## Ordinary composer and details

The same frozen scope supplies exactly one X-Workspace-Conversation-Scope header
through the existing conversation client fetch, P6 raw fetch, and separate
createSessionClient.details transport. Headers/options and X-Session-Observation
are preserved. Native EventSource receives one events-only conversationScope
query; it cannot carry the custom fetch header. P2 consumes/compares that expected
scope under admission and after waits; it is not authority and cannot retarget.

Pi dispatcher/draft binding waits for the first current scoped snapshot's actual
nonempty string threadId. Before that, text remains in memory and default form/
keyboard submission is blocked. Existing key families use the isolated
pi.<encoded scope>.<encoded actual threadId> suffix. There is no empty/old-key
read or migration, implicit send or restored-attempt replay. Repeated snapshots
do not duplicate listeners. Retired callbacks may settle only the original
receipt under its original key. Pi uploads stay entirely nil/unmounted; no draft,
metadata, XHR or download capability is created. Codex stays eager and unchanged.

Pi details accepts only the frozen current epoch/scope and exact typed backend/
interaction/held fields, without Codex recovery or redirect-to-lead. It cannot
adopt the first thread identity, clear receipt uncertainty or replace native/P6
proof. Missing P6 does not hold ordinary interaction. Stale success/error,
malformed flags, replaced scope and removed member cannot enable or retarget it.

## Remaining integration

Raw fetch is necessary because app.js createRequest throws valid HTTP409 mode
rejections. The accepted helper preserves that result, no-store same-origin reads,
exact response/acceptance IDs, explicit actions and no optimistic mode/replay.

P2 still supplies the carrier producer, authenticated routes, same-origin/CSRF
checks, permissions, retained guards, same-Manager ports and coherent observation
refresh/invalidation/wake composition. P3's real workflow proof and attachment
barrier are committed dependencies. The page hook alone does not prove actual
central routing, installed flow or live controls, and advertises no capability.

Focused fixtures use the existing Node fake-DOM/VM source-section harness and
actual committed helper. They cover backend/listener isolation, settings ownership,
raw409/card/mode/Plan paths, automatic/reconnect uncertainty, delayed imports/reads,
teardown and namespace draft isolation. No new test framework, service, native
harness, persistent schema, migration, deployment or default integration is added.
