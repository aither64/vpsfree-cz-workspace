# Review remediation

Original reviewer: /root/archive_final_review, catalog Astra/xhigh. See
review-report.md. All findings accepted for correction, none waived.

R1: stream Git's decoded exact saved tree/commit objects and compare each raw
Git object hash before removal. Missing/corrupt blobs before capture and before
removal refuse while retaining working bytes. No full-history fsck or per-file
Git subprocess. Stream is bounded in memory.
R2: create Git recovery targets with --no-checkout, reconstruct raw files on each
owned incomplete retry, then apply saved permissions and index. Completed receipts
continue to forbid replacing operator edits. New partial registered-checkout test
also changes smudge configuration and checks exact bytes/index.
R3: 60-second deadline across attempt commands and tracking lock waits, five-second
TERM grace, separate ten-second owned-index cleanup allowance. Normal hooks stay
enabled. Hanging-hook/concurrent-revive test proves pending receipt, released locks,
coalescing and unrelated staged-byte preservation.
R4: running worker clears observer finish time; terminal worker result replaces it.
The restart test persists/reloads the receipt and checks the actual final timestamp.
Its fake systemd-run now publishes argv atomically; the earlier failure read a
partially written fixture file, not worker behavior.

review-final-isolated-ruby.log: 8 runs/301 assertions pass with global and system
Git config disabled. review-fixes-go.log passes stored-receipt restart checks.
The first corruption fixture attempted to change a read-only disposable Git object;
it now makes that fixture object writable before corrupting it. All four fault
paths pass. No production permission policy changed.

CI38931338795 failed the filter fixture because its disposable bare clone had no
Git author identity; local global config masked that omission. Declare identity
in the disposable fixture. ci-2d7-failure.log retains evidence. This is a fixture
isolation fix, not a blind rerun.

Configuration preserves the other initiative's reviewed DeepSeek correction
9721c331. Runtime pin streams are consolidated after final runtime commits. No
new persisted formats or application database migrations are introduced by fixes.
Relevant re-review is needed because streaming raw restoration and deadline
propagation add implementation behavior beyond the original review.

Residual: completed supervised archive units stay in the user manager until it
restarts or an operator stops them. They do no work after exit. A future bounded
collector should stop exact units only after a durable terminal portal receipt
and no active matching lifecycle journal. This follow-up is not needed for the
archive's recovery or completion proof and is not a generic task framework.

Follow-up review(review-followup-report.md) accepts R1-R4 and history/format lineage.
R5 requires file type matching: implemented the exact narrow full-copy fallback.
review-narrow-fixes.log passes2runs58assertions, including core.symlinks=false,
regular-file restoration, exact index/bytes and unchanged external sentinel mode.
No new design or format. Lead directly verified under mandatory-review step9;
no further independent turn is required. Final direct delta is review-narrow-fix.diff.

CI38934477747 failed only its hook-start marker. The fixture used /usr/bin/env bash
instead of the hermetic suite's established /bin/sh. It now uses /bin/sh, has
startup/error diagnostics and a five-second test deadline rather than two seconds.
Narrow isolated hook regression passes. Final package check must verify hermetic
execution; no blind CI rerun was requested. Full logs:ci-73bc-failure.log.

Final exact acceptance heads are in acceptance-heads.json. Consumer pin refreshes
are generated-only, preserve all other locked inputs and are consolidated one per
stream. Final composition check passes the same runtimeb8fc9914 in both consumers.
