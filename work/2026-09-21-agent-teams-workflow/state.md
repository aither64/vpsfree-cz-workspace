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

Implementation is complete on `2026-09-21-agent-teams-workflow` in the
`dev-workspace` feature worktree at `269799d` (`teams: preserve roster and
lifecycle invariants`), following `f597c1d` (`teams: use independent Codex
member threads`). The direct roster, portal Team tab, terminal commands,
roster-address-only member transcript reader, and root lifecycle synchronization
are committed. The legacy managed access gate is disabled so old virtual state
no longer denies a root conversation. New sessions start with their normal
lead and add a direct roster afterwards.

Quick verification passed under a fresh Luna/low watcher:

- `nix develop -c bash -lc 'cd portal && GOFLAGS=-mod=mod go test
  ./internal/teamruntime ./internal/web && node --check internal/web/static/app.js
  && cd .. && ruby test/dev_session_test.rb'`
- Go packages and browser syntax passed; Ruby result: 332 runs, 3694
  assertions, 0 failures, 0 errors, 0 skips.

The repository's normal vendored Go invocation remains blocked before
compilation by an existing vendor metadata mismatch with `portal/go.mod`;
focused verification deliberately uses Go module mode. The consolidated
Sol/xhigh review covered general, architecture, scope, and
risk/compatibility lanes. It found and the lead corrected: lost roster data in
the automatic Team refresh; removed members being revived or forked as active;
team mutations racing lifecycle transitions; report sender attribution; preset
reapplication adding duplicate members; public retention of the retired
selection flags; and inaccurate busy-member documentation. The fixes stay
within the reviewed direct-thread contract. Post-fix focused verification passed
with the same zero-failure result. Packaged `nix flake check --print-build-logs`
also passed under a fresh Luna/low watcher; the complete log is
`logs/direct-team-flake-retry.log`. VM boot logs were expected and no unexpected
local kernel build occurred. The aitherdev user profile was switched from this
exact worktree successfully. The switch initially refused two stopped stale
vpsAdmin development clusters, so their exact disposable states were reset:
`2026-08-18-vpsadmin-password-reset` and
`2026-09-09-ip-release-mechanism`. The new router and portal service are
active; `dev-session validate` validated 55 manifests and the stable portal URL
returns its expected Basic Auth challenge. No configuration pin change is
planned.

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
- Implement all phases before a single consolidated Sol/xhigh review. Do not
  request review for intermediate commits or phases.

## Next actions

1. Obtain user feedback from the deployed Team controls, including creating a
   member, assigning work, inspecting its messages, and root conversation
   access.
2. Address any deployment feedback before any configuration integration.
