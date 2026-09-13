---
lifecycle: active
---

# 2026-09-13-portal-file-links

## Repositories

- Shared coordination checkout: /home/aither/workspace/ai/vpsfree.cz, master.
- Feature slug/branch: 2026-09-13-portal-file-links.
- Generic worktree: worktrees/2026-09-13-portal-file-links/dev-workspace,
  base origin/master (8f75ece30462b184065f21867508af5e14365c4a).
- Consumer worktrees: vpsfree-dev-workspace, workspace and
  vpsfree-cz-configuration under the same worktree group.

## Status

The feature is deployed on aitherdev and merged into all four remote master
branches. Local integration checks passed, and all feature/integration worktrees
have been removed. The session remains open for follow-up. The user explicitly
requested no waiting for the new default-branch workflows, so their running
status is recorded in integration.md and the lifecycle remains active.

Current heads (all branches 2026-09-13-portal-file-links):

- dev-workspace: f41d4220dd1d5ade08ba3bb28f964e9570a11ed9,
  base 8f75ece30462b184065f21867508af5e14365c4a.
- vpsfree-dev-workspace: 9f3142248f6e40d602115aa0fad66701595ef232,
  base 213a3db57dea9298f61309eb157c0853f2310e9b.
- workspace: 9c3e33c03654ca6ddc502518d936e71e7480ae1b,
  base ec3f99b42a7f6b850c3eb14219ae796ccacba98a (initial tracking commit).
- vpsfree-cz-configuration: 3d9ffa45c7e0388c96434fd3a6127d0a54c0b9ea,
  integration base c8e5dadcf361e3f86b86d43cf8836c7f296b75ef; original base
  8ef765d339ac792ef4f01a5c7a160e48600adcaf.

The four worktrees were under worktrees/2026-09-13-portal-file-links/<name>.
They are now removed; portal.yml retains each repository and its exact final
head. Both local and remote feature branches are preserved.

## Commands run

- Inspected current implementations, local AGENTS.md files, generic and Codex
  repository refs, workspace package pins and previous deployment notes.
- dev-session current initially reported no current session. Started
  dev-session start portal-file-links --no-codex --no-attach --json.
- Verified current with DEV_SESSION_SLUG and DEV_SESSION_WORKSPACE set to this
  exact session and workspace. Read mandatory review, handoff, writing and
  English humanizer skills.
- Fetched workspace and generic origin. Shared master matches origin/master;
  unrelated dirty tracking records are preserved.

## Results

Root cause: shared portal Markdown renderer keeps absolute file destinations as
site paths; routing has no corresponding handler. Existing review editor already
supports full-file mode and highlighted line reveal. Existing artifact opening
and repository resolution provide the boundaries to reuse.

- Focused checks passed in generic nix develop: Go repository/session/web tests
  matching TestSource, TestReviewMetadata, TestSessionStyles and TestArtifact;
  source-file.js and editor.js syntax; git diff --check. Tests cover escaping,
  original transcript preservation, redirects, live edits, staged additions,
  literal filenames, untracked and metadata rejection, symlinks, FIFO rejection,
  source limits, archived exact commits and curated artifacts. Initial archive
  fixture lacked required finalized_at; corrected the fixture and reran green.
- Generic Actions 34771566528 passed at 6735370851447ec62f6fbce25175c21db97c4686.
- Workspace package evaluation passed (nix eval default drvPath). Actual
  deployment checker passed with both generic pins at 6735370.
- Configuration created successfully but its checkout hook initially reported
  missing ambient gems (existing documented worktree-hook behavior). Re-entered
  its nix develop, registered the existing worktree, and ran confctl inputs
  channel set --commit dev-workspace devWorkspace 6735370. Retained the generated
  commit message unchanged, including its allowed text-width warning.
- Running workspace unit tests inside configuration's bundled Ruby environment
  failed to load minitest/autorun. Rerun in the workspace's own Ruby environment;
  no implementation change is required.
- Workspace deployment-contract unit tests passed with nix shell nixpkgs#ruby:
  3 runs, 14 assertions, no failures/errors/skips.

Review classification: high due to a remote file-read authorization boundary and
cross-package deployment. Required lanes: general, architecture, scope and risk;
each uses gpt-5.6-sol/xhigh. No migration, new persisted state, or Codex protocol
change. The local development host operator is trusted; remote inputs are not.

## Review and integration validation

- General, architecture, risk and scope reviews completed at the initial heads
  recorded in review-packet.md. No blockers. The important artifact validation
  mismatch and three advisories were fixed and folded into the final heads.
  See review-reconciliation.md for exact finding dispositions and focused tests.
- Final generic Actions 34772498526 passed at f41d422. Organization Actions
  34772521732 passed both its flake check and devcluster-check at 9f31422.
- `nix flake check --print-build-logs` passed in the generic worktree, including
  the host module VM checks. No local kernel build was required.
- `nix build .#default` passed in the workspace worktree. Packaged Go tests and
  Ruby suites passed (297 runs / 2989 assertions / 12 skips; 73 runs / 438
  assertions / 3 skips). Package: /nix/store/gzhi8hrjb7j2pbzlxs0bcv4abqkg2r7q-dev-workspace-0.2.0.
- Deployment contract checker passed with final generic pins f41d422 in both
  the user package and configuration. `confctl build -y
  cz.vpsfree/machines/aitherdev` passed, generation 2026-09-13--19-47-18.
- Packaged Firefox fixture passed at desktop 1440x1000 and narrow 390x844:
  original absolute URL redirects, referenced line visible and highlighted,
  gutter navigation, reload/back/new tabs, copy link, invalid/missing lines,
  rapid hash changes, HTML shown as literal source, curated artifacts, exact
  archived commit after worktree removal, pre-feature editor asset crossover.
  Screenshots visually checked; see browser/results.json and browser-check.py.
- Authenticated pre-deployment baseline: health 200, example link 404;
  unauthenticated health 401. Credentials are read in-process only.

## Deployment and live verification

- Dry activation passed for confctl generation 2026-09-13--19-47-18.
- `workspace-host switch --source <workspace feature worktree>` passed and
  selected user profile 37, package gzhi8hrjb7j2pbzlxs0bcv4abqkg2r7q.
- `confctl deploy -y --generation 2026-09-13--19-47-18
  cz.vpsfree/machines/aitherdev switch` passed; 2 health checks passed.
  Active system: /nix/store/6zn634xr6m6rn0vvxiv4fvrzzrk3mk7l-nixos-system-aitherdev-26.05.20260911.21a67dc.
- Router, portal, Codex and nginx are active. Router PID 1822368 and portal PID
  1822372 use the new package. Codex PID 1090021 is unchanged (0.154.0), so the
  application package update did not interrupt the shared Codex process.
- Both exact user example URLs now redirect with HTTP 302 to the viewer and
  return HTTP 200 file content. Firefox confirms lines 10 and 95 selected and
  highlighted with syntax coloring. API text equals each current local file.
  See live-browser/results.json and the two live screenshots.
- The first live browser assertion normalized expected indentation with strip(),
  but code lines preserve indentation. Corrected the harness to compare DOM
  textContent with the exact expected line; rerun passed. No product change.
- Unauthenticated file/health requests return 401; artifact traversal returns
  400. Post-activation session, health and declared review artifact reads all
  return 200. No credentials are stored in artifacts or browser profiles.

## Default-branch integration

- User authorized merging into default branches and cleaning up. Session
  archival/deletion is not requested; retained feature branches stay available.
- Fresh fetches confirm generic and organization master are unchanged. Workspace
  master is an ancestor of the reviewed feature. Configuration master advanced
  to c8e5dadc with password-recovery changes. Rebased our generated input commit
  without conflicts to 3d9ffa45c7e0388c96434fd3a6127d0a54c0b9ea.
- `git range-diff` reports the rebased configuration commit as identical (`=`);
  only its parent changed. The reviewed implementation and package pins are
  unchanged, so no review rerun is needed. Integration checks run from fresh
  detached worktrees under worktrees/<slug>/merge/<project>.

- Generic and organization flake checks passed in the fresh merge worktrees.
  Workspace deployment-contract tests passed (3 runs, 14 assertions). The
  aitherdev build and matching runtime-pin check passed at the rebased config
  head, generation 2026-09-13--20-55-09.
- All four remote master heads were verified against the final local and remote
  feature heads. All merges were fast-forwards. The shared workspace stayed on
  master, preserving unrelated changes.
- Generic master CI 34776166574 and organization master CI 34776215446 were
  running at handoff. Per the user's explicit instruction, did not wait for
  these workflows. Earlier feature CI at these exact application heads passed.
- Integrated workspace package evaluation matches the deployed package. Portal
  health, session and sample file API remain HTTP 200 after worktree cleanup.
  See integration.md for the full integration and cleanup result.

## Open questions

None. User chose current worktree content with archived-final fallback and
verified repositories plus curated artifacts. Aitherdev deployment is authorized.

## Cleanup

All four feature worktrees and three temporary merge worktrees are removed.
Generated shell files, raw logs and temporary build/browser links are removed.
Feature branches, session records and curated evidence are retained.
Integration is authorized and complete; no archive or delete was requested.
No operator action is required to use the deployed file links.
One consolidated integration/cleanup checkpoint preserves the final record.
No extra tracking-only commits were made for individual implementation results.
Stable portal URL:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-13-portal-file-links/
