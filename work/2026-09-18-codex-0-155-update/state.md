---
lifecycle: complete
---

# Codex 0.155.0 rollout for aitherdev

## Status

Codex 0.155.0 is deployed on aitherdev and active in the shared workspace
profile, portal and App Server. The exact final heads of all four feature
branches are fast-forwarded to their remote `master` branches. The source
feature branches are intentionally retained; their clean worktrees were
removed as the requested cleanup.

One unrelated development cluster was terminated during the App Server
systemd-service restart. Its terminal client was restored, but the cluster is
not this initiative's ownership to recreate.

## Next actions

No operator action remains for this rollout. Investigate App Server cgroup
ownership in a separate initiative before a future profile switch is allowed
to coexist with long-running development clusters.

## Documentation

The runtime README and `docs/dev-sessions.md` were checked. Existing durable
guidance covers profile/App Server pairing and rollback; this session records
the one-time site rollout and its evidence.

## Repositories

| Repository | Branch | Base | Worktree |
| --- | --- | --- | --- |
| dev-workspace | 2026-09-18-codex-0-155-update | fe67863a2b8fcf3bb10e1b3a74220582e3283fa3 | worktrees/2026-09-18-codex-0-155-update/dev-workspace |
| vpsfree-dev-workspace | 2026-09-18-codex-0-155-update | ab74ed67b83f488f7825884b12a58c17c3ca3e2b | worktrees/2026-09-18-codex-0-155-update/vpsfree-dev-workspace |
| vpsfree-cz-configuration | 2026-09-18-codex-0-155-update | 6ac2068b3aea8c3669bb9fa81dc713034ea501bd | worktrees/2026-09-18-codex-0-155-update/vpsfree-cz-configuration |
| workspace | 2026-09-18-codex-0-155-update | e4bfa8d34074951792398aabed10d5c299c9ae01 | worktrees/2026-09-18-codex-0-155-update/workspace |

## Commands run

- Read applicable workspace, repository, documentation, lifecycle, deployment,
  verification, commit, review and monitoring procedures.
- Fetched the four remote default branches.
- Created the portal session with `--no-attach --no-codex`, model
  `gpt-5.6-terra`, and `xhigh` effort.

## Results

- Upstream `github:numtide/llm-agents.nix` revision
  `ddc89534b9a73cd99ff4d33656569ce3be6e6490` evaluates Codex to `0.155.0`.
- `workspace-host status` reports the active profile package and its Codex
  executable; the system and active App Server use Codex 0.155.0.

## Open questions

None.

## Cleanup

The user explicitly requested integration and cleanup. Retain the four local
and remote feature branches, remove their clean worktrees, and do not archive
the session because archival was not requested.

## Review preparation

All four feature branches are pushed and clean:

- `dev-workspace`: `18817f4bf60f9918932d980d5c91b92852ba3cfa`
- `vpsfree-dev-workspace`: `e170ea0ead2babef823aa415e2d1b354d1648173`
- `vpsfree-cz-configuration`: `c7ed1210fc90434e50de2b1e4752a7ae38d9a491`
- `workspace`: `1042c1f66106059c1f4b8378712e11a6d2d32a50`

Quick Nix evaluations of the generic runtime, extension, configuration and
consuming workspace each returned `0.155.0`; `git diff --check` passed for each
feature range. The configuration generated commits passed Nixfmt and
commit-message hooks. Its initial checkout hook lacked local gems outside Nix;
`nix develop --command overcommit --install` restored the declared hook setup.
No tracked files were changed by that repair.

The review packet is `review-packet.md`. This is high operational risk because
of deployment and App Server restart, but all commits are dependency pins. At
the user's explicit request, review is one General lane with
`gpt-5.6-terra`/`xhigh`; omitted specialist lanes are covered by concrete
protocol validation, build, dry activation and live verification.

## Review result

The single General review completed with a fresh `gpt-5.6-terra` reviewer at
`xhigh`; there were no Blocking, Important or Advisory findings. The result is
in `review-general.md`. The user explicitly requested this abbreviated one-lane
review; remaining operational risk is gated by the planned flake checks,
aitherdev build/dry activation, deployment, profile protocol/catalog validation
and idle service reconciliation.

## Long verification

A fresh `gpt-5.6-luna`/`low` watcher ran the authorized verification batch at
all four recorded heads. `nix flake check --print-build-logs` passed for the
generic runtime, extension and consuming workspace. `confctl build --yes
cz.vpsfree/machines/aitherdev` passed and produced generation
`2026-09-18--12-27-33`. The batch completed in about 6m23s with no unexpected
local vpsAdminOS kernel build. Full output is `verification-build.log`.

## Deployment and live verification

The exact built generation `2026-09-18--12-27-33` dry-activated successfully,
then deployed to `cz.vpsfree/machines/aitherdev` with all health checks passing:
`systemd` reported `running` and `firewall.service` reported `active`.

After deployment, `/run/current-system/sw/bin/codex --version` reported
`codex-cli 0.155.0`. `workspace-host switch --source` from the consuming
workspace feature worktree built profile generation 52, validated the Codex App
Server protocol contract, and completed the service transition. The active
profile Codex symlink resolves to the 0.155.0 store path, the active
`workspace-codex@vpsfree-cz` App Server uses it, and the portal command line
contains `--codex-version 0.155.0`. Both user services are active, no pending
Codex reconciliation file exists, and a TLS probe using the workspace public CA
reaches the portal with expected unauthenticated HTTP 401.

During the App Server restart, `workspace-codex@vpsfree-cz`'s systemd cgroup
also killed an unrelated long-running vpsAdmin development-cluster runner,
virtiofsd helpers and QEMU guests. The switch output restored terminal Codex
clients, but it did not restore those cluster processes. This initiative must
not alter another session's cluster; the observed cgroup-coupling behavior is
recorded in `notes/cross-project/2026-09-18-profile-switch-devcluster-cgroup.md`
for follow-up.

## Default-branch integration and completion

All integration was fast-forward-only. Remote `master` contains the exact
final feature head for each repository:

- `dev-workspace`: `18817f4bf60f9918932d980d5c91b92852ba3cfa`
- `vpsfree-dev-workspace`: `e170ea0ead2babef823aa415e2d1b354d1648173`
- `vpsfree-cz-configuration`: `c7ed1210fc90434e50de2b1e4752a7ae38d9a491`
- `workspace`: `dbbd29e6d64debde26a75113f339e77e6331891d`

`git ls-remote` confirmed every remote default head above. The workspace
feature was rebased onto the shared master before its fast-forward integration;
the reviewed package change remains the same `flake.lock` pin. The deployed
profile was built from the pre-rebase workspace feature tree, whose package
inputs are identical. A second profile switch was deliberately avoided because
the first switch restarted the shared App Server and terminated another
initiative's development cluster.

No review rerun is needed for the rebase because it changed only the workspace
feature parent to include tracking commits; the reviewed package diff, Nix
checks, configuration deployment and live protocol verification are unchanged.

## Final cleanup

All four feature worktrees were clean and have been removed. Their branches
remain both locally and remotely as rollback references. The session remains in
`work/` until an explicit archive request or the configured auto-archive policy
acts.
