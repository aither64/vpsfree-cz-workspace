# Independent profile forward-recovery review

## Finding

### R6 — Important — Helper interruption releases the attempt lock while activation can continue

General and risk/compatibility lanes. Commit
`7521a4eaf2e67c54944c197053f8dbe4f159260a`,
`docs/maintenance/recover-archive-profile-2026-10-16.rb:88`, `:107` and `:115`.

The helper owns `worker.lock`, then starts `workspace-host activate-prepared`
with `Process.spawn` and waits for it. The child is not given the lock descriptor;
ordinary Ruby file descriptors are close-on-exec and this spawn supplies no
inheritance mapping. There is also no signal handling or child cleanup before
the parent releases the lock. `rescue StandardError` does not handle `Interrupt`
or default signal termination.

If the helper is terminated or crashes while the activation child survives, the
worker lock becomes available immediately. A helper retry can pass validation
against the unchanged original unknown receipt and `profile_intent`. If the
candidate has already been selected, the automatic native reconciler can also
acquire the lock: it checks the original operation service, which has already
exited, and does not know about this recovery child. Both paths can invoke
`activate-prepared` again while the first activation is still running.

The installed transition lock does not provide equivalent exclusion for the
whole activation. In the pinned package, `activate_prepared_command` releases it
before `complete_candidate_activation`, which waits for sockets and verifies
registration before taking the lock again. A second activation can therefore
overlap that completion, replace pending transition state or restart services.
This violates the brief's promise that the worker lock excludes reconciliation
throughout activation. Retaining the ledger claim alone does not prevent two
executors of that same attempt.

Keep exact-attempt exclusion for the full lifetime of the activation process
and its owned work, including parent cancellation. A bounded solution may retain
the lock in the activation child and manage cancellation/waiting, or bind the
recovery to supervised execution whose live state also fences retries and
reconciliation. Do not merely add another rescue clause or record that the
parent exited. Verify the chosen mechanism with a disposable activation stub:
interrupt the parent while the child remains active, then demonstrate that
neither another recovery nor reconciliation can acquire the attempt until that
work has ended. No live activation is needed for that verification.

## Authorization and ownership boundary

The intended recovery stays within the recorded deployment direction. The
retained approval quotes the instruction to proceed after the creation blockers
were fixed and covers `profile_activate` on `vpsfree:aitherdev` without reboot.
This helper retains the same owner, reservation, admitted job/attempt, snapshot,
artifact and candidate. It does not release or transfer the machine, change
the candidate, fabricate an applied result, rewind a phase, edit the foreign
creation journal or authorize integration. A separately directed exceptional
ownership transfer/release is therefore not part of the proposed action.

The fixed preflight checks bind the original error and request digest, one
unknown history entry, the original predecessor/token or exact forward
candidate, and the deployed system. The native Store validates and atomically
publishes the reservation-state adjustment, preserving the original reconciling
job and resource claim. Native `activate-prepared` still applies lifecycle,
cluster, capability, source, registration, profile-token and exact-claim checks.
Normal reconciliation re-enters the selected candidate to complete activation
before writing its own unknown-to-applied result and history disposition.

These are appropriate boundaries for this actual preselection deadlock. R6 is
an execution-lifetime defect inside that boundary, not a need to expand the
deployment authorization or to bypass another owner's reservation.

## Whole history, scope and migration conclusions

Reviewed workspace range:
`90f878616573e3f16b444e3a28709293c0f552d2..7521a4eaf2e67c54944c197053f8dbe4f159260a`.
The worktree was clean at the stated head. Its complete ordered series is:

1. `e93d73a9a296e15009ccb3e89d6f4f19559a9593` — accepted lifecycle documentation.
2. `abdeefc472bb96da2ca15f3aee2599987d10ab6e` — accepted final archive runtime pin.
3. `7521a4eaf2e67c54944c197053f8dbe4f159260a` — this dated recovery helper.

The sole change after the previously accepted head is the 140-line helper.
The final branch diff contains that helper, the lifecycle procedure and the
existing `flake.nix`/lock update. No obsolete unmerged approach, extra fixup or
repeated pin stream is retained. One final runtime-pin commit remains.
The deployed application candidate is still the separately retained package
built from `abdeefc4`; adding this operational source does not silently select
another application build.

**No database migrations or changes to native runtime formats.** The helper's
schema-1 recovery record is isolated operational evidence, not a replacement
for the native attempt request, phase, result or reservation history. Original
archive format lineage and prior review conclusions remain unchanged. Preserve
the new recovery record and native evidence until the attempt is settled.

## Four-lane conclusions and interruption limits

- General: exact tuple checks and the negative preflight cases address ordinary
  mistakes. History and commit separation are sound. R6 needs correction before
  this helper is accepted for execution.
- Architecture/repetition: the native Store owns persistence, the installed
  command owns activation and the native reconciler owns outcome publication.
  Pinning a dated helper to these exact installed interfaces is appropriate;
  a second generic activation or ledger framework is unnecessary. The helper
  must preserve the worker-exclusion contract when it creates a child process.
- Scope/proportionality: a one-attempt source-only recovery is proportionate to
  the demonstrated circular refusal. It does not broaden runtime behavior or
  require another archive implementation review. Correct the narrow process
  lifetime defect without introducing general recovery machinery.
- Risk/compatibility: owner and candidate retention, atomic state publication,
  forward-only selection and ordinary reconciliation are sound. A failure
  before spawn leaves the original claim recoverable. A normally observed
  activation failure restores `blocked_recovery`; a later retry remains bound
  to the original candidate. A crash after successful activation can be settled
  by normal reconciliation. Parent exit while activation is still live is the
  uncovered case in R6.

Reviewer: `/root/archive_final_review`, retained `gpt-6-astra` / `xhigh`, all four
mandatory-review lanes. Read the packet/brief, complete committed helper/history,
prior reports and the pinned installed coordination contract, operations guide,
Store, worker/reconciler and activation implementation. Supplied syntax,
read-only preflight and negative-case evidence were inspected. No recovery,
source edit, test, build, integration or nested agent was executed by the reviewer.

Conclusion: **not yet accepted for execution because of R6**. The exact-attempt
authorization, history and migration boundaries are otherwise accepted. Preserve
all prior archive implementation approvals and complete the focused correction
and interruption proof before the recovery proceeds.
