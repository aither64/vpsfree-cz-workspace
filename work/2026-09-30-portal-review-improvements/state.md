---
lifecycle: active
---

# 2026-09-30-portal-review-improvements

## Status

- Phase: implementation.
- The portal performance and automatic-history changes are merged on
  `dev-workspace/master` through `7c133c5`.
- Retained delegated roster is ready: `architect0` (design, GPT-6 Astra/xhigh,
  workspace write), `implementer0` (implementation, GPT-6 Sol/xhigh, workspace
  write) and `reviewer0` (review, GPT-6 Sol/xhigh, read-only).
- Registered feature worktrees exist for `dev-workspace`,
  `vpsfree-dev-workspace` and `workspace`; `codex-web` is registered for
  read-only protocol comparison and currently needs no edits. A clean,
  read-only `vpsadmin` worktree was registered at `5c76e329` because the
  cluster runner requires this session's `worktrees/<slug>/vpsadmin` path.
- Accepted [design.md](design.md) from `architect0` as the implementation and
  verification brief. Deployment is still pending.
- The first `dev-workspace` unit is committed as `f00a0e5` (role defaults),
  `4f500a5` (live settings draft) and `ce282b6` (retained/Load-all diffs),
  with a clean worktree. The member's socket-free Go, Ruby,
  Node syntax and repository browser checks passed; Nix daemon and socket-based
  fixtures were blocked by the member sandbox; the lead ran the socket-based
  Go checks from its Nix environment. The commits include explicit Load-all
  and stale-settings browser fixtures.
- Lead Nix shell entry passed. Its default `GOFLAGS=-mod=vendor` needs a
  `-mod=mod` override for source-worktree quick checks without a vendor tree;
  `TestShippedBrowserClientMatchesSessionAPI` then passed with loopback sockets.
  The complete `internal/teamruntime`, `internal/web` and
  `cmd/workspace-portal` Go package suites passed from the lead environment
  (`GOFLAGS=-mod=mod`, 2026-09-30), including socket-based web fixtures.
- First-unit follow-up adds live browser fixtures for Load-all retention,
  bounded batching, failure retry and stale settings reads. Node syntax, Ruby
  creation tests (11 runs/73 assertions), repository navigation contracts and
  `git diff --check` pass. The new Playwright fixture has not yet run; it is
  reserved for the post-review browser check. The lead applied the required
  user-facing-writing pass to the new guide paragraph and settings error.
- The GitHub-only repository origin boundary preserves manifest and API
  compatibility.
  It is committed at `91cd9fbb3971f6b1c5227204b02df32ceb1d6c64` with
  a clean worktree. Repository, manifest, web/template and browser-navigation
  quick checks pass. The lead applied the user-facing-writing pass before
  commit. Its live Playwright fixture remains for post-review verification.
- The immutable staged/unstaged snapshot unit is coded and locally checked in
  the `dev-workspace` feature worktree; its commit is pending. It includes
  non-ignored untracked files, ephemeral comparison IDs and frozen previews.
  The repository package, focused web API tests, Node syntax, browser
  navigation contract, formatting and diff checks pass. Live Playwright
  coverage remains for post-review verification. The lead applied the
  user-facing-writing pass to snapshot errors, notices and guide text.
- `implementer0` is assigned the next unit: bridge-mode, side-by-side React
  WebUI integration in `vpsfree-dev-workspace`, with the PHP UI retained.
  Workspace model policy and configuration pins follow.
- An early capture review found a full tracked-file scan in the draft reader.
  The member proved Git's `ls-files -m`, `diff-files --name-only` and porcelain
  status can invoke hostile clean filters. The accepted [design clarification](design.md)
  uses stage/debug index stats and no-follow lstat to select candidates before
  bounded reads. Oversized candidates will be metadata-only with an explicit
  “content not compared” warning and unknown line totals. Tests must prove
  hostile filters do not run and unchanged large files are not opened.
- The accepted gitlink clarification keeps unstaged review of unrelated files
  available. Frozen `unverifiedSubmodules` metadata sits outside changed-file
  and line totals, with a “working state not inspected” notice. It does not
  claim a submodule is changed, clean or dirty; staged/committed gitlink diffs
  retain their existing behavior.
- The `vpsadmin` worktree-add command returned nonzero from an inherited
  Overcommit post-checkout signature check, after creating and registering the
  worktree. Branch, portal registration, exact HEAD and clean status were
  verified; no vpsAdmin files were edited. No vpsAdmin commit is planned.
- `architect0` completed the [design correction](design.md) for the WebUI
  cluster unit. The extension's packaged vpsAdmin smoke input predates the
  required OAuth client fields; enabled smoke must pin selected compatible API
  `5c76e329` or a proved descendant. A separate runtime seed must follow
  database/general seeding and credential preparation. Existing HaveAPI CORS
  already supports the token header without cross-origin cookies. Bridge is
  the acceptance path; enabled local mode must refuse until both browser and
  BFF can reach one exact provider origin. Recovery keeps the selected
  compatible API/schema while disabling React if needed.

## Phase checklist

- [x] Verify there is no current initiative and create an isolated session.
- [x] Verify the retained roster and saved access.
- [x] Record the approved plan and compatibility/deployment constraints.
- [x] Complete and accept the architecture/verification brief.
- [x] Create/register project worktrees from current remote defaults.
- [ ] Implement and commit all intended changes with quick checks.
- [ ] Complete mandatory independent review and reconcile findings.
- [ ] Run long integration/build verification through a Luna watcher.
- [ ] Deploy the reviewed portal package and verify it is ready for use.
- [ ] Prepare whole-branch history/migration inventory and handoff.

## Next actions

- Commit the checked snapshot unit. Implement the vpsFree cluster, then the
  workspace policy/pin changes. Apply the user-facing-writing pass before each
  implementation commit.

## Documentation

- [Design and verification brief](design.md)
- [Team sandbox verification note](../../notes/dev-workspace/2026-09-30-team-sandbox-verification.md)

## Repositories

- `dev-workspace`: branch `2026-09-30-portal-review-improvements`, worktree
  `worktrees/2026-09-30-portal-review-improvements/dev-workspace`, initial base
  `7c133c562ac51076c1f45af46e180f8bfbabe836`.
- `vpsfree-dev-workspace`: same branch name, worktree
  `worktrees/2026-09-30-portal-review-improvements/vpsfree-dev-workspace`,
  initial base `bd961682cecb0b3b2bf729a53d2e08bda3d48eb2`; current upstream
  `6a0a2eb873e7cb376092c74bdf82fc2c51c349da` is incorporated.
- `workspace`: same branch name, worktree
  `worktrees/2026-09-30-portal-review-improvements/workspace`, initial base
  `d66bda525c823fe0ce52ea9a1c35550f147b569c`.
- `codex-web`: same branch name and worktree under that initiative group,
  initial base `d210d3f7cc93981d0ab163b1fcf0718f9587f47e`. It is currently
  a read-only comparison with no changes planned.
- Read-only dependency: `vpsadmin-webui` at reviewed head `534caa83`.
- `vpsadmin`: same branch name and clean worktree under that initiative group,
  base/current head `5c76e3290481b297dcd0baa76d246133f0353d8f`;
  read-only source required by the cluster runner.

## Commands run

- `dev-session current`
- `dev-session start portal-review-improvements --team delegated ...`
- `dev-session team list 2026-09-30-portal-review-improvements --as-is`
- `dev-session worktree add ...` for the five registered repositories above.

## Results

- Stable portal URL:
  `https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-30-portal-review-improvements/`

## Open questions

- None. Native browser find and side-by-side WebUI placement were selected
  during planning.

## Cleanup
