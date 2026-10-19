# Session creation provider handoff recovery

Fix the reported post-redirect initialization refusal and preserve text selection
on the creation progress page. This follow-up is isolated from the completed
provider-switch initiative because this external conversation has no inherited
session environment. It owns the new initiative created through `dev-session
start --no-codex --no-attach`; the lead owns investigation and application edits.
No team was added. Existing sessions and requests must remain intact.

Affected application: generic dev-workspace. Workspace/configuration pin changes
will follow only if needed to deploy the corrected application under existing
user authorization. No Codex modifications or updates.

Initial evidence: the accepted creation request serializes `provider`, while
Ruby's direct-team and managed-team request allowlists omit it. Confirm the
entire request contract, delegated CLI settings and retry identity before editing.
The progress renderer assigns error text on every poll, replacing selection.

Acceptance:

- Accepted default/explicit provider requests pass the actual Ruby initialization
  receipt validation, preserve their provider and complete/recover initialization.
- Changed or invalid provider/receipt identities still fail closed.
- Error text can be selected/copied during repeated status polling; offer a
  dedicated copy action if useful and preserve error display on retries.
- Add a cross-component regression covering beyond HTTP acceptance, rather than
  stubbing the initializer at the boundary where this failure occurs.

Compatibility: retain existing receipt/journal schemas and exact saved identity.
Requests without provider remain valid. Retrying existing failed receipts must not
create a duplicate thread, team or initial turn. Respect supported old-package
rollback and record any incompatibility. No database migration is expected.

Verification: reproduce the refusal before fixing it, focused Ruby receipt and
initialization checks, shipped browser HTTP/CLI contract, DOM selection regression,
quick Nix-environment checks, committed independent review, then only necessary
package/integration checks. Deploy and verify the corrected runtime through the
ordinary coordinator with exact ownership, review, reservation and recovery proof.
Preserve and diagnose failed evidence; do not retry another session's request.

Documentation readers are future runtime developers/operators. Keep request and
retry invariants in owning project docs, exact rollout/results in this initiative,
and reusable testing gaps in workspace notes.
