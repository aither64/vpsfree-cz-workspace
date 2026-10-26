# Independent review resolutions

Preserve review.md and reboot-review.md as their reviewers wrote them. Their
exact reviewed ranges remain in those reports. The final source is library
8b60554bc10c2a6bcbf9732a8b77ad959c317036; final downstream pins are being generated.

- Important, original general review: mounted retries could borrow newer draft
  attachments for an originally attachment-free send. Fixed by selecting the
  retained empty array whenever a retained attempt exists. Mounted-browser
  regression fails before and passes after the correction, retaining UUID,
  original text, empty attachments and the newer draft/upload.
- Advisory, original general review: single-attempt SQLite timing lacked the
  attempt ID. Fixed by filling the sole scoped ID; genuinely thread-wide events
  retain no attempt identity.
- Blocking, affected risk review: an unreferenced durable backup could be ignored
  before an import journal committed, publishing an empty ledger after /run was
  lost. Fixed exactly as requested: no-source empty initialization refuses when
  this database's backup prefix remains. It neither guesses a snapshot nor
  publishes fences/readiness. Regression preserves backup bytes and verifies no
  authoritative journal. A Go overlay with f391c5e's migration code fails the new
  regression; the final full Go suite passes (codex 23.1 seconds).

The final guard is a narrow implementation of the reviewer's explicit correction,
not a new design or expanded public contract. Mandatory-review step 9 requires
focused inspection/checks rather than a redundant confirmation turn. The parent
verified the guard, failure-before/pass-after evidence, documentation and final
history folding. No schema version or migration from an intermediate unpublished
implementation is retained or supported. No reviewed source was deployed yet.
All three corrections are folded into owning commits. Whole-branch history and
migration lineage conclusions from both reviews remain applicable, with exact
final range comparisons and pin proof required before readiness.

The prepared one-off original-attempt operation was inspected by the affected
reviewer. It remains unexecuted on live state. It follows the reviewed exact
row/claim, persistent backup and transaction requirements. The target has advanced,
so the planned follow-up is the normal stale-plan recovery endpoint, not a new
implementation send. Native acceptance is rechecked immediately before recovery.


## Affected baseline review: plan source admission

The retained reviewer found an Important risk/general issue: changing the shared
source verifier to wait also changed accepted plan creation, which calls it while
holding destination/provider creation admission. The planned no-destination-lock
boundary was proved only for forks.

Resolve by removing that unintended expansion: verify_creation_source! defaults
to nonblocking, as before; only the fork caller explicitly opts into waiting
before destination/provider admission. Its second source acquisition already
waits only for an accepted receipt. Plan creation retains its existing behavior.
This is a narrow scope reduction under mandatory-review step 9; no new design or
additional source-wait guarantee is claimed for plan creation. The primary
message-delivery and implement-plan dispatch fixes are unaffected. Correct the
feature documentation and design wording to state the fork boundary. Focused
fork/source and existing plan-creation checks must pass before committing.

The reviewer independently confirmed complete inherited blob/delta equivalence,
whole-branch history, single pin per stream, and sound migration lineage. No
other finding exists. Preserve baseline-review.md with its assessed exact ranges.
