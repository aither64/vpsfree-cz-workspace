---
lifecycle: active
---

# 2026-10-18-unrestricted-team-access

## Status

Implementation in progress. This external conversation owns the newly created
initiative; no pre-existing session was selected or modified. The session was
created tracking-only and currently has no retained roster. Lead owns design
and implementation; required independent review uses installed catalog fallback.

- [x] Plan and user decisions established.
- [ ] Detailed design and implementation.
- [ ] Quick checks and committed final branch history.
- [ ] Independent final review.
- [ ] Packaged/live verification.
- [ ] Coordinated deployment and deployed acceptance.
- [ ] Authorized integration, exact-head proofs and reservation completion.

## Next actions

Finish schema-6 integration, native utility configuration and focused checks.
Prepare a retained native conversation solely for ordinary coordinator identity;
the external lead supervises foreground operations and retains implementation.
This is a genuine routing handoff checkpoint needed to preserve the exact
committed tracking baseline before native conversation creation. No threadless
bootstrap or ownership bypass is authorized.

## Documentation

## Repositories

codex-web, dev-workspace, workspace and vpsfree-cz-configuration; all target master.

All four worktrees are under worktrees/2026-10-18-unrestricted-team-access;
branches share that slug. Initial bases are in portal.yml. codex-web final
functional commit is currently 4a2b49ecff8bca628272e5d107cb09a67698247f,
published after consolidating queue/protocol acceptance into the same commit.

## Commands run

## Results

Confirmed original failure source: member policy chooses read-only/workspace-write
and shared client rejects danger-full-access. Host operator config already uses
danger-full-access/never; Nix daemon socket permits ordinary connections.

Integration authorization: user said "when it is deployed and verify, you can
merge it" and selected "All four repositories" in the scope question. Covers
codex-web, dev-workspace, coordination workspace and vpsfree-cz-configuration into
master, conditioned on successful deployed verification.

## Open questions

## Cleanup

## Verification evidence

Environment preparation watcher prepare_nix_environments used installed
Luna/low utility policy and completed three pinned environment exports plus
configuration bundle/hook install and signing, all exit 0. Mode-0600 exports
and GC-rooted profiles remain local. Configuration checkout hook initially
failed before gems existed; setup was repaired in the same checkout and
registration retried successfully without bypassing hooks.

Focused codex-web lifecycle/send/queue/retry tests passed. Focused runtime
catalog, member policy, peer delivery and browser/team tests passed. The first
browser run read the host /etc provider catalog; subsequent checks select a
nonexistent session-local catalog to isolate fixtures. A later Unix socket
fixture exceeded path length because exported TMPDIR nested Nix directories;
checks use TMPDIR=/tmp. Neither failure required source changes.

No active superseded codex-web CI run remained after the force push; the old
head run was complete and the current head run was in progress.
