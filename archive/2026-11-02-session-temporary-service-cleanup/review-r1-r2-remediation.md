# R1 and R2 core remediation

Owner: implementer0, under the lead's narrow-fix release and architect's published
first-root admission brief. Final owned fixup:
`399136d8d6db71b140b2df3d859a7cbe31840abd`, parent
`85760a7a673f3ec072c7c16dc88006e89214d448`, tree
`61aacb00ba779f5259db50ea39dfe48753a21c80`.
Subject targets core commit `08a0df822b4a01cef25207ba663df861b2b4006d` for later
coordinated consolidation. A did not rebase, rewrite B commits or publish.

Five owned paths changed: the Ruby service owner, `dev-session`, focused service
tests, `docs/dev-sessions.md` and `docs/session-archive-recovery.md`. They and the
Git index are clean. B's three disjoint source changes remain unstaged; A returns
the Git lane to the lead/B with no unfinished command.

## R1: preserve registration metadata compatibility

`requirements` still strictly loads and validates paired registration state and
identity, then requires the existing schema/policy capabilities for every retained
marker, including initializing, ready-empty, retired and archived registrations.
Only absent registration avoids the gate. Pending cleanup and malformed/missing/
orphan state retain their existing refusal behavior.

The capable ordinary delete remains the sole implemented transition that moves
retired registration evidence to its existing private removal recovery and clears
the active namespace. No old-delete reconciler, history collector, migration,
new capability key or unregistered-service gate was added. The predecessor
observation-format compatibility proof remains useful without waiving this
registration preservation requirement.

Focused lifecycle proof covers initialization and ready-empty state, retired
state, archive/revive retaining the requirement, partial evidence-transfer
interruption failing closed, unchanged recovery evidence and successful normal
delete completion removing active registration. B owns host preparation/candidate
activation refusal before an incapable predecessor can dispatch delete.

## R2: bounded first-root refusal

One read-only Runner admission helper uses the existing strict Store load:
absence returns, a validated null retained root refuses, the same nonnull retained
root passes, and existing corruption/loss/identity errors remain errors. Resource
phase does not affect this rule.

The helper runs under existing creation/session locks in `start` before sensitivity,
revive-start, receipt, journal or native mutation, conditional on `run_codex`.
Both fork destination admissions call it, including the second check after source
work releases destination locks. The source root is never gated. No downstream
native/Go reader, root rebinding, transition schema or record deletion was added.

Tests prove live and retired first-conversation refusals leave tracking and
registration bytes unchanged and reach no sensitivity, receipt, journal, provider
or native publication. Listing, stopping, archiving/reviving without a root, and
normal deletion remain usable afterward. Additional proofs cover initializing and
empty refusal, no-registration/headless admission, actual same-root retained start,
early fork destination refusal and registration arriving between fork admissions
without changing its registered source.

The exact lead-approved CLI message and final contextual docs wording are applied.
The docs require conversation creation before first service registration, explain
that stop/retirement/archive/revival retain registration history, and preserve
ordinary session-without-conversation service/lifecycle use. They do not advise
discarding evidence or deleting a session to bypass admission.

## Verification

Final relevant quick batch ran in the runtime Nix shell and passed:
**34 tests / 484 assertions / no failures, errors or skips**, 26.86 seconds.
Full output and exact filter are in
[review-r1-r2-quick.log](review-r1-r2-quick.log). It includes all 27 service-owner
tests and seven existing normal start/browser receipt/same-root/unshared/fork
regressions. Earlier focused R1 lifecycle/metadata proof was 5 tests/76 assertions;
R2 admission/empty proof was 6 tests/91 assertions. Ruby syntax and staged
whitespace checks passed.

The final amend changes prose only after that passing code run. Commit used a
temporary message file through the Nix shell with normal hook policy and no
bypass. Temporary pre-wording fixup `d84684ce` was unpublished and superseded in
place. No long campaign, push, pin, claim, build/copy, live service/session action
or activation occurred.

Next: lead inspects the direct committed correction under the narrow-fix policy;
B commits its disjoint host/docs/R3 fixes; coordinated consolidation and the
required final history/migration conclusion precede publication and long checks.
Current observations in earlier handoff/preparation files remain scoped to their
recorded pre-fix ranges, not this head.

Session stays open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/
