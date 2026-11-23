# 2026-11-23-pi-goal-completion

## Goal

I'd like you to evaluate Pi integration in the portal. I miss something like setting a goal to work towards, Pi tends to stop turns without its work being done. How could this be implemented?

## Affected repositories

- `dev-workspace`: owns the portal, its backend operations and the managed Pi worker.
- `codex-web`: compare the shared conversation UI and Codex goal contract; any change depends on what the existing contract can express.
- The evaluation used no project worktree. First execution step is a disposable, offline test of the installed SDK; application changes follow the worker feasibility gate.

## Approach

Trace the goal UI and the end-of-turn contract across Codex and Pi. Separate a clean but premature end from failures, deliberate pauses and human dependencies. Recommend the smallest feature that keeps Pi working toward a user-authorized objective after an ordinary turn ends.

## Decisions

The user wants an in-house, chat-first solution: the agent maintains one working objective from actionable user requests, folds in follow-up bugs and features, and records remaining work and completion evidence. The goal strip above the lead's message box is for visibility and correction, not setup for each task. Reserve no row when there is no goal; otherwise show a single non-wrapping excerpt that fits the available width. Show full text, progress and controls only on demand, without resizing the composer. Tie scope updates to the exact current human input, prefer user corrections over stale agent reports, and do not restart idle work or reset a running allowance just because a goal was edited. Run bounded in-session continuation through Pi's `agent_before_settle` hook; let Codex use its native goal runtime where it can support the same behavior. Do not build a scheduler or a second model to judge intent or completion. No merge or rollout approval.

## Compatibility and deployment

Assess existing sessions without goals, native Codex goal behavior, and portal/worker version skew. Leave ordinary turns unchanged. Preserve Stop/restart/lifecycle behavior, and expose running edits only when the adapter proves that prior-revision results cannot complete an updated goal. No deployment at this stage.

## Documentation

Record the proposal in [design.md](design.md). If implemented later, document shared behavior and Pi-specific limitations with the owning portal/runtime interfaces.

## Testing plan

The offline pinned-SDK fixture proved plain-answer continuation and abort during the settle hook. Next prove managed-worker queue/input lineage under natural Follow Up; then test goal updates originating from an exact human input, stale goal reports, and edit handoff without a budget reset before exposing the shared portal surface. See [design.md](design.md) for the staged package and backend comparison tests.
