# 2026-11-03-lead-wakeup-delivery

## Goal

Investigate recurring failure to wake an idle lead after asynchronous monitoring finishes. Prepare an evidence-backed root cause and concrete solution proposal for the user.

The user explicitly requested a NEW workspace session with the installed Full team preset with FOUR implementers (delegated_4), ordinary architect/implementer/reviewer ownership and retained preset settings. Their exact request:
"please start another workspace session with a full team (4 implementers) that will investigate and handle the wake-ups. I see this issue repeatedly, the lead says that it continues monitoring and ends his turn, but never wakes up again when it finishes. a subagent may be running, but I guess it doesn't work. so this needs fixing. suggest a solution."

Scope: investigate the runtime-owned completion/escalation delivery path and suggest a minimal maintainable fix. Begin with diagnosis, reproducible evidence and a concrete design/implementation plan. The final request is a solution proposal, so do not infer integration/deployment/lifecycle permission. Keep this session open. Do not expand into unrelated runtime architecture.

Seed evidence, to verify independently against canonical source:
- A session lead launched a fresh native collaboration utility (gpt-6-luna/low, fork_turns none) to observe an exact long-running GitHub Actions run with gh run watch. The native utility continued running after the lead ended its turn.
- Native collaboration.send_message delivers updates to an ACTIVE parent but does not establish a supported wake/new-turn path for an IDLE lead. The lead's claim that it would automatically continue was not verified.
- Testing the application-owned mcp team_reporting report_to_lead capability from that native utility returned exactly: "This caller is not an active team member in this workspace." The utility is deliberately outside the retained team roster.
- Retained roster members' report_to_lead messages do reach the lead through normal application-owned team reporting; investigate the exact lifecycle/identity difference rather than spoofing a member or reconfiguring retained model/purpose/access.
- Installed package observed at failure was /nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0, catalog metadata digest 495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7, utility verification_watcher = gpt-6-luna/low, operation lifetime, full-access/never native policy.
- The original lead is keeping its turn active as an immediate workaround. Its live monitoring and conditional merge belong to that original session and must not be disturbed.

Architecture direction to assess, not an approved implementation:
A runtime-owned, durable operation completion/escalation notification should enqueue a real lead turn for the exact owning live session, independent of native parent activity. Bind operation/session/thread identity and outcome; handle duplicate delivery/idempotency, lead busy vs idle, disconnection/restart, stop/archive/revoke boundaries and no automatic replay loop. Reuse existing prompt/notification infrastructure if appropriate. Do not turn temporary utilities into team members, impersonate a lead, change saved team settings or depend on policy text telling an idle model to notice.

Likely owners to determine using the project map: generic dev-workspace runtime/notification/prompt plumbing, codex-web integration or vpsFree extension/monitor skill. Use your own session-owned worktrees and canonical SSH repositories; architect owns substantive investigation/design and writes design.md before source implementation. Delegate bounded independent diagnostic packages to your four implementers. Follow mandatory independent review for any later completed substantive deliverable; planning/findings alone do not trigger review. Use isolated/disposable runtime state for tests, not the live registered workspace.

Acceptance for the proposed solution:
- Demonstrate actual lead turn activation after an owned utility succeeds, fails or escalates while the lead is idle, not merely a log or delivered native message.
- Preserve exact source/run/attempt/outcome identity, duplicate suppression and active-turn steering semantics.
- Verify cancellation/restart/disconnection and ownership boundaries without touching real peer sessions or lifecycle.
- Preserve ordinary team member reports and saved settings; no credential disclosure.
- Explain smallest affected components/files, compatibility/recovery, test plan, remaining user decisions and limitations.

No cross-session communication grant is included by this creation request. Do not access the original session's files, worktrees, transcript, team or credentials. The seed facts above are sufficient to begin independent investigation. Do not send messages to the original lead unless the user explicitly approves the exact pair through ordinary session_communication. Do not take over or alter its live CI watcher, branch or conditional merge.

## Affected repositories

Investigate generic dev-workspace first; inspect codex-web and the vpsFree extension only for the notification/native-monitor boundary. Use canonical SSH refs and this session’s isolated worktrees. No source implementation, integration or deployment in the proposal phase.

## Approach

Architect owns investigation synthesis and design.md. Four implementers own independent diagnostic packages: runtime reporting, native utility identity, prompt dispatch/recovery, and monitor policy/source provenance. Each records source revisions, file/line evidence, reproducible checks and limitations. Lead accepts evidence and prepares the user proposal. No peer-session access.

## Decisions

## Compatibility and deployment

Assess additive durable operation identity/outcome state, old/new package behavior, rollback, restart and stop/archive/revoke fences. Reuse existing prompt machinery where safe. No changes to retained settings or temporary roster membership; no production/runtime mutation.

## Documentation

Readers: user and future runtime implementer. Findings and evidence stay here; design.md is a proposal, not an implemented contract. Project docs change only in a later authorized implementation package.

## Testing plan

Prefer bounded disposable-state reproductions showing actual turn activation; distinguish current-path failures from proposed-path acceptance checks. Cover idle success/failure/escalation, busy steering, duplicate delivery, exact run/attempt identity, disconnect/restart/cancel and ownership boundaries. Long checks use the installed monitor skill and fresh utility.
