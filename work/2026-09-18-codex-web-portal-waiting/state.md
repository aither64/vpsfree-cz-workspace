---
lifecycle: active
---

# 2026-09-18-codex-web-portal-waiting

## Status

- Dedicated feature worktrees exist for all five affected repositories. The
  configuration worktree needs its Nix/Ruby hook environment restored before it
  can be committed; worktree creation otherwise completed.
- `codex-web` now has an Apache 2.0 license, a user-focused README, and the
  former technical README preserved byte-for-byte in `docs/reference.md`.
- `dev-workspace` has a compact amber indicator on the Codex tab when an
  interactive conversation is idle after a turn or has a blocking request. It
  clears when the activity read fails. No endpoint, persisted state, or polling
  behavior changed.
- The two Ruby entry-point suites now load feature-focused files and shared
  support classes. Their original commands pass with the same run and assertion
  counts as the detached baseline.
- Project changes and downstream dependency pins are not committed yet.

## Next actions

- Commit the codex-web and dev-workspace changes after focused checks finish.
- Run the required Terra/xhigh review, address its findings, and update the
  downstream pins in dependency order.
- Build and deploy the configuration feature branch to aitherdev without
  waiting for CI. Verify the portal and user-profile services.

## Documentation

- The codex-web README and `docs/reference.md` own reusable user and API
  documentation. `dev-workspace/test/README.md` documents the retained test
  entry points and focused files; its README documents the visible indicator.
- This initiative owns deployment, review, exact revision, and recovery
  evidence. The accepted plan is in [plan.md](plan.md).

## Repositories

| Repository | Branch | Worktree | Base |
| --- | --- | --- | --- |
| codex-web | `2026-09-18-codex-web-portal-waiting` | `worktrees/2026-09-18-codex-web-portal-waiting/codex-web` | `7429ff29d3ae35c43b155a99b1bd34c6a33ae187` |
| dev-workspace | `2026-09-18-codex-web-portal-waiting` | `worktrees/2026-09-18-codex-web-portal-waiting/dev-workspace` | `18817f4bf60f9918932d980d5c91b92852ba3cfa` |
| vpsfree-dev-workspace | `2026-09-18-codex-web-portal-waiting` | `worktrees/2026-09-18-codex-web-portal-waiting/vpsfree-dev-workspace` | `ab74ed67b83f488f7825884b12a58c17c3ca3e2b` |
| workspace | `2026-09-18-codex-web-portal-waiting` | `worktrees/2026-09-18-codex-web-portal-waiting/workspace` | `77afe04b318a82a8eea72b031bac2da856eb6abc` |
| vpsfree-cz-configuration | `2026-09-18-codex-web-portal-waiting` | `worktrees/2026-09-18-codex-web-portal-waiting/vpsfree-cz-configuration` | `c7ed1210fc90434e50de2b1e4752a7ae38d9a491` |

## Commands run

- `dev-session start codex-web-portal-waiting --no-attach`: completed after
  App Server disconnect recovery; portal URL is
  `https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-18-codex-web-portal-waiting/`.
- Detached baseline Ruby suites: `dev_session_test.rb` passed with 316 runs and
  3,526 assertions; `workspace_host_test.rb` passed with 77 runs and 490
  assertions. The refactored entry points passed with the same results. Logs
  are in `/home/aither/.local/state/dev-workspace-evidence/2026-09-18-codex-web-portal-waiting/`.
- `nix develop -c bash -lc 'cd portal && go test -mod=readonly ./internal/web'`
  passed in 31 seconds. The root invocation lacked a module and the first
  portal invocation inherited vendor mode; neither started tests or changed
  sources.

## Results

- No current session existed before initialization. The helper created ready
  session `2026-09-18-codex-web-portal-waiting`.
- Current deployed runtime is Codex 0.155.0. The checked generic runtime base
  already pins it; this initiative changes neither Codex version nor protocol.
- The portal indicator uses the existing activity and pending-request snapshots.
  It is absent until a successful activity snapshot arrives and absent after a
  failed activity read. The tab gets an accessible waiting label and the dot is
  absolutely positioned within the existing icon width.

## Open questions

- None. The user selected the current waiting-state indicator and Terra for
  implementation/reviews.

## Cleanup

- Retain the initiative, branches, worktrees, and prior user-profile generation.
- Do not archive, delete, or merge the configuration branch without explicit
  direction.
