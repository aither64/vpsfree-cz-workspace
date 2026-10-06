# Lost root helper response: bounded recovery correction

Accepted correction, implemented and independently reviewed at runtime924c0ec:
adopt the proven live, unmaterialized root without resuming it. SDK missing-thread
recognition remains strict. The diagnosis below supersedes the earlier hypothesis
that requireMissingCreationThread rejected a new missing-thread error form.

The original fault root is now unavailable and remains untouched. The fresh
corrected-provider continuation passed actual host preflight, all four independent
review lanes and one watched real run. Lost-response retry retained its exact new
root; partial-team retry retained the root and completed member. Both sent one
goal and passed model, progress and final-evidence checks. This is mixed-provider
fault verification; full-package activation and canary are separate gates.
[Actual results](verification-corrected-faults.md),
[preparation](verification-corrected-fault-preparation.md) and
[root observations](root-observation.md) record the evidence and limits.

## Observed failure and source contract

The original candidate `0klh7dhca2dwyfwsz0m67pbjj2nml70d` at runtime `8ae46f9`
passed all five sequential Full-team measurements: 6.121214866638184,
6.401348829269409, 6.332730054855347, 6.500733852386475 and
6.4283411502838135 seconds. Median **6.401348829269409**, maximum
**6.500733852386475**. The parent reports one goal, model completion and no tools
for each; the retained result confirms the five durations and timing pass.
These remain measurements of that exact revision, not new-candidate timings.

The real `root-response` wrapper received successful root-helper JSON for
`01a0fe38-b8e0-76c1-b8f0-fd84783964a5`, retained its ID, withheld stdout and
returned failure before Ruby could save it. Receipt
`a4ad299484ab1972eb099a9b08793976cc442dc0ce8bae6fa768bba282e37634` then failed
on retry attempt 2 after loaded/indexed discovery and a complete filesystem
scan (11,162 ms for that stage). The exact diagnostic was
`Codex RPC -32600: no rollout found for thread id 01a0fe38-b8e0-76c1-b8f0-fd84783964a5`.

Read-only noncredential evidence under `/tmp/pcp-oct02-a` confirms the creation
journal is schema 3 / `creating`, the manifest is schema 2 / `creating`, has no
`thread_id` key, and has `initial_goal_sent: false` and
`initial_goal_attempted: false`. No roster exists for this fault. No active or
archived rollout filename contains that root ID. Filename absence alone is not
authority to replace a live thread. No rollout content or credentials were
read during this diagnosis.

| Retained artifact | SHA256 observed during diagnosis |
| --- | --- |
| `result.json` | `4d7c81f9b0acec3a6506cad62b1f4fad5c0657b9b533c9af29bfb06c14044e39` |
| `fault.json` | `b99dbbec2a6b4a49d981556fa845f819ad69ed4f0c59543ea743e2c35328eabf` |
| `creation-root-loss-before-retry.json` | `924211b540dbe4a819fbeae13f5f570ad581fee18817850941ac5f3419bd2ed0` |
| Fault receipt, `state/portal/workspace-e015aa0dc07aa15b/creations/2026-10-02-creation-root-loss.json` | `bd037b9aa67a7e14a07636c7c506113578ce4fddc0b9204289c28e405c313832` |
| `workspace/worktrees/.locks/2026-10-02-creation-root-loss.creation.json` | `41d668a80d47352d894fa48ba03da7ba9efd43aab91014bf9044e6c56dad39e5` |
| `workspace/work/2026-10-02-creation-root-loss/portal.yml` | `758e7c86cfa45d433237351dc45a06e5ab5cbb0bec54b0f21413b8c98720227d` |

Selected source was inspected directly at
`/nix/store/kdq60x8qayhgkx6d3zbfdgw1i7dqp9q5-source`:

- `codex-rs/app-server/src/request_processors/thread_processor.rs`,
  `read_stored_thread_for_read` / `read_thread_view` (around 2885–3005): exact
  missing-rollout storage errors become no persisted entry. A loaded thread
  still yields live metadata; otherwise the response is `thread not loaded: ID`.
- The same file, `resume_running_thread` (around 4277–4330), reads stored
  metadata **even when `thread_manager.get_thread` succeeds**.
  `thread_store_resume_read_error` (5916) maps missing storage to the observed
  `no rollout found for thread id ID` invalid-request error.
- `codex-rs/thread-store/src/local/read_thread.rs` produces this error when no
  stored thread/rollout can be resolved; it does not inspect live thread ownership.

The corresponding primary release sources are
[thread processor](https://github.com/openai/codex/blob/rust-v0.160.0/codex-rs/app-server/src/request_processors/thread_processor.rs),
[local stored-thread reader](https://github.com/openai/codex/blob/rust-v0.160.0/codex-rs/thread-store/src/local/read_thread.rs)
and [RPC error codes](https://github.com/openai/codex/blob/rust-v0.160.0/codex-rs/app-server/src/error_code.rs).
Line positions in the selected store source are the local references above.

The runtime's `RecoverCreatingThreadWithOptions` currently calls
`ResumeThreadWithSettings` for every nonzero-policy candidate, including one
that `HistoryMaterialized` has proved unmaterialized. The root policy is always
nonempty. In this fault the manifest supplies no recorded ID, so
`requireMissingCreationThread("")` returns immediately without an RPC. Together
with the completed discovery stages and selected read semantics, this identifies
the resume branch as the failure path; no new RPC was issued to diagnose it.

## Error ownership and compatibility

| Existing form/interface | Meaning and treatment in this correction |
| --- | --- |
| SDK raw `-32001` / exactly `thread not found` | Existing compatibility recognition remains. `ReadThreadMetadata` wraps it in `ThreadNotFoundError{ThreadID: requestedID}`. The raw form contains no ID; the typed wrapper supplies request binding. |
| Typed `ThreadNotFoundError` | `IsThreadNotFound(err, requestedID)` requires exact ID equality. Preserve it. |
| Selected `-32600` / exactly `no rollout found for thread id ID` | Missing persisted rollout; can describe a still-loaded root. Preserve as an error, including exact-ID matches. Never classify arbitrary `-32600`, substrings or a different ID as disappearance. |
| Selected `-32600` / `thread not loaded: ID` | Not accepted by the current missing-thread predicate. Keep its conservative refusal in this unit; restart/deletion semantics need a separate proof before changing it. |
| Timeout, transport, permission, malformed metadata or other RPC error | Uncertain; refuse. No catch-and-replace fallback. |

The shared predicate lives in `codex-web/codex/client.go` and is used by
`ReadThreadMetadata`. Runtime consumers are
`portal/internal/workspacecodex/client.go:requireMissingCreationThread` and
`portal/internal/teamruntime/runtime.go` in `deleteUniqueFreshMemberLocked`,
`removeLocked` and `clearPreviouslyRetiredMemberAttempts`. Broadening it would
also change lost-delete-response, removal and prior-retirement cleanup proofs.
Those consumers and the SDK protocol contract remain unchanged. The fixture
using `-32001` is not evidence that real 0.160 emits that form after restart;
the existing conservative restart gap remains explicit, outside this fault fix.

## Implementation boundary and invariants

1. In `dev-workspace/portal/internal/workspacecodex/client.go`, change only the
   successful unmaterialized-candidate return condition in
   `RecoverCreatingThreadWithOptions`: remove the empty-policy qualification.
   Keep the materialized candidate's `ResumeThreadWithSettings(... Policy ...)`
   path. Update the adjacent resolver comment to distinguish retaining the
   original live policy from refreshing a materialized root's policy.
2. Keep loaded/index/full discovery, bounds, errors, ambiguity, wrong cwd/source,
   fork rejection, exact roster/project exclusions and retained-root protections
   unchanged. Complete successful filesystem discovery still precedes adoption.
   `HistoryMaterialized` must still prove exact ID/cwd, a valid missing rollout
   path, application source, non-ephemeral paginated history, idle state, empty
   preview and explicitly empty turns. Errors never enter the early return.
3. Policy preservation comes from the original successful `thread/start`:
   `rootThreadSettings` / `LeadThreadPolicy`, SDK `settingsParams` /
   `applyThreadPolicy` / `applyThreadMCP`, and the supplied session environment.
   The trusted creation journal freezes the accepted preset/settings before
   that call; recovery does not resolve today's catalog for an existing root.
   Adoption retains this live configuration. It does not attest arbitrary
   external changes or repair a foreign thread's instructions. A changed or
   unprovable creation identity remains a refusal. Do not use
   `thread/settings/update` as an invented policy replacement: its selected
   contract does not replace thread-level developer instructions/MCP/environment.
4. Ruby `libexec/dev-session` keeps the existing manifest write and exact
   initial-goal attempt handling. `EnsureInitialMessageWithOptions` already
   supports direct `turn/start` on a proven fresh thread only when explicitly
   allowed, then verifies persisted matching history. It does not reapply thread
   policy. An already-attempted, still-unmaterialized goal continues to refuse.
   No reset of journal, goal digest or attempt state belongs to this correction.
5. Update owning `docs/dev-sessions.md` to explain adoption before materialization
   versus resume afterward. No helper flags, SDK capability, schema, migration,
   root project, fork behavior, team order or progress transport changes.

This is a consequential refinement of design step 6: an unmaterialized root
retains its start-time policy rather than attempting to restore it through an
unsupported resume. It was reported to the native lead; parent owns acceptance.
Old readers can load every resulting record. Rolling back restores the old
failure on this rare retry, without a format rollback. SDK `UseStateDBOnly`
and its default/omission behavior remain unchanged.

## Focused checks for the implementer and reviewer

- Replace the false assumption in
  `portal/internal/workspacecodex/client_test.go:TestRecoverCreatingThreadRestoresPolicyBeforeFirstRequest`.
  Model a loaded-only, unmaterialized root with a nonempty frozen policy;
  require complete filesystem discovery, then the same returned ID and **no**
  `thread/resume`, `thread/start` or settings resolver call during adoption.
  Cover both an empty manifest ID after lost helper JSON and an exact recorded ID.
- Keep a separate materialized-owner fixture proving the existing policy and
  environment resume request, with no saved model/effort replacement. Cover
  original start-time lifecycle+lead instructions, MCP settings and environment
  using SDK/runtime request fixtures; a same-ID assertion alone is insufficient.
- Exercise the Ruby/helper boundary and existing initial-message fixtures:
  original start succeeds but its JSON is lost, retry adopts, team bootstrap
  completes, and the initial request occurs once. Already-attempted unsaved
  history must refuse; matching materialized history must not submit again.
  The owning Ruby files are `test/dev_session/session_recovery_test.rb`,
  `test/dev_session/session_initialization_test.rb` and
  `test/dev_session/agent_team_creation_test.rb`; extend only the cases needed
  for this boundary, using their existing support helpers.
- Preserve negative cases for duplicate/hidden filesystem roots, wrong ID/cwd/
  source, forks, materialized different roots, absent or inconsistent history
  fields, active turns, unreadable paths, incomplete scans and unknown RPC errors.
  Include retained partial roster, exact ready-member exclusion and unchanged
  member IDs; no missing-root replacement when a roster remains.
- SDK `codex/client_test.go` may add focused negative assertions without changing
  production SDK: exact/different-ID no-rollout messages, other `-32600` and
  `thread not loaded` remain false; typed wrong-ID remains false and the existing
  legacy fixture stays true only through its current contract. Do not turn the
  observed resume error into a positive missing-thread fixture.

Use the affected repositories' Nix environments for focused SDK/runtime Go and
Ruby checks. Parent owns commits, whole-branch inventory and independent review
before longer real-App-Server verification. This design task ran no test suite,
integration, history RPC or model request; source/metadata checks are diagnosis,
not evidence that the application correction passes.

Preparation verification: 16 read-only assertions passed for the selected
source branches, existing SDK/initial-turn guards, document links, all six
private evidence hashes, five retained sample values and failed attempt 2.
The scoped `git diff --check` passed. These checks neither launched the
application nor changed private files. The parent retains tracking-phase and
implementation ownership.

## Historical same-root continuation proposal, superseded

The instructions in this section depended on the old root remaining provably
live. Subsequent observation failed that prerequisite. The original driver was
never executed; the separately reviewed fresh cases above supplied acceptance.

Preserve the current result, all five sample artifacts/events, first failed
receipt snapshot, attempt-2 receipt, journal, manifest and disarmed fault record
outside Git before later writes. Retain every earlier continuation claim and
service. A future bounded driver must validate this exact diagnosed fixture,
the parent's actual process/socket proof, unchanged catalog/settings, no root
goal attempt and no member-fault creation. Make one new exclusive preservation
claim only after the parent authorizes and reviews that concrete driver.

For the existing root fault, use the ordinary retry endpoint with the **same**
receipt ID and expected attempt **2**, requiring attempt **3** on acceptance.
Do not call `create(..., "creation-root-loss", ...)` again or rearm its fault.
The original recorded root must remain live and be recovered with that exact
ID; replacement is a failure of this particular continuation even though other
recovery cases have a conservative replacement path. Run normal final receipt,
manifest/roster, progress/stage, exact-one-goal, assistant/completion and no-tool
checks. Normal runtime may submit the previously unattempted root goal once;
the driver must not submit a goal directly or resubmit any previous sample goal.
Record retry elapsed time separately; it is not a sixth timing sample.

Then call the existing `create(..., "creation-member-loss", ..., "member-progress")`
once, using its original real-helper fault boundary and retry. Require a proper
partial roster (at least one ready and at least one unfinished), the same root
and all previously ready member IDs, complete discovery excluding only validated
roster members, one root goal and all normal final evidence. A missed partial
boundary remains inconclusive, never a pass. Do not call
`finish_creation_samples` again: that repeats five names and the root fault.
Reuse `http`, `wait_creation`, `ready_evidence`, `wait_model`, `progress_evidence`
and the existing member-fault `create` owner; no generic continuation framework.

**Parent-owned operational prerequisite:** `workspace-host switch` calls
`require_no_unfinished_lifecycle_operations!`, which refuses this creating
journal and failed schema-3 receipt. An ordinary switch cannot be assumed to
refresh this fixture while it is stuck. Restarting the App Server would also
destroy the very unmaterialized-root case being verified. Establish a supported,
explicitly reviewed corrected-helper execution boundary before any retry; this
design does not authorize helper/profile swapping, forged registration,
clearing claims, marking ready, cancelling or bypassing generation checks.
If no such boundary exists, preserve the stuck fixture and report that limit;
the exact retained-receipt fault cannot yet be claimed verified.

Normal release sequencing remains runtime correction and focused checks →
review → exact consumer/configuration pins and builds → guarded fault checks →
parent-owned deployment and canary. SDK need not change unless adding its
negative tests. Retain original timing revision and corrected fault revision
separately; no timing rerun is required solely for this isolated recovery branch.
Changes to fresh creation or common timing paths would invalidate that premise.
Recovery completion, the unattempted member fault and deployment remain pending.

The parent accepted the source correction and assigned a follow-up boundary
assessment. [verification-fault-preparation.md](verification-fault-preparation.md)
now prepares an existing-adapter compatibility check: old selected Ruby and
services, with only the two fault slugs' `thread create` calls dispatched to an
explicitly reviewed corrected Go binary. It preserves every original runtime
argument and generation check. This resolves the test-provider execution
boundary without a package switch; it does not authorize production recovery
or replace full-package activation/canary verification. The new finite driver
and its focused evidence remain subject to parent review and actual preflight.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-02-portal-creation-performance/>

## Subsequent read-only root observation and accepted fresh cases

**Resolved at 2026-10-02 21:24:27 UTC:** the parent's pinned SDK 4c probe
succeeded for loaded enumeration (six IDs, target false), while explicit read,
turns-list and idle checks each returned exact-target `thread not loaded`.
Original process identities remained unchanged. No current root ownership,
idle or materialization proof exists. The old receipt/root/journal must remain
untouched; retry, replacement, repair and profile switch are not authorized.

The parent accepted fresh exact fault slugs
`2026-10-02-creation-root-loss-corrected` and
`2026-10-02-creation-member-loss` in the retained isolated runtime. The
[prepared new driver](verification-corrected-fault-preparation.md) uses the
reviewed existing adapter boundary with frozen corrected provider `xl9…`
(runtime `924c0ec`), a new exclusive preservation claim and separate fault/result
files. It reuses the original normal creation/retry/acceptance helpers and
requires exact new-root/ready-member identities. No old-root replay, goal
resubmission or repeated timing sample is included. Actual host preflight,
affected-lane review and one watched run subsequently passed. This fresh case
proves the correction against a real lost helper response; it does not prove
that the earlier unavailable root can be repaired. The
conditional alternatives below are historical, superseded by this choice.

The parent ran old candidate `0kl`'s public `thread observe` against the retained
socket, exact cwd and root. It returned `-32600: thread not loaded: <exact ID>`.
No fault continuation claim or retry followed. This is not proof of deletion or
permission to replace the root. The prior same-root driver is held pending a
method-labelled observation report.

`ObserveThread` first calls `ListThreadActivity` → SDK `ReadThreadMetadata`
(`thread/read`), then `RequireThreadTurnsIdle` (`thread/turns/list`, with a
metadata-read fallback on error). Either stage can propagate this bare error.
The selected source can produce it in both `read_thread_view` and
`load_thread_turns_list_history`. Later pending-request and queue errors acquire
their own prefixes. The aggregate failure therefore does not identify its RPC.

Prepare a fixed-target `root-observer/` Go prototype pinned to SDK
`4c170393a96ed0a6ac2e43488d073f6fcab36132`, using its exact published module
version and existing consumer checksums. Per the parent's explicit clarification,
the ordinary SDK client may use its public `LoadedThreadIDs` API; close that
connection afterward. A separate `ObserverOnly` client performs explicit
`thread/read(includeTurns: false)`, metadata-only turns-list and SDK idle checks.
SDK4c's observer allowlist excludes loaded-list, so do not weaken it or add a
second wire implementation. No resume, start, subscription, queue/turn mutation,
activity recorder, credential access or rollout payload read. Output only the
target's membership, identity/cwd/source and idle/materialization metadata,
method-labelled sanitized errors and timestamps. Parent builds/runs/freezes the
actual host report; preparation is not a runtime observation.

If that report proves the root remains loaded and exact, fresh/unmaterialized
and idle, the parent can reassess the original same-root driver after review.
If it is consistently not loaded and metadata reads fail, leave its old journal,
receipt, claims, faults and five measurements intact. Do not retry or authorize
replacement from those errors. The smallest conditional acceptance option is
two **new, absent, explicitly frozen fault slugs** in the retained isolated
runtime, using the reviewed corrected-provider adapter for those names only.
They exercise a new real lost-helper-response plus its immediate same-root
retry, then the existing partial-member fault and same-member retry. Preserve
the old result/fault data before the new case writes; never reuse the old slug,
claim or receipt. Keep all goal/model/no-tool/progress/roster checks and label
the result old-consumer/new-provider compatibility, not full-package activation.

If the retained runtime cannot safely host independent new slugs through its
normal interfaces, use a separate fresh final-package fault-only fixture with
its own public registration/profile/state/sockets. That option needs parent
authorization and a concrete prepared driver after the observer result. It
does not copy production history, reset old state or repeat the five timing
samples. Neither option is prepared for execution or accepted yet. Conflicting
loaded/read/turn observations remain uncertainty, not an ownership inference;
do not expand SDK error classification or repair policy to make a case pass.
