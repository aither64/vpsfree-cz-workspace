---
lifecycle: complete
---

# 2026-09-18-archive-empty-branch-fix

## Current status

Implemented, reviewed, tested, deployed, and exercised by archiving the
affected session. The old `2026-09-14-kernel-history-fix` session archived
successfully even though its `vpsfree-dev-workspace` feature ref is absent on
the remote: its local head equals the recorded initial base. Its tracking
directory and five temporary worktrees were removed; retained feature refs
and archived records remain. All four implementation branches are now
fast-forwarded into their configured remote default branches. This initiative
is complete after the remaining session archive cleanup.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-18-archive-empty-branch-fix/

## Findings and decision

`2026-09-14-kernel-history-fix` had a local `vpsfree-dev-workspace` branch at
its recorded `initial_base_sha`, while the corresponding remote feature ref
was absent. The remote default branch already contained that commit, so this
was an unchanged local base rather than an unmerged feature. Archive fetched
the feature ref unconditionally and failed with exit 128.

The runtime now permits an absent remote feature ref only when the local head
matches the registered `initial_base_sha`. It always fetches and proves the
default branch, rechecks the feature ref after that fetch, and preserves exact
local/remote equality and ancestry checks whenever a feature ref exists.
Registered worktrees that disappeared still fail closed when their local
branch cannot be proven from the registration, preserving the existing
automatic-archive safety behavior.

## Final project revisions

| Project | Branch | Final commit | Remote status |
| --- | --- | --- | --- |
| `dev-workspace` | `2026-09-18-archive-empty-branch-fix` | `fe67863a2b8fcf3bb10e1b3a74220582e3283fa3` | pushed and merged into `master` |
| `vpsfree-dev-workspace` | `2026-09-18-archive-empty-branch-fix` | `ab74ed67b83f488f7825884b12a58c17c3ca3e2b` | pushed and merged into `master` |
| `vpsfree-cz-configuration` | `2026-09-18-archive-empty-branch-fix` | `6ac2068b3aea8c3669bb9fa81dc713034ea501bd` | pushed and merged into `master` |
| `vpsfree-cz` workspace | `2026-09-18-archive-empty-branch-fix` | `e4bfa8d34074951792398aabed10d5c299c9ae01` | pushed and merged into `master` |

The runtime commit centralizes initial and recovery archive proof in
`archive_branch_proof`, and adds coverage for unchanged unpushed branches,
changed unpushed branches, and interrupted archive retry. Documentation was
updated in `dev-workspace/docs/dev-sessions.md`. The extension and consuming
workspace pins make the runtime available to the deployed user package.

## Review and verification

Mandatory change review used fresh `gpt-5.6-luna` reviewers at low effort as
requested by the user. General, Scope, Risk, and the final Architecture rerun
reported no Blocking or Important findings. Architecture's initial finding
(duplicated proof logic and missing retry coverage) was fixed with the shared
helper and retry test, then rerun successfully. Remaining advisory limits are
that no fixture simulates a non-absence transport/authentication failure and a
feature ref created after the final absence check remains an unavoidable
remote-side race; the implementation rechecks after the default fetch and the
later archive reproof remains authoritative.

Quick checks on the final runtime passed: syntax, whitespace, the archive
focused suite (19 tests, 401 assertions), and the missing-worktree regression.
Final full checks, run by fresh Luna watchers, passed with zero failures and
zero errors for both `dev-workspace` at `fe67863` and
`vpsfree-dev-workspace` at `ab74ed6`:

- `/tmp/dev-workspace-flake-check-fe67863.log`
- `/tmp/vpsfree-dev-workspace-flake-check-ab74ed6.log`

## Deployment

`vpsfree-cz-configuration` pins `devWorkspace` to `fe67863`. Configuration
generation `2026-09-18--10-39-15` built successfully and passed both dry
activation and live deployment to `cz.vpsfree/machines/aitherdev`; system and
firewall health checks passed 2/2. The consuming workspace branch pins the
extension at `ab74ed6` and was switched successfully into the user profile.
The active package is
`/nix/store/fmqb032pkv81nf6fxvnzisp6kvj6xwid-dev-workspace-0.2.0`.

The first switch attempt from the generic runtime worktree failed because
that flake does not include the vpsFree extension's development-cluster
providers. It did not change the profile. The extension worktree also does
not expose the consuming default package. Switching from the top-level
consuming workspace succeeded and is the supported deployment path.

## Affected session archive result

`dev-session archive 2026-09-14-kernel-history-fix --as-is` completed with
`archived session`. The archived manifest records the unchanged local
`vpsfree-dev-workspace` head as both initial base and final head, while the
remote feature ref remains absent. `dev-session list` reports no active work
or worktrees for that slug. The unrelated
`2026-08-18-vpsadmin-password-reset` session and its cluster were not changed.

## Worktrees and next action

Current implementation worktrees:

- `worktrees/2026-09-18-archive-empty-branch-fix/dev-workspace`
- `worktrees/2026-09-18-archive-empty-branch-fix/vpsfree-dev-workspace`
- `worktrees/2026-09-18-archive-empty-branch-fix/vpsfree-cz-configuration`
- `worktrees/2026-09-18-archive-empty-branch-fix/workspace`

All four are clean and their exact heads are present on remote `master`.
Archive this completed initiative to remove its temporary worktrees and move
the durable tracking records under `archive/`; retain the feature refs.
