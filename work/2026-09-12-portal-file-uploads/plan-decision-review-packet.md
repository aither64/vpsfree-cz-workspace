# Current plan decisions review

User-approved follow-up in 2026-09-12-portal-file-uploads. Read the final follow-up
section in plan.md and state.md in this directory, plus repository AGENTS.md.
Review only this follow-up (bases below); preceding uploads/menu work is already
deployed and must retain compatibility. Workspace preceding feature commits were
rebased onto current shared master as required; supplied base is the rebased
previous deployed tree. No default merges or session closure authorized.

Acceptance: after an earlier plan and a newer ordinary reply, enabling Plan mode
must leave the normal composer visible. Only a nonempty explicit plan item from
the newest completed turn qualifies. Empty, failed, interrupted or newer ordinary
turns invalidate prior plans. Both server implementation destinations enforce this.
Existing submitting/accepted sends recover their receipts without sending again;
prepared requests still require freshness. Validated new-session creation retries
retain their durable approved snapshot.

A genuine decision replaces the entire composer, preserves drafts/files/uploads,
hides the redundant waiting strip, leaves queued messages and delivery receipts
visible. Keep planning restores/focuses input; implementation restores it when
accepted/active; canceling the new-session dialog keeps the decision. Dismissal is
page-local by turn+content, so identical content in a later turn may show again.

Ownership: codex-web owns additive Transcript.latestTurnId and ReconcileSend,
which extracts Send's existing durable ledger reconciliation without submission.
The conversation HTTP handler serializes Transcript; existing clients ignore the
additive field. dev-workspace owns plan selection, implementation policy, and
portal composer visibility. Its codexController adds the recovery method; the
shared conversation.Client interface is unchanged. Organization, workspace and
system config select exact runtime/provider revisions through pins only.
Missing latestTurnId fails closed with ordinary composer available. No App Server
version, persisted state, schema, protocol requests, model or upload changes.
Static app.js/style.css already use no-store; shared versioned assets unchanged.

Trust: local workspace operator is trusted to administer host; remote clients
remain untrusted. Preserve resolver, same-origin, identity/digest validation,
existing locks, private ledgers and state. No extra compromised-operator defenses.

Commit split: provider metadata then independent non-submitting recovery API;
runtime provider pins then server freshness+retry behavior, then browser decision
presentation (associated tests in each). Downstream pins isolated. Preserve prior
deployed commits; no abandoned schemas or migration shims added.

Quick verification: provider go test ./... passed; runtime go test ./... passed
including browser contract (28.9s web suite); node --check app.js passed. Nix
Go vendor hash regenerated with deliberate mismatch and correct hash recorded.
Config confctl generated pin precommit hooks passed (expected message width warning).
Long browser/package/deploy checks have not started, pending required review.

Overall risk HIGH: public cross-project additive API, durable recovery path and
mixed-version deployment. All four lanes required, gpt-5.6-sol xhigh. Deploy
provider/runtime as one built user-profile package, system config through confctl
feature branch. No state changes; rollback loads the same ledgers/drafts. Codex
0.154.0 process should remain running. Integration into defaults is out of scope.

Repositories (absolute worktree, base -> head):

- codex-web: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-file-uploads/codex-web
  4a4c77b4acc2bbaef44e2327c37d9c984e091867 -> c0fbae9d4828bb05fdf5f17f9b85a66eaf98c612

- dev-workspace: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-file-uploads/dev-workspace
  14871f50bb6f57542d3452de32924357ff629037 -> 2bfb0ee6aa4d56cbcbe079ef49c79d772a2e8fcf

- vpsfree-dev-workspace: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-file-uploads/vpsfree-dev-workspace
  6063618bcf1fc3eefe57187a22ccc3b1bf0b22b6 -> 909fde20f06384a54cd36297688182456f1dc7b1

- workspace: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-file-uploads/workspace
  96ec50e609a48372fc4ab5300e34dc12f6ba9733 -> f9d156a2f2447ba033b4dd3ceb967203cfe972e3

- vpsfree-cz-configuration: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-file-uploads/vpsfree-cz-configuration
  c79a68ea6ef80dcaaef95cf17950fa87afbe976d -> 4362c8c1a866b125a398fa40737fbd9082913223

Architecture review identified an Important pending-request classification issue.
The current browser commit now matches the implementation message and exact
plan:<digest> context, after hashing, for both default-mode eligibility and label.
Regressions cover ordinary same-text attempts, other-plan attempts and a match.
Focused browser contract and JS syntax passed. This is a direct narrowing fix;
general and architecture reviews need no confirmatory rerun. Pins were consolidated
into each owning unmerged follow-up commit. Scope review uses these final heads.

## Turn-bound receipt correction

Risk review found that identical plans in later turns could reuse an earlier
unacknowledged client ID. Runtime commit 2bfb0ee fixes the browser matching and
server action context together: new same-thread requests send planContextVersion=2
and use plan:<turnId>:<digest>. The existing matchingSendAttempt helper owns
message/context/attachment equality. Both the banner and click handler use it.
Unversioned old-page requests may only reconcile already submitting/accepted
legacy plan:<digest> receipts; absent/prepared requests receive a reload conflict.
Unknown explicit versions are rejected. There is no ledger-format migration.
Legacy prepared records cannot establish which repeated plan turn was approved,
so they are intentionally not submitted. A fresh page and current Plan mode allow
a new request. Observed legacy sends retain ordinary transcript acknowledgement.
Rollback reads the same ledger, rejects incompatible action contexts, and may need
a fresh page; it never reuses a v2 attempt as a legacy submission.

Regression coverage: legacy accepted recovery and prepared rejection, current
receipt recovery after newer turns, rejecting an old ID for a later identical
plan, accepting a fresh ID, and browser matching across equal text/different turns.
Focused Go/browser contract and JS syntax pass. No provider change since review.
The correction is one inseparable browser/server request-identity commit because
both sides must bind the same intent. Prior server freshness and UI presentation
commits remain separate; old legacy context predates this follow-up and was deployed.

Re-review the bounded correction and final pins, not the already reviewed upload
feature. Full initial general/architecture reports and risk finding are retained.
