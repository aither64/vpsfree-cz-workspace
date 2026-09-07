---
lifecycle: active
---

# 2026-09-07-vpsfstatus-index-stale-2

## Repositories

- Canonical bare repositories: `repos/vpsf-status.git` and
  `repos/vpsfree-cz-configuration.git`; inspect `origin/master` and deployed pins.
- No feature worktrees or project code changes are currently needed.
- Workspace coordination checkout remains on `master`.

## Status

- Session created with an initial request.
- Verified `dev-session current` and `VPSFREE_DEV_SESSION_SLUG` both match
  `2026-09-07-vpsfstatus-index-stale-2`. Other sessions are untouched.
- Inspected the supplied screenshot: a regular sawtooth, roughly four minutes
  between resets, with peaks close to 300 seconds.

## Commands run

- `dev-session current`, workspace `git status`, repository `git grep` and
  `git show`, screenshot inspection.
- Read workspace orchestration, handoff and mandatory-review instructions.

## Results

- Located the alert in `modules/clusterconf/monitor/rules/vpsfree-web.nix`
  and the metric producer in `vpsf-status/exporter.go` and `index.go`.

## Open questions

- What determines the observed interval between successful renders?
- Are firing alerts caused by rendering, metric caching/scraping or rule timing?

## Cleanup

- Preserve unrelated shared workspace changes. No project mutations or
  background services have been started.
