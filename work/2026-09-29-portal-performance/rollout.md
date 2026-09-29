# Aitherdev portal rollout

Status: corrected and reviewed recovery candidate built and rooted; two authorized paused
archive journals must complete before the user-profile switch. The site application is selected from the user
profile, not from `vpsfree-cz-configuration` system pins. No NixOS, nginx or
`confctl` change is part of this rollout.

## Preconditions

- Commit and pin the reviewed `codex-web`, `dev-workspace`, and
  `vpsfree-dev-workspace` feature revisions into the workspace feature worktree.
- Complete focused checks, mandatory independent review, package checks and
  browser compatibility checks before switching the live profile.
- Record the exact four feature heads, consuming `flake.lock`, current
  `workspace-host status` package and switch generation in `state.md`.
- Check pending lifecycle/package journals and current authority generation.
  Resume an unfinished transition before any conflicting switch.

## Prepared switch

From this workspace, build the complete consuming package from
`worktrees/2026-09-29-portal-performance/workspace`. Inspect the pin-chain diff
and package metadata, then run:

```sh
workspace-host switch --source /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-29-portal-performance/workspace
```

After the switch, confirm `workspace-host status`, portal and App Server service
health, session/team/authority access, a bounded page on the target conversation,
older-history loading, composer and pending/queue behavior. Run the 30-load
browser benchmark without a scan and with overlap from the scheduled archive
worker. Record all samples, failures, p95, response sizes, CPU and lock errors
without recording conversation content.

## Recovery

`workspace-host rollback` intentionally refuses older package generations
because team registration is forward-only. If the switch is interrupted, retry
the supported switch path first. If the new package fails acceptance, prepare
a **newer** package that restores the previous application behavior while
retaining current state readers and site composition. Review and switch to that
newer recovery package. Do not retarget profile symlinks, edit generation
markers or truncate state by hand.

## Execution record

- Pre-switch package: `/nix/store/zpfyl4kkdmv6c7r8a0r6rl1s4wpikkla-dev-workspace-0.2.0`.
- Exact feature chain: `codex-web` `d210d3f7cc93981d0ab163b1fcf0718f9587f47e`, `dev-workspace` `e58f8f61ce43058aba49361a0b3bd1ecd98af866`, `vpsfree-dev-workspace` `9c9833579e148e108b5811d618c81ec497b809bf`, workspace `50c3dcf74f7eb816671caf4efd365f9c466e387a`.
- The generic runtime package build passed in 3m14s. Codex-web, generic runtime, and vpsFree extension CI passed for their exact feature heads.
- The complete consuming workspace package build passed at `238ee9a684579e732fd3bab3c37409c892a05ebe` in approximately 176 seconds.
- `workspace-host status` confirmed the old package is active and the portal, App Server, router, and tmux services are running. No unfinished package-transition artifact was found before the switch.
- The first watcher correctly refused because it inspected the dirty coordination checkout instead of the clean source worktree. No switch command ran.
- The corrected switch verified clean source head `238ee9a684579e732fd3bab3c37409c892a05ebe`, then failed closed before activation because archive journals for `2026-09-26-codex-queue-ledger-capacity` and `2026-09-27-architect-lead-policy` remain paused at `tracking_committed`.
- Both affected records are already under `archive/` with `lifecycle: complete`; the remaining journal work is runtime retirement. The latest scheduled worker retry deferred the first because a team member thread is already archived and the second because multiple threads share its archived tracking cwd.
- The old package remains active. Manual repair/resumption touches other sessions and requires explicit user direction; do not bypass the lifecycle gate.
- The user explicitly authorized recovery of both named journals. The corrected consuming package passed at `50c3dcf74f7eb816671caf4efd365f9c466e387a`; `candidate-workspace-package` resolves to `/nix/store/yhnzp6nmq4ngmlvh0wxxhzkbpzda4c0y-dev-workspace-0.2.0`, and its runtime contract matches the selected predecessor byte-for-byte. Dev-workspace Actions run `36641815619` and vpsFree extension run `36641987050` passed at their exact corrected heads.
