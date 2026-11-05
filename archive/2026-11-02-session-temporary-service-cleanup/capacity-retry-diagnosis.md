# Capacity retry diagnosis — 2026-11-03

Read-only investigation complete. The portal recognized this capacity failure,
but the long-running turn had already lost automatic-retry eligibility when its
bounded admission evidence was retired. This is the installed conservative
retention policy, not a wording/classification failure or CI failure.

## Exact evidence

- Selected package: `/nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0`.
  Its derivation identifies source
  `/nix/store/pw7ffd5bsg55wvcbqwc3vs91h9f1894i-source`; source citations below refer there.
- Bound session: `2026-11-02-session-temporary-service-cleanup`;
  lead thread `01a19ca7-6c3e-7a43-8896-186fa0d2d5bf`.
  `dev-session current`, both environment markers and retained roster matched.
- Failed turn: `01a19de7-008c-7513-b64f-9e649c4db784`, completed
  `2026-11-02T22:30:30Z`. Exact native `thread_turns.error_json` records
  `codexErrorInfo: serverOverloaded` and
  `Selected model is at capacity. Please try a different model.`
- Native history contains **74 distinct user-message client IDs** for that turn.
  The generic submission database retains **73 accepted steer receipts**, all
  bound to that exact turn. Its initial client ID remains in native history,
  without a current generic receipt. Prompt contents were not exposed.
- The retry record was enrolled, epoch 1, with `handled` equal to the failed
  turn, no chain/class/pending attempt, zero attempt/capacity counters and no
  cybersecurity charges. At inspection it held exactly **64 snapshots**:
  the latest 60 steers from the failed turn plus four newer-turn admissions.
  There was no aggregate executed proof for the failed turn.
- Session policy has capacity and cybersecurity enabled, an older active-turn
  enrollment boundary, and no lead-thread suppressions. The failed turn was
  neither the terminal enrollment baseline nor a disabled class.
- Exact native turn context: `gpt-6.1-sol`, effort `high`, mode `default`,
  approval `never`, execution `danger-full-access`, expected session CWD.
  Saved binding/provider is `codex-lb`; retained snapshots use epoch 1 and that
  binding. Roster lead settings agree. No settings were changed.

Native evidence came from read-only exact-thread queries of
`codex-homes/vpsfree-cz/{state_5,thread_history_1}.sqlite`, the exact lead rollout,
the socket-keyed `submissions/*.sqlite`, and this session/root's
`turn-retries/<workspace-sha256>/<slug>/<thread-sha256>.json` and
`turn-retry-policy/<workspace-sha256>/<slug>.json` below the user state root.
No other conversation's records or private message content were exposed.

## The skipped gate

`portal/internal/workspacecodex/turn_retry_proof.go:21–34` preserves native
`serverOverloaded`; the special older `other` message matcher is irrelevant here.
`turnretry/state.go:21` limits the record to 64 snapshots, also subject to its
byte budget. `workspacecodex/turn_retry.go:captureRetry` admits each managed input
using the current native turn, before sending it. `turnretry/state.go:478–529`
retires oldest accepted, turn-bound evidence when needed. Retiring a contributor
of the current turn calls `SuppressTurn` (line 435), which sets `Handled` and
removes that turn's cached aggregate proof. It does not guess the lost settings.

The 73 accepted steers alone exceeded the 64-snapshot bound while the turn was
active. The later failed-turn observation hits the handled-turn return in
`State.Observe` (line 268), before scheduling; `retryBackend.Prove` also refuses
handled turns. No retry UUID was created. This is not quota exhaustion or a
dispatch-time generation/admission refusal. Other execution gates still exist;
their hypothetical success cannot be established by this historical diagnosis.

The current `manual_input` cancellation reason reflects subsequent managed
input and is not the original cause. The ledger does not preserve the exact
first eviction timestamp or whether count versus byte pressure first triggered
it. Do not identify the 65th input as the exact first eviction. The persistent
handled watermark and retired evidence must remain intact.

## Existing behavior and recommendation

This policy is explicit in `docs/turn-retry-recovery.md:38–47`. Existing tests
`TestRetentionAcceptedOnlyAtomicSuppression` and
`TestRetryRetentionCachedProofSuppressedAndNewQueueEligible` preserve suppression
across restart/preferences/settings and allow a new independent turn with complete
proof to qualify. `TestRetryRetentionAggregateAndAutomaticAtCap` also reserves
space for the derived proof; 64 messages is not a promised safe operating limit.
Tests were inspected, not run during this investigation.

For future work, let natural milestones finish as separate turns instead of
continually steering one long turn. A later independent managed turn can retain
complete proof and qualify under the ordinary gates; this does not restore the
failed turn. No current turn interruption, manual continuation or replay is
requested by this report. Changing the model or toggling retry settings is not
a repair and is not authorized.

No classifier or scheduler correction is justified by these findings. Better
visibility of admission-evidence retirement is a separate possible product
improvement; preserving retry eligibility for larger turns would require its own
bounded-proof design. Neither is part of the service-cleanup delivery. Do not
raise thresholds, aggregate proof, migrate schemas or mutate retained records
under this diagnosis. No application/Git/settings/runtime changes, tests, builds,
native sends or lifecycle actions were performed.

## Accepted implementation follow-up — 2026-11-03

The preceding diagnosis describes the selected predecessor and its original
read-only scope. The lead subsequently accepted the compact-current-turn design
in design.md and released a separate capacity correction. Implementation is now
committed at `18432f0c8f86dec7405257f5dc244762d7a788ed`, after the three original
service commits. The runtime worktree and index are clean; no publication or
live retry-state change occurred.

Full state, workspacecodex and session package checks pass, along with the
retry web selection, host guards (12 tests/238 assertions), and the shipped
composer and browser API contracts. Exact commands, scoped earlier red/green and
large-input evidence, failure/invocation reconciliation, source NAR, all 676
source entries, unchanged nine-node input graph and four-commit inventory are in
[capacity-managed-turn-final-receipt.json](capacity-managed-turn-final-receipt.json).
The exact source is held by an ordinary indirect Nix GC root for active review.

Owning behavior and forward-recovery documentation is
`dev-workspace/docs/turn-retry-recovery.md`; the lead's prose pass and final
factual check are complete. Strict schema 1 remains the supported predecessor;
ordinary admitted saves write schema 2. There are no database migrations.
Previously handled failures remain handled. Final independent review and the
lead's subsequent integration/native proof gates remain; earlier EE3 pins and
artifacts do not certify this new source. All owned commands are settled.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/

### Narrow compatibility inventory correction

The reviewer identified that Ruby globbing could hide ordinary retry-state
directory inspection errors. The existing policy-state traversal now serves both
retry guards. Exact retained-record capability checks and policy wording are
unchanged; no payload is parsed or rewritten. Root/nested I/O refusal and
preparation/activation controls pass (15 tests/309 assertions).

The correction is folded into final fourth commit
`d1872f5defe01f02e05ac6ce083541789f1222f6`; all three service commits are unchanged.
Reviewed `18432f0c` and exact tested fixup `6adec2f8` refs/source evidence remain
retained. [The correction receipt](capacity-managed-turn-inventory-fix-receipt.json)
binds the two-file delta, red/green evidence, tree equality, unchanged full input
graph and freshly hashed/rooted exact source. The source/Git lane is returned to
the lead for direct inspection; no publication or deployment occurred.
