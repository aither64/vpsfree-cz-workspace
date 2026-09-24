---
lifecycle: active
---

# Team settings drafts and member write access

The original Team-settings package is deployed on aitherdev, and a new
architect member successfully wrote to this initiative's worktree. At the
user's later request, a role-neutral `team update-access` command is committed
and pushed with exact downstream pins. Review, final checks, activation, and
the selected older architect's live write canary passed: ready, awaiting merge
approval. The shared checkout remains dirty with unrelated work, which has
not been staged. This shell has no trusted development-session binding, so
this is a separate initiative.

## Next actions

1. Await explicit approval for default-branch integration of generic
   `dev-workspace`, `vpsfree-dev-workspace`, and workspace `master`. Keep this
   initiative active and its feature refs retained until then.

## Evidence and decisions

- `architect0` in the observed team has a saved `read_only` policy;
  `implementer0` has `workspace_write` in both the roster and Codex rollout.
- The implementer's `dev-session current` fails opening
  `/home/aither/.local/state/dev-workspaces/transition.lock` for writing from
  its workspace-write sandbox. That failure does not prove its worktree is
  read-only.
- The user initially chose not to migrate existing architects, then explicitly
  selected `2026-09-23-storage-redesign` for a one-member exception. Its
  `architect0` is now `workspace_write`; `implementer0` was already
  `workspace_write` and was not changed.
- OpenAI documentation confirms workspace-write permits edits within the
  writable workspace, while protected paths and paths outside it remain
  constrained. See <https://learn.chatgpt.com/docs/agent-approvals-security>.

## Repositories

- `dev-workspace`: `worktrees/2026-09-24-team-settings-write-access/dev-workspace`,
  branch `2026-09-24-team-settings-write-access`, base `88587b0`, current head
  `9e97536`.
  Commits: `fcdb5d7` (portal draft preservation and access display), `e9a8c63`
  (read-only host transition lock for inspection commands), `c44b1e7` (review
  remediation for failed-save status and legacy access labels), `4763ab8`
  (host-lock fixture), `bb45ad3` (profile-switch test timing), and `2f9beb3`
  (frozen direct-team snapshot validation), `9c8eca9` (explicit candidate-entry
  switch), `e4debd7` (quiesce with the installed generation), and `9e97536`
  (explicit retained-member access override). This feature
  branch is pushed; default-branch integration is not approved.
- `vpsfree-dev-workspace`: `worktrees/2026-09-24-team-settings-write-access/vpsfree-dev-workspace`,
  branch `2026-09-24-team-settings-write-access`, base `8f06fdb`, current head
  `1a022c2`. Its single consolidated pin commit selects generic `9e97536`. The feature branch is pushed, with
  no default-branch integration approval.
- Workspace: `worktrees/2026-09-24-team-settings-write-access/workspace`,
  branch `2026-09-24-team-settings-write-access`, rebased onto shared master
  `140fb4e0`, current head `ff0cc0a` (future architect policy/lead guidance,
  then consolidated extension pin). Its pin selects extension `1a022c2` and generic
  `9e97536`. `git range-diff` confirmed
  the rebase preserved both patches.
- Stable portal URL:
  <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-24-team-settings-write-access/>.
- Project documentation changed in the generic runtime's portal guide and
  workspace-host documentation, and in the site team's role guidance. A
  reusable local browser-check caveat is recorded at
  `notes/dev-workspace/2026-09-24-local-portal-browser-check.md`.

## Verification

- Ruby read-only lock tests passed, including a non-writable state directory,
  missing lock, and a package-generation change while blocked on an exclusive
  transition. Focused suite: 13 runs, 53 assertions.
- Node syntax checks passed for the portal application and browser regression.
- Focused Go rendering test passed in module mode. The first default-mode Go
  invocation stopped before executing tests because this checkout's vendor
  metadata is inconsistent with `go.mod`; no dependency files were changed.
- Nix evaluation confirms future architect and implementer access is
  `workspace_write`, while reviewer access remains `read_only`.
- `git diff --check` passed in all feature worktrees.
- The first mandatory review used one standalone `gpt-6-sol`/`xhigh` reviewer
  for general, architecture, scope, and risk lanes (High risk: member sandbox
  policy and host transition lock). It found a Blocking package pin gap, an
  Important failed-save status loss after an unchanged POST, and an Advisory
  mislabeled legacy access value. The pin chain and both UI cases are fixed in
  committed follow-ups. No other findings were reported. The same reviewer
  inspected the cross-repository pin changes and found no remaining findings.
  Later fixture and timing-only fixes and final SHA pin updates received
  focused verification; the review workflow does not require a new
  whole-change review for those narrow follow-ups.
- Extension focused Ruby policy tests passed (2 runs, 18 assertions) and its
  `nix flake check --no-build` evaluated successfully. Site instruction tests
  passed (4 runs, 48 assertions) and its `nix flake check --no-build` evaluated
  successfully. The prior site lock resolved extension `a5409b0` and generic
  `bb45ad3` exactly; the current lock resolves `82dc72e` and `e4debd7`.
  Node syntax and focused Go rendering tests passed after
  the UI review fixes.
- Initial generic CI run `35973324463` and its transitive extension run
  `35973443953` failed because a deployment-flags fixture omitted the now
  required pre-existing transition lock. Generic commit `4763ab8` creates the
  lock in that fixture; 14 focused Ruby tests then passed.
- Generic CI run `35974101203` reached Go tests but hit an existing
  timing-sensitive compensated profile-switch test: its 100 ms observation
  pause consumed half of the request's 200 ms lock deadline. Generic commit
  `bb45ad3` reduces the pause to 10 ms without weakening the lock/generation
  assertions; 20 focused repetitions passed. The matching generic CI run
  `35974679082` and full local generic package check both passed.
- The first local browser run lacked Playwright modules. After supplying the
  pinned Nix Playwright package and browsers, the full browser suite failed in
  the pre-existing page-lifecycle timing test with local TLS handshake errors;
  the new Team-settings browser subtest passed in isolation at `bb45ad3`.
  Browser evidence is under `/tmp/browser-deps-watch.GFm6mY/` and
  `/tmp/team-settings-browser-test.sfAnKd/`.
- At site pin `4f7f950`, the site instruction suite passed (4 runs,
  48 assertions) and `nix flake check --no-build` passed. Full extension and
  site package checks passed, as did extension CI run `35975338558`.
- The first `workspace-host switch --source` stopped before changing the
  profile: the installed host validator rejected the *ready* schema-3
  creation journal for `2026-09-23-storage-redesign`. Read-only inspection
  showed a valid expanded snapshot with saved read-only architect access.
  The host validator only accepted legacy snapshots, while `dev-session`
  already accepted expanded snapshots. The foreign session was not changed.
  A focused host-validator fix now accepts both frozen shapes and either
  saved architect access in expanded snapshots. Syntax and the focused host
  tests pass (19 runs, 95 assertions). The standalone `gpt-6-sol`/`xhigh`
  reviewer found a Blocking deployment deadlock: the installed command still
  rejects the journal, while a candidate command fails the generation guard.
  An explicit candidate-entry switch was reviewed at generic `9c8eca9`.
  It requires the exact source package and an unchanged installed profile,
  then runs the ordinary transition checks. Focused profile transition tests
  passed (34 runs, 179 assertions), including a ready expanded journal and
  candidate identity/unfinished-creation refusals. Running only the profile
  test file initially failed before assertions because its shared
  `TransitionHost` test fixture is defined in `suspension_test.rb`; loading
  both files resolved that test-only dependency. The same reviewer inspected
  the bridge and found no remaining findings across general, architecture,
  scope, and risk
  lanes. Its only residual test gap was no candidate-specific injected
  post-selection failure; existing tests cover the shared recovery path.
  Generic `3e34df5` only narrowed the reviewed documentation wording;
  extension `86eefb6` and site `471a495` pinned it exactly. All three full
  local package checks and exact-head CI runs passed.
- The first candidate-entry activation stopped before profile selection while
  quiescing sessions: it invoked its own `dev-session`, which rejected the
  still-selected old profile. The profile remained on the old package.
  Generic `e4debd7` now quiesces and restores pre-selection failures through
  the selected old package and restores after selection through the candidate.
  Its integrated test verifies the helper path, generation, failure recovery,
  and retry (34 runs, 185 assertions). The first local test run had three
  failures because a new test double stubbed every `capture_env!` call,
  including cluster checks; limiting the stub to quiesce calls fixed it.
  Extension `82dc72e` and site `9f482e3` pin the amended generic head.
  All three are pushed. The same Sol/xhigh reviewer found no issues in the
  general, architecture, and risk/compatibility lanes. Generic and composed
  site package checks passed at the exact heads, and extension CI run
  `35980072115` passed at `82dc72e` with `nix flake check` and
  `devcluster-check`. The first activation retry stopped before profile
  selection because `2026-09-23-storage-redesign` had an `inProgress` Codex
  turn; the installed profile and terminal clients were restored. The user
  paused that session, and the second retry completed successfully. The
  selected package is now
  `/nix/store/ghf6928pwwcr5j0cabjgqjrgqdhmwmb1-dev-workspace-0.2.0`.
  `workspace-router.service` is active; an unauthenticated HTTPS request
  returned the expected 401 (the local curl lacked the internal CA).
  `dev-session team add` created `architect0` in this initiative with
  `workspace_write`; its assigned Codex turn created the requested one-line
  file in the generic worktree. The file contents were verified and the
  temporary file was removed. The canary changed only this initiative's
  roster.
- Repository comparisons were recaptured for the current exact heads with
  bases generic `88587b0`, extension `8f06fdb`, and workspace `140fb4e0`.
- The later `team update-access` request is committed at generic `9e97536`.
  It validates the saved purpose and requested access, requires the selected
  member thread to be idle, preserves its thread/instructions/model/effort,
  and clears only that member's catalog digest for a manual override. The
  focused Go runtime test passed; the portal command package compiled, Ruby
  syntax passed, and both downstream `nix flake check --no-build` evaluations
  passed. The ambient default Go test invocation still fails before tests
  because this checkout's vendor metadata disagrees with `go.mod`; the
  focused test passed with `-mod=mod`. A fresh standalone catalog reviewer
  (`gpt-6-sol`/`xhigh`) found no issues across general, architecture, scope,
  and risk lanes at the initial committed access head. Extension CI run
  `35983321836` then exposed a Ruby helper call that omitted the new access
  keyword; this was the root cause, not an infrastructure rerun. Making the
  keyword optional in the helper was a narrow remediation, and the exact
  failing Ruby test passed (1 run, 6 assertions). The review workflow does
  not call for a new review of that one-line correction. Generic `9e97536`,
  extension `1a022c2`, and site `ff0cc0a` are pushed with exact pins. Generic
  and site full package checks passed on these final heads. Generic CI run
  `35984153808` passed at `9e97536`; extension CI run `35984275670` passed
  at `1a022c2`, including `nix flake check` and `devcluster-check`.
  Candidate-based activation from site `ff0cc0a` completed and selected
  `/nix/store/rvnahc2nfixg7v2brzm04v6cfri2ibaz-dev-workspace-0.2.0`.
  The selected storage-redesign `architect0` was idle and its saved access was
  changed from `read_only` to `workspace_write` without changing its thread
  `01a0d230-6806-7c50-88c2-57970a8f9d1d`, Sol/xhigh settings, or
  instructions. The member's next turn wrote the exact temporary canary in
  its `vpsfree-maintenance-tasks/2026-09-24-storage-inventory` worktree.
  The marker was removed; the worktree still has only its three pre-existing
  modified files. `implementer0` remains `workspace_write` and `reviewer0`
  remains `read_only`; neither thread was replaced. No other roster was
  changed by the access operation. The package logs contain warnings about
  unrelated legacy or detached worktrees, but activation returned zero.
  The old-head generic and site local checks were stopped as superseded; their
  interruption is not a completed failure. Superseded extension run
  `35983057833` was canceled after its branch head was replaced.
