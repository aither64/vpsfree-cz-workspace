---
lifecycle: active
---

# 2026-11-23-kernel-retention-policy

## Status

- [x] Confirmed the current request is for a proposal, not source edits or live pruning.
- [x] Scoped the revision: direct weekly staging commits, no PRs, and cleanup of kernel-owned livepatches/tests rather than retention exemptions.
- [x] Revised the [implementation and verification plan](design.md) to require a kernel-entry check on incoming `staging` PRs and add stable-by-default test-authoring guidance.
- [x] User authorized feature branch implementation (“proceed with implementation”). This does not authorize integration into `staging`, repository settings changes, or activating production pruning.
- [x] Registered the vpsAdminOS feature worktree at `worktrees/2026-11-23-kernel-retention-policy/vpsadminos`, branch `2026-11-23-kernel-retention-policy`, base `b86287c105b749827cd63632ac35936533910f63` (`origin/staging`).
- [ ] Implement and run quick checks, then request independent review before longer verification.

| Package | Owner | Acceptance | Status |
| --- | --- | --- | --- |
| Revised design (`design.md`) | `architect0` | Required PR check, stable test guidance, cleanup and direct-push safeguards | Accepted |
| A: backfill, offline validator, hook, PR check | `implementer0` | Review dates, staged-index and CI checks; diagnose existing hooks | Executing |
| B: stable tests, instructions and owned registrations | `implementer1` | Reusable tests track stable; release-specific registrations drop with owner | Executing |
| C: owned livepatches and private package data | `implementer2` | Exact ownership, shared-target safety, no-build evaluation | Executing |
| D: retention tooling and weekly writer | `implementer3` | Pure policy/collector executing; writer awaits settled A–C interfaces | Executing (offline portion) |

## Next action

Resolve the worktree hook trust/tooling before giving a shared index/commit window; let A–D continue in disjoint paths. Required-check enforcement and weekly writes remain out of scope for branch development. Verify fleet coverage and the actual staging rules before activation.

## Setup evidence

- Initial `dev-session worktree add` linked the requested checkout but reported a missing Overcommit post-checkout signature. A repeated invocation verified and registered the existing exact worktree. Overcommit trust is shared by default across linked worktrees, so do not rotate shared signatures without isolation.
- Workspace tracking fast-forward initially hit a verified ownerless, zero-byte stale index lock (moved aside), then refused to overwrite three other-session tracking paths. Verified the paths were byte-for-byte identical to the incoming blobs, and used a scratch worktree override under the tracking lock to fast-forward only the workspace Git base without rewriting those working files.
