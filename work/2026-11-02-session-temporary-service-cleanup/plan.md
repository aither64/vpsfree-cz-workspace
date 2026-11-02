# 2026-11-02-session-temporary-service-cleanup

## Goal

Investigate and propose a solution for automatic cleanup of all session-owned temporary services and servers during workspace session archival. PROPOSAL ONLY: explain the problem, delegate investigation/design to this Full team's architect, record a minimal design and verification plan, and present the proposed solution to the user. Do not implement, merge, deploy, archive/delete any session, stop/remove any existing service, or otherwise change the running workspace yet. The user will continue directly in this new session after reading the proposal.

User's exact request in the originating conversation:
"that's cool, but we won't always remember to do that. the archiving process must handle this scenario automatically: all temporary services/servers must be stopped/deleted during the archiving process. start a new workspace session using the same provider and with a full team. describe the problem and let it suggest a solution. I'll take it from there."

Context and concrete evidence (copied here so no access to the originating session's private files/transcript/team is needed):
- HaveAPI documentation preview was launched as an independent transient systemd USER service, outside the managed terminal and agents. It was intentionally retained while the user reviewed the feature; that feature is now merged into HaveAPI/master.
- Example live unit: haveapi-doc-language-preview-20261101.service; extra temporary loopback candidate units: haveapi-doc-language-candidate-20261101.service, haveapi-doc-language-nov2-candidate-20261101.service and haveapi-doc-language-cachefix-candidate-20261101.service. These belong to the originating session 2026-11-01-api-doc-language-settings. They are examples/evidence, NOT authorization for you to inspect that session's files or stop its services.
- The live unit's launch was /bin/sh /home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-api-doc-language-settings/preview_launch.sh; working directory was its isolated preview-source-eb91a4d0 under the same tracking directory. Dependencies also included an ignored gem home under the session's project worktree. The preview served an in-memory fixture on port4567; candidates used separate loopback ports.
- Read-only systemd inspection showed empty PartOf and BindsTo, StopWhenUnneeded=no and Restart=no. Therefore killing the session's terminal/agents does not itself stop these independent services.
- Installed archive implementation stops managed agents/terminal and releases development clusters, prunes tracking to Markdown/portal.yml and removes owned project worktrees. Read-only inspection did not identify registration/shutdown of these separately launched preview services. Pruning/removing the source/assets/dependencies can leave a live process serving broken requests, holding ports or unable to restart. This was a source/unit inspection, not a destructive archival experiment.
- Selected package at investigation time: /nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0. Relevant installed sources: libexec/workspace-portal/.dev-session-wrapped (archive_with_access, quiesce_explicit_archive!, quiesce_and_require_idle!, retire_session_runtime!), libexec/workspace-archive-cleanup.rb and libexec/workspace-tracking-summaries.rb. Reverify current behavior rather than assuming this package remains selected.

Requested outcome and proposal boundaries:
- Archival must reliably stop/reap and remove session-owned temporary servers/services before removing their runtime files. Users must not have to remember a separate manual cleanup step. Include temporary candidate/preview services as well as the obvious main server.
- Investigate ownership/registration/launch semantics, existing native systemd/session facilities and the smallest maintainable lifecycle integration. Recommend how agents should launch/register temporary resources so archival can discover them reliably. Consider existing unregistered temporary services and explain their supported migration/recovery boundary, rather than silently ignoring them or guessing ownership from broad names/PIDs.
- Preserve unrelated sessions and durable/production services. Do not kill arbitrary processes because they use a port or a matching pathname. Distinguish temporary resource cleanup that becomes part of an explicit archive request from the separate rule that ordinary task completion/handoff never authorizes stopping or archiving a session.
- Account for graceful shutdown, descendants, failed/uncertain stop, unit/artifact removal, idempotent retry and interrupted archival. State whether archival should fail safely before deleting files when cleanup cannot be proved, and how existing lifecycle journals/revival remain compatible. Assess explicit and automatic archival under their existing policies; identify related deletion behavior only as needed for coherent lifecycle semantics.
- Follow this new session's verified identity, workspace procedures and team roster. Likely owning project is reusable dev-workspace (git@github.com:aither64/dev-workspace.git); determine whether site integration in vpsfree-dev-workspace or workspace instructions is actually needed. No speculative framework or cross-project expansion.
- Produce a clear recommendation with alternatives/tradeoffs, exact ownership/API/implementation boundaries, compatibility/recovery implications, and focused verification criteria using disposable fixtures. No actual lifecycle experiment against live sessions/services. Save proposal/design in your own session records, then stop at presenting it for the user's decision.

Creation preferences explicitly requested: same provider as originating session, codex-lb (Snajpa codex-lb), and a Full team. Do not add a cross-session communication grant or assume access to the originating session; this self-contained brief is sufficient.

## Affected repositories

- Investigation/design owner: reusable `dev-workspace`
  (`git@github.com:aither64/dev-workspace.git`). Confirm boundaries from the
  selected installed package before recommending changes.
- Site extension and workspace instructions: assess only whether launch guidance
  needs a pointer; no speculative runtime or configuration scope.
- This proposal changes only this session's coordination records. No project
  branches, worktrees, implementation, deployment or lifecycle operations.

## Approach and ownership

- Lead: verify session identity and retained team, explain the supplied evidence,
  maintain plan/state/portal, inspect acceptance, present recommendation.
- `architect0` (retained Astra/xhigh, workspace-write): inspect selected package
  and owning sources/docs read-only; write `design.md` with the minimal ownership,
  launch, cleanup, retry and migration contract and disposable verification plan.
- Implementers: no assignments in proposal phase. Reviewer: no automatic review
  for planning/investigation records. No team settings are changed.

## Decisions and boundaries

The supplied HaveAPI service names are evidence, not authority to inspect the
originating session or change its services. No cross-session communication grant
is requested or created. No live lifecycle experiment is permitted.

The recommendation must cover every preview/candidate, descendants, graceful and
bounded forced shutdown, exact ownership, failure before file removal, unit and
artifact retirement, interrupted/retried archival and revival. Compare explicit
archival with the existing automatic-worker policies; mention delete only for
shared cleanup semantics. Ordinary task completion/handoff must retain its
current non-authorization boundary.

## Compatibility and deployment

Assess older sessions/unregistered services, existing archive journals and
revival, selected package generation/rollback and durable or unrelated services.
Do not silently infer ownership from names, ports, PIDs or matching paths. Record
unproven behavior as a verification obligation. There is no deployment in this
proposal; any implementation or rollout requires a later user instruction.

## Documentation

Readers: the user deciding the next step, and the implementation owner if later
approved. Keep the proposed contract and focused verification brief in
[design.md](design.md), with current evidence/status in [state.md](state.md).
No reusable project documentation is edited before implementation is requested.

## Testing plan

Now: read-only source/document inspection, evidence reconciliation and local
record/link checks. Do not create services, run archive/delete/revive, stop units,
launch builds or execute lifecycle tests.

Later if authorized: disposable fixtures covering ownership/isolation, every
candidate and descendant, graceful/forced/uncertain stop, launch/archive races,
crash/retry boundaries, old journal/package compatibility and unchanged worker
eligibility. The architect defines bounded checks and stopping conditions.
