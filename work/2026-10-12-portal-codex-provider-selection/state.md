---
lifecycle: active
---

# Portal Codex provider selection

## Current status

Implementation is in progress under the user's "Implement the plan" direction.
This includes safe rollout on aitherdev through the configuration feature branch
and the workspace user profile. Default integration, archive/delete/session stops
and forced interruption remain unauthorized. Live settings are unchanged.

The lead owns design and source edits. This tracking-only initiative has no valid
native lead/retained roster; do not invent team settings or members. Mandatory final
review will use the installed review fallback. Temporary verification utilities
follow the installed watcher policy; they do not join a roster.

## Phase checklist

- [x] Load instructions and verify the isolated initiative.
- [x] Finalize the implementation and verification brief in design.md.
- [ ] Finish implementation and quick checks (in progress).
- [ ] Commit/publish exact heads and complete independent whole-branch review.
- [ ] Complete longer verification and scoped build/dry-activation.
- [ ] Deploy the host catalog and composed user-profile application safely.
- [ ] Verify previews and guarded subscription/Snajpa switching.
- [ ] Default integration (requires separate explicit user direction).

## Implementation checkpoint

codex-web has an explicit lifecycle provider override, an application-owned routing
resolver covering start/resume/fork/reconnect, and effective-response verification.
Focused routing tests pass. Calls without provider overrides retain their behavior.
No Codex version upgrade is included.

dev-workspace has initial catalog/state readers, LB usage/model probes, separate
provider limits caches, public status/switch/cancel endpoints, popup preview
controls, a host worker/native helper, reservation checks and additive runtime
contract fields. Existing focused Codex limits tests pass; Go packages compile
using an external temporary Go workspace connecting the local client worktree.
Ruby and JavaScript syntax checks pass. Implementation is unfinished, unreviewed
and undeployed. Recovery/terminal race handling, focused provider contracts,
protocol coverage and lasting documentation remain.

Configuration declares Snajpa plus the built-in subscription, retaining codex-lb
as the existing native ID and initial choice. Secrets stay in the private token
file. The first configuration worktree add hit missing Ruby gems outside Nix;
entering the declared development shell and installing Overcommit resolved it.
The worktree is now registered. No hooks were bypassed.

The environment watcher used installed verification_watcher policy
(gpt-6-luna/low, catalog digest
437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd).
All three Nix environment setup commands passed. Logs are private /tmp evidence;
environment dumps must never be printed or committed. No kernel builds occurred.

## Branches and ownership

All four repositories use branch 2026-10-12-portal-codex-provider-selection and
owned worktrees under worktrees/2026-10-12-portal-codex-provider-selection/.

- codex-web base/current pre-feature head: 7aff1632ee97c177e68c8bc45258abe055a087dd.
- dev-workspace initial base: 60c679c52c263a0fc7a4b08c5f83a291cfd89191;
  fetched/fast-forwarded base: 1a27453c0b67c8c24cbe1474d5a05607eb698a9a.
- configuration base: 1697613eab00a4bb0642b79c355c0b673b758a41.
- workspace base: edbb8d7b5ab25f715167ccc30d1119ee067060d7.

No feature commits yet. Initial tracking commit is 313ff5b2. Preserve unrelated
shared index/working-tree changes and all retained branches. Workspace feature
scope is the composed runtime pin; shared master stays put.

## Risks and next action

Native 0.160.0 loaded resumes ignore provider overrides. Cold resumes must carry
the retained model/effort; members rebind saved roster access/instructions. Codex
cgroups can contain VMs and the portal cgroup can contain tmux. A provider switch
must stop only a proved sole native daemon and preserve both boundaries.

Next: finish recovery/terminal journaling and admission races, add focused contracts
and docs, then publish exact client/runtime heads for downstream pins. Independent
review precedes long integration tests and production rollout.

Stable portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-12-portal-codex-provider-selection/
