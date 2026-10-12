# Final plan decision recovery review

Initiative 2026-09-12-portal-file-uploads; this packet supersedes earlier request
recovery descriptions. User wants enabling Plan mode after an ordinary reply to
leave the composer visible, and a genuine plan decision to replace the composer.
Only a nonempty plan item from the newest completed turn qualifies. Preserve
drafts/uploads, receipt/queue visibility, focus restoration, and dialog cancel.
Newer empty/ordinary/failed/interrupted turns invalidate earlier plans. Identical
text in a later turn is a distinct decision.

Initial code was reviewed in all four lanes. General and scope have no findings.
Risk found identical later text could reuse an older accepted request. New v2
identities bind plan turn+digest. A subsequent architecture/risk review found
legacy prepared records could block lifecycle checks, and an old page could still
interpret legacy receipt recovery as approval of a later identical plan.

Review this bounded final correction (no need to reread the preceding upload/menu
history): provider c0fbae9d4828bb05fdf5f17f9b85a66eaf98c612..HEAD;
runtime 2bfb0ee6aa4d56cbcbe079ef49c79d772a2e8fcf..HEAD, plus final pins below.
The runtime provider pin was consolidated into its initial follow-up pin commit;
other code from the earlier reviews is unchanged by that history rewrite.

Final contract:
- New same-thread implementation requests carry planContextVersion=2 and exact
  plan:<turnId>:<digest> identity. Existing v2 submitted receipts recover before
  freshness checks; new/prepared requests require the current completed proposal.
- Every unversioned action=same request requires a reload BEFORE reconciliation.
  An old page can never mistake an old receipt for a new approval.
- action=recover is separate and can never send or change mode. It recovers
  submitting/accepted receipts. For legacy records it may retire prepared/absent
  attempts. For v2 records it must establish a known newer/different proposal
  before retiring a prepared attempt; a current or unproven proposal is retained.
- Provider DiscardPreparedSend is the only ledger retirement owner. Under its
  queue and durable ledger locks, it matches exact ID/message/context, retires
  prepared or already absent requests idempotently, and refuses submitted states.
  Write failure restores memory. The ledger schema and App Server protocol remain
  unchanged. RequireSubmissionAttemptsResolved succeeds after prepared retirement.
- Fresh browser refreshes recover unknown legacy attempts and unknown v2 attempts
  whose source turn has been superseded. Only confirmed retired retry records are
  removed locally; submitted receipts retain normal transcript acknowledgement.
  Recovery does not click/approve the current plan. MatchingSendAttempt owns the
  equality rule for banner eligibility and implementation clicks.
- A rollback page/server may reject newer contexts/actions and require reload.
  It does not reinterpret v2 identities as legacy. Existing stored ledger data is
  still readable. We intentionally do not implement any automatic message retry,
  general migration engine, hidden workflow execution or schema conversion.

Ownership and consumers: codex-web owns Transcript.latestTurnId, ReconcileSend,
DiscardPreparedSend and provider ledger semantics. The shared conversation.Client
interface is unchanged. dev-workspace codexController consumes these methods and
owns plan policy and browser recovery. Organization/workspace/system pins are
mechanical. All unrelated uploads and lifecycle features were previously deployed
and are outside this correction. Static portal app/style already use no-store;
shared cached browser assets are unchanged. Codex stays 0.154.0.

Commit split: additive provider metadata, receipt recovery, then prepared retirement.
Runtime provider pin, server freshness, browser layout, turn-bound request identity,
then obsolete-retry recovery (inseparable browser/server recovery action). Associated
tests stay with each behavior. Downstream pins remain single commits per follow-up.

Quick verification: provider go test ./... passed; runtime full suite passed before
last bounded v2-obsolete extension and reruns now; focused retirement/current-vs-stale,
legacy old-page rejection, identical later plan, browser contract and JS syntax pass.
Go vendor hash remeasured. Full browser acceptance, package builds and deployment
remain after review. Browser fixture covers desktop/narrow layout, drafts/files,
legacy retirement, queue/receipts, and a held old receipt plus identical later plan.

Risk HIGH for API/recovery/deployment. Required lanes sol xhigh. Local operator is
trusted; remote clients untrusted. Keep existing resolver/origin/identity/body
bounds and locks. No default merges, archive, deletion or session stop authorized.
Review packet/state/artifacts are under work/2026-09-12-portal-file-uploads.

Final worktrees and heads:

- /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-file-uploads/codex-web
  ee9ab42791a84b79315d952501264a6cbafc8695

- /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-file-uploads/dev-workspace
  7f0d1abd0c382088cc05e7f82d2e65af5b5dd4c8

- /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-file-uploads/vpsfree-dev-workspace
  a4b837f1c976c7611493e2f4f87ad49a008a4853

- /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-file-uploads/workspace
  ab7a866482b3dcd0d1cc2d675a58e8ce00d2527b

- /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-file-uploads/vpsfree-cz-configuration
  c7d639ec9d63e5d1f69d3508cf06b49d72b76a36
