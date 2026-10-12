# Risk and compatibility review

Reviewed directly, using commit objects rather than later working-tree changes:

- codex-web `269962e..bba2ae1`
- dev-workspace `bcbaf82..774c208`
- vpsfree-dev-workspace `c4df383..d0ebe39`
- workspace `e0d3dee..bfc80f2`

## Blocking

1. **A receipt accepted immediately before rollback can permanently shadow a valid session created by the previous package generation.** Commit `5bcf254`.

   `portal/internal/web/creation.go:129-136` persists the receipt before starting the worker, leaving a legitimate window where no CLI `.request` binding exists. The preceding generation ignores receipts and creates sessions through the legacy path (`bcbaf825:portal/internal/web/server.go:865-926`). After rolling forward again, `portal/internal/web/creation_store.go:112-143` restores the receipt as paused, and `portal/internal/web/server.go:746-750` renders the creation page before attempting `session.Find`.

   The valid session cannot satisfy `proveCreation`, which requires receipt-bound evidence (`creation.go:250-296`). Retrying cannot recover it: `libexec/dev-session:2832-2854` rejects existing session or journal state when the `.request` binding is absent.

   Scenario: accept receipt → stop before CLI binding → roll back → create the same slug with the supported old package → roll forward. The canonical session page remains hidden behind an unrecoverable retry state. This violates the packet’s requirement that rollback leave additive state harmless.

   Add an explicit mixed-generation conflict/reconciliation state that neither adopts an unrelated session as receipt completion nor shadows the valid session, with a head→base→head test beginning before CLI binding.

## Important

1. **Completed creation receipts have no retirement lifecycle and impose a 512-session lifetime ceiling.** Commit `5bcf254`.

   `creation.go:101-105` permanently reserves every recorded slug, while `creation.go:121-122` rejects all new creation after 512 records. `creation_store.go:112-145` reloads every terminal record; no path removes a receipt when it becomes ready or when its session is deleted.

   Consequently, a long-lived portal eventually cannot create sessions. Deleting a browser-created session also does not release its slug: the same request reuses the stale ready receipt and a different request is rejected. Introduce bounded, lifecycle-aware terminal retention without weakening duplicate-prevention guarantees.

2. **A recoverable fork is stranded if its source is archived or deleted after the destination journal is durable.** Commit `5bcf254`.

   Every retry reopens and requires a currently active source (`creation.go:62-92,378-385`). The CLI repeats that check at `libexec/dev-session:1000`, before loading the existing fork journal at line 1009 or entering recovery at lines 1030-1038.

   This conflicts with the journal recovery design: the journal already contains the exact source slug/thread, and recovery uses that recorded identity without rereading the source manifest (`libexec/dev-session:1014-1042,1201-1267`). The preceding generation likewise recovers from the journal before consulting the source (`bcbaf825:libexec/dev-session:975-1024`).

   Test interruption after receipt binding and fork-journal publication, followed by source archive/delete and retry. Once the exact destination journal is established, recovery should use its authority rather than require unrelated source availability.

3. **Large supported comparisons can silently lose rename metadata.** Commit `6dcf756`.

   `portal/internal/repository/review.go:29` permits 5,000 changed files, but `review.go:318` invokes Git rename detection with `-l1000`. Comparisons with enough rename candidates therefore skip exhaustive detection and report additions/deletions instead of renames. Git can still exit successfully, and `review.go:108-138` discards successful-command stderr, so the API presents the degraded result without warning.

   This contradicts the required rename preservation. Either keep rename detection exhaustive within the declared limits or explicitly reject/report degraded comparisons.

4. **Activity persistence has no compaction lifecycle and eventually disables recording.** Commit `bba2ae1`, consumed by `774c208`.

   The ledger retains all per-thread intervals and request boundaries (`codex/activity.go:54-67`). Resolved requests are marked but never removed (`activity.go:366-390,409-415`), and archived/retired portal workers do not prune their thread history (`portal/internal/web/activity.go:87-129`).

   Every reconciliation persists the complete ledger (`codex/activity.go:451-491`), while each session worker reads every 5 or 30 seconds (`portal/internal/web/activity.go:132-169`). Persistence marshals and fsyncs the whole file, then refuses the next checkpoint exceeding 64 MiB (`codex/client.go:26`, `codex/activity.go:180-226`). With no compaction, subsequent checkpoints continue failing and timing coverage becomes unavailable until manual state removal.

   Define retention/compaction semantics for completed requests and retired threads, and exercise near-limit restart and continued-recording behavior.

## Advisory

1. **One long history read serializes activity reads for every session on the shared observer client.** Commits `bba2ae1` and `774c208`.

   `codex/turn_history.go:75-99` holds one client-wide `turnHistoryMu` across every paginated App Server request, potentially up to the 100,000-turn limit. The portal shares one observer among all session workers (`portal/internal/web/activity.go:42-54`), each with a four-second read context (`activity.go:156-165`). Mutex acquisition is not context-aware, so cold-start reads for unrelated sessions queue behind the longest history.

   Prefer per-thread cache locking or keep network I/O outside the global cache lock. Add a concurrent many-session/long-history test.

## Boundary assessment and remaining gaps

Within the stated trusted-local-operator boundary, I found no remote authorization bypass, arbitrary browser-controlled Git ref/path execution, Git mutation, activity-persisted prompt/answer content, unsafe external activity link handling, Codex-version mismatch, or inconsistent downstream pin.

No tests were run during this read-only review. Remaining gaps include:

- Head→base→head creation recovery and rollback.
- Receipt retirement, deletion/recreation, and the 512-record boundary.
- Fork-journal recovery after source archive/delete.
- Rename-heavy comparisons beyond Git’s configured rename limit.
- Multi-session history contention and activity-ledger compaction/near-limit recovery.
- Planned packaged Nix, VM, live App Server, real portal browser, upgrade, rollback, and deployment acceptance.