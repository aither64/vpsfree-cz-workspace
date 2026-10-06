# Codex web mandatory review result

## Review identity

- Reviewer: retained `reviewer0`, GPT-6 Sol, xhigh, read-only.
- Initial reviewed range: `e92dd887c888d5a9f50c70febc714f875cb44378..ef1173767aacd584d7c38e84878715bd1c55767a`.
- Risk and lanes: high risk; general, architecture and repetition, scope and
  proportionality, and risk and compatibility.
- Scope: both committed `codex-web` changes plus the uncommitted downstream
  portal consumer. This was a pre-push review, not the final branch-readiness
  gate.

## Findings

1. **Blocking:** `conversation/assets/conversation.js` clears all retained
   transcript history on `transcript_reset_required`. The next newest-page
   refresh therefore shows only that page and has no retained range to repair.
   The downstream portal repeats the behavior. A latest active turn completing
   can legitimately trigger this reset.
2. **Important:** `readTranscriptPage` checks `expectedThreadId` on page
   responses but not after authorized fallback to `/thread`; the documented
   cross-thread invariant does not hold with an older server.
3. **Important:** the portal acknowledges durable sends against only the
   arriving page instead of the complete retained transcript. If an older-page
   acknowledgement races with another acknowledgement, the receipt can remain
   pending indefinitely.

## Positive conclusions and residual risks

- The page handler retains read authorization and target verification; the
  reviewer found no direct data exposure.
- Shared history helpers are used by the downstream portal and the two commits
  have coherent scope.
- There are no migrations in the reviewed diff.
- Exact Codex 0.155.0 cursor behavior, concurrent appends, receipt races, and
  the planned latency and metadata CPU benchmarks remain verification gaps.

## Reconciliation

- All three findings are accepted. They must be corrected and covered by
  focused tests before push.
- Rerun the affected general and risk/compatibility lanes after the corrections;
  include architecture if the shared helper contract changes materially.
- The fixes were folded into unpushed browser commit
  `056fe002899b5c42447d1c35a68ae8b3a85ff503`; the rerun is pending.

## First rerun

- Reviewer: the same retained `reviewer0`, Sol/xhigh, read-only.
- Lanes rerun: general, architecture and repetition, and risk and
  compatibility.
- The legacy fallback identity finding is resolved.
- The portal retained-history acknowledgement race is resolved in the
  uncommitted consumer.
- **Blocking remains:** reset repair can close a disjoint replacement while
  dropping an intermediate authoritative page, and a replacement that removes
  an item can leave the stale retained item visible after repair. Reset
  traversal must preserve the old display while accumulating an authoritative
  replacement range, then replace the covered retained range only when
  continuity or end-of-history is proven.
- Live cursor behavior, mounted reset recovery, metadata rebuild cost, and the
  latency benchmark remain verification gaps.

## Second correction

- The reset recovery model was replaced at amended head
  `313f4adbfdafed04f6ff00cf0a8b4ea9f77db49a`.
- Old rows remain visible while a separate authoritative fresh range is built.
  Completion replaces the covered range only after reaching the retained oldest
  key or end-of-history.
- Regression contracts cover disjoint replacement, deletion from an overlapping
  lineage, concurrent newest-page updates, and stale in-flight repair rejection
  in both the generic mount and portal consumer.
- The second focused rerun is pending.

## Second rerun

- The original Blocking reset-reconciliation defect is resolved. Both the
  disjoint-lineage and deleted-item reproductions pass.
- **Important:** completing reset recovery does not advance `repairVersion`, so
  a response already in flight can pass the mounted-interface version guard and
  overwrite fresh rows after completion. The reviewer reproduced the race.
- The focused Codex and portal browser contracts pass. Delayed live responses,
  metadata rebuild cost, exact live cursor behavior, and latency acceptance
  remain open.

## Third correction

- Reset completion now advances `repairVersion` at amended head
  `f16fcff6fa9a5476545c98b50ecf1c2db04bf602`.
- Regression contracts cover completion through both a repair page and a newer
  newest-page response. The narrow reviewer confirmation is pending.

## Final pre-push confirmation

- The Important completion race is resolved at
  `f16fcff6fa9a5476545c98b50ecf1c2db04bf602`.
- Reset completion advances `repairVersion`; both generic and portal mounted
  readers reject responses and errors captured before that completion.
- The reviewer reproduced the former stale-response race and confirmed the
  authoritative entry remains intact. No new finding arose.
- All Blocking and Important findings from this pre-push review are resolved.
  Delayed live requests, exact live cursor behavior, metadata rebuild cost, and
  portal latency remain rollout verification gates. Final branch readiness is a
  separate later review.
