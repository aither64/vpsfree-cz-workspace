---
lifecycle: active
---

# 2026-09-21-agent-teams-workflow

## Status

The prior virtual managed-team implementation reached a deployed feedback
candidate but failed its intended portal interaction: the user receives
"Conversation access denied" and the controls do not represent real agents.
The user has explicitly replaced that design. Its old immutable catalog,
virtual member ledger, selection transitions, and managed dispatch are now
superseded work, not a foundation to extend.

The replacement retains the root App Server conversation and the existing tmux
session per initiative. It creates independent persistent member threads and
uses direct correlated App Server turns as the team transport. `lead` remains
the attached terminal conversation; specialist members use compact stable
addresses such as `architect0` and are headless until assigned work.

## Current implementation scope

- `dev-workspace` is the primary implementation repository.
- `codex-web` is updated only if its public client must expose a generated
  App Server operation needed by the new direct-thread runtime.
- `vpsfree-dev-workspace` is updated only for needed vpsFree.cz session/team
  instructions. No configuration repository code change is planned.

## Decisions

- The portal and terminal share one team runtime and roster; neither is a
  secondary or simulated interface.
- There is no external bus, SQLite store, or daemon. App Server turns are the
  task/result transport, and existing send-ledger recovery is reused.
- Existing virtual team state is reset at the forward-only aitherdev cutover.
  Root conversations, worktrees, tracking, and tmux sessions are retained.
- Long verification always uses a fresh Luna/low watcher and is not a member.
- Implement all phases before a single consolidated Terra/xhigh review. Do not
  request review for intermediate commits or phases.

## Next actions

1. Inventory the virtual-team touchpoints and current App Server client
   contract, then replace the old state/runtime boundary.
2. Implement the shared CLI/portal runtime and direct member thread transport.
3. Complete portal UX and session lifecycle support, then run the consolidated
   verification, review, and aitherdev deployment.
