# Refresh ownership correction: committed affected review packet

Final clean runtime `4ed9af55127743b7564cb4dd01d10c9f7fee5120`.
Amended fifth delivery `012f6184faa62b7d476555058f1473adcd908528`.
Sixth status-row patch replayed as final4ed9af55. First four objects unchanged.
Exactly six logical commits over832d9f1. HOLD publication/pins/long/browser/native/
provider operations for retained affected committed review of this new correction.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/>

## Scope and evidence

Lead accepted architect design.md section "5a07708e browser fixture: Enable
observation failure". The sealed feedback-5a-browser.log/status failed before
Test/push, with no request/controller/registration evidence to prove its actual
ordering. Source inspection independently established a missing refresh ownership
guard. Neither the original fixture cause nor physical Firefox/macOS display
cause is proved by this correction.

Only three paths changed (241 insertions/19 deletions):

- portal/internal/web/static/browser-notifications.js;
- portal/internal/web/attention_browser_test.cjs;
- portal/internal/web/notifications_browser_test.cjs.

No Go fixture, template, docs, worker, shared store, transport, sender, server
API/format, dependency, visible copy or persistent field changed. Old-ID/digest
cleanup, Test cancellation, menu/spacing/hidden Settings/no-load mutation remain.

## Implementation and contracts

Refresh captures a generation and registration identity. Worker/subscription/
server observations stage locally and commit only if still current outside an
action/page retirement/cross-tab revocation. Both success and failure, local
values, status/buttons and launched resume work are guarded. Newest refresh wins
reversed completions. WorkerReadiness refresh writes reuse the current guard.

Enable/Disable/Test invalidate old reads before beginning; triggers during action
are ignored and already-running reads stay invalid after action completion.
Pagehide invalidates reads. Cross-tab revocation retires further observations
under the old identity until explicit Enable, retaining cleanup obligations.
No registration mutation occurs from refresh and no generalized framework was
introduced.

The actual-browser fixture preserves the deliberately existing local fake
subscription, original assertions and worker activation. It explicitly captures
/register and requires2xx without relaxing auth/profile/origin/store guards.
Failure-only diagnostics retain the latest48safe rows and at most8KiB output:
numbered request/response/completion ordering, HTTP status, query-ID absent/
current/stale/unavailable, ID-presence and registered/available booleans,
controller state and fixed exception categories. Snapshot/trace waits are bounded.
No raw URLs/queries, IDs, endpoints, keys, bodies, private browser dump or arbitrary
messages are emitted. Final failure output is a safe exception category.

## Quick evidence and limits

Cached declared Node24.19.0 only. Per-check delivery-feedback-refresh-*.log/status
and quick-results.json record:

- actual-module Node suite32namedPASS,0failures/skips, command2.123s;
- changed client, module CJS and actual-browser CJS syntax PASS;
- git diff --check PASS.

Original26contracts remain plus five deterministic refresh ordering contracts
and one actual trace-helper privacy/bounds contract. Cases force old GET success/
rejection after Enable, local read before Enable, controller/visible triggers
during action, reversed completions, completion after Disable/Test/revocation/
pagehide, and genuine failed registration for absent/existing local-sub starts.
Canaries include raw capability/ID/body/exception material; none reaches output,
and overflow records explicit dropped counts. No browser is launched to exercise
the trace helper.

No unchanged Go/live check, browser/native/provider/host/build/integration/daemon/
network/credential operation ran. One fresh exact-head fixture after affected
review must collect its own evidence and stop on failure. Current quick checks
prove controlled ordering and output contracts, not the original cause or OS
appearance/click acceptance.

## History, source proof and preservation

Reviewed5a/50fba refs were preserved before modification under
refs/session-evidence/2026-10-14-i-d-like-the-dev-workspace/delivery-feedback-refresh/
with reviewed-final-5a07708e and reviewed-delivery-50fba34d names.
A normal <=80-column body-file commit was autosquashed into owning fifth, then
sixth replayed without conflict; original fifth rationale retained. No hook bypass.
Final tree3c0747c55490b7a9cddb6131f9991ea89f422875 equals the quick-tested tree.

The sixth content/stable patch-ID is unchanged:
1fea1a8447c111f44efc6e4f65ce5694c8b04a72. Its diff blob headers and assertion
line offset differ because new fixture trace lines precede it; the actual deletion
and assertion are identical. First four commit objects are unchanged. No transient
fixup remains in the final series. change.patch and final-delta.patch are
byte-identical original5a->final deltas. Full range-diff/series/whole-branch patch/
stat and owning-delivery patch/stat are retained with freeze/consolidation records.

All167previous sealed packet/live-bundle/failure files matched the initial
preservation manifest. Mutable lead reconciliation was excluded deliberately.
Original failures, heads, packets and live-native-a5 remain untouched; no new
native bundle was prepared. Earlier pre-display evidence is not relabeled.

## Complete lineage and review gate

832d9f1 -> feature96717cde -> providerbb9e6291 -> processgroup6e1 -> UI867 ->
amended delivery012f6184 -> status-row4ed9af55. All earlier reviewed/consumed refs
remain preserved. No repeated dependency/pin stream, migration or new format.
/test additive reply, optional IDBv1test fields, private notificationv1,
capable-helper receipt pairing/forward-only transitions, payloadv1, cleanup and
upstream supported capability-journal lineage remain unchanged. No dependencies
or vendorHash changed. Original provider/processgroup/physical causes unproved.

This is a new substantive bounded correction and needs retained affected
committed review, not a confirmation-only review. Lead owns reviewer assignment,
state/artifacts, publication/pins and finite post-review verification. No queue,
reservation, lifecycle, host, SSH/HTTPS, credential, display, push, merge or pin
operation occurred. Exact session/env and saved ready workspace_write roster17
were reverified; applicable repository/workspace guidance and documentation skill
read/reused. No new copy requires a writing pass.
