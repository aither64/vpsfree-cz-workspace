# Initial mandatory review result: dev-workspace

Reviewed range:
`d20bb64c45db1d803fc3b7a8c2956049860d72dd..6f8a03eeb7d1a5771518a89dfe31fd5e985055f4`

Reviewer: retained `reviewer0`, `gpt-6-sol` with xhigh effort, read-only.

## Blocking

1. A queued continuity-repair timer can erase a failed older-page operation
   without explicit Retry. `scheduleHistoryRepair` checks `historyError` only
   when arming the timer. An independent newest refresh can create a gap and
   arm that timer while an older read is pending; if the older read then fails,
   the queued callback can still start repair and `runHistoryRead` clears the
   typed failure. The pinned history helper can create this gap without changing
   `repairVersion`, so stale-read rejection does not guarantee safety.

   Required correction: recheck `historyError`, `historyFailure`, the current
   gap, and repair cursor immediately before the callback starts repair; cancel
   or invalidate queued repair timers when recording a retryable failure. Add a
   held older read plus concurrent newest-gap update plus older failure test to
   prove that no repair or retry starts until explicit Retry.

## Important

1. The live wheel test starts at `scrollTop = 150`, already inside the
   200-pixel threshold. It covers the immediate path but not the deferred input
   gate that starts above 200 and crosses into the threshold after native
   scrolling.

   Required correction: add a real wheel case that starts above 200, crosses
   the threshold, produces exactly one older-page read, and does not cascade.

## Advisory

- No additional findings. Firefox and physical touch remain later smoke-test
  limits; widening the implementation is not required for this change.

## Clean lanes and branch conclusions

- General: only the Important verification gap above.
- Architecture and repetition: no findings.
- Scope and proportionality: no findings.
- Risk and compatibility: only the Blocking timer race above; no authorization,
  secret, persistence, API, schema, or protocol surface changed.
- The branch contains one focused commit and no obsolete committed approach,
  fixup commit, unused transitional path, or superseded history.
- No migrations exist, so there is no migration lineage or
  merge/release/deployment/external-consumer provenance to preserve.
