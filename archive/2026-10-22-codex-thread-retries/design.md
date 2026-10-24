# Automatic failed-turn retries

Status: implementation brief, 2026-10-22. Owner: architect0. The user has
authorized implementation. Lead owns assignments, tracking commits, acceptance
and deployment coordination. This document supersedes the investigation's
provisional retry limits and first-deployment behavior.

Current accepted work (2026-10-23): implement the UI/session-policy successor
below. The user explicitly requested implementation after accepting the plan.
The deployed Incident 2 delivery fixes and accepted provenance-retention
behavior remain required. Historical briefs below retain their evidence; this
section governs the successor's presentation and policy changes.

## Urgent native descriptor limit and creation recovery (2026-10-24)

This incident takes priority over optional expansion. Architect0 owns this
brief; implementer0 owns bounded host evidence and the lead-authorized live
limit adjustment; implementer1 owns the service-only persistent correction
and B Git. Existing retry/delivery contracts and pending verification remain.

**Evidence and limits of attribution.**
`incident-emfile-625e1f52/units-proc-104445.json` records native App Server
PID 3387667 at 905 descriptors, soft `RLIMIT_NOFILE=1024`, hard 524288;
902 descriptors have CLOEXEC. The portal has 26 descriptors and effective
soft 524287. The system file table is not exhausted. This identifies little
native headroom, not a proven leak or the original creation failure's cause.
Installed package `1zkafvr6ns84wdmdh7qrmhx77c90wpxw-dev-workspace-0.2.0`
and B's `nix/systemd/workspace-codex@.service` omit `LimitNOFILE`.
`libexec/workspace-host:1539` executes the selected native binary directly;
the unit's low soft limit therefore remains effective in the native process.
Resource limits are inherited by future children across exec; existing children
keep their own limits. CLOEXEC descriptors do not become ordinary child handles.
The separate reported fatal "application network permission was revoked"
in `2026-10-22-limit-autostart-alerts-to-boot` has no established causal link;
owner0 may correlate bounded journal timestamps without reading conversations.

**Released persistent package.** Add exactly `LimitNOFILE=524288` to
`[Service]` in `nix/systemd/workspace-codex@.service`. A single value sets soft
and hard together. Preserve native version, launch arguments, restart policy,
all other units, state schemas and thread/request identities. No generic
resource framework, cleanup, native patch or automatic recovery is part of
this correction. Quick validation is a declarative unit check for exactly one
effective setting in the correct section and an otherwise unchanged unit;
the existing packaged `user-namespace` check must retain that setting after
template substitution. No new VM/native campaign solely for this line.
Include the committed correction in affected final review and ordinary final
package/profile verification. A is unchanged. The already held deployment
reservation and normal compatible forward profile procedure still apply.

**Immediate operational relief is separate.** The lead authorized owner0 to
raise only the exact running native MainPID's soft limit to its existing hard
limit, without changing that hard limit, restarting, signaling or touching
children. After the held-claim check, capture and revalidate unit InvocationID,
MainPID, process start time, executable and UID plus current limits; the
intended command shape is `prlimit --pid VERIFIED_PID --nofile=524288:524288`.
Any identity or limit mismatch stops the action. Read back the effective limit
and identical process identity immediately; retain both receipts. Profile
selection may preserve that native process, so a successful package activation
alone does not prove its effective limit changed. The service setting covers
future starts. Do not lower the live limit as an automatic rollback while
descriptors above the old ceiling may exist. More headroom is not a leak fix.

**Exact creation and recovery boundary.** Metadata-only inspection binds
request `625e1f52-0a41-4127-80c4-bc058fdbfa45` to destination
`2026-10-24-flake-update-downgrade-guard` and receipt
`b356d2fb581567d68c1eb80aa1a9e9c92969e66e0c44fe68affa448fe41bbdf9`.
Preparation attempt 1 is handed off; creation attempt 2 is failed, last updated
`2026-10-24T10:35:43.783684222Z`, with the reported reviewer0 recovery error.
`teamruntime/runtime.go:1118` emits that error when a successful project/cwd
thread listing returns zero matches. Its recovery branch at approximately
line 1430 already has `CreateAttempted=true`; absence is not proof of no native
effect. Preserve its project and pending member reservation, all existing root
and member threads, saved settings, original request and receipt. No fresh
StartThread, reset, replacement ID, manual record patch or prompt resend.

After resource relief, exact-identity observation must first establish whether
the original member exists. A positive unique project/cwd/nonfork match can
use the ordinary same-receipt retry, which recovers the existing member and
continues initialization. Missing, ambiguous or unreadable identity remains
unknown; increased limits alone do not clear it. Any additional recovery
implementation requires source-backed positive proof and a separate lead
decision. The supported `GET /api/session-creations/<request-id>` can perform
durable confirmation/reconciliation (`preparation.go`, `creation.go`), so this
read-only diagnosis used a metadata-only projection of its records instead.
Later authorized recovery uses the current receipt/attempt, not the saved
attempt number if another actor has advanced it. Acceptance requires the same
request/receipt, exact retained root/member identities, one initialization and
ordinary ready proof, plus no new EMFILE at the relevant operation; no success
or causal claim is inferred before those observations.

**Post-relief observations and unresolved recovery.** Owner0's accepted
`incident-emfile-625e1f52/live-nofile-relief-20261024T105239Z/result.json`
records successful same-process relief at 10:52:39Z, effective soft/hard
524288, no restart. At 10:52:48Z, public `project/read` confirmed exact
reviewer project `01a16d77-7491-7000-8a7d-46711538faef`; its exact project/cwd
`thread/list` with `useStateDbOnly=true` returned zero and no next cursor.
At 10:55:16Z, after the lead explicitly permitted ordinary index repair,
the same public listing with `useStateDbOnly` omitted also returned zero
and no next cursor. No receipt retry was dispatched.

At 10:54:18Z, `thread/loaded/list` returned 135 IDs. A bounded metadata-only
inspection of the five IDs in the creation's 10:30–10:37 UUID timestamp window
found four matching this destination cwd: the exact retained root and three
ready members, with no reviewer project match. The time window limits the
inspection; it never establishes ownership or universal absence. The roster
retains reviewer0 as creating, `CreateAttempted=true`, empty thread ID and no
bootstrap attempt. Root identity is `01a16d77-3723-7732-85bb-cec0be2de793`.

Pinned native source explains the cold/loaded distinction but does not fill
this proof gap: [`thread_processor.rs:3013–3022`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/app-server/src/request_processors/thread_processor.rs#L3013)
allows metadata-only reads before persistence; its
[`fallback snapshot:6600–6606`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/app-server/src/request_processors/thread_processor.rs#L6600)
has `project_id: None`. `thread/start` stages the project before starting
([1484–1535](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/app-server/src/request_processors/thread_processor.rs#L1484)),
and error cleanup may remove that staging
([1541–1555](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/app-server/src/request_processors/thread_processor.rs#L1541)).
An internal-error string or zero listing is not a retained no-effect receipt.
The deployed member reservation has no durable native thread-start result;
the public start request supplies no replay identity that resolves this
unknown. No supported completion under the current no-new-identity/no-record-
patch boundary has been established. Repeated same-receipt recovery currently
repeats the safe refusal. Preserve the failed request; any exceptional recovery
needs a separate exact proof and lead decision. This limitation does not block
the accepted service-limit correction or imply the separate network error is
fixed.

**Network-permission disposition and bounded recovery.**
`incident-network-permission/findings.md`, `evidence.json` and
`native-source.json` establish exact root
`01a163b4-e2c6-7081-b9cb-e7a0e78eab4b` in
`2026-10-22-limit-autostart-alerts-to-boot`, fatal at
`2026-10-24T10:33:34.880958126Z`, with eight affected threads in the same native
process. This is `NetworkPolicyDenied::Revoked`, not the capacity/cyber retry
classifier. Owner0's `incident-emfile-625e1f52/relief-final.json` supersedes
the initial zero-match journal report with nine EMFILE errors and successful
same-process relief. Socket EMFILE preceded this root's fatal by 497.261126 ms.
Requirements-load failure can revoke shared application permits; the initiating
failure is still unproved, and account/policy invalidation remains possible.

The recommended one-shot public `config/read` operation is now complete under
lead release. The verified whitelist receipt
[`config-read-ws-once.receipt.json`](incident-network-permission/config-read-ws-once.receipt.json),
SHA-256 `fe0bd5d7faaeb161e80faf8769851eef0098b4fa0d544ba819b4a638e628dd61`,
records success at `2026-10-24T12:43:23.394297948Z` after 4.329 seconds.
Before, immediately-before-request and after identities match; the same
connection's peer remained PID/UID/GID `3387667/1000/100`. The held claim and
native invocation/start/executable/socket identities are retained. The earlier
wrong-transport receipt remains unchanged; accepted source/fixture/binary and
execution evidence remain in the same directory. This one-shot release is
consumed: no further operation or model continuation is authorized here.

The supported invocation uses the verified existing workspace App Server,
with `{"includeLayers":false}` and cwd omitted. This
loads current shared requirements through the normal native owner; it does not
change configuration files, credentials, account, provider selection or thread
settings. It is an operational policy refresh despite its read-shaped API:
[`ConfigManager::read`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/app-server/src/config_manager_service.rs#L119)
calls `load_config_layers`, which refreshes/publishes the application policy.
Use a bounded deadline and record only method, UTC, verified socket/process
identity and success or sanitized error category. Discard the entire config,
origins and layers payload; do not print or retain credential-bearing values.
No repeated poll, thread start/resume, continuation or synthetic provider call.

A successful response establishes that the normal current-policy reload and
revision checks completed. It does not establish provider reachability, grant
access to denied destinations, repair already revoked requests, or prove the
original cause. A failed load may revoke other outstanding permits through the
same shared controller; stop and retain a sanitized diagnostic instead of
overriding requirements or looping. Preserve all original identities and the
existing no-restart boundary. Lead owns release and the operation receipt.

After successful refresh, the user may manually continue the same retained
conversation through ordinary managed delivery. This is a new user-authorized
continuation, not a replay of the failed request. No assistant sends one under
this brief. Source also shows ordinary
[`turn/start:540–543`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/app-server/src/request_processors/turn_processor.rs#L540)
checks `check_thread_model_provider`, which refreshes application policy too;
the separate config read is a bounded health/recovery observation without a
model turn, not a new required application gate. No product implementation,
automatic retry-class widening or new deployment dependency is needed.

**User-authorized destroy/recreate: exact failed creation only.** The lead
relayed the user's explicit instruction, "I want that session to be created...
or destroyed and created anew", and selected destruction/recreation of
request `625e1f52-0a41-4127-80c4-bc058fdbfa45`, destination
`2026-10-24-flake-update-downgrade-guard`. Owner0 executes the ordinary recovery
package after lead release; no further user confirmation is needed beyond
answering the CLI's existing confirmation for that exact target. This supplies
no lifecycle authorization for our coordinator session or any other session,
and no machine-release authorization.

**Revised order and completed replacement.** The lead subsequently released
replacement before deletion. Owner0's
[`replacement-ready-final.json`](incident-emfile-625e1f52/replacement-ready-final.json)
and [`replacement-handoff.md`](incident-emfile-625e1f52/replacement-handoff.md)
record ordinary ready completion at `2026-10-24T11:23:03.219604363Z` for
`2026-10-24-flake-update-downgrade-guard-replacement`, request
`911b102e-c607-4a76-bbd9-20b35eced722`, receipt
`f2445d7c103956f54a1129df9dc3d78bea9300ff8ddba15f409930973d6ab453`, root
`01a16da6-0939-78f3-98a1-9894df368ec8`. Positive original manifest evidence
showed both initial-goal flags false before the one new POST. The preserved
584 input bytes, no attachments and exact provider/team/settings match; all
four members are ready under fresh identities and initial-goal delivery is
confirmed. The old receipt and roster remain byte-unchanged; no old deletion
was attempted. A retained ready creation journal is completed state, not an
unfinished operation; the receipt preserves the verifier's correction.
The original ordering below is historical and superseded: replacement is
complete, while exact old-target deletion remains separate unfinished work.
Do not recreate or resubmit again when that deletion completes.

1. Before deletion, privately preserve the exact accepted preparation/receipt,
   raw original prompt, attachment bytes/order/metadata, original provider and
   resolved team/lead/member model/effort/access/instructions. Keep content in
   a mode-0700 recovery directory outside the failed target with mode-0600
   files; public tracking contains only hashes, identities and status. Preserve
   original request/receipt/root/project identities and the removal journal's
   eventual recovery location. No prompt/history export to reports.
2. **Known tooling barrier, report before destruction:** ordinary
   `dev-session delete 2026-10-24-flake-update-downgrade-guard --as-is` reaches
   team idle/archive checks; forced deletion reaches `RetireAll`. Neither
   establishes ownership of the unknown reviewer. `archiveAllLocked` rejects
   an empty thread ID even with force (`teamruntime/runtime.go`, approximately
   line 1893). The current reviewer has exactly that state. `libexec/dev-session`
   prepares its removal journal and can quiesce the root before team retirement;
   failure is not an atomic no-effect result. Do not run `--force` as a bypass,
   patch records, clear CreateAttempted, invoke private helpers, or loop the
   known refusal. Owner0 can complete preservation, then must report this
   product barrier for the lead's narrow disposition. No supported completed
   destroy/recreate route is established until that barrier is resolved.
3. When ordinary deletion is supported, use only that exact target and its
   normal confirmation, retain the removal operation/recovery evidence, and
   prove deletion complete before recreating. An interrupted deletion resumes
   its original journal; do not start a competing creation or reset the journal.
4. Recreate through ordinary New session admission (`POST /sessions`) with
   a fresh client request ID, original explicit name/date, original raw input
   and exact execution choices. Re-upload preserved attachments into a fresh
   ordinary upload scope with new upload IDs while preserving bytes/order;
   deleted upload IDs and the old request ID are not reusable. Verify the
   current catalog resolves to the saved exact team settings before submission;
   a mismatch requires a supported exact-input route, never default substitution.
   Lost responses reconcile this new request, not another new ID. Retain the
   old-to-new operation/receipt/root lineage and normal deletion-history epoch.
5. Acceptance is the new operation's ordinary ready proof, intended full team,
   exact preserved settings and one initial submission, with the old operation
   terminal/gone and its evidence retained. No unknown reviewer identity is
   adopted or reused. Owner0 reports the concrete outcome or retained blocker;
   architect performs no lifecycle or submission action.

### Failed-creation deletion remedy: retain unknown reservation, retire known threads

This remedies the deletion barrier above; it does not add retry authority.
Implementer3 owns the bounded B package below after lead release. Owner0 has
completed the separately released replacement; the old target stays untouched
until the corrected package is reviewed, checked and selected through the
normal deployment boundary. Owner1 remains sole B Git owner;
serialize edits to the shared command file and all compile/source freezes.

**Native boundary and representation.** Pinned
[`project/delete`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/app-server/src/request_processors/projects.rs#L224)
delegates to the store; [`state/runtime/projects.rs:339–373`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/state/src/runtime/projects.rs#L339)
sets matching threads' project IDs to NULL and deletes the project record.
It neither cancels a pending start nor archives/deletes those threads. Do not
call it: that would discard the useful unknown-start identity. No A/native
API change, native enumeration-as-absence proof or cleanup worker is needed.

Use the existing schema-1 member terminal representation `state=removed` and
`removedAt`, with empty `threadId`, preserving `projectId`, `createAttempted`,
all settings/instructions and original member/root identity. Roster.Validate
already permits that combination. Its meaning in this deletion context is
"managed reservation explicitly abandoned; native outcome remains unknown",
never "native thread proved deleted/archived/absent". Keep the project intact.
Existing `preserve_removed_state!` moves the complete roster to the deletion
operation's private `team.json` beside `recovery.json` and the original creation
journal. This is the durable tombstone; no new global ledger or schema.
An unmaterialized native thread may later appear, but receives no bootstrap,
assignment or adoption from this operation. Native orphan/resource cleanup is
not claimed. A new root and root-derived project key cannot reuse this record.

**Deletion-only admission and order.** Add one internal command
`team prepare-delete --deletion-operation-id ID [--check-only]`, backed by
`Service.PrepareDelete(ctx, slug, rootThreadID, operationID, checkOnly)` in a
new `portal/internal/teamruntime/deletion.go`. It is not a public team action
and cannot be invoked through ordinary member Remove, archive or preset routes.
The normal Ruby deletion owner supplies its exact validated journal ID while
holding the existing lifecycle/generation/creation/runtime exclusions. The Go
helper must match the live deletion journal's workspace, slug, operation ID,
force and phase, the validated manifest's exact retained root, and the roster
root under its existing operation lock. Reuse existing bounded private journal
and manifest readers; a presentation projection alone is not deletion approval.
Only this ordinary deletion command plus its live owner supplies approval.
Do not introduce an all-writer lock or acquire the outer runtime lock inside
the already admitted child. Missing/changed journal, root or malformed state
refuses before roster mutation.

The journal's validated persisted force value is authoritative; the released
helper signature needs no additional caller force argument. Use a bounded
strict schema-1 removal-context reader locally, plus `session.Find` for full
manifest validation and a bounded presence-aware decode of the same manifest
identity to require both initial-goal flags explicitly false. Missing or null
is not false. Revalidate journal/manifest identity and immutable context,
including force, before the single Store.Update publication. Within one helper
call, a changed-context test must refuse before mutation. Between the separate
check-only and mutating calls, the Ruby owner's continuous outer locks, exact
operation ID and immutable journal context provide serialization; do not claim
a stateless helper compares two independent calls. Normal journal phase
advancement is allowed only by that owner. Confirmed-member idle checks derive
force from this journal and retain ordinary semantics.

The special candidate is strictly: non-fork direct-team roster; manifest
creation still `creating`, explicit `initial_goal_attempted=false` and
`initial_goal_sent=false`; member `creating`, empty thread ID, canonical UUID
project, `CreateAttempted=true`, `BootstrapAttempted=false`, empty RetireIntent.
Validate every member before changing any candidate. A creating member with
no attempted start, a legacy synthetic/missing project, a fork reservation,
attempted bootstrap or conflicting retirement is outside this exception and
retains its existing refusal. A confirmed thread follows existing retirement
checks; nothing clears its generic submissions, queue, retry state or history
without those checks. Existing already-removed threadless tombstones replay as
no-ops under the same deletion context; keep their original RemovedAt.

In `libexec/dev-session#delete_with_access`, after ordinary removal validation
and before quiescence, run the new `--check-only` preflight when a direct roster
is present. Its expected journal phase is `validated`. It substitutes only the
delete call site's `require-idle`: eligible unknown reservations need no invented
idle proof; all confirmed members retain ordinary idle/submission checks for
non-force deletion. A saved force deletion retains its existing verified
interruption/retirement semantics for confirmed threads. No archive call site
changes. Quiesce the existing root normally, then durably advance the existing
removal journal to `thread_retiring` BEFORE running the mutating helper.
At that phase, revalidate the exact context/candidates and atomically save all
eligible tombstones in one Store.Update before ordinary team archive/retire.
Subsequent existing checks skip removed reservations and retire confirmed
threads normally. Do not make the helper recreate/bootstrap fresh members.

If tombstone persistence fails or its result is uncertain, stop before further
retirement; the non-discardable `thread_retiring` journal owns retry. After a
successful tombstone write followed by failure, ordinary delete resumes that
journal and rechecks the same root/operation; it neither reopens the reservation
nor changes its project/attempt. A journal before `thread_retiring` cannot
authorize mutation. No new journal fields/phases or rollback conversion.
Older schema-1 readers can read the tombstone; a partially applied operation
remains recoverable through deletion, never through session creation. Preserve
existing generation validation and forward-only package selection.

**Owner3 file package.** Production: new
`portal/internal/teamruntime/deletion.go`, minimal dispatch/flags in
`portal/cmd/workspace-portal/main.go`, and only deletion-specific call plumbing
in `libexec/dev-session`. Existing runtime.go may receive a small private idle
checking extraction to share confirmed-member checks without changing its
public behavior; no broader refactor. Tests: new
`portal/internal/teamruntime/deletion_test.go`, owning command tests, and
`test/dev_session/deletion_recovery_test.rb`. Add one short explanation to
`docs/dev-sessions.md` in the deletion/recovery section. No retry policy,
browser fixture, A/pin, native, unit-limit or creation-initializer edits. If
the existing journal reader cannot provide the narrow check, allow a local
bounded deletion-context reader in the new file; do not create a general
lifecycle API or weaken existing decoders. Owner1 coordinates main.go edits
and commits after owner3's scoped patch/quick checks.

**Acceptance and quick checks.** Require focused Go teamruntime/command tests
and Ruby deletion-recovery tests in B's Nix shell, plus formatting/syntax.
Cover the real current composition: ready confirmed members plus one attempted,
unbootstrapped, threadless member; actual deletion owner ordering must reach
`thread_retiring` before the helper can save, then ordinary archive/retire and
private recovery preserve all unknown project/attempt fields. Assert zero
start/resume/bootstrap/send/project-delete calls for the unknown and existing
archive behavior for known threads. Ordinary archive, member Remove and forced
RetireAll without the new deletion preparation still refuse the unknown.
Cover wrong operation/root/workspace/phase, force mismatch, malformed record,
bootstrap/fork/retirement negatives, active known member non-force refusal,
save failure, crash before/after tombstone publication, exact replay and recovery
after restart. Verify a fresh deletion epoch/root produces a different project
key and never adopts an old unknown by cwd alone; recreation still uses its
ordinary explicit new-creation path. A synthetic cross-language command
fixture must exercise Ruby deletion ordering and the real Go helper, not only
an always-successful team stub. Use disposable state and synthetic native wire;
no live model/VM campaign for diagnosis.

Commit and run retained affected general/architecture/risk review before longer
verification/selection. This lifecycle correction adds focused deletion and
recovery/package checks to the remaining gate plan; it does not waive existing
creation failures or authorize an automatic full VM rerun. Lead selects the
bounded longer checks from the final diff. No live deletion until the corrected
package and exact preserved input are ready; owner0 then executes the already
authorized old-target deletion after lead release. The replacement is already
ready; no second creation or initial submission is required. Our session stays open and
the machine reservation stays held.

### Failed-creation repair must run before profile selection

**825 repeated discovery refusal: stored roots with no preview (2026-10-24;
proposal, implementation held).** Final B825 / candidate31sy again returned
the expected-root discovery error. In this version (`client.go:597–625`) that
means exact nonarchived root proof succeeded, indexed discovery was empty,
and the loaded fallback completed without finding the original ID. A loaded
metadata/JSON/ID/CWD/source error, matching sibling or cancellation would have
returned a different error. The root was not archived by this invocation;
the refusal precedes `thread/archive` and attempt cleanup. These observations
do not establish why the root was omitted or its current state.

Owner0's `backend-successor/rollout-825c1d2b/effect-reconciliation-20261024T175741Z.json`
and `effect-reconciliation-175741Z-handoff.md` retain zero inspected record
hash/provenance changes, the same operation `198ff95148b957a0e2fd2f3f73d9c49410d80550dd488e7bdb29ad5e962bb43c`
at `thread_retiring`, byte-exact private start, existing member archival/D1
tombstone, unchanged tracking/authority/runtime/profile/claim, and no completion.
No global no-effect or native-absence conclusion follows. Recovery, portal
reconciliation and activation remain held.

**Producer contract explains a real missing case, not the live cause.** Pinned
0.163 `state/src/runtime/threads.rs:1444–1445` adds `threads.preview <> ''` to
ordinary active listing. Its own `archived_threads_without_previews_remain_listed`
test (`:1710–1762`) proves an existing empty-preview active row is omitted while
the archived row is visible. `thread-store/src/local/read_thread.rs:31–55`
can return that exact stored identity without requiring a preview;
`thread_processor.rs:3004–3012` returns it without a loaded manager entry.
The loaded list (`:2887–2934`) enumerates manager IDs only. Ordinary filesystem
listing also requires a preview (`rollout/src/list.rs:291,585,815–816`), so
switching off `useStateDbOnly` does not solve this case. These additional
upstream source reads were matched to the saved rust-v0.163.0 tree blob IDs:
threads `1179126f6241be8a8d39cefcbd5ded38660d8cb9`, read_thread
`3401702d75d5ec4a454f92fee1f76484a8b49959`, list
`bfed9a7097b9c44d9863ffd5584dc656165341d2`. A cached unrelated source directory
did not match these pinned files and was not used as authority.

Thus feasible boundaries include a stored, unloaded empty-preview root; a
stored metadata/file/index discrepancy; and a root changing between the exact
read and loaded enumeration. A public manager excludes internal registrations,
but metadata claiming literal `vscode` does not by itself prove the manager's
registration classification. No live read was made to select among these
possibilities. B825 covers loaded-only roots and deliberately refuses absent
loaded roots; its fixture does not exercise the native stored-empty-preview
producer. No existing public recovery command guarantees continuation here.
Do not activate/resume/start/send, set a preview, alter an index, or call archive
around the ordinary owner to make its discovery predicate pass.

**Smallest positive-proof extension for lead release:** keep existing indexed
and loaded discovery, conflict refusals, structured-source exclusion and
archived replay. When both discovery paths omit the original root without
error, admit only an exact **persisted active, unloaded, empty-preview** root:
fresh exact-ID metadata has canonical original CWD, literal `vscode`, explicit
non-ephemeral state, empty preview and exact `notLoaded` status; the existing
`proveArchivedThread(... SourceKind=vscode, RequireActiveFile=true)` path must
return `ArchiveActive`. Reuse its canonical active-path/filename, regular-file
and stable metadata/file recheck; do not accept `ArchiveFresh`, a missing/nil
path, an archived path, wrong identity or drift. Retain that same identity
through the following metadata/history check, require materialized history,
ordinary terminal-turn idle proof and resolved submission-attempt proof before
the unchanged exact `ArchiveThread` call. Discovery absence alone never grants
permission, and force does not bypass these new identity requirements. Keep
the ordinary operation and all D1 tombstone/private provenance untouched;
archive error or uncertain response retains evidence and resumes through
ordinary positive archived proof. If this narrower proof fails on the actual
target, report its specific failed predicate rather than widening admission.

Own this inside B `portal/internal/workspacecodex/client.go` with its existing
`client_test.go` and a short recovery-documentation amendment; reuse existing
proof helpers, with no A/API/schema/host/Ruby change. Quick regression selector
`TestRetireThread|TestRetirementDiscovery|TestProveMaterializedActiveThread`:
materialized empty-preview/notLoaded root with both lists empty succeeds once;
missing/nonregular path, nil path, nonempty preview, wrong source/ID/CWD,
loaded or changing status, file/metadata drift, sibling, unresolved submission,
active turn, cancellation and archive failure refuse without clearing evidence.
Preserve all prior loaded-root/structured-source/archived replay negatives.

Before any further live recovery, require one **separately released disposable
producer regression**, not another model/retry campaign. Reserve
`portal/cmd/workspace-portal/retire_empty_native_integration_test.go` under the
existing `live_switch_integration` tag and `LIVE_SWITCH_CODEX` exact-package
selection. Use isolated HOME/CODEX_HOME/workspace/socket, no credentials or
registered session. Native start with no user turn, ordinary archive then
unarchive of that disposable identity can construct the stored, unloaded,
empty-preview case: pinned archive persists the fresh root and unloads it;
unarchive reads stored metadata without starting/resuming it. Assert the actual
producer preconditions (exact readable active metadata/file, empty indexed and
loaded root discovery) before calling real B `RetireThread`; require positive
archived proof and exact replay without another archive. No fabricated RPC
response/index/file or provider request may establish the precondition; if the
selected producer does not produce it, fail and report, with no synthetic
fallback or skip. Target one case, 60-second fixture context and 120-second
test timeout; compile/normal/race quick checks and affected committed review
precede its separately released watcher execution. This is planning only, not
authorization to run native or any test now. Retain prior passing evidence for
its exact inputs; only the changed retirement boundary and rebuilt downstream
package identities need new evidence. No UI, model, VM or broad audit gate.

**032 root-retirement discovery refusal (2026-10-24; source disposition only).**
The corrected `9xzxx3z535s5l52vmmy7vwk5wklnbfhb` candidate passed authority
publication and reached durable `thread_retiring`. Owner0's
`backend-successor/rollout-032badc8/effect-reconciliation-20261024T165419Z.json`
binds operation
`198ff95148b957a0e2fd2f3f73d9c49410d80550dd488e7bdb29ad5e962bb43c`,
force=false, exact private start transfer, three known members archived and
the unknown reviewer reservation removed with its original project/attempt
provenance. Tracking remains; no completed removal exists. All continuation
must retain this operation, original request/root and private recovery.

The Ruby owner calls root retirement after start transfer and team retirement
(`libexec/dev-session:2443–2447,6895`). The exact Go error occurs at
`portal/internal/workspacecodex/client.go:617`: successful
`ProveArchivedRootThread` has already read and validated the exact retained
root/CWD/source, then `retirementCandidate(... archived=false,indexed=true)`
finds no row. The proof was nonarchived (`ArchiveFresh` or `ArchiveActive`);
the error alone does not distinguish those states or prove native absence.
This invocation returns before `thread/archive` and attempt cleanup. Earlier
member effects remain real; neither global no-effect nor deletion completion
follows from the root refusal.

This exposes an incomplete discovery path for a supported loaded root. Pinned
0.163 source, saved in `native-thread-processor-01630.rs`, constructs metadata
for a loaded unpersisted root at 3013–3022; list builds rows from the store and
enriches only that fixed slice at 2707–2755. Its archive owner explicitly
persists a loaded non-ephemeral root before archival at 1731–1740. Consequently
changing indexed listing to ordinary scanning alone cannot guarantee discovery
of a fresh root. Existing fresh-retirement test (`client_test.go:936`) supplies
the root in the indexed list and misses this case. Whether this actual root
is unmaterialized or has a stale index remains unmeasured; no native probe was
run for this diagnosis.

**Accepted correction; owner1 implementation released:** in B's ordinary
`RetireThread`, only after successful nonarchived exact-root proof and an empty
indexed candidate result, supplement discovery with the existing public
`LoadedThreadIDs` and metadata reads. Require the original root positively
present and uniquely matching the existing retirement CWD/source policy;
reject another matching candidate, unreadable/invalid loaded metadata or
identity disagreement. Recheck the retained root through the existing following
metadata/history/idle path before dispatch. Empty loaded discovery is still a
refusal. Preserve indexed all-provider ambiguity checks, archived-root proof,
existing fresh/history/idle/submission rules, force semantics and cleanup only
after archive success. No root adoption, start/resume/activation/turn, index
manufacture, tombstone conversion or direct operational RPC bypass. No existing
supported command was found that guarantees this continuation without changing
the root state; blind same-state replay cannot fix the discovery assumption.

**Accepted source-filter clarification.** `ThreadMetadata.Source` is `any`;
`ReadThreadMetadata` binds the returned ID and validates JSON without source
normalization. Keep its ID/JSON errors, canonical CWD and present-source checks.
The original root must have the exact retained ID/CWD and literal `vscode`
source; another candidate matching that same retirement policy still refuses.
Non-root structured sources remain opaque and excluded, including at the same
CWD. Do not impose an all-loaded string/enum restriction: that would reject
legitimate structured sub-agent sources already excluded by the existing
policy. Owner1 adds bounded structured-source positives at the same and an
unrelated CWD and repeats only the current normal/race checks; final affected
review inspects them. No decoder, API, framework, policy or user-facing prose
change. This recording adds no approval gate; implementation/commit release
continues, while live operation `198ff95148b957a0e2fd2f3f73d9c49410d80550dd488e7bdb29ad5e962bb43c`
remains held.

Owning production/test paths are only
`portal/internal/workspacecodex/client.go` and its existing `client_test.go`,
plus a short correction in `docs/session-archive-recovery.md`; no A/Ruby/host
API, journal or policy change. Focused selector:
`TestRetireThread|TestRetirementDiscovery|TestProveArchivedRootThread` in
`./internal/workspacecodex`. The new main regression must use real exact-root
proof with disposable metadata/files, an empty indexed list, the original
loaded root and actual archive request forwarding, without a fabricated index
row or stubbed archive proof. Include no-loaded-root, loaded sibling,
metadata/cancellation/drift and nonfresh/active refusal; archive failure keeps
attempt evidence, while positively proved archived replay retains its existing
no-new-archive behavior. Keep D1 reservation and current operation tests intact.
Require affected quick checks and committed review before any separately
released longer check; reuse unrelated PASS receipts only with exact unchanged
input evidence. No new native/browser/VM campaign is implied. A rebuilt reviewed
candidate must resume this same ordinary deletion, then completed proof must
precede separate portal reconciliation and forward selection.

**Actual missing-authority refusal (2026-10-24; proposed correction, not released).**
The supported Git-source invocation of final B `e06578e4` / W `8f5af317`
candidate `n20dykix725cs9hqc381pgfpqncqinck` reached confirmation and then
refused the old target as an `untrusted same-name tmux session`. See
`backend-successor/rollout-e06578e4/recovery-worktree.status.json` and owner0's
`effect-reconciliation-20261024T160001Z.json`. The latter records no runtime
authority, no removal journal or private removal directory, intact tracking,
and exact managed tmux `$207` with the original root, socket and creation nonce.
Owner0's completed handoff records all six originals byte-identical through
16:01:47Z, with profile/native/claim unchanged and no visible durable retirement
or move. Together these identify the initial trust gate. Authority absence now
does not prove historical absence, and this inventory does not exclude every
transient preflight effect. No target/live inspection or recovery was run by
the architect.

Source explains a legitimate interruption: `libexec/dev-session:1233–1275`
creates and synchronizes the managed terminal, then calls
`apply_direct_team_preset!` before publishing the `creating` runtime authority.
Neither `create_tmux_session` nor `sync_slug` publishes that authority. A member
initialization failure can therefore leave exactly the retained terminal and
start journal without authority. The failed-creation verifier at `:6237–6256`
accepts absent authority when the exact creation/root/terminal proof passes;
ordinary deletion at `:2422` then invokes `ensure_retirement_identity!`, which
requires authority whenever its directory is configured (`:8627–8631`). This
precedes `prepare_removal!`, retry cancellation, lifecycle binding, quiescence
and native retirement. The same error also exists at later runtime retirement;
the saved absent-removal evidence distinguishes this occurrence. Interactive
confirmation alone did not establish a deletion phase.

**Disposition:** the failed-creation recovery path is incomplete for a
source-supported pre-authority interruption. No applicable existing public
recovery was found: ordinary start reaches team initialization again; sync
does not publish authority; force does not change this predicate. Repeating
the same command with unchanged state cannot bridge it. Do not retry member
creation, patch authority by hand, stop the terminal or weaken generic trust.

The smallest proposed implementation belongs only to the ordinary delete
owner in `libexec/dev-session`, with focused additions to
`test/dev_session/deletion_recovery_test.rb`,
`test/workspace_host/failed_creation_delete_recovery_test.rb`, and the existing
failed-creation section of `docs/session-archive-recovery.md`. No host entry,
Go/provider/native, schema or UI change is needed. Before the existing trust
gate, allow authority publication **only** from the already validated private
`FailedCreationDeleteContext`, with configured authority directory, genuinely
absent authority and a present exact terminal. Under existing runtime,
creation and slug exclusions, revalidate context and terminal by ID, name,
managed mark, environment slug, workspace, configured tmux socket, original
creation nonce, retained root, native socket and client version. Use the
ordinary atomic authority writer with state `creating`, preserving that exact
nonce and all identities, then run unchanged ordinary trust/deletion checks.
This publishes positively proved ownership; it must not invent a nonce, mark
creation ready, overwrite malformed/conflicting authority or infer ownership
from the slug. Existing authority uses its existing strict path. No terminal
means no new authority. Archive, generic deletion without this context, start
and other lifecycle paths retain their current behavior.

Before implementation release, the lead accepts this narrow authority rule and
assigns the Ruby owner; owner1 remains sole Git owner. Suggested focused test
name selector in both Ruby files: `/failed_creation.*authority/`. Cover the
real public candidate-to-ordinary executor with configured authority and a
live disposable terminal (the existing positive fixture currently supplies
`FailedCreationNoTerminal`); prove one ordinary removal and original nonce,
no start/bootstrap/new identity, and exact completed replay. Negatives cover
missing/changed context, terminal ID/nonce/root/socket/version/environment
drift, and existing malformed/conflicting authority, with no publication or
retirement. Inject interruption immediately after authority publication but
before removal preparation: replay must accept the same creating authority,
retain original start/receipt/team evidence and create only the ordinary
current removal operation. Retain existing generic same-name trust negatives
and existing subordinate-start/crash/epoch recovery cases.

Verification is limited to this changed Ruby/host recovery boundary: focused
quick checks in the declared Nix environment, committed affected independent
review, then required affected packaged checks. Preserve prior browser32,
Go/native and composed PASS receipts as evidence for their exact inputs;
reuse unchanged checks only with identical source/dependency/derivation
evidence. The new B package requires fresh downstream pins and composed output
identity, not a claim that old `n20` contains the correction. No automatic
browser/native campaign or broad re-audit. After separate execution release,
the public recovery keeps the same source-bound target/request and any
ordinary removal operation established by its owner; only completed deletion
proof permits the separately released portal reconciliation and forward
selection. Replacement, coordinator and machine hold remain untouched.

**Final recovery source form (2026-10-24).** The attempted raw immutable W
source failed at source fingerprinting (`source snapshot exceeds its file
limit`), before target validation or deletion. Use the supported Git-backed
directory form for the already-authorized public invocation:
`--source /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/workspace`.
This corrects only the immutable-directory assumption in
`failed-creation-candidate-recovery/operations-preparation/operation-brief.md`;
retain that preparation's exact target/request, confirmation, held ownership
and separate portal-reconciliation ordering. Preserve its historical receipts.

The final candidate's `libexec/workspace-coordination-host.rb:11–25` explicitly
supports `.git` as a file or directory: fingerprint HEAD, binary HEAD diff and
nonignored untracked contents. The 20,000-file recursive snapshot limit applies
only without `.git`. Candidate `.workspace-host-wrapped:906–920` still demands
one ordinary source build output equal to its own package root, then repeats
the fingerprint under transition exclusion with unchanged generation/contract/
target guards. No limit change, source edit, extra selector in `--source`, or
shared-master substitution is needed.

Saved `backend-successor/composed-e06578e4` receipts bind this exact clean W
worktree at `8f5af317d1b6b805a1bd13beffab880f60f8e7a7`, tree
`7454ab059213f5b5ba3e3833cab01868ae292f5a`, to immutable source
`/nix/store/b9hvy1r4xiq7qisiywq13qbnk1hpyyj4-source` and built default output
`/nix/store/n20dykix725cs9hqc381pgfpqncqinck-dev-workspace-0.2.0` (derivation
`/nix/store/7dlrw0yyavc1ixjiqq0snwr6dhx4hhfh-dev-workspace-0.2.0.drv`).
Executor revalidation must retain that clean frozen source; this source-only
disposition did not run fresh Git/build/target operations or execute recovery.

**Deployment blocker confirmed, not a waived gate.** Source inspected at B
`ef773d223e946f1b5ca453f217a600b7e463e8b7` plus the recorded installed
`1zkafvr6ns84wdmdh7qrmhx77c90wpxw-dev-workspace-0.2.0` has the same guard:
`libexec/workspace-host:648,662,691` checks unfinished operations in ordinary
preparation, candidate preparation and activation. At `:2242–2287`, every
nonready CLI creation journal blocks. At `:2432–2475`, a schema-3 portal
creation receipt in `failed` state also blocks independently; only ready,
conflict or positively proved no-effect cancellation passes. The already
recorded failed request 625e and creating manifest therefore cannot accompany
selection of the corrected package. No fresh live inventory was needed.
`--from-candidate` retains these checks; do not alter them.

The preceding select-repair-then-delete ordering is superseded by this blocker.
There is currently no supported candidate deletion entry. Ordinary candidate
`bin/dev-session` supplies its own package as `--expected-host-generation`
(`workspace-host:1352–1374`), which the lifecycle executor checks against the
selected profile (`dev-session:9496`). `recover-archive` (`workspace-host:782–879`)
requires an eligible archive journal, archived tracking and ready creation;
it cannot start this failed-creation deletion. Direct private-helper calls or
operator-supplied generation overrides are not supported recovery.

**Accepted package extension, source-only release.** The lead accepted this
package and delivered implementer0's release in
[`candidate-recovery-release.md`](delete-guard/candidate-recovery-release.md)
(turn `01a16dd3-12ee-7211-a5cd-10bdd0d21ac5`). Add a public
candidate-only `workspace-host recover-failed-creation-delete --source PATH
--workspace NAME --session SLUG --request-id UUID`, implemented beside the
existing archive recovery entry. This authorizes implementation and focused
disposable quick checks only; live recovery and selection remain unreleased.
Reuse its exact source-output/predecessor
profile-token binding, selected native executable/version/protocol validation
and transition exclusion. Validate the exact failed direct-creation receipt,
registered workspace, original retained root and roster, explicit unattempted/
unsent initial goal and the accepted deletion eligibility. No arbitrary ready
session, fork, conflicting operation or request substitution is admitted.
Preserve the ordinary deletion confirmation and all coordination/lifecycle/
creation/runtime checks. Use the candidate's ordinary deletion executor/helper
under predecessor generation authority, explicitly handed off by this public
host entry while it owns the transition lock, as modern archive recovery does.
No profile selection, services restart, native replacement, direct tombstone
write or bypass of ordinary retirement occurs in the host entry.

The source runtime contract differs from the installed predecessor only by
`turnRetrySessionPolicy`; whole-object archive-recovery equality cannot be
copied unchanged. Limit this new entry's compatibility check to exact equality
after validating this one intentional addition: predecessor absent, candidate
`turnRetrySessionPolicy: 1`, or both already equal at 1. All other fields,
especially lifecycle schemas/private flags, must match exactly. Retain normal
candidate capability/state checks and selected native protocol proof. The
entry cannot initialize session retry policy or migrate any state. Any other
contract difference requires a new disposition, not permissive decoding.

An interruption re-enters the same public command and resumes the exact
ordinary deletion journal; after tracking moves, bind the request/root through
its validated private recovery manifest and roster. Completion is recognized
from the exact completed removal evidence, never by guessing that a missing
target had no effect. Profile/native identity must remain unchanged before and
after. Failed or uncertain deletion leaves its normal journal/recovery intact.
Do not hold the transition exclusion while asking the running portal to
reconcile: its own admission requires a shared transition lock.

**R1 removal-epoch binding clarification.** Reuse the accepted receipt and
preparation's matching `deletionHistorySha256`; add no persisted field or API.
The existing Ruby `completed_removal_history` and Go
`CompletedRemovalHistory` hash the sorted unique validated completed operation
IDs joined by newline. Completion times are validated metadata, not ordering
authority. Let C be that complete set and E the accepted digest. Under the
existing ownership locks, first validate the inventory and both accepted
request bindings; never discard an invalid record to manufacture a match.

- A live ordinary removal journal selects only its own exact operation O.
  Require hash(C excluding O) = E; if O has not completed, this is hash(C) = E.
  Preserve exact journal/root/private-record and phase consistency checks.
- Live tracking without a removal journal requires hash(C) = E. Select no
  historical completion; ordinary deletion creates the current operation.
- With neither live tracking nor journal, select exactly one completed O whose
  exclusion restores E, with one unambiguous validated recovery location.
  Apply all existing exact request/root/manifest/creation/team/start checks to
  it. No such candidate, multiple candidates or conflicting locations refuses.

This supports zero, one or two prior removals without choosing by timestamp,
directory name or latest record. Missing target with only preacceptance history
does not prove current deletion. Changed accepted epochs, an additional distinct
postacceptance removal, malformed history or conflicting duplicate evidence
refuses. Owner0's isolated two-file R1 package retains its boundary; focused
cases cover those histories for fresh/live-journal/completed replay plus these
negative cases. This clarifies the existing exact-operation recovery contract,
not a new recovery mechanism or live-operation release.

**Concrete order after implementation/review/build.** Keep the selected profile
and held machine claim. Run the new reviewed candidate recovery entry for only
the authorized old target, then retain its exact deletion/recovery proof and
release its transition exclusion. Next use the selected portal's ordinary
exact-request status reconciliation for `/api/session-creations/625e1f52-0a41-4127-80c4-bc058fdbfa45`;
this is an explicitly authorized stateful reconciliation, not a read-only
health check, and must not invoke retry/start. `creation.go:507–523` calls
`retireAbsentCreation`; `creation_store.go:229–266` requires absence of retained
tracking/authority/journals plus changed completed-removal history for this
failed receipt before its owner retires it. Preserve original private receipt
provenance before this step. CLI deletion alone moves the CLI journal but does
not remove this portal receipt (`dev-session:6413–6431,6543–6568`). If ordinary
reconciliation cannot prove completion, stop with that precise blocker; do not
edit the receipt or force a terminal state. Then normal forward switch performs
the full unchanged guard again, including any other unfinished sessions.
Replacement 911b is already ready and is never recreated or resubmitted here.

**File and verification boundary.** Owner3's ordinary deletion package is the
executor dependency; D1 is closed at `fda46ca1` through lead step-9 inspection.
Implementer0
owns only `libexec/workspace-host`, new
`test/workspace_host/failed_creation_delete_recovery_test.rb`, and narrow
`docs/session-archive-recovery.md` changes in the main B worktree. Owner1
remains sole B Git owner; owner0 performs no Git/index operations. Serialize
shared file edits and compiler/source-freeze windows.
Use disposable source/profile/native/portal fixtures to prove wrong source,
profile turnover, wrong request/root, other contract delta and conflicting
operation refuse before effects; eligible first deletion and interrupted replay
use the same normal journal; candidate generation is not selected; unknown
provenance survives; completed deletion plus real ordinary portal retirement
unblocks the unchanged switch guard. Keep existing candidate-switch unfinished-
creation negative tests. Focused Ruby and existing Go receipt-retirement checks,
the complete combined commit and quick checks must precede final affected
independent review, which precedes long watcher verification. Final package
verification precedes operation;
no automatic full VM campaign. This is a demonstrated deployment dependency,
not optional expansion. Architect makes no application or live-state changes.

### Exact interrupted terminal-start ownership during failed-creation deletion

**Additional blocker and evidence.** The preserved `original-target-2.json`
is 164 bytes, SHA-256
`9d019c977412df26518c51b78eb06dda8e3a4e82303bfdbf7d0a482bbce0a3c1`.
It contains exactly schema 1, the old target slug, `state=creating` and
`tmux_identity=834ceec5d66b2f409e78fdd348b52bf9f3b60e031e2ffae113988bda65f0d0dc`.
That identity equals the preserved schema-3 creating creation journal. Only
these preserved nonsecret fields were inspected; no live target read occurred.
`dev-session:4311–4363` owns this terminal-start journal. Start publishes it
before creating tmux (`:1228`); applying the direct team (`:1247`) precedes its
removal (`:1276`). A failed member initialization can therefore leave this
legitimate terminal reservation. It is not a native member-start receipt.
The generic conflict guard (`:6161–6170`) refuses it before deletion admission.
There is no supported start-cancellation command: `resume` requires ordinary
ready metadata, while `start` re-enters the unresolved member initialization.
Neither is the deletion recovery operation requested here.

**Accepted narrow executor seam, source-only release.** The lead accepted the
subordinate-start design and extended owner0's release in
[`candidate-recovery-release.md`](delete-guard/candidate-recovery-release.md),
message `7e58b63f-eeac-425b-93b8-d5040df5f1c6` in turn
`01a16dd3-12ee-7211-a5cd-10bdd0d21ac5`. Keep the generic conflict guard
strict. Add a private deletion-only validator/context passed from
`delete_with_access` while its existing lifecycle, creation and runtime locks
are held. Only this validated context may admit the one matching start journal;
it is not an `ignore_start` flag or public bypass. Before effects require the
existing failed/direct-creation admission, creating manifest with explicit
initial-goal attempted/sent false, exact retained root/roster, valid creating
CLI creation journal and strict bounded schema-1 start journal with identical
slug/tmux nonce. Any retained authority or live terminal must match that nonce
and the ordinary workspace/root/socket ownership proof; do not invent a missing
nonce or adopt a same-name terminal. All fork/archive/revive/migration/foreign
start conflicts remain refusals. The public candidate recovery entry validates
the same context; it must not reject this exact subordinate start unconditionally
or introduce a separate weaker decoder.

The initial exception is read-only admission. Prepare and validate the ordinary
removal journal, run normal deletion preflight and root quiescence, then
durably advance removal to `thread_retiring`. Only now atomically move the exact
start file, unchanged, to that operation's mode-0700 recovery directory as
`start.json`, with both directories synced and normal same-filesystem checks.
Do this before team tombstone/native retirement. This is an explicit transfer
of the interrupted terminal reservation to the non-discardable deletion owner,
not successful completion or proof of no native effect. Do not call the ordinary
start completion unlink helper, rewrite it ready, clear its nonce, or retry
native initialization. Existing deletion then retires confirmed identities and
preserves the unknown member as already designed.

Before `thread_retiring`, failures leave the original start journal intact and
retain ordinary discard/restore semantics. After that phase, failure/restart
resumes the same deletion operation: validate either the original source before
the move or the exact private `start.json` after it against the same creation
identity, never both different records. Atomic rename cannot lose both copies;
missing or conflicting required provenance refuses. Repeated recovery preserves
the bytes and does not create a new removal operation. After tracking moves,
use the validated private manifest/creation/team/start records. A completed
removal retains `start.json` permanently with its other recovery evidence.
No schema, phase, native API or ordinary archive change is required. Earlier
instructions to leave the source start journal until runtime retirement are
superseded by this precise non-discardable-phase ownership transfer.

**Ownership and focused checks.** Owner0 additionally owns the ordinary
executor seam in `libexec/dev-session` and
`test/dev_session/deletion_recovery_test.rb`, sharing one private validated
context with the already assigned candidate host package. Serialize edits with
owner3/owner1 incorporation; owner1 remains sole B Git owner. Keep
the owning recovery explanation in `docs/session-archive-recovery.md`. Test
exact matching start admission, wrong nonce/slug/root/authority, malformed or
oversized journal, missing explicit flags, unrelated lifecycle/fork conflicts,
and archive/ordinary start behavior unchanged. Inject failures before the
durable phase, during move, after move and during native retirement; verify
one removal identity, exact bytes in exactly one location, no start/bootstrap/
send, preserved unknown member, and safe replay after tracking relocation.
Candidate/source/profile/native checks remain unchanged. No live start/delete
or private-helper operation is released by this design clarification.

**Minimal cross-boundary receipt evidence.** Keep owner0's disposable public
host-to-ordinary-Runner composition with synthetic external effects. It must
produce real schema-1 removal metadata through the ordinary phase writers and
preserve real start/creation/team records; stubbing the final removal marker or
manually declaring the host guard clear is not proof. Owner1 owns a short Go
compiler window for existing `TestCreationEvidenceGapDeletionRetiresTheExactRequest`
and `TestCreationReclaimsDeletedReceiptsForUnrelatedAdmissionAndStartup`.
The former already invokes the real Ruby removal serialization, then real Go
`CompletedRemovalHistory`/receipt retirement; it covers absence/other-slug,
runtime-lock and stale-retry negatives. Its current receipts are schema 1.
Add only a focused valid schema-3 direct-new/failed variant in the same owning
`portal/internal/web/creation_test.go` if no equivalent existing case covers
that decoder/restart boundary; owner1's test-only package was released in turn
`01a16ddd-4d2f-77d1-b452-c06fd29814b4`.
Verify exact failed receipt retirement after the lock is released and completed
removal is visible, with no creation dispatch, while incomplete/unchanged
removal keeps the receipt. Keep the unmodified host switch-guard tests before
and after terminal receipt ownership. These two source-bound fixtures prove
producer and consumer contracts; report them as composed evidence, not a single
full-system run. No new browser/VM/native campaign or product receipt API is
needed for this gap.
The lead accepted this proportional producer/consumer proof. The dependent
host/executor/test package still requires a complete combined commit and quick
checks, then final affected independent review before long watcher execution.
Replacement remains ready; the old target stays preserved until separate
operational release.

## Accepted UI successor: presentation first, session-wide policy

Architect0 owns this brief only. Implementer0 owns package A (`codex-web`);
implementer1 owns package B (`dev-workspace`). Lead owns assignments, user-facing
prose, screenshot acceptance, review, final pins and operations. Verified
baselines are A `ac62eeeb9d8b1fa7b8ed8fb95ba8160acb7efa1c` and
B `7b8c646974df72e0df3e576d10f09d79823ae004`. Retained architect settings are
GPT-6 Astra/xhigh/workspace_write; both implementation owners are ready with
their saved settings. No further product choice is open.

### Milestones and independent implementation boundaries

**First milestone: a complete presentation slice.** A implements the optional
activity DTO, notice renderer/client adapter and focused contracts. B implements
Session Settings controls, transcript ownership, styling and a focused private
actual-template Playwright fixture consuming the fixed DTO below. Controlled
fixture responses supply rare states and action transitions. Capture desktop
and mobile screenshots for user review before backend expansion, long/native
verification or live deployment. Keep preview infrastructure test-only; do not
create an interactive preview application, live service, real model request or
forced provider error. Production controls remain unavailable until their
real capability/provider is present. A and B can develop their presentation
packages independently against this contract; B owns updating its A dependency
once A publishes the completed slice.

After the user reviews the presentation, B implements the durable policy,
actions, controller integration and runtime guard. A finishes server-side
activity validation/error contracts as needed. Each owner supplies tests and
lasting documentation for its component. Consequential deviations return to
the lead. The first screenshot milestone does not imply backend completion,
final review or deployment readiness.

| Owner | Files and responsibilities |
| --- | --- |
| A / implementer0 | `conversation/retry.go` or focused `retry_activity.go`, optional `Target`/capability fields and handler routing, `conversation/assets/retry.js` or a dedicated activity module, client exports, focused Go/Node/browser contracts, `docs/reference.md`. No runtime scheduling, session preferences, ledger schema or Codex-native changes. |
| B / implementer1 | `portal/internal/web/templates/session.html`, `static/app.js`, `static/style.css`, focused actual-template browser fixtures; later `web/turn_retry.go` and session-policy route, `turnretry` policy/store/controller, managed adapter gates, runtime contract and `libexec/workspace-host` compatibility checks, relevant Go/Ruby tests and `docs/turn-retry-recovery.md` / portal guide. Preserve Incident 2 route/recovery code. |

### Product and DOM contract

Session Settings contains exactly two switches: capacity and cybersecurity
automatic retries. Both apply to the lead and every current/future retained
member. There are no per-conversation exceptions or switches. Fixed existing
backoff/jitter and cybersecurity quota remain unchanged.

Remove B's permanent retry row above the transcript. Keep `#transcript` as the
actual scroll owner, with two stable children:

```html
<div id="transcript" class="transcript">
  <div id="transcript-entries" role="log" aria-label="Codex conversation"></div>
  <div id="automatic-turn-retry" hidden></div>
</div>
```

B owns these nodes and the scroll/anchor behavior. Full and incremental message
renderers own only `#transcript-entries`, including date rows and empty states;
they never replace/remove the footer. Message-key/date-key lookup and anchor
selection move to message-list descendants, while scrollTop/scrollHeight and
follow behavior continue to use `#transcript`. A mounts only inside the footer
and must not replace its parent or message list. Keep the notice at the bottom
inside this viewport, above the composer, with responsive controls and no
reserved height, grid gap or margin when hidden/dismissed. Preserve selection,
scroll-up position, filters, backfill, full refresh and member changes. An
unmanaged appended transcript child or a sibling above the viewport is wrong.

The notice shows active retry count, total elapsed including waits, class and
countdown/status. Retry now appears only for a scheduled attempt and accelerates
that attempt. Stop retrying cancels only this chain; it does not toggle either
switch or call native Interrupt. Continue showing the summary during accepted
retry execution. Freeze it at success, quota exhaustion, stop, superseding input
or permanent block. Terminal result stays until browser-local dismissal for the
exact conversation and chain. Reload preserves dismissal; a new chain appears.
Idle/off and legacy cancelled state without actual retry activity create no
notice. Keep only current/latest result per conversation, not an accumulating
result archive.

Accepted gallery correction: the user said, “looks good, just instead of the
dismiss button, put an X icon on the right.” Terminal results use a `×` button
in a right-aligned header/grid cell, with both `aria-label` and `title` set to
`Dismiss retry notice`. Keep it terminal-only. Preserve active Retry now/Stop
actions, count/elapsed presentation, exact conversation+chain dismissal
persistence and keyboard/focus behavior. This is a visual correction with no
backend, architecture or API change. Implementer0 owns the A renderer change;
after A publishes, implementer1 owns the sole final A pin/cache identity and
existing fixture-selector adoption. Lead reports UI/keyboard browser checks
passed in attempt 4e1; this correction retains those acceptance requirements
and does not resolve the separate composer member-upload finding.

#### Align the dismiss icon with existing portal controls

On 2026-10-24 the user asked to unify the retry X with existing portal controls,
questioning whether it was bold. This refines the accepted icon above. Source
inventory uses frozen A `a58f07064c560bb30efb0228ec6307bcd991d7ab` and B
`207ccfe0d55e8b68fde8a1b68fa80f051cc5a124`; no new browser observation is claimed.

Standing user preference: preserve uniformity for all controls that appear in
multiple portal locations. Before adding or changing a repeated control, inspect
existing occurrences and reuse their established appearance and interaction:
control type, size, typography, color, spacing, hover, focus, disabled state and
keyboard behavior. Keep context-specific differences deliberate and justified
by the control's purpose or accessibility. Implementer1 owns the lasting
repository `AGENTS.md` guidance under the lead-approved prose. This principle
governs future changes; the current A/B package remains the narrow dismiss-style
refinement, with no new framework, general refactor, backend or mechanism.

The closest representative is the ordinary message-receipt dismiss control in
the same transcript. B `static/app.js:4073–4078` uses the same `×` character;
`static/style.css:349–350` sets normal weight 400, size 1.1rem, line-height 1,
zero padding, a transparent borderless surface, muted text, .2rem radius and
a 1.5rem square target. Hover/focus uses panel-2 background and normal text.
The restored-session notice instead uses an 18px SVG cross with stroke width 2
(`templates/session.html:51`) in the general 28px `icon-button` target. Its
muted/hover colors and explicit accent focus ring are at `style.css:518–520`.
Settings dialogs use textual Close/Cancel controls; they supply no competing
X-glyph convention. No separate drawer-close icon was found in the inspected
portal templates/static controls. This is a local refinement, not a portal-wide
icon/component consolidation.

A's retry dismiss (`conversation/assets/conversation.css:175–186`) uses 1.5rem
text in the normal foreground, versus the receipt's muted 1.1rem: it is about
36% larger at the same root size. Its class-level `font: inherit` overrides B's
generic element-level `button { font-weight:700 }`; the title's 600 weight
belongs to a sibling. Thus source predicts normal weight, not bold. The size
and contrast explain a concrete mismatch without claiming measured pixels.
The retry control also lacks its own hover rule, allowing B's more-specific
`button:hover` background to win. Explicit hover/focus styling is part of this
correction.

Implementer0 owns a CSS-only A package in `conversation/assets/conversation.css`:
retain `×`, the header's right grid cell and existing renderer/action behavior;
set dismiss glyph size 1.1rem, explicit weight 400, line-height 1, grid centering,
zero padding/border and .2rem radius. Use existing `--codex-muted` for its resting
color, with a portable fallback, and explicit hover/focus styling that cannot
inherit a host's primary-button background. Retain the existing 2rem desktop /
2.5rem narrow-screen retry hit target; only the glyph becomes smaller, preserving
the existing touch area and heading layout. Keep the visible keyboard outline.
Do not change shared Retry now/Stop button styling or renderer JS merely to
restyle dismissal.

Implementer1 owns B's scoped theme mapping in `portal/internal/web/static/style.css`
and final A dependency pin. Match the receipt's resting `var(--muted)`, hover/
focus `var(--panel-2)` background and `var(--text)` color. Match the ordinary
receipt's browser-provided keyboard outline, as corrected by the capture 7
finding below; the earlier icon-button accent-ring choice is superseded.
Scope this to the retry dismiss selector; preserve receipt/dialog controls,
their positions and behavior. Reuse existing theme values, with no new public
styling API or generalized control framework. The larger transparent retry hit
target is intentional; its visible glyph, weight and colors match the receipt.

B also owns fresh CSS cache identities in `templates/session.html`: advance
`conversation.css?v=11` and `style.css?v=23`, plus the corresponding existing
`browser_asset_versions_test.go` expectations. A assets have a five-minute
cache lifetime; pinning new source alone does not refresh an old CSS URL.
For this CSS-only correction, unchanged JS/module URLs need no artificial
version bump. If implementation changes a JS asset, refresh its actual parent/
child consumers under the established cache contract. Old and new styles keep
the same DOM, labels and storage keys, so mixed cached assets cannot change
delivery, dismissal identity or backend capability.

After owner quick checks, extend the existing actual-template visual fixture
with a controlled ordinary receipt dismiss and terminal retry dismiss in the
same desktop/mobile page. Compare resting, hover and keyboard-focus glyph size,
weight and color; assert the preserved retry hit target, right alignment and
accessible name/title `Dismiss retry notice`. Retain terminal-only presence,
Enter/click dismissal, exact-chain reload persistence, new-chain appearance,
zero dismissed footprint and unchanged active controls/count/elapsed checks.
Keep capture 6's passing evidence intact and obtain a fresh visual comparison
for this refinement; it supplies no new user acceptance by itself. No test,
capture, native/CI run, source edit or operation is authorized by this design
lane; the lead assigns implementation and later verification. Backend and
rollout gates remain unchanged.

#### Capture 7 correction: use the same receipt focus outline

Capture 7 passed in 32.521 seconds at A
`5743f94c2fbd01b65438847d2e2bab0f01df32ae` / B
`1f737473e322c2b6f6e914b99f6315c98e986d02`. Its saved desktop/mobile
`dismiss-ordinary-focus-*.png` images show the receipt button's light browser
outline, while `dismiss-controls-focus-*.png` show the new retry button's green
outline. Independent inspection of those actual images confirms the lead's
finding. The comparison JSON includes font, glyph colors, background and radius
but no outline fields. The fixture then separately asserts the green 2px solid
outline with 2px offset (`retry_activity_browser_test.cjs:178–181`). The pass
therefore does not establish focus-outline equality or visual acceptance.

Source cause: B `static/style.css:278` implements the earlier design's explicit
accent outline; the ordinary receipt rules at `:352–353` set hover/focus colors
but leave outline to the browser/user stylesheet. Simply deleting B's retry
outline rule would expose A's generic 2px/currentColor/2px fallback, which also
does not reproduce the receipt's native outline treatment.

Smallest correction belongs entirely to implementer1 in B: replace only the
retry dismiss `:focus-visible` outline declarations with `outline: revert;`
and `outline-offset: revert;`. This rolls those properties back past author
styles to the browser/user defaults, just as for the existing receipt button.
Retain the scoped foreground/background rule. Do not use `initial`, `unset`,
`none`, a guessed white color, a browser-specific focus-ring token, or runtime
copying of computed CSS. Keep A's portable generic fallback and its pin unchanged.
Do not restyle the existing receipt, global icon-button or other portal control.
The retry hit target remains 32px desktop / 40px narrow, with existing right
alignment, visible keyboard focus, accessible label/title and exact persistence.

Extend the real-template comparison before accepting the remedy: record each
focused control's `outlineWidth`, `outlineStyle`, `outlineColor` and
`outlineOffset` under the existing genuine Tab/Shift+Tab sequence. Require exact
equality with the ordinary receipt in the same browser/page, plus nonzero width,
non-hidden/non-none style and a visible outline; retain the screenshots for
visual confirmation. Replace the old green-ring constants with this reference
comparison rather than deleting focus coverage. Preserve glyph/rest/hover
equality, 32/40 target checks, dismissal/reload and active-control assertions.
Save the expanded focus values in the desktop/mobile comparison JSON. Their
exact values were not retained by capture 7 and are not inferred from pixels.

B owns `static/style.css`, the focused fixture and the applicable stylesheet
cache-identity assertion/update in `templates/session.html` and
`browser_asset_versions_test.go`; unchanged A/JS assets need no new identity.
Keep capture 7 artifacts intact. The lead owns step-9 review remediation and
the fresh focused capture before renewed visual acceptance. This amendment is
design/evidence only: no browser, test, source, CI, native or live operation was
performed by the architect; backend and rollout gates are unchanged.

### Fixed shared A/B API and fixture DTO

Add a source-compatible optional interface; retain the old `RetryProvider` for
other embeddings. `Target.RetryActivity` and `Capabilities.RetryActivity` opt in.
All methods receive the server-resolved native thread, never browser routing.

```go
type RetryActivityProvider interface {
    ReadRetryActivity(context.Context, string) (RetryActivityStatus, error)
    RetryNow(context.Context, string, string) (RetryActivityStatus, error)
    StopRetry(context.Context, string, string) (RetryActivityStatus, error)
}
```

Routes are `GET retry/activity`, `POST retry/now`, `POST retry/stop` beneath the
existing conversation route. Each POST accepts only `{ "token": "..." }`.
Successful reads/actions return the same JSON shape. Use these exact field
names for both presentation packages and fixtures:

```json
{
  "serverNowMs": 100000,
  "activity": {
    "chainKey": "opaque-stable-chain-key",
    "class": "capacity",
    "phase": "scheduled",
    "confirmedStarts": 3,
    "unconfirmed": 0,
    "countQuality": "exact",
    "startedAtMs": 30000,
    "elapsedMs": 70000,
    "timingQuality": "exact",
    "finishedAtMs": null,
    "nextAttemptAtMs": 115000,
    "outcome": "",
    "reason": "",
    "retryNowToken": "opaque-attempt-token",
    "stopToken": "opaque-chain-token"
  }
}
```

`activity:null` means no notice. `chainKey` is the opaque stable identity used
with the application conversation ID for local dismissal. Classes are capacity
or cybersecurity. Presentation phases are scheduled, submitting, reconciling,
running and terminal; terminal outcomes are success, stopped, exhausted,
superseded and blocked. Reason is bounded safe presentation text, never raw
native data. Action tokens are empty when unavailable. Counts are bounded
nonnegative safe JSON integers; `unconfirmed` is 0 or 1. Unknown counts use
`confirmedStarts:null`, not a fabricated zero. Count/timing quality is exact,
partial or unavailable. Missing historical timing uses null startedAt/elapsed
with unavailable quality. `finishedAtMs` and `nextAttemptAtMs` are nullable.
Exact active elapsed advances from the server observation; terminal elapsed is
frozen. The renderer must not claim approximate/partial data is exact.

A exports `mountRetryActivity(root, {client, conversationKey})` and optional
client methods `retryActivity()`, `retryNow(token)`, `stopRetry(token)`; the
controller exposes `refresh()` and `destroy()`. It owns only footer children,
coalesces refreshes, suspends timers off-page and ignores stale responses after
conversation changes/destruction. Browser dismissal uses localStorage keyed by
exact conversationKey+chainKey and causes no backend write. Failure to persist
dismissal affects reload persistence only, never sends/preferences. Countdown
uses serverNowMs and a monotonic browser clock, not browser/server wall-clock
agreement. Do not announce a changing countdown every second to screen readers.

B adds `GET/POST /api/sessions/{slug}/retry-policy`. Response is
`{revision, capacity, cybersecurity}`; POST requires both booleans and
`expectedRevision`. Use an opaque revision string to avoid integer precision
coupling. A differing stale choice returns 409. An already-current same-valued
POST returns current state with no effects, including after a lost reply.
Revision changes only for an effective preference change, never for reads,
metrics, checkpoints, Stop or RetryNow. Bootstrap establishes the first revision.

Provide bounded typed errors for stale action and reload-required (409), and
unavailable policy/action state (503). B's successor rejects legacy boolean and
tokenless cancel POSTs as reload-required; it never reinterprets a thread toggle
as a session-wide mutation. A's old interface remains usable by other
applications. No new native/client ID or options fields enter browser payloads.

### Exact action identity and cancellation

Tokens are server-issued comparison identities, not authentication or native
execution grants; normal authorization is always required. They bind the exact
session incarnation, conversation, chain, policy revision and operation.
RetryNow additionally binds Pending.ID. Opaque deterministic digests of these
server-owned identities suffice; no new credential/signing service is needed.
Stop deliberately does not bind attempt/status revision so it remains valid
across retries in that chain. Both operations recheck under existing admission.

RetryNow shortens only that saved scheduled deadline. It never generates a UUID,
increments count/quota or invokes native execution. A duplicate for the same
already-accelerated/submitting/reconciling/running attempt returns current state
without mutation. A different Pending ID, new chain or policy revision returns
stale. The worker still applies all ordinary authority, policy, queue, prompt,
failure, settings and reconciliation checks before dispatch.

Stop persists cancellation using the existing exact schema-1 State.Cancel and
Handled behavior before acknowledgment. Same-chain duplicate Stop succeeds
without further mutation, including after its cancellation tombstone exists.
Different chain or policy revision refuses. Preserve unresolved Pending,
immutable options and cyber charge; later exact accepted ResultTurn is consumed
and cannot revive the stopped chain. Do not use optional metrics persistence as
cancellation authority. If the authoritative ledger write fails, do not claim
success; if only summary checkpoint fails, acknowledge the saved stop and show
partial/unavailable summary. An unreadable policy sidecar already holds fresh
automation; report action unavailable rather than inventing token validity.
Keep exact receipt-only recovery reachable before an activity-known gate: an
unresolved UUID must not prevent its own reconciliation or durable suppression.
That narrow path never grants fresh dispatch or cold activation.

### Session policy storage, bootstrap and class gates

Leave deployed retry schema1, MaxSnapshots64 and generic submission schema3
unchanged. Add one strict versioned sidecar per session outside the existing
per-thread `*.json` count, under a dedicated `turn-retry-policy` directory.
Use current workspace/slug/root/incarnation identity, policy revision and two
booleans; up to 128 current-incarnation thread entries hold per-class baseline
observations, bounded current-chain/pending cancellation identities and compact
current/latest summary. Limit the file to 1 MiB. It stores no prompt, settings
snapshot, credentials or duplicate submission ledger. Atomic replace/fsync and
a short interprocess read-modify-write lock follow existing private-state rules.

Bootstrap once under runtime EX with stable retained membership. Read exact
matching legacy root and all nonremoved current-incarnation member records:
any Enabled=false makes both session switches false, otherwise both true.
Missing legacy record is old default-on; malformed/unproved/unbounded inventory
holds automation instead of guessing. Persist before using the policy. Once a
sidecar exists, no fallback to legacy Enabled or per-thread exception is allowed.
Explicit saved session choices govern all current/future members. Do not eagerly
rewrite all per-thread ledgers or add a migration bridge.

Adopt a pre-existing owned pending chain only through exact identity when its
inherited class is enabled; inherited off suppresses it without losing unknown
settlement. Already-failed tasks without an owned chain remain excluded.
Controller/internal gates take explicit effective per-class authority rather
than temporarily replacing or persisting State.Enabled. Apply it to all fresh
Begin/Reserve/Continue paths, including restarted positively never-submitted
attempts. Exact reconciliation runs regardless of on/off. Cross-class failures
use the newly observed failure class while retaining the same chain identity.

### Preference transaction and enable boundary

Reuse the existing session runtime SH/EX fence; do not add another all-writer
policy lock. A preference POST selects context-bounded EX directly before
roster/conversation locks, never upgrades a held SH. Acquisition, inventory of
at most 128 threads, both cold observations and commit share one 30-second
request budget. This is a finite upper bound, not a guarantee every inventory
fits. Timeout or incomplete identity proof aborts without policy mutation or
native/default inference. Same-valued requests perform no enrollment/cancellation.

Under stable membership, read exact terminal/active identity twice. An unchanged
independent inProgress turn qualifies if it fails after enabling; a terminal
turn at the final observation is consumed. Turnover or failed reads aborts the
transaction. The final verified observation is each thread's enable boundary,
followed by one atomic policy save and acknowledgment. Native completion can
race the observation/file commit: this is the accepted observation boundary,
not a subsecond wall-clock or native CAS guarantee. Independent direct native
writers remain outside the managed contract.

Turning a class off records affected current-chain/uncertain identities in the
same atomic policy commit. Lazy per-thread cancellation/settlement may follow;
the committed class gate prevents new dispatch meanwhile. Turning back on
retains stop/off/settings/retention suppression and uncertain UUID tombstones,
so toggling cannot revive a cancelled retry chain. Preserve independent active
task eligibility under the two-read rule. New members receive the saved session
choice and enroll before first managed dispatch, with their own incarnation;
do not transfer another member's baseline or use enqueue defaults as execution
proof. Bound tombstones per current chain rather than accumulating history.

### Locks, failure isolation and preserved incident contracts

Existing managed participation is source-backed: B `web/server.go:2030` session
HTTP and `:3670` conversation resolution take runtime SH; `web/turn_retry.go`
dispatch/reconciliation takes SH; `libexec/dev-session:1816` team mutations and
membership use `with_slug_lock`, whose `:7952` implementation holds the same EX
lock across helper execution. Provider/lifecycle paths retain their fences.
Low-level native clients remain outside the managed guarantee.

Order is package transition -> runtime SH/EX -> roster when required ->
conversation -> per-thread admission -> generic ledger/native queue. Sidecar
RMW is a short inner checkpoint only: never hold it across native RPC or acquire
an outer/admission lock from it. Preference EX observations happen before its
final short sidecar write. Per-thread actions/workers under SH+admission may
checkpoint under sidecar RMW; read the latest sidecar before writing, preserving
concurrent policy and other-thread fields. Polling never takes runtime EX.

Manual Send/Queue/Implement/team delivery MUST NOT depend on reading,
bootstrapping, validating or writing this optional sidecar. Corrupt/full/read-
only summary or policy metadata can stop automatic dispatch and degrade its
presentation, but cannot add a manual-send refusal or block exact generic
receipt settlement. Keep current native/ledger safety and existing provenance
admission rules. Manual paths may leave optional summaries for later observer
settlement. Do not create a metrics event ledger or duplicate generic receipts.

Retain Incident 2 prepared nonqueued exact-first-execution proof, receipt-first
plan recovery before ordinary activity proof, immutable original UUID/text/
options/context, old-epoch exclusion, finite context-aware HTTP SH wait and all
post-acquisition generation/lifecycle/authority checks. Automation remains
fail-fast when session runtime is busy. Retain ed2 accepted-only retirement,
current-turn proof invalidation, protected unknown/queue records and original-ID
replay under >64-message pressure. New policy/summary data must not add another
capacity condition to those ordinary delivery paths.

### Honest count and elapsed-time checkpoints

Start elapsed time when a new retry chain first schedules, including backoff,
execution and restart waits. Increment confirmed starts only on exact accepted
native receipt/history for a new Pending.ID; duplicate reconciliation adds zero.
At most one possibly submitted/unconfirmed attempt is shown separately. Polls,
clicks, Begin/quota reservation, definitely unsubmitted preparation and refusals
are not starts. State.Attempt is unsuitable because Begin increments before
native dispatch. Quota continues to use its existing conservative charge ledger,
never the presentation count.

Store only cumulative confirmed count, last confirmed UUID, chain start/frozen
end and quality in the compact summary. Checkpoint around scheduler/receipt
transitions without making metrics a delivery prerequisite. Restart, legacy
adoption or a persistence gap must show partial/unavailable unless original
native evidence proves exact count/time. Never infer missing starts from polls,
wall-clock time or quota. A terminal result freezes elapsed at its evidenced
terminal observation; unavailable original timing remains unavailable.

### Compatibility and recovery

Publish `turnRetrySessionPolicy: 1` alongside unchanged `turnRetryStateSchema: 1`.
Before creating policy sidecars, install guard support in the selected package
and candidate-activation path. Presence of even a malformed sidecar requires a
candidate with matching support. Preserve sidecars in supported session recovery
and archive/revive ownership flows; their presence must not create lifecycle
permission. Old packages can parse legacy ledgers but ignore session choices,
so rollback after sidecar creation is operationally unsafe. Recover forward;
do not delete state or reset opt-outs to select a predecessor. No native upgrade,
Codex patch, new schema1 fields or submission-format migration is in scope.

Capability-gate production controls and old POST refusal as described above.
Stale browsers refresh on stale/reload-required responses and never fall back
to generic Send. Preserve existing runtime host-module and workspace nested
selection; application stays in the user profile. Lead owns final A -> B ->
workspace/config pins, reviewed build/copy, activation and user acceptance under
the retained machine claim. This brief authorizes no integration, lifecycle
action, claim release or deployment by the architect.

### Acceptance and verification gates

First produce controlled real-template desktop/mobile screenshots of:

- Session Settings with both switches and explicit whole-session scope.
- Capacity: 3 confirmed starts, 15-second countdown and total elapsed.
- Cybersecurity, one unconfirmed submission, and accepted/running continuation.
- Success, stopped and quota-exhausted dismissible results, including partial
  metrics and stopped before a first confirmed retry where applicable.
- Idle/off/legacy-cancelled and dismissed states with zero footprint; reload,
  a new chain, member switch, scrolled-up transcript and narrow mobile composer.

Use a focused private httptest fixture patterned on
`web/question_browser_test.go:21`: actual template, CSP, assets and Playwright
with synthetic API responses. Assert screenshots use the real template, not a
mocked layout. Preserve footer across filters, history prepend, full render,
member change and live update; verify scroll anchors, focus/selection, accessible
labels, count/time formatting and no persistent spacer. Give images to the user
before backend expansion. Fixture-only capture requires no real provider or
native run. A/B owners run their appropriate focused Go/Node quick checks and
compile the fixtures; screenshot execution follows the lead's verification
ownership and required monitor procedure when duration is uncertain.

Backend quick/race and real-wrapper regression gates then include bootstrap
inheritance, exact current-incarnation scope, classes independently enabled,
same-valued policy no-op, same-active enable/terminal exclusion/turnover refusal,
off-on cancelled-chain exclusion, current/future membership, crash at each
commit, restart/unknown settlement, stale policy/new-chain tokens, duplicate
Stop across retries and duplicate RetryNow for one UUID, unchanged quota, finite
lock cancellation and sidecar concurrency. Malformed/full/unwritable optional
data must leave actual root/member Send, Queue and Implement-plan usable.
Retain actual HTTP prepared-plan/ack-history recovery, EX-contention wait,
post-wait authority refusal and ed2 pressure/replay tests; do not replace them
with helper-only fixtures. Verify successor downgrade refusal and forward
recovery without rewriting strict deployed ledger fixtures.

After completed commits and quick checks, the same independent reviewer checks
affected general/architecture/scope/risk lanes before long/native verification.
Lead selects final packaged A/B checks, applicable focused controller/native
checks, W/C composition and scoped system/profile builds; reuse unchanged
successful checks only with exact input/derivation receipts. No automatic
unrelated hour-long VM campaign. No deployment until presentation acceptance,
review and required verification are complete. Post-deploy acceptance includes
portal/naming/root/team continuity and retry UI/settings behavior without forced
live policy failures or synthetic work in a registered conversation.

Source evidence: baseline B `templates/session.html:108` puts the old row above
the viewport; `static/app.js:4447` and `:4472` replace/prune transcript children;
`static/style.css:272` owns scrolling. `turnretry/state.go:148` retains per-thread
preferences and `:310` increments Attempt before send; controller lines 105/200
use Enabled directly. `web/turn_retry.go` owns current projections/actions;
`libexec/workspace-host:2787` checks only the existing schema capability. A
`conversation/retry.go` owns the existing optional API. Preserve these baseline
contracts while replacing their UI/policy behavior as explicitly scoped here.

### Backend release contract after presentation acceptance (2026-10-24)

The user accepted capture 8 at A
`5743f94c2fbd01b65438847d2e2bab0f01df32ae` / B
`59c0eb55da9b8918c7f1a4dd8a8cb4c09fbdcb11`. This fulfills the presentation-first
gate above; it does not establish backend implementation or deployment. The
accepted policy/action/metrics contract remains in force. Incident 2 prepared
plan recovery/runtime waiting and ed2 provenance retention remain mandatory.

**Fixed storage/capability consumer contract.** The Go owner writes one private
file at `$DEV_WORKSPACES_STATE/turn-retry-policy/<workspace-sha256>/<slug>.json`,
where the workspace hash is lowercase SHA-256 of the exact canonical workspace
string used by the existing retry store. Its separate short RMW lock is the
same pathname plus `.lock`. The file has strict schema `1`, maximum 1 MiB
(read at most limit+1 and reject oversize), mode 0600 and owned mode-0700
directories. Require workspace, slug, retained root and nonempty incarnation;
incarnation is the existing `session.ObservationIdentity` for that exact root
and tracking directory, not native sessionId, package generation or roster
revision. That identity uses directory device/inode and retained root, and
survives the supported tracking rename. Identity mismatch never means empty
policy or permission to overwrite it. Preserve the record and hold automation.
The strict envelope holds the policy revision/two booleans and at most 128
current-incarnation thread entries as specified above; no generic receipt copy
or schema1-ledger changes. Go owns JSON validation and its internal field layout;
Ruby neither parses nor edits the sidecar payload.

The packaged `portal/internal/session/runtime-contract.json` publishes exact
integer `turnRetrySessionPolicy: 1`, retaining `turnRetryStateSchema: 1` and all
other capabilities. Any policy `.json` beneath the dedicated directory requires
that exact candidate capability independently of legacy retry-record presence.
Malformed, oversize, empty or wrong-incarnation files still require support;
inspection failure is not absence. Do not inspect all payloads to decide the
guard, silently delete them, infer defaults or migrate them. Empty directories
and lock/temp files alone are not committed policy. Existing selected-package
preparation/activation checks and candidate self-activation must enforce this
contract before selecting or starting an incompatible package. Supported
archive/revive/recovery leaves these user-state records in place alongside the
legacy retry ledgers, preserving preferences and cancellation evidence. No
cleanup or lifecycle action is authorized by their existence.

**Independent Ruby package — implementer0.** Own only B
`libexec/workspace-host`, `portal/internal/session/runtime-contract.json`,
`test/workspace_host/profile_transition_test.rb`, and any narrowly necessary
Ruby host test support/activation tests agreed with implementer1. Add the
presence guard to the existing session-recovery compatibility chain; do not
change lifecycle lock modes, timeouts, generation checks or policy contents.
Keep `docs/turn-retry-recovery.md` with the Go owner; send that owner the guard
wording so both contracts have one documentation home. Required focused tests:
no-sidecar compatibility unchanged; sidecar-only state without legacy ledgers;
empty/malformed/oversize sidecar still blocks absent/wrong capability; exact
capability succeeds without modifying bytes; legacy schema guard remains;
selected prepare/activation and candidate activation cannot bypass refusal;
retained state survives successful compatible selection and refusal. Use
existing disposable Ruby host fixtures, no live package operations.

This Ruby package is independently releasable to the lead now. Both owners use
the same B worktree: implementer0 makes scoped uncommitted edits or a patch;
implementer1 is the sole B Git owner until an explicit serialized Git turn.
No concurrent staging, commits, branch changes or history operations. Owner1
does not edit the contract JSON/Ruby files while owner0 owns this package.
Integrate guard support before any production sidecar creation; ship Go and
Ruby support together in the final reviewed package. Forward recovery is the
only supported path after sidecar creation; old packages must not be selected
by deleting policy state.

Source revalidation at B59c: `session/observation.go:24` owns incarnation;
`session/authority.go:52` already supplies context-aware SH waiting and the
private lock loop supports either mode; `workspace-host:2773` chains recovery
guards, with prepare/activation call sites at 666, 694 and 1015. The existing
retry guard at 2790 checks only legacy files, hence the independent presence
guard is required. This does not alter the accepted native no-CAS boundary.

**Go backend package — implementer1.** Own B `portal/internal/turnretry/`
(new policy store/decision/summary units and existing controller/state methods),
`portal/internal/web/turn_retry.go`, a new `turn_retry_policy.go`, the narrow
route/provider wiring in `server.go`, and their tests. Consume the fixed EX
helper from implementer0 below. Own any necessary `session/contract.go` accessor/tests,
but leave `runtime-contract.json` exclusively to implementer0. Own narrowly
required `workspacecodex/turn_retry*.go` adapter changes and production wrapper
tests; manual capture, delivery and recovery remain policy-sidecar independent.
Own `docs/turn-retry-recovery.md` and `docs/workspace-portal.md` reconciliation.
No presentation redesign or new A change is required: A5743 already publishes
the optional activity interface, DTO and typed errors above. Wire
`Target.RetryActivity`/capability to that interface; preserve the accepted
frontend/cache identity unless actual integration requires a bounded asset
change. Lead owns visible copy and later pins.

**EX helper ownership update — implementer0.** Lead released the additive
`session.LockRuntimeExclusiveContext(ctx context.Context, directory, slug string)
(*RuntimeLock, error)` helper to implementer0 after owner1 confirmed the files
were untouched and reserved. Owner0 alone edits
`portal/internal/session/authority.go` and new
`portal/internal/session/authority_exclusive_context_test.go` for this package.
The helper delegates to the existing `lockRuntimeContext` with suffix `.lock`
and EX mode. Do not add a private flock loop or change existing fail-fast
SH/EX/lifecycle callers. Disposable tests cover exclusive contention, successful
acquisition after release, cancellation/deadline and lock release. Owner1 consumes
that exact API and leaves both files untouched until handoff. Owner0 supplies a
scoped patch/uncommitted edits without Git operations; owner1 remains sole B Git
owner. The accepted-fork evidence package below is queued for lead release after
this helper handoff; no accepted-fork product wait fix is authorized.

Internal implementation names may follow local conventions; the interfaces
between packages are fixed by the sidecar path/capability above and the existing
A DTO, not by a new public Go protocol. The controller must receive an explicit
per-thread session-policy decision (revision, class permissions, enrollment
watermarks and suppression identities) under its caller's runtime fence and
per-thread admission. Absence/error is no fresh automatic authority. Replace
all uses of legacy Enabled for fresh scheduling/Begin/reservation/dispatch,
including the positive-never-submitted restart path. Do not temporarily assign
Enabled or rewrite it on disk. Leave its value available only for one-time
legacy inheritance; all subsequent session decisions override it. Receipt-only
reconciliation must remain usable without a policy decision or summary writer.

**Transaction wiring and enrollment.** Dispatch the exact `retry-policy` route
before `sessionAPIForSummary` enters its general mutation SH branch. POST takes
package transition SH, then context-bounded runtime EX directly, then freshly
validates package generation, lifecycle, root/incarnation, runtime authority,
provider and stable retained roster. Reuse the 30-second total budget above;
do not call the ordinary resolver inside EX if it reacquires SH. Process thread
observations/admission locks in stable thread-ID order, with no native call
under the sidecar RMW lock. Commit the complete preference/baseline/tombstone
candidate once; failed/partial inventory, identity change, turnover or timeout
cannot leave a partly changed policy. Same-valued POST returns the current
revision with no baseline/ledger/summary writes after normal authorization.

Bootstrap is a separate bounded session transaction before automatic work,
using the same runtime EX path. A per-thread worker holding SH must release it
and request/retry bootstrap separately; never upgrade or recursively reacquire
runtime locks. GET/polling is read-only and never takes EX; absent/unavailable
policy reports unavailable until bootstrap completes. A failed bootstrap holds
automation and leaves manual flows usable. Include all nonremoved retained
members in the inventory, not just ready members dispatched by the worker.

Per-class baseline entries distinguish an unchanged active independent turn
from the terminal turn consumed at the enable boundary. Existing cancellation,
settings/epoch, quota-exhaustion and retention suppression always take priority.
An off commit records the exact affected chain and unresolved Pending.ID before
lazy ledger cancellation. Retain those identities across off/on until exact
settlement or independently admitted new work makes them irrelevant; bounded
replacement must never discard unresolved cancellation evidence. A new member
inherits the saved session choice. Its ordinary managed capture still performs
the existing per-thread enrollment before native delivery without consulting
the sidecar; the worker can materialize its policy entry lazily from the exact
same-incarnation enrollment/proof before automatic dispatch. Do not impose a
sidecar write on that first manual message or discard its eligible failure
merely because the policy entry was not yet materialized. Missing/unproved
enrollment holds automation. Member replacement never inherits another native
thread's baseline or chain.

**Action/recovery wiring.** The exact action tuples remain incarnation/thread/
chain/policy revision/operation, plus Pending.ID for RetryNow. Validate under
the normal generation/runtime/retained-identity/conversation/admission order.
Stop's authority is the saved schema1 cancellation/Handled, with Chain retained;
same-chain duplicates do not need a second tombstone write. Consume the exact
scheduled failure or accepted result as appropriate and retain an uncertain
Pending until exact settlement. A summary checkpoint failure cannot undo or
prevent acknowledgment of this authoritative saved Stop. If policy identity
cannot be read, do not invent a token match. RetryNow only changes a scheduled
deadline; an already accelerated or progressed same Pending is a no-op, while
a new Pending/revision/chain refuses. Neither action invokes Continue,
Interrupt, resume, queue activation, settings or new native IDs.

Do not repeat Incident 2's outer-guard failure: the owning unresolved intent
must reach exact receipt-only recovery and durable Stop even when ordinary
activity-known admission would reject it. Use the existing internal
reconciliation identity checks as the model for a narrowly scoped action
resolver; verify the token against the exact saved thread/chain/Pending before
allowing its own unresolved tuple. This is no general unresolved-attempt bypass
and never grants fresh dispatch. Test actual Server.Handler resolution for
root and member. Keep existing exact prepared-plan reconciliation before
ordinary mutation validation intact. Reject legacy boolean/tokenless action
POSTs with reload-required, never convert them to session preferences.

**Summary isolation and crash boundaries.** Keep only current/latest chain,
cumulative confirmed starts, last confirmed Pending UUID, bounded timing and
quality/checkpoint identity per thread. The ledger/generic receipt remains the
sole execution/uncertainty authority. Save the retry ledger's accepted result
first; only then checkpoint its confirmed start once. A count checkpoint cannot
precede native acceptance. Before replacing an accepted Pending with the next
attempt, settle its summary checkpoint or explicitly lose exactness; if crash
continuity cannot be certified, hold further automatic progression or report
partial/unavailable, never reconstruct counts from Attempt/quota. No metrics
failure may fail manual delivery, remove protected Pending or roll back an
accepted receipt. Native unknown contributes at most one separate unconfirmed
attempt. A current chain stays visible through running; terminal observation
freezes its elapsed time. Legacy idle/off/cancelled with no retry activity
produces no notice. The sidecar lock is short read-modify-write inside existing
outer locks, never sidecar-to-admission/native. Per-thread metrics writes preserve
other threads and policy revision. Stale summaries cannot restore old tokens.

**Source-backed scope and release gates.** Existing B59c participation supports
the approved runtime fence: portal mutations/resolver hold SH, retry dispatch
and reconciliation hold SH, and `libexec/dev-session` team mutation/membership
uses `with_slug_lock` EX across the helper (`:1838`, `:7952`). Native writers
outside these managed paths remain outside the guarantee. ObservationIdentity
is retained directory/root identity, not proof of native loaded generation.
No new all-writer lock or lifecycle lock redesign is needed. The additional EX
context wrapper is HTTP/bootstrap-specific; ordinary bounded SH waiting and
existing fail-fast automation/lifecycle callers retain their behavior.

Owner1 quick checks cover `turnretry`, `workspacecodex`, `web` and `session` in
the repository Nix environment, with `go test -mod=readonly` and focused race
selectors for the new store/transactions/actions. Owner0 runs the focused Ruby
host transition suite through its existing suite runner, then the relevant
Ruby contract checks and focused `session` EX helper contention/cancellation
tests for its separately owned helper. Owners report exact selectors/results; the architect
does not execute them. Required regressions beyond the acceptance list above:

- Deployed schema1 bytes remain readable with unchanged validation; legacy
  false inheritance, independent class override, same-value stale-revision
  no-op, incarnation mismatch, absent member entry, new member enrollment and
  max-128/1-MiB refusal only for automation/policy changes.
- Real runtime EX/SH barriers prove preference changes serialize with portal,
  team and worker admissions; no SH upgrade, no RPC under sidecar RMW, finite
  EX timeout with zero mutation, and all post-wait identity checks. Two-read
  active/terminal/turnover boundaries and off/on unknown tombstones survive
  crashes before/after policy rename and before lazy ledger cancellation.
- Actual root/member HTTP Stop/RetryNow, stale/new-chain tokens, lost replies,
  same-chain Stop across attempts, same-attempt RetryNow through acceptance,
  exact unknown settlement while off/stopped, and unchanged quota charging.
- Actual root/member Send/Queue and plan HTTP recovery with corrupt, full,
  missing or unwritable optional metadata; retained >64 accepted-message
  pressure, original-ID replay, protected queue/unknown records, settings
  epoch exclusion, same-active binding and manual/controller admission races.
- Confirmed-count idempotency, persistence faults around acceptance/next
  scheduling, restart partial/unavailable quality, no poll/click/refusal counts,
  frozen final timing, and no notice for inactive legacy state.

After both disjoint packages are complete, owner1 serializes their commits and
the combined quick checks. Same reviewer affected general/architecture/scope/
risk review precedes long verification, including the exact host guard and all
new persisted-state semantics. Later selection remains packaged B/A checks,
affected Ruby shards/aggregate with exact derivation reuse, focused native B
controller/recovery, W/C composition and scoped builds. No new native protocol
is introduced; do not automatically repeat unchanged A native cases. Final
backend wiring still needs real-template interaction/regression verification;
capture 8's accepted presentation evidence is retained, not replaced by a
backend unit test. Lead owns final selectors, watcher, deployment and acceptance.

The earlier creation-CI SH/EX failure remains a separate unresolved diagnosis
and verification gate. This feature neither waives it nor claims its holder or
latency is explained by retry policy. No sleeps, authority weakening, lifecycle
lock changes or unmeasured optimization are included in either package.

### Remaining backend verification and independent browser package (45e14be3)

Planning baseline: A `5743f94c2fbd01b65438847d2e2bab0f01df32ae`; B
`45e14be3d34a9ca2d3b418c310da927351b7f330`, tree
`edb3f41dec072a44e03a4f4a7a4c4e8894b440f4`. The four final review lanes in
`backend-successor/review.md` apply with the narrow I-B1 correction accepted
in `backend-successor/I-B1/step9-disposition.md`. That disposition supersedes
the earlier pending wording in its owner handoff. Completed pressure evidence
now passes in 61.278 seconds, exit 0, all 19 required top-level tests and 14
pressure leaves, zero skips; see `I-B1/pressure-lead-acceptance.json`. Do not
repeat that diagnostic batch without a relevant source/environment change.
Accepted-fork attempt 1 stopped before tests because gcc was missing. Owner0's
environment-only preparation and its subsequent execution remain separately
owned; this is neither a source finding nor a passed/waived creation gate.

**Remaining browser gap and package.** Capture 8 remains accepted presentation
evidence at A5743/B59c. Its actual template fixture intercepts policy/activity/
action responses (`retry_activity_browser_test.cjs`), whereas the new Go HTTP
tests exercise the real backend without the browser. Connect those boundaries
with one test-only package; do not redesign presentation or repeat its gallery.
Both packages are released by the lead. Implementer1 owns the complete new
`portal/internal/web/retry_backend_browser_test.go` and
`portal/internal/web/retry_backend_browser_test.cjs` package; both files were
absent at ownership transfer. Implementer0 owns the bounded fork fixture
diagnosis/fix in existing `portal/internal/web/creation_source_lock_test.go`
and `test/support/accepted_fork_runner.rb`. The browser package makes no changes to A, pins,
assets, production routes/providers/stores, existing test helpers or native
fixtures. Reuse existing helpers from `plan_delivery_test.go`,
`turn_retry_policy_test.go` and `turn_retry_activity_test.go` by calling them.
If they cannot support the fixture without edits, report the exact seam before
expanding ownership. Owner1 remains sole B Git owner; both packages coordinate
edits/compilation/source freezes in the same Go package, with final source
freezes and commits serialized with any active verification.

New `TestRetryBackendBrowser` uses disposable TLS httptest with actual
`Server.Handler`, trusted origin, root/member resolver, real
`workspacecodex.Client`, private synthetic wire, policy transaction/store and
`RetryActivityProvider`. Follow the existing question fixture's actual
template/CSP/assets/allowed-origin setup. Synthetic native read/effect adapters
and test-only scenario controls may initialize strict private records through
their owning APIs and expose exact receipt/history states. Do not fulfill or
rewrite retry-policy/activity/action HTTP responses, fabricate DTOs/tokens, or
replace provider/authority/receipt logic. Display-only native surfaces may use
local test adapters. Workers are explicitly controlled so a due deadline cannot
accidentally dispatch while checking buttons; no real daemon/model is started.
Unknown/accepted scenarios use the existing exact synthetic-wire acceptance and
reconciliation pattern, not a browser-invented count. A fixture response-loss
barrier may drop the response only after the real handler completes its write.

Use four named Go subtests `desktop-root`, `desktop-member`, `mobile-root`,
`mobile-member`, at the existing 1440x1000 and 390x844 viewports. Each reports
these eight named case results in a machine-readable manifest; require all 32:

1. `policy-scope`: bootstrap through the real transaction; both Settings
   switches read/write the same session preference from root/member, with no
   per-thread toggle. An effective change advances revision; reads do not.
2. `policy-stale-and-lost-reply`: actual second-tab revision conflict reloads
   current values; a post-commit lost response triggers readback without a
   second write. Same-choice exact POST replay has no effects.
3. `scheduled-now`: actual activity response renders countdown/count/elapsed
   inside the stable transcript footer. Retry now posts only the issued token,
   shortens the same Pending deadline, and neither dispatches nor changes
   UUID/count/quota. Explicit same-token replay is idempotent.
4. `stop-and-stale-token`: Stop cancels only the exact current chain, preserves
   preferences and ordinary native execution, acknowledges durable ledger
   cancellation, and is idempotent across same-chain replay. A new policy/chain
   invalidates old tokens; no stale response falls back to Send/Interrupt.
5. `unknown-and-confirmed`: a synthetic accepted-but-unconfirmed original UUID
   displays one unconfirmed; exact recovery counts its start once and retains
   the same chain. Stop remains reachable through its own unknown, without
   duplicate native mutation. Include an I-B1 stale checkpoint to show
   unavailable/partial count rather than falsely exact zero.
6. `terminal-dismissal`: terminal count/elapsed persist across reload, X is
   terminal-only and browser-local, reload stays dismissed for that exact
   conversation/chain, and a different chain reappears. No dismissal POST.
7. `footer-refresh`: ordinary refresh/filter/history rendering preserves the
   real footer and scroll anchor; idle/off/legacy-no-activity/dismissed leaves
   zero footprint. Preserve accepted controls, focus and composer layout.
8. `optional-unavailable-manual`: unavailable/corrupt optional metadata disables
   retry controls honestly while the actual ordinary HTTP send using its
   original browser identity remains usable; exactly one synthetic acceptance,
   no browser-generated retry UUID. Existing comprehensive pressure/plan/queue
   tests retain their own scope rather than being duplicated in this browser.

Fixture controls operate only inside the disposable test server and may return
bounded stage/counter diagnostics, never application status stand-ins. Assert
no unexpected page errors/HTTP failures/native methods. Save a small set of
actual-backend screenshots for root/member active, uncertain/partial and
terminal/dismissed states; these supplement accepted capture 8, not a request
to reopen style choices. Do not introduce a preview service or product hook.

**Bounded browser-fixture response expectations (2026-10-24).** Owner1's
source diagnosis establishes that policy controls render the saved value while
their POST is pending. Use one real checkbox click, arm the real response
observation before the click, then assert the exact policy response/readback,
eventual saved checkbox state and exactly one POST. Playwright `uncheck`'s
immediate local-state assumption is not this asynchronous product contract.
Do not change product behavior or add a second click/write to satisfy it.

The minimal TLS host deliberately lacks ancillary attention, coordination,
browser-notification, provider/limits and autoarchive configuration. Accept a
small fixture-local response expectation table only for owner1's exact
source-confirmed unsupported endpoints: fixture origin, HTTP method, full
resolved pathname/query and diagnosed status, plus a short missing-configuration
reason/source reference. The literal contract is now saved in
[`ancillary-expectations.json`](backend-browser/policy-ui-remedy/ancillary-expectations.json),
including each source reference and missing-service reason. Match only the
exact `base` or `manualBase` TLS fixture origin and these seven entries:

| Method | Path | Query | Status |
| --- | --- | --- | --- |
| GET | `/api/sessions/example/attention` | empty | 503 |
| GET | `/api/browser-notifications` | `?registrationId=` | 503 |
| GET | `/api/sessions/example/coordination` | empty | 503 |
| GET | `/api/codex-providers` | empty | 503 |
| GET | `/api/codex-providers` | `?session=example` | 503 |
| GET | `/api/codex-limits` | `?session=example` | 503 |
| GET | `/api/sessions/example/auto-archive` | empty | 409 |

The empty registration value is the exact fresh-context request from
`browser-notifications.js:308`; absent, nonempty or additional query parameters
do not match it. No prefix, arbitrary-member, status-wide or arbitrary-query
match is allowed. Preserve the
actual responses and record matched ancillary counts separately in the result;
do not intercept routes, return success/DTO stand-ins or suppress all failures.
These expectations describe this fixture's limited services, not production
health or a waiver of a failed retry assertion. No unrelated full-subsystem
fixture or new config framework is required.

Every unlisted HTTP failure, network failure, page exception and unexpected
native method still fails. Retry policy/activity/actions, ordinary Send/Queue/
reconciliation and the identity/settings interfaces supporting the 32 cases
cannot enter the ancillary table. Successful cases require actual successful
responses and durable outcomes. Deliberate owned failures, such as stale
revision, lost response and optional metadata unavailable, remain exact local
case expectations with their recovery/manual-delivery assertions, not global
exemptions. If a browser console diagnostic repeats a known HTTP failure,
correlate it to that exact expected response; never exempt arbitrary console
errors merely for containing 503/409. Keep all four viewport/role subtests,
all eight cases each, every existing retry assertion and zero-skip accounting.
This changes only the owned browser test package and its diagnostics; retain
the committed quick-check/review gate before another long run. Architect runs
no browser, source tests or live operation for this clarification.
Main and isolated compile roots may run independent quick checks concurrently;
each retains its own source freeze. Shared-worktree edits/compilation still
serialize, and owner1 remains the sole shared B Git owner.

**Eighth-case dependency check after attempt 8 (2026-10-24).** Assigned frozen
baseline: B `a62166a87658e16baa0efdddfea3a448ebebcc28`, tree
`49dee759cd203a94eb898c6af5f67fbe99474028`; pinned A remains
`5743f94c2fbd01b65438847d2e2bab0f01df32ae`. Attempt 8 reached six completed
cases per variant, then failed `footer-refresh`; that diagnosis and remedy
belong solely to owner1. This source-only check covers the unexecuted eighth
case, `optional-unavailable-manual`, and its final diagnostic acceptance. It
finds no additional concrete blocker and supplies no browser PASS or operational
readiness claim. No application/test edits, Git operation or execution occurred
in this check; owner1 must bind subsequent evidence to its final frozen source.

The CJS case uses a separate manual TLS host. Its Go constructor calls
`newPlanDeliveryFixture`, `addPolicyMember` and the real policy transaction;
only display reads/events are adapted. Corruption changes only that host's
optional policy file. The actual Settings error/disabled controls and activity
503 contract agree with the consumers. Ordinary Send still follows the real
Handler, member options where applicable, managed admission/recovery and pinned
A delivery. Root uses `/api/sessions/example/message`; member uses
`/codex/conversations/example~implementer0/message`. These are the paths selected
by `app.js` and A's `createConversationClient`, including the original browser
UUID and `retry:false` body.

The manual wire begins with a completed turn and positive recovery permission,
so this one fresh send reaches `turn/start`, whose response matches A's
`SendWithOptions`. Its `thread/resume` response omits `cwd`, but this path uses
`ReconcileThreadInstructionsWithPolicy`/`resumeThreadWithPolicy`, not
`ResumeThreadWithSettings`' strict ID/cwd response check; do not change the wire
or production validation on that unsupported suspicion. Managed admission
does not depend on the optional policy sidecar. The display adapter omits the
accepted user entry, so it does not consume the durable browser receipt:
`acceptMessageReceipt`, the exact sessionStorage key and `Sent to Codex` label
agree with the case's assertions.

Preserve one real message POST/202, matching receipt UUID, retained original
browser record, exactly one native start and byte-unchanged corrupt policy.
Diagnostic precision: `planDeliveryWire.updates`, exported as `settingsWrites`,
increments only for `collaborationMode` updates. Its unchanged value proves no
such mode update, not absence of every execution-policy settings RPC. Likewise
unchanged policy bytes prove no repair/write; the no-prerequisite-read conclusion
comes from the managed source path, not that hash alone. Neither limitation
requires weakening delivery proof or expanding this fixture.

Final acceptance remains the existing exact ancillary table plus the owned
deliberate failure expectations. In this case only same-manual-origin GET503
for the exact policy/activity paths and empty query is expected; manual POST
failure, page exception and any other unlisted failure still fail. Keep action
bodies token-only and all four manifests with the exact eight ordered cases
(32 total, zero skips). Footer correction and the retained quick/review/frozen
execution gates remain dependencies; this check adds no new package or test run.

**Attempt 9 queue-reconciliation failure: bounded source disposition.** Frozen
B `e22eecab01a691225f7464f0c8965526648f442a`, tree
`1aaa3b356b09875de643d9a1d76c1bd624ae3a7d`, with A5743. The full browser run
failed after 68.179 seconds despite all eight desktop-root scenario bodies
completing; the other three variants passed their manifests. Preserve the FAIL
in `backend-browser/footer-page-diagnosis/implementation/lead-attempt9-disposition.json`
and the original `browser-attempt-9/browser/{stdout.jsonl,artifacts/desktop-root/failure.json}`
under that implementation directory. No page errors occurred. This finding does
not reopen the eighth-case checks or waive the final negative assertion.

The rejected request is a real retry-host root POST
`/api/sessions/example/queue/reconcile`, empty query, body `{}`, HTTP404 during
`terminal-dismissal`. `app.js`'s `refreshQueue` invokes A's `reconcileQueue`
before GET queue; initial conversation synchronization, connected-state changes,
resumed page reads and the 30-second timer can trigger it. The terminal case
reloads twice, and its reload helper waits for retry activity plus two frames,
not ordinary queue settlement. Four root reconciliation requests were recorded
in that phase, without response-to-request IDs. Consequently the existing
artifact cannot select one exact trigger/request among those four.

This is not a missing route or missing queue RPC: B's legacy route forwards
to A's real Handler, both fixture wires implement empty `thread/queue/list`,
and the production queue-deletion reconciler is inherited. The saved server
log at `2026-10-24T16:21:01.46250015+02:00` identifies the rejection as
`resolve conversation: retained conversation or submission proof is unavailable`.
B's `requireOrdinaryRetainedMutation` returns that error from failed
`ObserveRetained`/unknown activity before A reaches `reconcileQueue`. It discards
the inner observation cause. No queue cleanup executed for this rejected POST.

There is a concrete production cancellation defect in the pinned A transport,
not a reason to fabricate fixture authority. At
`16:21:01.462392779+02:00`, 107 microseconds before the POST error, the same
root's thread/page verification reports
`failed to write msg: failed to acquire lock: context canceled`. A
`codex/client.go`'s `writeOffer` waits on shared `writeMu`, then calls
`connection.Write(ctx, ...)` without checking whether that caller was canceled
while waiting. Pinned websocket v1.8.14 can return that exact error before
writing a frame (`msgWriter.reset`/`mu.lock`). A then unconditionally calls
`markDisconnected`, clears the shared generation and fails every sibling
pending call. Ordinary navigation aborts old-document reads, so this path is
reachable without corrupt state or unknown delivery. It explains a possible
sibling observation refusal; the existing record does not prove whether this
particular POST was itself canceled or was a sibling casualty. Do not state
that the inner observation reason or exact pair has been measured.

**Proposed narrow production package, requiring lead release.** A owner0:
`codex/client.go` plus a focused `codex/write_cancellation_test.go`, reusing the
existing Unix-WebSocket and `waitFor` test helpers. Check caller cancellation
after acquiring the existing write/admission locks and before entering the
WebSocket write; return the existing `TransportError` wrapping `ctx.Err()`
without disconnecting the healthy connection when no write has been attempted.
Preserve generation and prompt-claim revalidation and lock release. Do not
ignore errors after entering `connection.Write`, parse its error text to infer
no effect, detach mutation contexts, retry an RPC, or change the submission
ledger/UUID/options/unknown-outcome contract. Cancellation during an actual
write remains potentially transport-fatal; this bounded guard does not promise
to eliminate that separate case.

Before accepting that correction, a deterministic disposable quick regression
must hold A's `writeMu`, register an RPC waiting behind it, cancel that caller,
then release the lock while an independently live sibling RPC is outstanding.
Assert zero native receipt of the canceled RPC, the existing cancellation error,
unchanged connection/generation and successful sibling completion without a
reconnect. Cover an already-canceled write as well; retain stale-generation,
changed-prompt-claim and genuine transport-failure invalidation checks. Use
barriers/current pending registration, not timing sleeps or native/model work.
The quick selector covers those named tests only; no unchanged native campaign
is implied. Demonstrate the canceled-before-write boundary explicitly rather
than relying on probabilistic browser scheduling.

B owner1 retains the browser package and sole B Git ownership. After lead
release and a tested/published A successor, consolidate its ordinary module/
flake pin using the existing pin workflow; no product route/admission/queue/UI
change is presently justified. If precise browser attribution remains needed,
the bounded test-only extension is request-object sequence IDs with start/end
and navigation generation, plus forwarding-only typed observation-error
diagnostics in the fixture. It must preserve every real call/result and avoid
new production logging APIs. Do not suppress queue refresh, wait away ordinary
navigation races, or add POST404 to expected failures. An unresolved or different
failure returns to diagnosis; do not broaden this proposed fix automatically.
Committed quick checks and affected final review precede any separately
authorized browser rerun. Acceptance remains all 32 cases, all four final
manifests, zero unexpected POST/HTTP/page/native failures, zero skips, and exact
final source/input proof. Existing `settingsWrites` diagnostic precision stands.
Architect performed source/artifact inspection and this design update only;
no implementation or rerun is authorized by the finding itself.

**Attempt 9 forwarding diagnostics package (before the next browser run).**
The lead reports A `11ec57d2` published with seven normal and seven race tests
passing; owner1's B pin package continues independently. That evidence proves
the corrected cancellation boundary, not attempt 9's unrecorded inner queue
cause. Add only fixture diagnostics to the two existing files
`portal/internal/web/retry_backend_browser_test.go` and `.cjs`, owned by owner1
after its pin quick checks/commit. No production file, shared fixture, exported
A hook, pin or asset change belongs to this diagnostic package. The source
baseline for its behavior is Be22/A5743, consumed through the new accepted A
pin when incorporated. Lead release and normal committed quick/review gates
remain required; the broad long gate is held.

Use the following small, forwarding-only contract:

- In CJS, assign each Playwright Request object a sequence ID in a WeakMap,
  with a stable watched-page ID, document-navigation ordinal, monotonic start
  time and phase-at-start. Increment the document ordinal on the main-frame
  document navigation request; hash changes are not new documents. Record
  response and requestfinished/requestfailed events by that same object,
  including end phase/time and status or the existing browser failure kind.
  Keep queue/reconcile and thread/page request lifetimes, including canceled
  ones that existing failure policy excludes, in a separate diagnostic array.
  Preserve existing `failures` phase semantics, filters, assertions and timing.
  Never pair identical URLs by arrival order; two reloads may overlap. Add no
  request headers, fetch wrappers, browser interception or network waits.
- For those same exact root/member conversation paths on the retry fixture
  host, allocate a server-local request sequence. Set one test-only response
  header, `X-Retry-Fixture-Request`, and attach its record through a private
  context key before forwarding to the unchanged Handler. CJS records this
  header against the corresponding Response.request object; server origin plus
  server sequence is the join key. A request with no delivered response/header
  remains explicitly unjoined, never matched by guess. Use the original
  ResponseWriter: no buffering/status-recorder wrapper, Flush/Hijack changes,
  response-body inspection or changed bytes/status. The extra diagnostic header
  is never used by the product or as admission authority.
- Wrap the fixture's existing ResolverFunc to call `s.resolveConversation`
  exactly once, and add forwarding overrides on `retryBackendBrowserDisplay`
  only for `ObserveThreadIdentity` and `VerifyThread`. Delegate directly to
  its embedded `planDeliveryClient`, returning the exact result/error and
  preserving Release/capabilities/locks. `teamService` takes this same adapter
  from `s.config.Codex`, so the observation override sees the typed error before
  `requireOrdinaryRetainedMutation` replaces it with its generic refusal. Use
  the request context record, not a global current-request variable; a single
  observation may cover root and member. Do not call observation again.
- Record stage entry/exit, synthetic subject label, parent/request context
  state and the actual stage context state (`live`, `canceled`, `deadline`).
  Record error identity using `errors.Is` for cancellation/deadline,
  `errors.As` for TransportError and the existing ObservationError.Code,
  otherwise a fixed `other` category. Record codes, not `err.Error()`, native
  payloads, bodies, prompts, options, configuration or credential values.
  Capture context states at the stage return before recording/formatting work.
  A live request with `transport_unavailable` differs from an already-canceled
  request; simultaneous cancellation/transport remains explicitly ambiguous.
- In the already-private retry native wire, record only accepted/closed socket
  connection ordinals and monotonic event times, with fixed read/write/normal
  termination categories. Do not change RPC replies or add RPC calls. These
  are native peer-connection observations, not A's internal generation number
  and not a mapping of every RPC to an HTTP request. A's generation is private;
  do not export it, inspect it through reflection, or claim the socket ordinal
  proves which caller caused a disconnect. No changes to the shared manual
  wire are needed for this retry-host failure.

Keep one bounded in-memory diagnostic sink per fixture, with short append-only
locking never held across a delegated call. A bound of 4096 small events is
adequate for this fixed run; overflow sets a diagnostic-incomplete marker and
fails the test gate after execution, never refuses an actual request or silently
truncates proof. Preserve an active-at-snapshot flag for unfinished requests.
The Go test writes a sibling `server-diagnostics.json` for each variant after
the child command returns and before any `t.Fatal`, on success or failure;
the CJS success/failure artifact retains its request diagnostic array. This
needs no diagnostic HTTP fetch, new route, timer, retry, drain wait or additional
browser action. Connection events and request stages share the Go sink clock;
the response header supplies exact browser/server correlation rather than
assuming browser and server clocks match.

**Quick acceptance and limits.** Keep focused Go checks in the same owned test
file, under `TestRetryBackendBrowserDiagnostics`: real root/member queue POSTs
through the existing fixture Handler still return their ordinary 200/body and
one correlated header; forwarding executes once and returns the original
result/error; overlapping distinct request contexts cannot exchange records;
controlled forwarding checks distinguish own cancellation/deadline, live-context
typed transport failure, semantic observation error and success; bounded sink
overflow is visible and never changes the delegate. Use barriers for overlap.
These tests may exercise the diagnostic wrapper with controlled delegates;
the browser fixture must always delegate to its real existing implementation.
Retain zero synthetic starts and unchanged retry ledger/policy for the empty
queue calls. Node syntax, gofmt/diff, compile-only and the exact new quick Go
selector are sufficient before affected review; no browser/native campaign is
part of these quick checks. The next separately authorized browser execution
must retain the exact failed request's browser/server join, local context state
and typed stage category if it fails, plus native connection intervals when
present. Missing/ambiguous evidence stays missing/ambiguous and blocks causal
claims. No POST404 expectation, queue suppression, extra settling delay,
altered 32-case assertion or error-policy exemption is permitted. This package
is proportionate and feasible without a production API; it diagnoses the next
failure and cannot reconstruct the missing attribution in attempt 9.

**Execution environment and quick/review gate.** In B's exact final Nix shell,
use the full declared tool PATH (Go, C compiler for cgo, Ruby, Node, Git and
helpers), preserving owner0's corrected environment receipt. Do not construct
a Go-only PATH or disable cgo to conceal missing gcc. The previous browser
environment is `NODE_PATH=/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules`
and `PLAYWRIGHT_BROWSERS_PATH=/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers`;
verify those immutable paths/versions before reuse. No npm download/floating
browser or substitution of a different browser without a recorded comparison.

New package quick checks: gofmt/diff, Node syntax, and compile-only
`nix develop --no-update-lock-file --command go -C portal test -mod=readonly ./internal/web -run '^$'`.
Compilation is not browser proof. Owner1 commits the complete test-only package;
retained final review covers the new fixture/path fidelity before its long
execution. Then a fresh utility runs, from B, with the browser variables above:

```sh
nix develop --no-update-lock-file --command env PORTAL_BROWSER_TEST=1 \
  go -C portal test -mod=readonly ./internal/web \
  -run '^TestRetryBackendBrowser$' -count=1 -json -timeout=360s
```

Target browser runtime is 1–3 minutes, bounded by 360 seconds; this is an estimate,
not measured evidence. Require top-level plus all four subtest PASS events,
all 32 manifest cases, zero selected skip/fail/missing, exit 0, complete JSON/
stderr and exact pre/post source identity. Missing browser dependencies fail the
selected run rather than silently skipping. No repeated whole question/gallery
suite unless changes or failures justify it. A final test-only successor gets a
new frozen head; retain 45e evidence with exact unchanged consumer-source proof,
and build the actual final source rather than relabeling 45e as that successor.

**Packaged and native gates.** Existing focused normal/race policy/controller/
HTTP/helper and I-B1 receipts retain their exact scope. The package check runs
all portal Go tests plus Node and protocol/pin checks and requires the Ruby
aggregate. It does not enable opt-in Playwright or tagged native cases, and
does not replace A's own Go/Node suite. From final B select:

```sh
nix build --no-link --no-write-lock-file --print-build-logs --json \
  .#checks.x86_64-linux.ruby-verification
nix build --no-link --no-write-lock-file --print-build-logs --json \
  .#checks.x86_64-linux.package .#checks.x86_64-linux.codex-package \
  .#checks.x86_64-linux.ruby-source-filter .#checks.x86_64-linux.host-module \
  .#checks.x86_64-linux.host-auth-benchmark .#checks.x86_64-linux.host-package-contract \
  .#checks.x86_64-linux.extension-catalog .#checks.x86_64-linux.agent-team-catalog \
  .#checks.x86_64-linux.user-namespace .#checks.x86_64-linux.generic-source
```

The first aggregate covers all 13 exported Ruby shards once; the second reuses
that derivation. `ruby-workspace_host-0` is directly affected by the guard;
`runtime-contract.json`, libexec and test support are in the shared Ruby source
filter, so never infer the other shards are unchanged from their test names.
All shard manifests must show complete unique coverage. The packaged real-tmux
opt-out is established fixture policy, not permission to skip selected new
tests. Package/default/host/portal aliases are the same B derivation, not extra
checks. A5743 `checks.x86_64-linux.default` and `generic-source` must have exact
successful receipts or be built once; no automatic repeat of unchanged A's
six-case native campaign.

Run the affected existing B native/controller/recovery selectors on pinned
0.163.0 after final source review; preserve `native-verification.md` isolation,
synthetic provider and exact receipt barriers. From B with `LIVE_SWITCH_CODEX`
set to the recorded exact binary (rehash/version at execution):

```sh
nix develop --no-update-lock-file --command env LIVE_SWITCH_CODEX="$LIVE_SWITCH_CODEX" \
  go -C portal test -mod=readonly -tags=live_switch_integration \
  ./cmd/workspace-portal -run '^TestNative(LiveSwitchReconnect|TurnRetryController)$' \
  -count=1 -json -timeout=5m
```

Require both top-level PASS/zero skips/missing/fail and actual native identity;
each existing fixture has a 90-second internal budget. The controller fixture
uses an explicit fixed Decision and tests real native admission/recovery; it is
not proof of browser/session-sidecar integration, which the new package covers.
No new native fixture or protocol expansion is necessary for that distinction.

**Composition, reuse and deferred operations.** Final W/C successor pins are
still placeholders until the owners report exact revisions. Current inspected
worktrees W3d613a16/Cb3498aed still select the deployed lineage, not final B45e;
the old identity table in `verification-build-brief.md` is historical for this
milestone. Preserve A5743, native0.163, extension767dfd58 and unrelated inputs.
After final B publication/review, lead assigns mechanical W/C selection and
checks full nested `vpsfree-dev-workspace/dev-workspace` and configuration
channel `devWorkspace` graphs. The existing build brief's exact selectors remain:
W `deployment-contract`, `agent-instructions`, `agent-team-policy`,
`cluster-provider-composition`; C `nix-store-cleanup`, `alert-recipients`,
`infra-monitoring-rules`, `infra-monitoring-config`, `vpsf-status-prometheus-rules`,
`vps-autostart-prometheus-rules`, `process-count-prometheus-rules`,
`newadmin-prometheus-rules` under `checks.x86_64-linux`.

Lead's later utility validates final flake outputs and captures selector ->
drvPath -> output, recursive derivation/input graph, source/NAR/head/tree,
toolchain/system/environment and completed success receipt before reuse.
Equal source files or a prior green CI label alone are insufficient. Ruby's
filter may allow exact reuse after a portal-only test addition; prove the
derivation identity. Retain/GC-root completed package/build outputs immediately.
No global quiet-build timeout: use fresh interruptible monitoring, report an
unexpected local kernel build and stop that owned build under the existing
escalation procedure. Packaged suite budget is workload-based (CI targets under
20 minutes warm); it is not permission for automatic retries or longer tests.

The eventual profile artifact is W's `packages.x86_64-linux.default`; verify
`bin/check-dev-workspace-deployment --workspace-root "$W" --configuration-root "$C"`
before its scoped build. CWD C selects `nix develop --command confctl build
cz.vpsfree/machines/aitherdev` for the scoped system artifact. Preserve exact
generation name/metadata/inputsInfo/config commit/system toplevel and the
profile store path under the existing build/generation receipts; no copy,
activation or moving/latest-generation command is authorized here.

Host idempotency/boot/archive VM selectors remain inventoried in the original
build brief, not an automatic campaign for this change. Lead must explicitly
disposition affected or failed gates; successful unchanged checks require exact
input/derivation receipts for reuse. In particular creation 9f, 207 and e7 stay
distinct and unresolved. Controlled accepted-fork evidence, when complete, can
support a separate decision but neither identifies historical holders nor
waives those failures. No source-wait fix, generic retry, sleep or full VM rerun
is released by this planning subsection. Deployment/use acceptance still follows
guard-before-sidecar ordering, preserved manual/recovery contracts and the held
machine's existing release conditions.

## Ordinary Send composer latency and question keyboard follow-up

User reports ordinary Send remains **Sending…** for up to five seconds with
the submitted text still in the textarea, making successive messages awkward.
This is independent of retry notice design and must remain prioritized alongside
its visual milestone. Deployed baseline is A `ac62eeeb9d8b1fa7b8ed8fb95ba8160acb7efa1c`
/ B `7b8c646974df72e0df3e576d10f09d79823ae004`; inspected undeployed UI sources
are A `f86290673d752c77b56c70228c3d26aced75e177` / B
`5e342788c7178ac1cb93c25591bdc42a83386c6b`. The lead accepted the bounded
composer correction and assigned the separate small question-keyboard package.
Architect changes only this design; no live Send, resend, native history or
prompt inspection was used for diagnosis.

### Evidence and scope

B `static/app.js:5490–5570` saves the browser UUID/text/attachments, disables
every form control including the textarea, awaits `client.message`, then clears
the matching draft. Thus HTTP latency directly prevents typing the next draft.
Its existing prefix store already retains multiple attempts. B clears on the
HTTP receipt, not on transcript acknowledgment. A's separate standalone
`createDurableSender` at `conversation.js:813` retains a singleton pending
attempt and `mountConversation:1567` additionally awaits refresh; transcript
acknowledgment at `:1328` can clear its draft. That standalone flow is not B's
ordinary submission path and must not be broadly redesigned in this package.

The five-second duration is a user observation, not a measured server-stage
attribution. Before a message HTTP receipt, source shows runtime/roster/
conversation admission, retained root/team observation, VerifyThread, attachment
preparation, retry provenance and generic receipt/history reconciliation, and
native start/steer/acceptance persistence. Any can contribute; repeated native
reads are not proof that one is the bottleneck. B `read_diagnostics.go` explicitly
excludes POSTs, so its GET Server-Timing cannot measure this send. Transcript
refresh and browser acknowledgment are subsequent work in B, not prerequisites
for its original HTTP receipt. No evidence justifies removing/caching a safety
check or attributing this report to the previous exclusive-lock incident.

This correction decouples editing from delivery acknowledgment. It does not
promise a faster native acceptance, weaken authority checks, add a background
outbox or dispatch multiple native mutations concurrently. Server optimization
requires a separate measured finding. A later targeted timing improvement, if
needed, should use fixed safe stage labels/durations without bodies, prompts,
paths, credentials or raw errors; it is not required for this composer fix.

### Remaining receipt latency: measurement boundary

The reported approximately five seconds remains unmeasured by server stage.
The composer package frees typing; it does not shorten HTTP receipt latency or
the interval before the next explicit Send can dispatch. This follow-up checked
the deployed A `ac62eeeb` / B `7b8c6469` sources, without reading live message
contents, generating a send, or changing services. No latency cause or speedup
has been established.

B's deployed `portal/internal/web/read_diagnostics.go:76–78` excludes every
non-GET request. Its `Server-Timing` and sampled `portal_read` records therefore
cannot attribute a message POST, and the log explicitly leaves admission and
native wait unmeasured. The relevant deployed portal/client sources contain no
per-stage send timing. An existing own-session message request retained in the
browser Network panel can supply its Timing tab's queue/connect/request/wait/
download durations without replaying it; retain only method, own session and
numeric timings. Do not export a HAR, request/response bodies, headers or attempt
identities. If the browser no longer retains the request, there is no recovered
measurement. Proxy timing, if already available to the operations owner, would
bound the HTTP request rather than identify its internal stages. No proxy log
format or retrospective duration was verified in this investigation.

The smallest proposed source follow-up is a fixed, bounded in-memory timing
trace for ordinary `POST message`, following the existing safe diagnostic
pattern. It is a separate owner-assigned change, not a dependency of the current
frontend package. B should first measure `total`, `resolve`,
`transition_wait`, `runtime_wait`, `retained_observe`, `roster_wait`, and
`managed_send` around their existing calls. `resolve` contains its admission
stages; `managed_send` includes its internal provenance/recovery/native work.
Report these as inclusive intervals, not an additive breakdown. A later narrow
A-owned hook is needed to distinguish the remaining `verify_thread`,
`conversation_wait`, `attachments`, `native_submit`, and `receipt_save`
intervals; do not label the whole managed Send duration as native execution.
In particular, `native_submit` ends at the RPC reply and does not measure model
turn completion or prove acceptance when the reply is lost. A response header
measures through response creation; browser timing measures through delivery.

Keep the vocabulary fixed, durations monotonic, and request memory/log sampling
bounded. No body, prompt, history, thread/attempt ID, attachment name, raw error,
arbitrary URL or query becomes a label. A server-generated diagnostic correlation
may link timings without reusing a submission UUID. Instrumentation must not add
native requests, persistent metrics, locks, admission failures or response
dependency on diagnostic persistence. Later focused tests would prove label
redaction/bounds, timeout/error coverage, unchanged request/receipt ordering and
zero extra native calls; no test or instrument was launched for this note.

Source-confirmed serial work includes root/member retained observations and,
within each observation, metadata/latest-turn reads before and after prompts,
queue and unresolved-submission checks (`workspacecodex/observation.go:180–292`,
`teamruntime/observation.go:143–196`). The paired reads establish unchanged
identity/activity; they are not removable duplicates. Prompt and queue reads
have independent inputs within that bracket, but `PromptsWithItems` returns
locally when no item-backed prompt exists (A `codex/client.go:1877–1888`), so
parallelizing them has no demonstrated benefit for ordinary sending. Do not
parallelize ledger/reconciliation, native mutations, proof brackets or roster
work on this evidence. Measure first; preserve Incident 2's bounded shared-lock
wait and post-acquisition authority checks, exact prepared-plan recovery, ed2
retention, existing lock order and the managed-only/no-CAS boundary. There is
currently no source-proven dispensable check or approved server optimization.

### B composer handoff contract

Implementer1 owns the B changes after its current screenshot capture source
freeze ends; coordinate sequencing through the lead. Primary files are
`portal/internal/web/static/app.js` and focused actual-template browser fixtures.
Reuse existing A durable-attempt store and upload-selection APIs. No A sender,
native, HTTP schema, retry policy sidecar or server admission changes are needed.

1. On explicit ordinary Send, snapshot the exact target/conversation/thread,
   current draft generation, text, attachment IDs and existing-or-new immutable
   attempt UUID. Validate and durably store/read back the attempt before
   clearing anything or starting HTTP. Storage/validation failure preserves
   the complete composer and performs zero message requests.
2. Once durable intent is retained, transfer it to the existing pending-message
   row with **Sending…**, then clear only that captured composer draft and
   detach its attachment selection. This state means local intent/in-flight
   delivery, never native acceptance. `mountUploads.clear()` saves empty draft
   selection without deleting server files. Perform its potentially failing
   persistence before clearing text; on detach failure retain recoverable
   original draft/attempt and do not dispatch a new request. Pending identity
   retains every original attachment ID even after selection is cleared.
3. Release text entry and next-draft upload selection immediately. Keep one
   ordinary submission HTTP request in flight per displayed conversation;
   disable Send/Queue dispatch while that request runs, not the textarea.
   Do not buffer a second click as an automatic later submission. The user can
   type the next message and explicitly send it once the first request settles.
   Existing uncertainty/authority checks decide whether later work is admitted.
   Do not introduce an additional browser capacity gate or automatic retry.
4. Receipt marks only its original pending row accepted. Request failure marks
   only that original row unknown and retains Retry original. Reload preserves
   that exact recovery identity; it must not invent a retry UUID. Do not restore
   old text over a newly typed draft, or clear a later draft whose text happens
   to equal the previous one. Success/failure/finally callbacks use captured
   target and attempt, not mutable current-member client/state.
5. Clear-at-handoff is the sole ownership transfer for that draft. Remove the
   late equality-only textarea clearing for its receipt/retry path; if an
   explicit recovery path owns a restored draft, require its exact draft
   generation as well as target/attempt. A late original receipt or history
   acknowledgment may retire its pending metadata but cannot mutate new text,
   attachments, focus or selection. Member switch/destroy cannot route the
   old request or response to another conversation.
6. Release ordinary dispatch on HTTP settlement, without waiting for transcript
   refresh/history acknowledgment. Preserve accepted receipts until their
   existing exact acknowledgment cleanup. A freshly composed explicit Send
   after known acceptance is new user intent, even with identical text; do not
   reuse an accepted/observed old ID merely by content. Existing unknown exact
   text/attachment replay keeps the old UUID, and the dedicated Retry original
   action always uses its stored tuple. Do not change plan action matching or
   queue identity semantics incidentally.
7. Leave Queue next's native semantics unchanged. Share appropriate button
   admission state so it cannot race the same in-flight ordinary Send; keep
   exact queue recovery, attachment protection and original action identities.
   Do not disable Interrupt or unrelated navigation solely because the old
   implementation disabled every control. Preserve independent settings/
   execution-hold/upload constraints when recomputing enabled controls.

The pending row remains the recoverable original message while a separate
editable draft exists. A local request error is not proof of non-delivery;
observed/accepted evidence wins over a late rejection. No early **Sent to Codex**
label, native receipt fabrication, blanket pending clear or silent text loss.
The normal draft retains its existing persistence behavior; this task does not
introduce a second text-draft journal or replace the durable attempt store.

### Separate A question keyboard package

User explicitly requires Enter to submit question answers and Shift+Enter to
insert a newline. Implementer0 owns the lead-authorized small A keyboard change
in `conversation/assets/questions.js`, the generic required-answer binding in
`conversation.js`, focused tests and one factual reference-doc sentence. Do not
mix a durable sender redesign into that commit or overlap B's frozen capture
files. B optional inline/pinned questions consume A's shared `createAsyncQuestions`
view and gain this behavior with the dependency update.

Use the shared textarea keyboard binding exported through `conversation.js` as
`bindQuestionAnswerKeyboard(input, submit)`, where `input` is the question
textarea and `submit` is its existing owning submit button, not a new RPC
callback. Implementer0 published this exact API in A
`55e0300b27b6927b1693b3792042762f31a385cc` (`questions.js?v=4`); its report and
package identities are retained in `question-keyboard-a/final.json`. B should
adopt the final A pin once, after its capture source freeze, rather than pinning
an intermediate keyboard revision. Plain Enter
prevents the textarea newline and activates that owning path once. Shift/Alt/
Ctrl/Meta Enter retain their current browser behavior. IME composition
(compositionstart/end, isComposing and legacy 229) never submits. Repeated plain
Enter prevents repeated newline/submission without activating the action.
Disabled, readOnly, hidden controls or disabled owning submit cannot activate.
Do not bind option/radio/button key events or change native form semantics.
Return an event-listener disposer for view destruction when required.

B's required multi-question wizard is separate (`app.js:5005/5138`): implementer1
adopts the helper only after its source freeze, routing to its existing
`form.requestSubmit`/Next/Submit path. Preserve saveDraft, required-other checks,
unanswered confirmation, question progression and existing accessible controls.
Enter on a question's text answer follows the same action its owning button
would perform; it must not prematurely send a partially completed multi-question
response. A's generic Answers-as-JSON textarea uses its existing Submit answers
validation. The main message composer shortcut is not redesigned in this work.

### Required quick and browser regressions

- Gate an actual ordinary message HTTP response in the real-template fixture:
  immediately after verified local persistence the pending row says Sending,
  text is empty/editable, original attachments remain in the immutable attempt,
  and a new draft can be typed. Assert zero accepted presentation before receipt.
- While HTTP is held, repeated Enter/click creates exactly one request/UUID;
  no second background send occurs. After accepted receipt, a second explicit
  message is sendable without transcript refresh/ack; its request uses a new
  UUID, including an intentionally identical new message after acceptance.
- Delayed receipt, lost reply, observed-before-reply, ack failure, page reload,
  member switch and changed next-draft selection never clear/replace the next
  draft. Retry original uses exact old ID/text/attachments. A definitely failed
  local persistence/detach step makes zero HTTP requests and preserves recovery.
- Exercise text-only, attachment-only and text+attachments; storage-write and
  readback failure; upload/draft detach failure; second-draft uploads while first
  request is pending; existing Queue next, plan, settings and Interrupt controls.
  Keep actual HTTP Incident 2 prepared-plan/runtime-wait tests and ed2 pressure/
  replay evidence; this UI change cannot replace or relax those backend tests.
- A keyboard tests cover inline and pinned optional questions plus generic
  required answers: Enter once, Shift newline, modified keys, repeat, IME/229,
  invalid/empty/disabled/readOnly/hidden state, radios and existing button click.
  B required wizard real-template tests cover Next progression, required-other,
  unanswered confirmation and final submit through the existing validation.

Use deterministic promise/barrier tests, not an arbitrary five-second sleep.
Owners run focused Node/Go quick checks and affected browser tests under the
repository Nix environment. Update the actual-template screenshot milestone to
show an editable next draft while an original row is Sending; no live synthetic
message is authorized for acceptance. Keep source changes serialized with the
retry visual capture work. Committed final changes require the normal affected
independent review before long verification and any deployment; this planning
supplement itself does not trigger review. No server/native/state migration is
expected; existing browser attempt format and recovery remain readable.

### Capture attempt 3: required-question fixture selector

Bounded source diagnosis at B `9f033875` / A `55e0300b`: the required-question
browser fixture times out at line 85 on exact radio accessible name `First`.
The original watcher event (`ui-successor/watcher-capture-3-corrected/stdout.jsonl`,
line 22) agrees with `ui-successor/capture-attempt-3/execution-record.log:95–102`.
The preceding awaited assertions completed: Enter progression, modifier/IME
guards, missing Other text validation, reload at page two, unanswered-question
confirmation, exact first response, and the new mouse-case first question.
This failure does not establish a keyboard-helper or wizard-progression defect.

B `static/app.js:5069–5086` wraps the radio in a label containing both the
option heading `First` and description `First approach`. Both contribute to its
accessible name; `style.css:375` displays the description as a block. Therefore
the fixture's exact heading-only role name cannot identify that control. The
earlier `None of the above` control has no description and is not equivalent.

Smallest correction, owned by implementer1: replace only that lookup with
`wizard.locator('input[type="radio"][name="answer-choice"][value="First"]').check()`.
Assert that exact option is checked. Keep the actual click, Next/Submit
progression, request-count and validation assertions. No forced click, timeout
increase, product label/ARIA change, helper
change or validation bypass is warranted. An accessible-name assertion may
separately check that both heading and description remain exposed. This is a
source-backed fixture correction, not a claimed rerun pass; the design lane ran
no browser, test, native request or live operation. Existing screenshot/capture
verification remains with the lead and source owner.

## CI 9f creation: source runtime contention diagnosis

Read-only finding for run `40020133863`, exact B
`9f03387583185d213c14ca09af190bcc27a7f309`. Saved metadata reports creation
failed, fast/archive passed, host skipped. At
`ui-successor/ci-9f-failure.log:4188–4192`, the accepted explicit-fork receipt
changes from running at `20:45:12.504` to failed at `20:45:16.346` with
`initialize session: error: another dev-session command is changing
2026-10-23-explicit`. The empty page-error list and `terminal()` assertion at
`creation_acceptance_browser.cjs:49`, reached through `usable():90` and fork
`:242`, establish a real failed creation receipt, not a selector timeout. This
does not waive the creation gate. Model-catalog warnings, SIGTERM and the prior
different hidden-plan failure do not establish its cause.

The failing source path is bounded: `creation.go:1064–1069` runs the recorded
`dev-session fork` command and wraps its failure; `libexec/dev-session:1493`
acquires the source's exclusive slug lock before source proof and native fork.
The ready source gets fail-fast behavior (`:7953–7960`); `with_host_lock:7796`
tries `LOCK_EX | LOCK_NB` and raises `SessionBusyError` on contention. This is
the same authority-directory `<slug>.lock` used by portal mutation SH admission
(`session/authority.go:46–53`, Ruby `:7822–7835`). Destination preparation can
already exist, so recovery must retain its exact accepted receipt and journal.
Do not treat this as permission to submit a new fork or erase partial state.

The fixture opens the ordinary source page and waits for transcript hydration,
then uses the real fork dialog (`creation_acceptance_browser.cjs:32–40,219–242`).
It does not explicitly acquire a competing test lock. Normal `refreshQueue`
issues POST reconciliation (`static/app.js:5339`), whose resolver holds runtime
SH. The response log includes two such source POSTs, but records neither their
lock intervals nor lock owners; it cannot identify the holder at the failed EX
acquisition. The tracking-sync job logged completion before fork acceptance;
that nearby log is not holder proof either. Normal portal/CLI contention is a
source-supported possible overlap, not a proven fixture-only cause.

Compared with the reported green `07e75335`, `libexec/dev-session`, creation
handler, resolver, runtime-lock code, creation browser fixture and VM driver are
unchanged. The sole `app.js` difference is the conversation asset import version
23 to 24. This establishes no new fork/locking implementation regression from
the current keyboard/composer patch; it also does not prove a harmless flake.
Keep the failed gate unresolved and let the independent screenshot work proceed.

Smallest next evidence package for B's sole source owner, subject to lead release:
add a deterministic disposable source-SH barrier around accepted fork execution,
using the real Ruby source-acquisition path rather than the fake initializer in
Go creation tests. Confirm zero native fork while held, exact refusal/recovery
on the present code, and one destination after the original receipt is resumed.
This requires no full VM campaign to establish the locking behavior. Capture
only lock mode, acquisition/release stage and timing in that fixture. Preserve
`TestCreationFastSourceLockDoesNotWaitForLifecycleMutation`: before acceptance,
an already EX-locked source must still fail promptly with conflict.

If the controlled overlap confirms the missing transient-wait behavior, the
narrow product candidate is waiting only for source EX acquisition of an already
accepted portal fork, within the existing cancellable creation-command budget,
followed by all current exact-source/lifecycle/provider/provenance checks. Reuse
the existing lock helper rather than retrying the whole command or changing SH/EX
modes; do not enable unbounded waiting for ordinary CLI/background writers or
hold destination/message locks while waiting. A change needs same-receipt retry,
timeout/cancellation, changed source/lifecycle and no-duplicate-fork regressions
before affected review and the separately authorized creation check. Existing
logs do not justify a sleep, hidden retry or suppressed assertion in the browser
fixture. No implementation, test, VM/native run or live operation was performed
for this diagnosis, and this candidate is not an implementation release.

### Disposable accepted-fork contention evidence package (2026-10-24)

This is a test-only release brief for implementer0, independent of implementer1's
Go retry-policy package. No product lock change, native/VM run or CI waiver is
authorized. Preserve the failed creation gate until its required disposition
and verification are complete.

The retained logs distinguish three observations. Run 9f failed explicit fork
as recorded above. `ui-successor/ci-207-failure.log:4790–4814` shows explicit
fork **ready**, followed by a plan-derived destination accepted at
`21:38:21.613847385Z` and failed at `21:38:23.481858543Z` with the Ruby source
slug busy error. `ci-e7-failure.log:4644–4659` instead shows a new-session naming
collision preparation receipt failed with the Go `session is changing` error
at `21:21:36.344700872Z`; it is not an accepted fork failure. Neither log records
the competing holder/lock interval. Preserve the corresponding diagnosis JSON
files and do not infer a shared holder, harmless scheduling, model-error cause
or a retry-feature regression from similar error wording.

Current source sharpens the earlier fork finding: `Runner#fork` calls
`verify_creation_source!` at `libexec/dev-session:1446`, which acquires source
EX at `:3987`, **before** destination request binding. It later reacquires
source EX at `:1493`, after the initial destination locks have been released.
The first check also occurs for plan-derived `Runner#start` at `:973`.
Thus the busy message alone does not identify which source acquisition failed.
Both use real `with_slug_lock`/`with_host_lock` and `LOCK_EX|LOCK_NB` on the
same authority-directory file as portal SH. The fixture must label the exact
acquisition it exercises. Separately, preparation's
`reservePreparationLocked` (`preparation.go:604–608`) has fail-fast creation
and destination runtime acquisitions; that is a relevant e7 investigation
entry point, not proof of its particular holder or failing lock.

**Independent file boundary.** Add
`portal/internal/web/creation_source_lock_test.go` and, if useful, a dedicated
`test/support/accepted_fork_runner.rb` test subprocess adapter. Keep helper
code local to these files; reuse existing fixtures by calling them, not editing
their owners. No changes to `authority.go`, `server.go`, `creation.go`,
`preparation.go`, `turnretry/`, `workspacecodex/`, the browser acceptance script
or `libexec/dev-session` in this evidence package. Existing
`creation_ruby_contract_test.go` and Ruby `fork_receipts_test.rb` provide patterns;
their receipt reader and external-effect adapters are useful, but a test that
calls only `prepare_portal_creation_receipt!` is insufficient. Owner1 retains
all B Git operations; owner0 supplies scoped uncommitted edits/patch and results.

**Real path and deterministic barrier.** Exercise actual `Server.Handler` fork
acceptance, `runCreation`/`initializeCreation`/`runCreationCommand`, and the
actual Ruby CLI/`Runner#fork` receipt/source/acquisition/journal/completion path.
The test executable loads the repository Ruby implementation and invokes its
ordinary CLI with the Go-produced arguments. A test-only Runner adapter may
replace native/provider/tmux effects with deterministic counted responses,
following existing fork receipt fixtures. It must not replace the initializer,
lock helper, source identity/lifecycle validation, receipt validation,
journal/completion writers or recovery logic, and must not synthesize a Go
success receipt. No real model, daemon, systemd or registered workspace is used.

Use separate real file descriptions/processes for holder and initializer. The
holder opens the fixture's exact private `<authority>/<source>.lock`, verifies
the same device/inode, acquires SH, and signals readiness through a pipe/socket.
A test-only stage observer may signal/wait immediately before calling `super`
on the selected source acquisition; it cannot replace flock or return a mocked
busy result. Release with an explicit handshake, not a timing sleep. Guard
every rendezvous with a short timeout and always drain owned subprocesses.

Required subcases and assertions:

- With SH already held, real preacceptance source SH can succeed and the fork
  receives HTTP 202. The first Ruby source EX refuses on current code, with
  zero native fork/start/settings/send calls and an exact failed creation
  receipt. Record that refusal; do not write a test that expects a wait which
  the product does not yet implement.
- Let the first source verification complete. At the second source acquisition,
  acquire the real SH barrier before allowing EX to run. Confirm destination
  request binding already exists, no destination lock is held across this
  source acquisition, zero native calls, and preservation of accepted receipt
  and binding after refusal. Do not fabricate a fork journal at this stage;
  retain one only if the actual path created it.
- Release SH and retry through the existing HTTP `creation/retry` route with
  the original receipt ID and current attempt. Require one synthetic native
  fork, one destination, matching source/thread/settings/provider, real Ruby
  completion evidence and ready status. Original receipt/request identity stays
  fixed; only the ordinary creation attempt counter advances. Duplicate retry
  at the current attempt is a no-op; a stale attempt/wrong receipt conflicts.
  Restart/readback uses existing completion proof without another native fork.
- In a fresh held/refused fixture, replace the disposable source identity before
  retry. Require refusal and zero native calls; original destination/request
  cannot adopt the replacement. Preserve the existing journal-bound recovery
  contract after a genuinely created fork rather than generalizing this check.
- Run unchanged `TestCreationFastSourceLockDoesNotWaitForLifecycleMutation`:
  source EX before acceptance still returns 409 within its existing 200-ms
  assertion. Do not weaken or remove that expectation.

Diagnostics are fixture-only: holder PID, lock mode/device/inode, stage,
monotonic attempt/acquire/refuse/release times, receipt attempt/state and native
effect counts. Include them in timeout/failure output. Exclude prompt/plan text,
credentials and live identities. These prove the controlled holder and interval;
they do not retroactively identify the CI holder. A lost-reply/restart case must
read the exact existing receipt and completion evidence, never create a second
destination or mutate ledger state to manufacture success.

Proposed exact Go selector from B's Nix environment, run from `portal/`:
`go test -mod=readonly ./internal/web -run '^(TestAcceptedForkSourceSharedLockRefusalAndReceiptRecovery|TestCreationFastSourceLockDoesNotWaitForLifecycleMutation|TestCreationReceiptRubyInitializerContract)$' -count=1 -timeout=45s`.
Use the first test name for the new grouped subcases. Target fixture runtime is
under 10 seconds excluding compilation, with at most 5 seconds per handshake;
this is an expectation, not a measured result. No native flags, browser launch,
VM or full CI rerun. First unknown-duration execution follows the normal watcher
procedure; lead owns launch selection. If a real initializer path cannot be
retained within these two test files and disposable external adapters, report
the exact missing seam before expanding files or weakening the path.

The owner reports the controlled refusal/recovery evidence and untouched
preacceptance assertion first. Only then may the lead decide whether to release
a separate narrowly scoped, cancellable wait for an already accepted source
acquisition. This package does not enable waiting, general command retries,
new lock modes, fixture sleeps, retries with new receipt IDs or unbounded waits.
Plan-derived and e7 preparation failures remain separately unwaived even if all
fork subcases pass; decide any additional bounded evidence package from its
actual result. No whole-VM campaign is implied.

## Incident 2: prepared plan delivery and transient runtime contention

Lead accepted the two exact A predicates and the B recovery/admission boundary
on 2026-10-23. Implementer0 owns A; implementer1 owns B. This supplement is a
source-backed implementation brief, not evidence of implementation or a live
recovery action. Baselines are A `c1f415ad5602c23e6443cced73cb59267a796f05`
and B `ed2a75b98a75f9b37b7a359e9091a94e9846644e`.

### Cause and supported correction

B `portal/internal/web/server.go:2527` fixes the plan message to
`Implement the plan.` and binds its browser UUID to
`plan:<plan-turn-ID>:<plan-SHA256>`. The handler reserves generic prepared
identity at line 2618, explicitly changes Plan mode to default at 2626, then
calls managed Send at 2652. The settings owner correctly advances the retry
epoch. B `workspacecodex/turn_retry.go:257` nevertheless treats the existing
prepared identity without a retry snapshot as an unproved historical send.
This refuses before native dispatch. Capturing before the settings change
would create the wrong epoch and is not the correction.

A `codex/client.go:2687`, `4977`, `5063` and `5202` establish the distinction:
Prepare persists exact intent without sending; SendAttempted includes prepared;
Reconcile returns false for prepared or absent; Send durably marks submitting
before native start/steer. Thus only a positive exact prepared, nonqueued
record proves that first execution has not begun. Missing history is no proof.
Called queue deletion/retirement paths remove their prepared record together
with the queue marker; native execution/reconciliation retains the queue marker.
Do not infer never-sent from a prepared record that has a queue attempt.

There is a separate HTTP admission problem: `server.go:2030–2062` checks
ordinary retained mutation before entering the plan handler. Its
`requireOrdinaryRetainedMutation` / `teamruntime.ObserveRetained` /
`workspacecodex.ObserveThreadIdentity` chain rejects that same prepared UUID
as unknown. Correcting managed Send alone cannot recover an existing request.

### A library boundary

Add these read-only public methods in `codex/client.go`, with focused tests
and their durable semantics in `docs/reference.md`:

```go
IsPreparedSendWithOptions(threadID, text, clientID, actionContext string,
    options TurnOptions) (bool, error)
RequireSubmissionAttemptsKnownExceptPreparedSend(ctx context.Context,
    threadID, text, clientID, actionContext string, options TurnOptions) error
```

The first returns true only for an existing exact `prepared` send with no queue
attempt. Normalize and validate text/action/options identity under the existing
per-thread queue lock and ledger transaction; changed identity or unreadable
state errors. Absent, submitting, accepted and delegated-queue identities never
produce this grant. Preserve the stored steering flag; do not delete/recreate
the record, mutate options, or change SendAttempted's existing meaning.

The second positively validates that same tuple and uses the existing private
`requireSubmissionAttemptsExcept(..., ownPreparedID)` primitive at A line 3059
to exclude only that exact prepared request from the known-submissions check.
Keep the shared queue lock across validation and proof. Every other send,
queue attempt and queue deletion receives the ordinary checks. A missing or
changed own preparation errors; this method does not authorize dispatch,
resume, settings changes, or an exception on any other thread.

### B operation and proof boundary

Keep exact generic reconciliation first in managed Send, including accepted
history after acknowledgment. When that sequence finds an existing attempt
but no retry snapshot, only the positive A prepared predicate permits first
execution capture. Capture current authorized settings after the explicit plan
mode update, then use the ordinary Send path with the unchanged generic tuple.
Root zero options stay zero in the generic ledger. Member model/effort/context
and authorized policy remain the saved immutable options. Existing old-epoch
snapshots are never rewritten, promoted, or rebound by this exception.

Accepted/submitting or queue-owned identities use their existing exact
reconciliation path; they never acquire current settings because retry evidence
is missing. Preserve original UUID, text, action context and attachment/context
identity across errors, restart and browser replay. Generic Send's final
receipt reconciliation and saved-steering-state check remain mandatory.

For the actual implement-plan HTTP route, validate the bounded request and
trusted root tuple before choosing the request-local observation exception.
Permit exact receipt-only reconciliation before the activity-known gate, after
the existing identity, current-package, runtime and lifecycle fences. That
phase cannot dispatch, resume, change settings or discard unknown work. An
accepted result returns its original receipt; unknown stays unknown. Include
exact accepted-history recovery after acknowledgment before plan freshness
could incorrectly reject the old receipt.

Fresh execution still passes the complete retained proof. Its root observation
may replace only its submission-known check with the second A method for this
positively prepared UUID; all other root facts and every retained member use
ordinary observation. No global prepared exception, prefix-based permission,
private-ledger parser, string-error inspection, or retry-record bypass. Absent
preparation uses ordinary proof; current plan-turn/digest, idle/mode and
original steering intent remain necessary. The existing obsolete-plan recovery
may retire only its positively unsubmitted exact request under its existing
rules, never a submitting/accepted/queue identity.

Expected B files are `portal/internal/workspacecodex/turn_retry.go`,
`observation.go`, the request-scoped retained observation plumbing in
`teamruntime/observation.go`, `web/server.go`, composed regressions and
`docs/turn-retry-recovery.md`. Keep lock ordering package transition -> runtime
-> roster operation -> conversation -> retry admission -> generic ledger/native
queue. Factor locked observation bodies if needed; never reacquire the same
roster flock while already holding it, or acquire roster under conversation.
Recheck exact prepared and authoritative identity at dispatch admission; an
observation exception is not a cached permission for later work.

### Ordinary HTTP contention correction

Owner0 observed repeated own-session `LockRuntimeShared` EWOULDBLOCK errors;
A's HTTP resolver maps them to `conversation is unavailable` before Send.
Lead subsequently confirmed that legitimate team assign/report operations hold
the session runtime lock exclusively across synchronous native RPCs. Browser
shared acquisition fails immediately during that work. This is distinct from
the prepared-plan ordering bug. B `session/authority.go:45–78` uses an immediate
nonblocking flock. No context-aware runtime equivalent exists; B already has
the bounded polling pattern in `web/server.go:850` for transition locks.

Add `session.LockRuntimeSharedContext(ctx, directory, slug)` using the same
owned lock/directory checks and file descriptor. Poll only EWOULDBLOCK/EAGAIN
with an interruptible short timer until the existing request deadline; return
other errors immediately. Close on cancellation and recheck context after
acquisition. Keep the existing fail-fast shared/exclusive/creation APIs and
their lifecycle callers unchanged.

Use it for conversation HTTP mutation resolution and session HTTP mutation
admission, including implement-plan. The conversation handler already supplies
an operation deadline. Establish the plan handler's existing 20-second deadline
before its outer runtime wait, rather than starting another budget afterward;
bound any other adopted HTTP call by its normal operation budget. Wait only
with the outer transition fence, never a roster/conversation/admission lock.
After acquisition, rerun current package/profile, creation/lifecycle, provider,
retained authority, tracking identity and interactivity checks from fresh state.
Do not downgrade the lock, kill a holder, proceed on timeout, or grant cold
activation. Existing conservative HTTP/error and browser original-ID recovery
semantics remain; no public error-schema or UI redesign is part of this fix.

### Required regressions and acceptance

- A: exact prepared true; absent, submitting, accepted, queue/deletion and changed
  text/action/options negatives; stored steering unchanged; ledger unchanged by
  reads; excluding own prepared still rejects a second unresolved attempt.
- B actual `Server.Handler` with retained runtime authority, real
  `workspacecodex.Client` and synthetic wire: Plan -> prepare -> default -> one
  original-ID native start. Exercise both new actions and deployed prepared
  state after restart, not only direct implementPlan or fake controller calls.
- Crash before/after mode update, before/after admission save, submitting lost
  reply and accepted receipt-save failure; recover same UUID only. Accepted and
  acknowledgment/history replays after newer work perform zero new native sends
  or settings changes. Changed tuple/stale plan rejects; unknown stays held.
- Root/member managed wrapper tests retain immutable options/context/policy and
  old-epoch exclusion. Cold delegated queues and all unknown/protected evidence
  stay protected. Keep the ed2 >64 accepted-steer, retirement/proof-invalidation,
  pressure/replay and all-protected predispatch refusal regressions.
- Actual HTTP exclusive-lock barrier: request waits without native work, then
  release yields exactly one original-ID delivery. Cancellation/deadline yields
  zero native work and retains the browser identity for recovery. Changed
  generation, lifecycle, authority or cold hold while waiting refuses after
  acquisition. Exercise root/member message and queue/reconcile routes plus
  implement-plan; verify no leaked locks or inverted acquisition order.

### Compatibility, verification and rollout

Schema-1 retry records, MaxSnapshots64, schema-3 generic ledgers, native Codex
0.163, HTTP payloads and browser UUIDs remain unchanged. Existing prepared
intents are recovered through normal exact requests; no migration, ledger edit,
reset, fabricated acknowledgment or synthetic live resend is needed. A's API
addition is source-compatible; B must pin that A revision before building.
Old binaries can read the resulting unchanged formats but retain the delivery
bug, so recovery is a reviewed forward package update.

Owners run focused committed Go and race regressions first. The same independent
reviewer checks affected general/architecture/scope/risk lanes before long
verification. Then lead selects exact packaged A/B checks, targeted native
recovery/controller checks and composed W/C checks/builds using retained
derivation/input evidence for unchanged checks. The new runtime-wait behavior
requires targeted package/lifecycle exclusion tests; it does not by itself
justify an unrelated full VM campaign. Lead owns final pins, build/copy,
activation and user acceptance under the held machine claim. Verify portal,
root/team continuity and real original-request recovery without inventing work
or policy errors. No deployment, lifecycle action or machine release is
authorized by this brief.

## Approved emergency hotfix: bounded accepted provenance retirement

Lead accepted this implementation scope on 2026-10-23. Implementer1 owns the
runtime change, production-path regressions and lasting runtime documentation;
architect0 owns this supplement. No codex-web public API, native protocol,
browser behavior or preference change is included. The affected deployed
runtime is B `d819ad044ef7fcc7bb4a111dc7676fe251383249`; A remains
`c1f415ad5602c23e6443cced73cb59267a796f05`.

The incident is a valid schema-1 record containing 64 accepted steering
snapshots for one current turn. `captureRetry` retains all of them and appends
a 65th, so `Save` refuses before the requested message reaches native delivery.
The existing valid record must load and recover through ordinary admission;
there is no manual record repair, reset or migration.

### Retention and delivery contract

- Keep private retry schema 1, `MaxSnapshots=64`, existing snapshot/record byte
  bounds, native submission-ledger schema 3 and package capabilities unchanged.
  Plan bounded candidate state before saving; do not append beyond a bound and
  then catch or ignore the validation failure. Invalid identity, hashes, state
  or persistence errors remain refusals.
- Retire the oldest positively accepted, turn-bound snapshots only, and only
  as needed to fit the candidate count and encoded byte budgets. An exact
  existing receipt/history binding supplies that evidence; age, a missing
  queue entry or a guessed current turn does not. Preserve every unbound or
  unknown admission, `Pending.ID`, `Pending.Snapshot.ID`, the immutable pending
  tuple and all generic native submission/queue records.
- If retirement removes a current turn's contributor, atomically persist
  `Handled=<that exact current turn>` and invalidate **all** cached
  `Proven`/`executed` snapshots for it before a new send. A protected pending
  proof cannot be invalidated to obtain space: reconcile or refuse instead.
  Partial contributor history must never authorize automatic continuation.
  Preserve enabled preference, epoch, binding authority, incarnation/enrollment
  boundaries, cyber history and unrelated pending uncertainty. Existing manual
  cancellation behavior still applies. A new independently admitted turn can
  establish complete proof normally.
- If all 64 records are protected, or eligible retirement cannot satisfy the
  byte bounds, refuse the fresh admission **before** native submission. There
  is no provenance-omission fallback, cap increase or unbounded collection in
  this hotfix. Keep the prior valid state and the original submission identity.
- Keep existing package/runtime/roster/conversation/per-thread/native-ledger
  lock ordering, generation/authority checks, recovery and unknown-outcome
  holds. Retention is subordinate to admission; it does not authorize loading,
  resuming, rebinding or otherwise bypassing an existing hold.

### Replay, aggregate proof and accepted receipt boundaries

Resolve the exact original UUID/text/action/options through existing generic
receipt/history reconciliation before fresh capture or binding effects. Return
an accepted original receipt without reconstructing provenance from current
defaults. A submitting outcome remains reconciliation-only. Prepared and absent
are distinct: `ReconcileSendWithOptions(found=false, err=nil)` alone does not
prove absence. Existing `SendAttemptedWithOptions` and browser `retry:true`
history recovery remain available; preserve their exact identity checks. Never
retag an evicted input with a later epoch/settings, allocate a replacement UUID,
or change the generic acknowledgement/deduplication contract. A prepared or
uncertain input lacking admission proof must not be treated as fresh solely
because its provenance snapshot is absent.

Apply the bound deliberately at every production `AddSnapshot` caller:

- `captureRetry`: accepted-only retirement, suppression and new admission are
  durably valid before ordinary send/queue proceeds. Missing capacity refuses.
- `retryBackend.Prove`: account for the derived executed-proof slot and bytes.
  If complete proof cannot be retained safely, consume that exact failure and
  return the existing missing-proof/manual-only outcome with a valid state.
  Never retain a cached aggregate after discarding its contributors and then
  use the cache to bypass the complete-history proof.
- `State.Accepted`/controller: preflight room for receipt/result bookkeeping
  and the automatic-result snapshot before any fresh automatic dispatch, using
  the same retirement exclusions. Reconciliation of an already accepted native
  result takes precedence over new dispatch; preserve its exact pending/result
  and quota correlation. Do not repeatedly append a 65th derived snapshot and
  fail to settle the same known receipt. Receipt settlement and continued
  automatic eligibility are separate: lack of safe proof space must hold the
  next automatic attempt, never replay the accepted one or discard its tuple.
  A real persistence failure retains ordinary unknown/reconciliation recovery.
  Any implementation requiring new schema or an omission admission path must
  return to lead rather than silently expand this scope.

#### Already accepted result when every snapshot is protected

Lead explicitly approved this receipt-settlement distinction: an exact native
acceptance can be settled without creating a redundant derived eligibility
snapshot. This is not permission to omit provenance for a fresh admission.
Choose the existing schema-1 **blocked** representation, not `running`:

1. Require the exact accepted receipt for the saved pending tuple. Preserve
   `Pending.ID`, `Action`, `Failure` and `Snapshot` unchanged; set
   `Pending.ResultTurn` to the exact accepted turn, rejecting any conflicting
   previous result. Preserve cyber charge identity and perform the existing
   acceptance/reanchor operation exactly once, keeping `ChargedAtMS` consistent.
2. Do not append another snapshot when accepted-only retirement cannot fit it.
   Keep every protected snapshot. Set `Phase="blocked"`,
   `Reason="settings_unproven"`, `Cancelled=true`, `DeadlineMS=0` and
   `Handled=Pending.ResultTurn`. Invalidate cached eligibility for that result
   turn without changing the immutable `Pending.Snapshot`. Preserve Enabled,
   epoch, enrollment/incarnation, binding, quota and exact pending/result tuple.
   Do not call the generic `Cancel` helper here: it clears non-uncertain Pending.
3. Save the receipt settlement atomically, then return reconciled/accepted with
   no dispatch. Repeated exact receipt settlement remains idempotent and cannot
   restore automatic eligibility merely because space becomes available later.
   Native work already running is not interrupted by this retry-policy state.

This representation is valid under the deployed `store.go:validate`: blocked
permits a nonnil validated Pending with ResultTurn and consistent charge fields.
`State.Uncertain` recognizes only submitting/reconciling, so a restart does not
reenter uncertain dispatch. `Controller.Step`/`Observe` skip the exact Handled
failure; an in-progress result leaves the blocked tuple intact; scheduled-only
dispatch cannot run. Ordinary later independent admission/settings/lifecycle
rules still apply, and may retire settled pending state under their existing
contracts. This is not new unresolved uncertainty or a native execution hold.

Fresh automatic dispatch must preflight sufficient count and byte budget and
refuse before native submission if unavailable. The exceptional settlement
above preserves already accepted deployed attempts. It does not relax byte
validation or promise success on an actual disk/persistence failure: a failed
settlement save leaves the prior durable uncertain tuple and generic accepted
receipt authoritative, and recovery only reconciles that same UUID.

Required regression: seed a valid deployed record with all 64 snapshots
protected and exact uncertain Pending; make the generic backend return its
accepted receipt. Reconcile/save/reload must retain all 64 and the complete
Pending/result/quota tuple in blocked state, with zero fresh native calls.
Repeat reconciliation and controller steps across in-progress then eligible
failed result, restart, and recovered free space: no 65th snapshot, no new UUID,
no extra quota reanchor, no proof resurrection and no automatic dispatch. Check
conflicting result identity and save failure separately. Pair this with fresh
automatic preflight refusal at the same capacity; no new-input omission path.

The public message error remains the existing conservative HTTP 503. This fix
does not add `notSent` or infer it from a status code, missing provenance,
timeout or save error. A post-native acceptance/save failure remains uncertain
to the caller. Retry the original browser submission/attachments/UUID; delivery
deduplication continues to belong to the generic ledger and exact history.

Source anchors at the deployed revisions: B
`portal/internal/workspacecodex/turn_retry.go` (`captureRetry`,
`SendWithOptions`, `QueueWithPolicy`, `bindRetryReceipt`),
`turn_retry_proof.go` (`Prove` and its cached-proof fast path),
`portal/internal/turnretry/{state,store,controller}.go`; A
`codex/client.go` (`ReconcileSendWithOptions`, `SendAttemptedWithOptions`,
`AcknowledgeSends`) and `conversation/handler.go` (`send`, `serverError`).

### Required checks and rollout boundary

Use synthetic private state and the actual managed root/member wrappers, not
only direct snapshot helpers. Required focused cases are:

- Exact deployed 64-bound-steer shape: the 65th and subsequent distinct sends
  reach native once each, retain at most 64 records and bounded bytes, and leave
  the truncated current turn ineligible. Test root and retained member paths.
- Same UUID after retirement, lost reply, restart and browser acknowledgement:
  exact ledger/history recovery returns the original outcome without another
  native send or retrobinding; changed text/action/options is refused under
  the existing delivery identity contract.
- Protected unbound queues, prepared/submitting/unknown attempts and pending
  snapshot identities survive unchanged. All-protected full state refuses
  before send. Queue order and execution holds remain intact.
- Existing cached executed proof cannot bypass suppression, including restart
  and preference/settings changes. A later independent fully proven turn stays
  eligible. Prove at the contributor/aggregate limit and near-byte-limit state
  never save invalid state; accepted automatic receipt reconciliation does not
  repeat native dispatch or reset quota when adding its derived proof needs room.
- Crash/save failure before compaction persistence, after persistence but
  before send, after native submitting, and after generic acceptance but before
  retry receipt save: no send before required persistence, no duplicate after
  uncertainty, no loss of exact receipt/queue identities. Public errors remain
  conservative, including postacceptance errors.

Lead's verification selection: committed focused Go/race checks, then the same
reviewer's affected general/architecture/scope/risk lanes. After findings are
resolved, a fresh verification utility runs the exact B packaged package check
(pinned A/Go/Node and Ruby aggregate), targeted native B recovery/controller,
W's four composed checks, C's eight checks, and scoped system/profile builds.
Compare selectors, derivation and full input identities with retained receipts;
reuse exact successful unchanged Ruby/other checks without duplicate execution.
Root completed outputs immediately and retain source/input graph receipts.
Pinned native 0.163 and A's six native cases are unchanged, so retain their
exact prior A evidence. Host/lifecycle/creation/archive VM source is outside
this bounded Go retention fix: no automatic full VM campaign unless changed
source or review identifies an affected contract. Owners must escalate that
concrete impact rather than silently omit a newly applicable check.

The successor must continue reading all deployed schema-1 records; no new
capability or eager state rewrite is needed. Older software can decode the
same format but retains this retention defect; normal forward recovery remains
the operational contract. Lead owns reviewed package pinning, exact build and
deployment receipts, acceptance and the existing held machine. This supplement
authorizes no deployment, integration, release, rollback or lifecycle action.
UI/session-policy design stays paused until the incident is handled.

## Scope and decisions

Implement server-side retries around the existing Codex App Server. Codex stays
unmodified. Enroll existing and new managed lead threads and ready retained team
members, enabled by default with a persistent per-thread opt-out. Native Codex
children, utilities and unrelated same-directory threads are not enrolled.

Only new failures after enrollment qualify. First deployment records a durable
baseline and never restarts a pre-existing failed task. Restarting the portal
retains that baseline and resumes already-recorded retry operations through
reconciliation and execution holds. It does not reenroll old failures.

Retry is a new, visible continuation turn in the same conversation. Use the
existing recovery text:

> Continue the interrupted task from the saved conversation. Inspect the current state before repeating actions.

Do not replay the original user input, rewind history, replay tool calls,
rewrite a policy/request, or change model/provider/effort/access. Partial results
and the failed turn remain visible. This design prevents duplicate automatic
submissions; it cannot promise exactly-once execution of earlier model actions.

Capacity delays are 15, 30, 60, 120, 240, 300 seconds, then 300 seconds
indefinitely until cancellation. Add uniform positive jitter from zero to
min(3 seconds, 10% of the base), with the final interval capped at 300 seconds.
Choose and persist the deadline once. No elapsed-time or attempt budget applies
to capacity. A fresh independent task starts a fresh backoff chain.

Cybersecurity failures retry on the next scheduler opportunity without a policy
delay. Permit at most 30 automatic dispatches per thread in the rolling interval
(now minus 300 seconds, now]. Original and manual submissions do not count.
After exhaustion leave the task failed for manual action; expiration of the
window alone never rearms it. Retain the rolling ledger across chains/restarts.

## Sources, baseline and protocol gate

- Lead verified remote dev-workspace
  `483d4e7eafeda974dfe19de45687795562072d7d` against all 535 files of installed
  `/nix/store/vq9x3djn7b5v42ywbyfwagr3cslk9wja-source`: no differences. It selects
  codex-web `ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5` and Codex 0.163.0.
  Earlier local bare HEADs and workspace locks were stale. Work starts from
  fresh remote ancestry containing these revisions. Implementer1 reports newer
  baseline `bf6d4b0c`, containing `483d4e7e`; verify final full heads in receipts.
  A concurrent profile switch subsequently selected `4cn1hh88...`; the lead
  must retain its full path/input graph and preserve its features before rollout.
- [Official App Server documentation](https://developers.openai.com/codex/app-server/)
  documents `turn/start`, `turn/steer`, interruption and terminal turn events.
  There is no established native retry endpoint or empty-input continuation
  contract. The supported design uses ordinary nonempty `turn/start`.
- Installed dev-workspace `portal/internal/web/recovery.go:513` supplies the
  existing visible continuation text and durable recovery precedent;
  `:309` supplies normal resolver/mutation authority. These are integration
  references, not authorization to call recovery activation from a retry.
- codex-web `codex/client.go` prepare/submitting/accepted ledger and
  `ReconcileSendWithOptions` are the submission authority. Generic
  `SendWithOptions` can steer a running turn and must not be used directly as
  the automatic dispatcher. `docs/reference.md` documents cold-thread holds,
  native queue auto-execution, options identity and accepted-options compaction.
- Protocol gate resolved by implementer0: pinned Codex 0.163.0 generated
  experimental schema using
  `/nix/store/wz4w670930cksh1ivz13y0gn3c23cjzl-codex-package-0.163.0/bin/codex`.
  `/tmp/codex-thread-retries-01630-schema/v2/ThreadTurnsListResponse.json`
  has exact `CodexErrorInfo` variants `cyberPolicy` and `serverOverloaded`
  at lines 63–64. Implementer0 owns assertions against generated schema.
  No real policy-violation request is needed. The existing capacity transcript
  fixture also uses `serverOverloaded` with the displayed capacity message.

Only terminal `failed` turns with these exact discriminators qualify. A native
intermediate `error`, including `willRetry`, an active turn, transport timeout,
quota/budget/authentication error, generic 429, ordinary assistant refusal or
unknown spelling does not qualify. Preserve unrecognized errors for display;
do not match human text or infer terminal status from a notification alone.

## Native 0.163 loaded terminal status correction (run 2)

Lead accepted this material protocol correction after native run 2. The run
did not retain the failed thread's status tuple; the conclusion below is from
pinned source, not a claimed empirical observation. Earlier references in this
brief to an "idle" continuation mean a **loaded, quiescent exact failed turn**,
with the predicate below. They do not require the literal native `idle` value.

Pinned evidence:

- [`bespoke_event_handling.rs:1034–1055`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/app-server/src/bespoke_event_handling.rs#L1034)
  calls `note_system_error` for `EventMsg::Error`, even before determining
  whether the error affects turn status. An error notification alone is not
  terminal failure authority.
- [`thread_status.rs:147–191`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/app-server/src/thread_status.rs#L147)
  clears `has_system_error` only on a new turn start. Completion clears running
  and pending-request counters but leaves the error flag. The native
  [`system_error_sets_idle_flag_until_next_turn` test](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/app-server/src/thread_status.rs#L619)
  confirms this persistence.
- [`loaded_thread_status:447–468`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/app-server/src/thread_status.rs#L447)
  returns `notLoaded` first, then `active` for running or approval/user-input
  flags, then `systemError`, otherwise `idle`. Thus `systemError` is a loaded
  status, not a cold-thread marker or a retry classification.
- [`thread/read:2976–3047`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/app-server/src/request_processors/thread_processor.rs#L2976)
  combines live/persisted metadata and watch status. Latest-turn listing
  [`3244–3272`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/app-server/src/request_processors/thread_processor.rs#L3244)
  also merges the live active-turn snapshot. Status reads are observations,
  not an atomic compare-and-start. In particular,
  [`resolve_thread_status:290–303`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/app-server/src/thread_status.rs#L290)
  upgrades running `idle`/`notLoaded`, not `systemError`; retain the independent
  exact terminal-turn check and all existing activity/admission holds.
- The public [`ThreadStatus` enum](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/app-server-protocol/src/protocol/v2/thread.rs#L1679)
  and pinned generated `v2/ThreadReadResponse.json:2374–2447` define precisely
  `notLoaded`, `idle`, `systemError`, and `active` with `activeFlags`.

**Owner A adds one shared typed observation predicate** in
`codex/turn_state.go`:

```go
func (s TurnState) IsLoadedFailedTurn(expectedTurnID string) bool
```

It returns true only for a nonempty expected ID equal to `LatestTurnID`,
`LatestTurnStatus == "failed"`, and native `Status` equal to `idle` or
`systemError`. Empty/unknown status, `notLoaded`, `active` (with any or no
flags), empty/wrong/newer ID, and in-progress/completed/interrupted turns return
false. Preserve the raw native status in `TurnState`; do not normalize it to
`idle`. This method proves only the loaded terminal observation tuple. It does
not classify the error, prove settings/authority, inspect queues/prompts or
authorize a send. `TerminalFailure` remains the separate exact error source;
B's `serverOverloaded`/`cyberPolicy` allowlist stays unchanged. Unknown failures
never become automatic candidates through `systemError` or message text.

A uses this method in `codex/continuation.go` at both existing preflight reads,
retaining exact submitting/accepted reconciliation before fresh checks,
queueUpdateLock, native queue and pending-request reads, unresolved ledger
holds, stable action/options identity, and final reread before claim/send.
Owner B uses the same method in
`portal/internal/workspacecodex/turn_retry_proof.go` (`retryBackend.Check`),
instead of duplicating native status strings. B retains exact historical
settings proof, current epoch/binding/provider/socket/policy checks and all
managed lifecycle/admission fences. No broader activity/lifecycle semantics,
I3 same-active-turn witness, state schema, quota or UI behavior changes.

Do not resume, rebind, change settings, clear native error state, or send a
dummy turn to obtain `idle`. Native queue, prompts, active/newer turn,
unresolved send and cold holds remain decisive. The managed-only/no-public-CAS
boundary is unchanged; `systemError` alone cannot establish fresh authority.

Owner A adds table tests for both accepted statuses and every refusal above,
schema assertions for the exact native variants/active flags, and continuation
tests proving queue/prompt/unknown-ledger/newer-turn refusal under
`systemError`. Existing reconciliation tests must still pass even when fresh
admission is refused. Owner B adds adapter/controller tests for identical
`idle`/`systemError` failed-turn behavior, including both eligible error codes,
and unknown-code/cold/active/binding-change holds. Native wait helpers use the
shared predicate and retain diagnostic tuples; they must not require literal
`idle`. A's separate approved test-only fresh-thread bootstrap correction is
unchanged. No native assertion may be removed to make the tests pass.

A documents this helper and the meaning of loaded quiescence in
`docs/reference.md`; B updates its retry contract in
`docs/workspace-portal.md`. Pin A into B after publication. No persisted-state
migration or capability bump is required for this additive public helper and
corrected protocol predicate. The old A predicate would keep these failures
held, so the deployment must use matching corrected A/B sources. Commit and
quick-check all intended changes, then obtain the same reviewer's affected
general/architecture/risk review before native run 3. Downstream C remains held
until final source/native evidence; lead owns owner release and final pins.

## Native direct-writer race disposition (run 3, accepted)

Lead accepted the following bounded compatibility disposition after inspecting
`native-verification/run-3-731bb742/library.jsonl`. The four passing native
default/plan/cyber/automatic-queue cases are valid evidence for A665 only; the
whole native gate did not pass. The direct-writer probe recorded a successful
RPC with the continuation and manual submission returning the same nonempty
turn ID, that turn still `inProgress`, and one provider request while the
provider was held. This is **implicit native steering into an existing regular
turn**, not evidence of replacement or refusal.

Pinned source explains the observed result:

- [`turn_processor.rs:661–734`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/app-server/src/request_processors/turn_processor.rs#L661)
  routes public `turn/start` through `start_or_steer_turn`, accepts both
  `Started` and `Steered`, and returns either accepted ID as `inProgress`.
- [`codex_thread.rs:414–422`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/core/src/codex_thread.rs#L414)
  documents that Core starts, steers, or declines. The Core-only idle-start
  primitive nearby is not a public App Server compare-and-start interface.
- [`turn_input.rs:373–390`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/core/src/session/turn_input.rs#L373)
  attempts steering without an expected-turn ID.
  [`813–896`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/core/src/session/turn_input.rs#L813)
  locks the active task, accepts a regular task, appends the input with its
  client ID, and returns that existing turn ID. The module contract at
  [`1–9`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/core/src/session/turn_input.rs#L1)
  distinguishes acceptance from persistence/sampling and says persistent
  thread settings also apply to `Steered` submissions.

This preserves the accepted managed portal/CLI/retained-team boundary. Every
managed writer must share the authoritative admission fence. Unmanaged direct
native writers do not, and can inject input or apply settings to active work.
Neither public `turn/start` nor the library receipt's `Steered == false` proves
that native implicit steering did not occur. The receipt reflects the requested
client path. No native patch, new public CAS API, product fallback, additional
override or wider external-writer guarantee is introduced.

Owner A keeps `native_direct_busy_race_compatibility` as a strict pinned-native
diagnostic. Its deterministic proxy barrier must establish a manual regular
turn active before allowing the automatic `turn/start` request that already
passed its final observation. Require precisely:

1. Successful native RPC; equal nonempty manual/continuation turn IDs; latest
   turn equals that ID and is `inProgress`; exactly one provider request at
   the held-provider observation.
2. After releasing the provider, bounded eventual observation of both exact
   client input IDs once each in that same turn and completion of that turn.
   Preserve the original failed turn/history; no distinct replacement turn
   or interruption may substitute for the observed behavior.
3. Retain the bounded RPC trace and request counts. A changed native version
   that refuses, replaces, interrupts or otherwise changes these semantics
   fails this diagnostic for explicit compatibility reassessment. Do not
   accept both refusal and steering, skip/delete the case, or make it an
   unconditional success. Provider count one is the held-point assertion,
   not a claim about the total count after pending input is processed.

This diagnostic establishes the unmanaged limitation, never managed safety.
The accepted lost-reply fixture correction may poll only reconciliation of
the same stable ID, bounded by its context, until history supplies the accepted
receipt. It must never issue a fresh submission to make that assertion pass.

Owner B adds a separate composed admission regression using the **actual**
managed `SendWithOptions`/`QueueWithPolicy` wrappers and actual
`turnretry.Controller.Step`, the authoritative shared fence, and deterministic
synthetic-wire/RPC barriers. Required outcomes:

- Manual send or queue admission wins: the pending retry is cancelled or
  superseded and no automatic native `turn/start` or `turn/steer` is emitted.
- Automatic dispatch owns the fence: competing managed input cannot reach
  native until its dispatch/receipt critical section ends; afterward ordinary
  manual semantics apply. Do not assert that explicit manual input can never
  steer an active task.
- Automatic outcome remains unknown: subsequent managed manual input remains
  held while the exact uncertainty is reconciled; no speculative second send.

Exercise production wrappers, not direct state-helper substitutes. Retain A's
active/queue/prompt/unresolved/final-reread refusal tests and B's interprocess
and roster-operation lock tests. The composed regression closes their missing
integration proof; a real synthetic-wire fixture is sufficient and does not
require another complete native campaign. If it exposes a product defect,
stop and route that defect through lead/design before changing production code.

Owner A updates `docs/reference.md`; owner B updates
`docs/workspace-portal.md` with the explicit native steering/settings limitation
and managed fence guarantee. Lead performs the main copy pass before commits.
This is test/documentation scope, with no new public API or persisted format.
After committed changes and quick checks, the same reviewer checks affected
general/architecture/risk lanes before the next final native campaign: changing
the diagnostic's accepted observation changes what release evidence certifies.
Evidence-only session updates do not separately require final review.

B731 remains frozen while lead's correctly rooted batch completes run 3;
its earlier wrong-CWD invocation produced no B test events and is not a pass.
Owner B may prepare the regression read-only, then edit only after lead confirms
that batch is finished. Do not change source during Go compilation. The final
A/B review and native campaign use newly reported exact heads and dependency
pins; earlier scoped passes do not certify those new heads. C remains held.

## Two-owner boundary and shared contract

Implementer0 owns all codex-web changes: generic terminal-state projection,
idle-only continuation primitive, optional HTTP provider and generic browser
controls, protocol/Go/browser tests and `docs/reference.md`/README updates.
Suggested new files are `codex/turn_state.go`, `codex/continuation.go`,
`conversation/retry.go` and adjacent tests. Existing `codex/client.go`,
`conversation/handler.go` and `conversation/assets/{conversation.js,conversation.css}`
remain this owner's files. A separate browser module is fine if embedded and
tested by this owner. No workspace policy belongs in codex-web.

Implementer1 owns all dev-workspace changes: durable retry store/policy/controller,
managed admission/settings provenance, trusted provider adapter, observer wiring,
root/member/cold-recovery/team/CLI integration, lifecycle/package fencing, Nix
contract metadata, runtime tests and documentation. Suggested new package:
`portal/internal/turnretry/`; integration points include
`portal/internal/{web,workspacecodex,teamruntime,session}/`,
`portal/cmd/workspace-portal/`, `libexec/` and `nix/` as required by existing
transition owners. This owner updates the codex-web dependency pins. Workspace
browser work is limited to enabling the optional generic UI and mapping opaque
lead/member conversation identities; do not implement a second countdown or
HTTP retry backend in workspace JavaScript.

Lead owns downstream configuration/workspace input selection and rollout
assignment. No implementer changes the other's repository. B's pure store,
policy and controller tests can start against the following interface before A
publishes a dependency revision. Agree any material interface change through lead.

### Generic Codex API (owner A)

Adopt the proposed signatures:

```go
ReadTurnState(ctx context.Context, threadID string) (TurnState, error)
ContinueFailedTurn(ctx context.Context, threadID, text, stableID,
    actionContext, expectedFailedTurnID string,
    options TurnOptions) (SendReceipt, error)
```

`TurnState` exposes the latest turn ID and status, and a nullable
`TerminalFailure{TurnID, Code, Message}`. Empty history is explicit; unknown or
contradictory identity/status is an error. Reading is cold and bounded, using
latest-turn metadata and the selected protocol's error payload. It must not
resume, update settings or execute native queues. Events only invalidate this
snapshot. No transcript text parsing or implied current-settings provenance.

`ContinueFailedTurn` first reconciles an exact existing submitting/accepted
attempt, even if a newer turn now exists. For a fresh attempt it requires an
already-loaded idle thread and verifies exact latest failed-turn identity, no
active turn, no pending requests and no queued native input under the existing
queue mutation lock. It never calls `thread/resume`, writes policy/settings or
rebinds instructions, MCP reporting or access, even while idle: resume can
activate a saved native queue or goal. Never steer or activate held cold work.
A known stale/busy/refused preflight sends nothing; an uncertain
dispatch preserves `UnknownSendOutcomeError` and the exact stable identity.
It uses the existing prepare/submitting/accepted ledger and history correlation,
not a parallel submission ledger. A same-ID retry must not pass through a fresh
dispatch after an unknown outcome. The application retains exact text/options
and binds the expected failure and settings-provenance digest into its unique
action context; changed identity must fail, not reuse an accepted receipt.

Existing generic send methods retain their zero/default settings behavior.
The continuation sends explicit model/effort and the proven additional context.
Its immutable `ThreadPolicy` remains part of the exact ledger identity but is
not reapplied. Instructions, MCP reporting and execution/approval access inherit
the already-loaded binding. B must prove that this binding and provider/mode
still exactly match the failed turn's authorized settings. No global defaults
changes or compensating rebind may satisfy this precondition.

The in-process `queueUpdateLock` is necessary but insufficient for two processes.
B must hold the shared application admission fence for the whole dispatch. A
must also preserve the ledger's atomic transition semantics so a competing
same-ID caller sees submitting and reconciles instead of issuing a second RPC.
Test this explicitly; do not advertise cross-process exclusion from a Go mutex.
No ledger file lock may recursively deadlock a helper that opens that same lock.

### Exact native turn context for queued execution (owner A)

Lead approved this bounded addition after confirming that native queue execution
has no managed execution callback. Add:

```go
ReadTurnContext(ctx context.Context, threadID, turnID string) (TurnContext, error)

type TurnContext struct {
    ThreadID          string
    TurnID            string
    Cwd               string
    Model             string
    ReasoningEffort   string
    CollaborationMode string
    ApprovalPolicy    json.RawMessage
    SandboxPolicy     json.RawMessage
    ApprovalsReviewer string
    PermissionProfile json.RawMessage // Optional; nil means absent.
}
```

This is a Go-only proof projection, not a browser payload. Read only the native
rollout returned by trusted `thread/read`, using the existing rollout reader
boundary. Validate the native session/thread identity and canonical directory;
match the requested `turn_context.payload.turn_id` exactly. Return model/effort,
the collaboration mode name, and the listed execution-policy values. Raw JSON
is limited to those structured policy fields, since approval policy can be an
enum or object; validate their selected-version shapes. Do not export the
collaboration mode's developer-instruction text, prompts, session credentials or
arbitrary native payload. Provider, common/role instructions and MCP binding are
deliberately absent: this context does not prove them.

The pinned 0.163.0 App Server `Turn` and `turn/started` schemas expose no effective
settings. Native history does: this architect verified exact `turn_context`
field names/types in this session's own 0.163.0 rollout, including `turn_id`,
`model`, `effort`, `collaboration_mode`, `cwd`, `approval_policy`,
`sandbox_policy`, `approvals_reviewer` and `permission_profile`. Existing
codex-web `codex/timestamps.go:130–235` already reads `turn_context` and
`thread_settings_applied` for display mode; extend the reusable reader without
mistaking its latest-mode convenience result for exact-turn proof.

Missing/incomplete context remains pending or unavailable, never falls back to
current defaults. Conflicting contexts for the requested turn fail closed;
identical repeated projections are harmless. Do not silently choose a later
context from a different turn. Validate persistence identity across read and
handle partial final records, replacement/truncation and inherited history
conservatively. Keep reads bounded/cancellable and reuse the existing incremental
metadata approach where possible; a large latest turn may place its context
outside a fixed suffix, so suffix absence is not proof that no context exists.
Native-version compatibility is pinned to 0.163.0 and covered by fixtures/native
verification; there is no claim that an untested version preserves this layout.

Observed native policy encoding is distinct from v2 request encoding: rollout
`sandbox_policy.type` is `danger-full-access` or `workspace-write`, with
snake_case keys such as `writable_roots`, `network_access`,
`exclude_tmpdir_env_var` and `exclude_slash_tmp`. This session's unrestricted
context has `approval_policy: "never"`, `approvals_reviewer: "user"`,
`sandbox_policy: {"type":"danger-full-access"}` and
`permission_profile: {"type":"disabled"}`. Its earlier managed context has
`permission_profile.type: "managed"`, a `file_system` object with
`type: "restricted"` and `entries`, and `network: "restricted"`. Entry paths
are tagged `path` (an absolute path) or `special` (a value object with `kind`);
entries carry `access` and optionally `missing_path_behavior`. These are observed
fixtures, not an exhaustive native-policy schema. Never compare native and v2
policy objects byte-for-byte or assume camelCase request enum spellings here.

### Optional HTTP and browser API (A defines; B implements)

Add `conversation.Target.Retry RetryProvider` and `Capabilities.Retry` without
widening the required `conversation.Client` interface. Provider contract:

```go
ReadRetry(ctx context.Context, threadID string) (RetryStatus, error)
SetRetryEnabled(ctx context.Context, threadID string, enabled bool) (RetryStatus, error)
CancelRetry(ctx context.Context, threadID string) (RetryStatus, error)
```

The trusted resolver supplies the provider and thread ID on every request.
Endpoints below each opaque conversation are `GET retry`,
`POST retry/enabled` with `{ "enabled": bool }`, and `POST retry/cancel` with
an empty object. Require exact origin, mutation authority and the common
mutation lock for POST. Browser input supplies no thread/socket/CWD, message ID,
model, retry options, policy or arbitrary reason. Set/cancel are idempotent
operations on current server state. A repeated cancel must not create work.
Absent provider/capability leaves existing embeddings unchanged and hides UI.

`RetryStatus` JSON contract: `enabled`, `class`, `phase`, `attempt`,
`nextAttemptAtMs`, `serverNowMs`, `cyberUsed`, `cyberLimit`, `reason`.
Times are Unix milliseconds; no deadline is null. Classes are empty,
`capacity`, `cybersecurity`. Phases are `idle`, `scheduled`, `submitting`,
`reconciling`, `running`, `cancelled`, `exhausted`, `blocked`.
`attempt` counts automatic dispatches in the current chain; `cyberUsed` is
rolling-window use, including conservatively retained uncertain dispatches;
`cyberLimit` is 30. `reason` is a bounded safe explanation, not private state.

A owns generic controls and their tests: per-thread Auto retry checkbox,
countdown/status near failed turn, Cancel retry, exhausted/manual explanation.
Use server deadline plus server/browser clock offset; reload/tab/focus reads
server state. The browser never schedules a submission. Cancellation stops the
current chain but leaves the enabled preference alone. Disabling also cancels
the chain. Enabling never revives the same old failed turn. Existing Stop remains
the way to interrupt a running turn; Cancel retry suppresses future automatic
continuations and cannot erase an already-dispatched request. Both lead/member
views use this module. Lead applies final user-facing wording conventions.

## Effective settings provenance (owner B, required before dispatch)

`ReadTurnState` and current `ReadThreadSettings` do not prove the failed turn's
effective settings. B must retain an immutable admission snapshot before each
managed submission can run, then bind it to the accepted native turn ID through
the exact send receipt/history reconciliation. Snapshot model, effort, provider,
collaboration mode, common and role instructions, execution/approval policy,
MCP reporting binding and additional application context. Include a canonical
digest/version and origin (root browser/CLI, team assignment, queue, continuation).
This is application authority, never browser-supplied policy. The continuation
uses that proven snapshot. Compare retained provider/mode, instructions, MCP
reporting and execution/approval policy against the unchanged authorized loaded
binding before dispatch. Missing or changed bindings block/cancel the old chain;
automatic retry must not resume the thread, refresh policy or rebind MCP to
repair them. This preserves the accepted no-resume/no-settings-write boundary.

Accepted authority boundary: these guarantees cover managed portal, CLI and
retained-team admissions serialized by the common runtime fence and generation.
An exact historical `ReadTurnContext` plus the saved successful managed loaded
binding establishes authority within that boundary. Neither the historical
context nor `ReadThreadPage.CollaborationMode` proves current loaded settings
against arbitrary external mutation; the latter is display metadata and must
not be used as mutation authority. Pinned `ThreadReadResponse` lacks loaded
collaboration mode/access; `ThreadResumeResponse` exposes them but resume is a
mutation and remains forbidden during retry. Do not add resume or new policy
overrides to manufacture proof.

Unmanaged direct native clients can bypass admission and change loaded settings
without a detectable generation change. Their concurrent writes invalidate
the managed guarantee; this design does not promise to detect every such write
or provide a native compare-and-start operation. Observed changed native
context/settings, foreign or unidentified input, execution holds, changed
binding or socket generation fail closed. Preserve uncertainty across restart;
do not rebuild authority from display caches or assume a native daemon restart
retained the loaded binding. This scope was explicitly accepted by lead after
B raised the current-mode/access observation limitation.

Capture paths must include managed normal sends, direct team assignments,
initial turns, explicit Continue and queue execution. For steering, inherit the
known active turn's settings and retain the added application-context provenance;
do not treat the steer's requested defaults as the active turn's model. A queued
message's enqueue-time defaults alone do not prove its eventual execution
settings, especially when native queues start automatically on resume. Bind the
actual execution boundary or show `blocked` for missing proof. Native-origin
turns on an otherwise managed thread remain manual when proof is unavailable.

For managed native queue execution, use the approved exact-context reader rather
than adding an execution callback, freezing user settings or replacing the
native queue. B retains the managed queue entry's stable client message ID,
text/options identity and authorized loaded-binding snapshot at admission.
After execution, a native user-message/history receipt must prove that this
exact client ID and content ran in the exact failed turn; a queue acceptance
receipt or missing queue row alone cannot prove that. Combine that receipt with
`ReadTurnContext` for this same turn ID. Native context supplies the actual
model/effort/mode/access at execution. The saved authorized binding and unchanged
loaded-generation proof supply provider, instructions and MCP. Compare native
execution policy to the retained authorized policy and current binding before
continuing; a mismatch or broken binding epoch blocks recovery. This proof must
survive portal restart without assuming that the native thread stayed loaded
across a native daemon restart or rebind.

This queued path accepts only known-empty additional application context, as
the existing native queue carries text but no per-message application context.
Other queued context, foreign/unidentified contributing messages, changed
provider/instructions/MCP, missing exact execution receipt or incomplete native
context remain manual and visible. Missing proof does not authorize replaying
the queue input. This is the managed-queue acceptance path, not a silent removal
of queue coverage from scope. Add fixtures for an automatically executed queue
whose actual model/effort differs from its enqueue-time defaults, exact-ID
correlation, later unrelated settings/context, missing/conflicting records and
partial append/restart recovery.

Accepted team options may be compacted, so `OriginalSendOptions` alone is not a
durable provenance store. Retain B's snapshot for the currently relevant task
and unresolved retry chain independently of compaction. Do not extend A's
`TurnState` with guessed options. When multiple messages contribute to a turn,
all retry-relevant application context must be accounted for; ambiguous context
fails closed. An unsupported managed admission path is an acceptance gap to
report to lead, not a reason to invent settings from today's defaults.

## Durable state and enrollment (owner B)

Use separate version-1 private records under the application's durable state
root, namespaced by canonical workspace/session/thread identity. Expose a
package capability `turnRetryStateSchema = 1` through the existing package
contract conventions; this is the agreed capability key. Preserve existing
schema-3 submission and recovery/roster records without rewriting their format.
Use interprocess locking, validation, bounded records, mode 0600, atomic replace
and file/directory sync. The current 16 KiB preference helper is not sufficient
for full instruction/context snapshots: choose an explicit bound consistent with
existing context limits, or store an immutable bounded snapshot separately.

Persist identity/version, enabled preference, enrollment boundary/watermark,
last handled turn, chain ID, exact source failed turn/class, settings snapshot
reference/digest, capacity count, next deadline, pending UUID/action/text/options,
dispatch phase/result turn, cancellation intent, cyber dispatch timestamps and
generation/authority context. Do not store credentials or unbounded transcript
history. Unknown versions/corruption stop automation with a diagnostic.

Enrollment is a durable state transition, not GET-side accidental migration.
For existing threads, establish a conservative cold latest-turn baseline under
admission exclusion before enabling observation. A terminal failure seen during
initialization is consumed as baseline and is never eligible. Record an
in-progress baseline turn separately: its subsequently proved failed completion
can qualify if it was still active at the completed enrollment boundary and has
settings proof. Concurrent uncertain completion is excluded conservatively.
New managed threads enroll before initial execution. No native timestamp alone
is a trustworthy ordering watermark; use native IDs plus terminal/active state
and durable admission/observation boundaries. Re-enabling after opt-out also
consumes current failure as baseline. Read failure means enrollment incomplete,
not permission to process old history. A restart reads the existing boundary.

State flow: observe eligible failure -> persist scheduled intent -> at due time
recheck authority/provenance/quota -> persist stable dispatch intent -> call A's
idle-only method -> retain accepted receipt or reconcile unknown outcome. An
accepted continuation's success ends the chain; its next eligible failure
advances the chain exactly once. A newer independent turn or manual action
supersedes it. Notification duplication, worker restart and polling must not
create a second continuation for the same failed turn.

Charge a cyber slot durably immediately before a possible outbound attempt and
associate it with the stable attempt ID. Reconciliation of that ID consumes no
second slot. Retain a charge when outcome is uncertain; reclaim only when
positively proved never submitted. Never exceed 30 possible sends by forgetting
an interrupted dispatch. Keep enough timestamp evidence to survive restarts and
clock anomalies; a backward wall-clock jump cannot expire charges early. Future
timestamps or unproved time changes must hold conservatively. Capacity deadline
recovery dispatches at most one overdue attempt, never catches up with a burst.

Use an injectable clock/random source and bounded global worker concurrency.
One active operation per thread. No blocking sleep while holding admission,
transition or state locks. The scheduler works without a browser subscriber.

## Admission, lifecycle and cancellation invariants

B routes browser sends, queue mutations/start, Continue, Stop, team assignments,
CLI equivalents, settings changes and retries through the same authoritative
admission ordering. Reuse existing team operation and package/session transition
locks with their established acquisition order. Extend missing root/cross-process
coverage. Define/test the final order before wiring; do not introduce opposite
orders between RPC helpers, roster operations and lifecycle commands.

The proposed order matches the inspected ordinary mutation paths at runtime
`bf6d4b0c`: package transition -> runtime shared (exclusive for an existing
lifecycle owner) -> team **operation** lock -> conversation mutex -> per-thread
interprocess admission -> short state/native queue/ledger operations. The team
operation lock is distinct from the short roster-data lock. Source anchors:
`web/server.go:resolveConversation` takes transition/runtime/member operation
before returning the conversation mutex; `web/recovery.go:309` follows that
resolver order; `teamruntime/runtime.go:642`/`:2205` takes the operation lock
around assignment; `session/authority.go:43` maps runtime shared to the CLI's
session lock; `libexec/dev-session:9356`/`:7945` takes transition then session.

Treat this as approval of the ordering, not an exhaustive review of new wiring.
Two concrete hazards must be excluded: root plan implementation already holds
the conversation mutex in `web/server.go:2546`, and creation source snapshots
hold it in `web/creation.go:900`. Do not hide acquisition of the outer team
operation lock inside a lower-level send/admission hook reached from those
paths. Acquire required outer locks before their existing conversation mutex,
or retain a narrow already-held-lock entry point. Likewise `Service.Assign`
takes the non-reentrant operation lock itself; a caller already holding it must
not call that public method recursively. Existing member wrappers intentionally
call the underlying client under their resolver-owned operation lock.

Keep retry-record write locks short and release them before calling native
queue/ledger methods; retain the outer admission fence across that sequence.
No native/ledger callback may reacquire an outer operation/conversation lock.
Test root plan submission, member HTTP send, CLI team assignment, Stop and
scheduled retry concurrently. Existing lifecycle owners preserve their recorded
outer creation/transition locks rather than acquiring them from inside retry
state. These bounded call-site checks do not replace final independent review.

Immediately before dispatch recheck: current generation; exact workspace/session
and thread ownership; active lifecycle; ready retained member with no retirement;
no provider/package transition; execution permission and socket generation;
same failed turn; no newer input/queue/pending requests/active turn; no unresolved
submission; proven unchanged authorized settings; enabled and uncancelled state.
Do not use thread resume, subscriptions or settings updates to bypass a cold
execution hold. Observation failure only delays and exposes a reason.

Manual send, queue admission/start, Continue, settings/provider change and Stop
invalidate a scheduled chain before competing execution. User queue work wins;
never delete/reorder it to make room for retry. Cancellation before dispatch
prevents the call. Cancellation after possible dispatch durably suppresses future
attempts and keeps reconciliation active; it cannot report that nothing was sent.
An unknown outcome blocks fresh automatic work and lifecycle completion until
the existing owner proves the outcome. Report the uncertainty visibly.

Scheduled/submitting/reconciling retries are owned work in readiness and idle
observations. Explicit stop/retirement/archive/delete must first fence new work
and record cancellation, then use their existing interruption/recovery contract.
The scheduler performs none of those lifecycle actions. Restored/cold/stopped
threads remain held even if a saved deadline is due. Revival never rearms a
cancelled task. Provider switches and successful package transitions must fence
workers; fresh compatible workers reconcile retained intent, old-generation
workers cannot dispatch after the transition. Preserve prior operation journals.

## Accepted final-review corrections (owner B)

Lead accepted final findings B1 (settings invalidation), I1 (retained resolver
reconciliation) and I2 (stale cyber charge). These narrow corrections retain the
public A interfaces and managed-only/no-CAS boundary. Reviewed source packet
remains the original evidence: B `85f6f7327e6948a13ad110c4c058d8b96b6ab2b9`,
A `d2d74f931cc50e39345c6c15931748062ee51951`; fixes and resulting final heads
receive affected-lane review. Architect does not rewrite that review packet.

### Exact owned reconciliation before ordinary dispatch admission

Use a separate internal reconcile-only pass, then the existing strict dispatch
path. Runtime state saying `submitting` alone does not make ordinary observation
unknown; an unresolved native schema-3 `prepared`/`submitting` attempt does.
Retained observation aggregates all threads, so one member's attempt can block
the entire retained session before `Controller.Step` reaches reconciliation.

The reconciliation pass validates exact workspace/session/root/member ownership,
retained ready identity, lifecycle and current package authority, with the same
transition -> runtime -> team operation -> conversation -> per-thread/record
lock order. It selects only a persisted owned Pending tuple and invokes existing
`ReconcileSendWithOptions` with unchanged UUID, text, action and options. It
never calls full `Step`, Continue, resume, steer, settings or queue activation
through a weakened resolver. Do not reinterpret `ActivityKnown=false` as send
permission or expose an HTTP/client-selectable admission bypass.

An exact accepted receipt may settle its bookkeeping even when a newer turn,
cancellation or cold hold makes new execution ineligible. An unresolved native
submitting outcome stays uncertain. For no receipt, use the existing exact
`DiscardPreparedSendWithOptions`/NeverSubmitted operation to prove absence or
retire only that matching prepared, nonqueued attempt. Preserve the runtime
Pending UUID/action/options for a possible later send, or finish cancellation.
Other unresolved attempts remain untouched and keep ordinary dispatch blocked.
Reconcile each owned pending root/member separately so aggregation does not
prevent recovery of any of them. Missing, corrupt, mismatched or foreign intent
does not authorize broad ledger cleanup.

Only after reconciliation and positive unsubmitted proof may normal retained
mutation admission, execution permission, provenance, idle/queue/request and
quota checks authorize a fresh call. Revalidate those checks under their normal
locks; a reconcile-only target is not a send capability. Keep existing pending
lifecycle owners and stopped/cold execution holds intact. Avoid calling a
self-locking team observation entry beneath an already-held operation lock.

### Settings intent is a durable provenance boundary

Introduce a nonzero monotonic provenance epoch in State, Binding and every
admission/execution Snapshot; include it in binding and snapshot digests. New
state starts at epoch 1. Under the managed admission fence, establish exact
current thread/turn identity before a settings effect, advance the epoch and
persist it, consume the exact current turn even if it is still in progress,
and cancel the old chain. Overflow, missing identity or failed persistence
refuses the settings effect. Do this even when Pending is nil or the failure
has not yet been observed. An RPC failure or uncertain settings outcome does
not roll back the durable invalidation.

Every pre-intent admission/execution proof is invalid for fresh automatic
dispatch. This explicitly includes queued messages admitted before the settings
intent when their execution relative to that boundary cannot be proved. Keep
those queued messages and their FIFO order unchanged; they may execute normally,
but their failures remain manual. This conservative settings-boundary exception
was explicitly accepted by lead. New independently admitted managed messages
and queue entries use the new epoch and remain eligible after exact native
execution proof; enqueue defaults still do not prove execution settings.

Retain old snapshots needed for receipts and uncertain submissions. Reconcile
their immutable old tuple first; do not rewrite its epoch/options/digest to
make it current. Old-epoch acceptance must not create new-epoch retry authority.
`recordRetryBinding` must include the epoch in its digest and may fill a missing
binding only for a current-epoch admission. Clearing Binding alone or recreating
the previous deterministic digest cannot invalidate old proof. Explicit managed
binding establishment may create the new binding; automatic retry never does.
Keep Enabled, enrollment/baseline, first-deployment watermark and cyber history
unchanged. Do not reenroll, reset quota, use display settings as authority or
force native mode/access overrides.

### I3: preserve proof for a new queue after successful warm settings

Lead accepted this bounded follow-up to B `cca49782ebd2d5135352cea4cb140548b36f7de9`.
Clearing Binding at settings intent correctly invalidates old proof, but a new
current-epoch queue admission while a manual turn is active cannot use the
ordinary idle-only binding establishment path. Reestablish inherited binding
only at the successful explicit user settings owner, using the following
positive warm-continuity witness; do not manufacture it at queue admission.

Before invalidation, require an existing verified Binding matching the current
epoch, socket identity, provider, authorized ThreadPolicy and common instructions.
Cold `ReadTurnState` must report loaded `active` with a nonempty exact latest
turn ID and `inProgress`. Retain that binding and turn ID locally while holding
the existing managed admission/lifecycle fence. Advance the epoch, consume the
old execution and persist Binding=nil BEFORE the existing user settings effect.
The effect must succeed unambiguously. Then repeat the cold checks: same exact
active in-progress turn, same socket/provider/policy/common/authority. Only this
positive continuity proof permits copying the inherited binding into the new
epoch, recomputing its digest and saving before admission is unlocked.

The same still-active turn proves warm continuity within the managed boundary:
native automatic unload requires inactivity; managed lifecycle operations cannot
interleave under the fence. The existing warm resume keeps the same native
thread object, including its MCP runtime, instructions and access. Model, effort
and collaboration mode are the user-requested settings changes; subsequent
queue execution still needs its exact receipt and native turn-context proof.
No native override, additional resume/rebind, retry-time write, A public API or
additional persisted schema field is introduced by this correction.

Pinned **rust-v0.163.0** evidence:

- [`thread_lifecycle.rs:59–65,80–83`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/app-server/src/request_processors/thread_lifecycle.rs#L59) requires both no subscribers and inactive state before automatic unload; the unload owner at line 559 is explicitly for an idle unsubscribed thread.
- [`thread_processor.rs:3872–3886`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/app-server/src/request_processors/thread_processor.rs#L3872) returns from the running-thread path before cold config preparation. Lines 4520–4530 obtain the existing object; 4566–4616 preserve it unless an idle unsubscribed override mismatch permits replacement; 4664–4783 attach its listener and return its configuration snapshot without rebuilding MCP.
- The same file's [`collect_resume_override_mismatches:114–232`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/app-server/src/request_processors/thread_processor.rs#L114) examines supplied overrides. A `client.go:3347–3349,4291–4292,4363–4375,4425–4431` with the runtime's `PreserveThreadInstructionsOnResume=true` supplies no instruction/MCP/execution-policy override for the implicit settings resume. A's `ThreadPolicy` rebinding warning remains necessary for a cold load; it does not establish loss of the MCP runtime on this proved warm path.
- **Do not use `sessionId` as a loaded-generation witness.** [`core/src/session/session.rs:932–952`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/core/src/session/session.rs#L932) restores it from persisted SessionMeta and otherwise uses the root thread identity. The public field identifies a session tree and can survive reload.

Missing prior proof, a completed/changed turn, idle/cold observation, changed
socket or authorized binding, failed/unknown settings result, postcheck failure
or save failure leaves the new epoch and nil binding. Never restore the old
epoch, rewrite old snapshot digests or retrobind old queued admissions. Lead
explicitly accepted this conservative turnover hold; continuity across a native
instance change is not claimed. A later ordinary explicitly requested managed
idle send/queue/load may establish its binding through the existing owner path.
Arbitrary external native writers remain outside the supported managed fence.

Owner B must test actual `UpdateThreadSettings` followed by actual
`QueueWithPolicy` while the same manual turn remains active, for both root and
retained member with MCP. Then prove native-style queue execution by exact
receipt/context and eligibility of the new epoch. Assert inherited MCP/tools,
instructions and access; old turn/queue remains excluded. Include completion,
automatic queue turnover, cold/unloaded, failed/unknown RPC, changed authority
and failed persistence cases. Direct helper calls to `captureRetry` followed by
`recordRetryBinding` do not cover this production composition. Native runs remain
after affected-lane final review; this brief authorizes owner B's implementation
and focused checks only under lead's release.

### Quota reservations belong to exact attempt IDs

Replace anonymous cyber timestamps with UUID-keyed charge records containing
the stable automatic attempt ID and conservative timestamp. Validate unique
UUIDs and exact correspondence with a charged Pending; equal timestamps are
valid for distinct IDs and never identify which charge to remove.

Before any possible fresh outbound retry, including a restart of a runtime
`submitting` intent with absent/prepared native ledger, first reconcile and
positively prove never submitted. Preserve the same UUID/action/options and
unique attempt count. Under the state lock, count other live charges, refuse
at 30, and replace or reserve only this ID's charge at current clamped time.
Persist before dispatch. Never reuse an expired pre-crash timestamp to permit a
new possible send. Quota exhaustion remains failed/manual; time alone cannot
rearm it. Capacity counts/deadlines retain their original behavior.

On accepted or reconciled acceptance, reanchor this ID's charge conservatively
to at least the receipt observation time before another chain step may send.
This upper bound on actual native acceptance prevents preflight/network delay
from expiring the charge too early. Commit the reanchor with the accepted-state
transition; duplicate receipt handling is idempotent and never creates another
charge. Unknown submitting outcomes retain pending exclusivity and only
reconcile, regardless of their age. Elapsed time is never proof of non-dispatch.
Positive unsubmitted preparation discard followed by a crash is recoverable:
the next pass proves absence and reserves the same ID again before sending.

### Final private schema and verification

Lead and owner confirmed this retry state is prerelease, unmerged, undeployed
and has no external consumer; prior instances are disposable fixtures only.
Define the **final private schema 1 directly**, retaining package capability
`turnRetryStateSchema=1`. Required nonzero epochs and keyed-charge validation
reject preliminary/missing-field shapes, anonymous charges, duplicate IDs and
inconsistent references fail closed. Do not silently default, migrate, reset
quota or add branch-iteration compatibility shims. Old-epoch retained snapshots
are valid records for reconciliation, not valid current dispatch proof. Fold
the final private shape into the original core commit as directed by lead;
preserve existing native schema 3 and unrelated persistent formats unchanged.

Required focused regressions before affected-lane final review:

- Exercise creation-less retained root and member recovery through the real
  resolver/worker path with native prepared, submitting and accepted receipts,
  not only direct `Controller.Step` or an already-accepted ledger. One member's
  unknown attempt cannot prevent reconciling another exact owned attempt;
  unrelated/foreign unknowns still prevent dispatch. Cancellation, cold and
  stopped holds never load or execute work.
- Settings intent during an active manual turn and after failure but before
  observation; model/effort and default/plan changes; RPC failure/unknown and
  restart after epoch persistence; queued auto-start racing the boundary;
  old empty-binding snapshots cannot be retrobound. New managed input/queue
  after the boundary can prove actual settings and retry; old queue/FIFO,
  Enabled, enrollment and quota are preserved.
- Crash after Begin before ledger write, native prepared state, restart beyond
  300 seconds with 29 or 30 other live charges, equal timestamps on distinct
  UUIDs, exact window boundary/backward-clock handling, lost accepted response,
  delayed receipt and duplicate reconciliation. At most 30 possible actual
  dispatches in a rolling window; unknown outcome never resends. Fail-closed
  decoding of preliminary shapes and valid final-shape restart must be tested.

Implementer1 owns source/tests/docs and final commit correction. A's public
Reconcile/DiscardPrepared/Continue contracts suffice. Long native tests remain
after final review; adjust the native recovery fixture to cover the resolver
boundary if its previous direct-controller flow would miss I1.

## Compatibility, rollout and recovery

No database migrations, Codex history edits, native protocol changes, client or
Terraform changes, vpsAdminOS node ordering or new public network API are needed.
The optional codex-web provider keeps existing embeddings source-compatible.
Older browsers can omit the new controls; server authority remains decisive.
Do not claim that an older runtime can safely manage in-flight retry records
merely because separate JSON files are syntactically ignorable.

Publish matching package state/transition support and enforce it when state
exists. Unsupported package generations fail closed before activation. Stop old
writers during generation change. Existing workspace package switches are
forward-only: recovery uses the same/newer compatible package, retained retry
state and exact submission receipts. Disabling automation is a control action,
not permission to discard uncertain records, reset enrollment, or delete history.

Ordered delivery: A library -> B runtime pin/integration -> matching downstream
workspace nested runtime and configuration channel -> reviewed/built composed
package -> authorized deployment. Preserve extension revision and unrelated
input graph. Host configuration selects its channel-managed `devWorkspace`;
workspace selects `inputs.vpsfree-dev-workspace.inputs.dev-workspace.url`.
Application remains in the user profile, not system pins. Run the existing
`bin/check-dev-workspace-deployment` on final graphs. Read installed coordination
guide before activation, build/copy first, then machine-only ownership for
aitherdev's confctl dry-activate/no-reboot switch and workspace profile switch.

Lead retains exact source/input graphs, full system/profile store paths,
deployed/final heads, aliases and acceptance evidence in rollout records.
Deployment does not authorize default-branch integration. Keep the physical
machine held until approved integrated feature lineage, user acceptance and
explicit release direction all exist. Session remains open.

## Acceptance and verification

Quick checks in each repository's Nix environment, before final review:

- A: protocol schema assertions for both variants; cold latest-state identity
  and unknown errors; idle-only continuation vs active/queue/request/newer turn;
  exact correlation/receipt/options identity; duplicate and uncertain requests;
  no steer/no implicit activation; optional-provider compatibility, origin and
  authorization checks; browser countdown/opt-out/cancel/reload behavior.
- B: fake-clock exact schedule/jitter/cap and rolling-window boundaries;
  30 possible sends including crashes, no reopening after quota expiration;
  defaults/enrollment/re-enable and old failures excluded; active enrollment
  race and missed notification recovery; duplicate observers/processes;
  persisted deadlines/quota/options and accepted/unknown restart outcomes;
  all admission paths' failed-turn settings provenance, compaction, steering
  and queue-execution settings; manual/Stop/team/settings/provider/lifecycle
  races; generation change and unsupported package-state contract;
  native-child exclusion; stopped/cold recovery holds and corrupt state.
- Run focused Go tests (`-mod=readonly` for dev-workspace), affected Ruby tests,
  browser contracts and syntax checks as declared locally. Do not use live
  registered workspace state as a test fixture.

After complete commits and quick checks: independent mandatory final review
includes full branch history, no-migrations conclusion, cross-repository
contracts, lock ordering, uncertain dispatch and enrollment semantics. Resolve
findings before long tests. Fresh verification utility owns long/uncertain
checks under the monitoring skill.

Long checks: disposable pinned App Server plus synthetic provider verify actual
terminal error shapes, nonempty continuation, preservation of plan/default mode,
model/effort/provider/policy, partial tool history, active-turn race/refusal,
native queue auto-execution and disconnect/restart receipt recovery. Generating
a schema does not prove server busy-turn behavior or settings inheritance.
If the pinned server can replace an active turn despite local idle checks,
report that material concurrency limit to lead before enabling dispatch; do not
promise atomic native compare-and-start that the protocol lacks.

The exact fixture payloads, owner boundaries, compile-only selectors and
post-review watcher commands are in [native-verification.md](native-verification.md).
That handoff requires named `go test -json` PASS evidence; missing or skipped
cases do not count as native verification.

Then full packaged flake checks, exact composed dependency/host graph checks,
authorized rollout and live acceptance of both lead/member controls, one new
synthetic retry, cancellation, opt-out, old-failure exclusion and continuity
after portal restart. Review/CI is not user acceptance.

Runtime behavior belongs in dev-workspace's portal guide; durable state,
upgrade/forward recovery and lifecycle fences belong in its operations docs.
Generic API/optional UI belongs in codex-web's reference. Individual rollout
evidence remains in this session. This brief is planning documentation, not an
assertion that implementation or tests have passed.
