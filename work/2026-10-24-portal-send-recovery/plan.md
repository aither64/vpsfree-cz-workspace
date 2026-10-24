# Portal message delivery recovery

Implement the plan approved in the external conversation
`01a16f77-9ed3-7932-8a25-7b6050604f2d`. Tracking was authorized after the initial
read-only investigation. This separate initiative was created with
`dev-session start --no-codex`; do not adopt the affected confctl session or
another initiative's runtime worktrees.

## Outcome and decisions

- Distinguish definitely-unsent, uncertain and accepted message submissions.
- Avoid poisoning an attempt when caller cancellation precedes its mutation
  frame. Preserve uncertainty once a write might have occurred.
- Finish admitted portal sends and receipt recording independently of browser
  disconnect, within the existing operation budget and server shutdown.
- Provide explicit duplicate-aware resending for genuinely unknown outcomes.
  The user selected portal recovery instead of changing native Codex.
- Clear stale composer errors after a successful newer submission. Preserve
  individual unknown receipts and protect feedback against late older failures.
- Preserve attachments, drafts, original options, existing ledger schemas,
  execution holds, authorization and current native Codex.

## Repositories and documentation

`codex-web` owns transport evidence, delivery errors, HTTP integration and shared
browser primitives. `dev-workspace` owns portal receipts, composer feedback and
package composition. `vpsfree-cz-configuration` owns the matching aitherdev host
selection. The coordination workspace owns its composed application selection.
Maintain the owning projects' delivery/recovery explanations, and record exact
rollout identities separately here.

## Verification and rollout

Use focused Go and browser regressions first. Commit completed source, then run
independent final review before packaged/browser/native integration checks.
Use disposable sessions and sockets; never resend the affected user's message.
Publish feature branches without integrating defaults. Match runtime selections
in configuration and workspace composition, run the deployment-contract check,
build aitherdev, then use coordinated machine/profile activation under the
shared reservation. Preserve deployed lineage and other owners' operations.

Existing schema-3 submission records remain readable. Unknown legacy attempts
must not be reset from negative history evidence. Browser replacement metadata
is additive. Deployment and successful verification do not authorize merging
feature branches or archiving this initiative.
