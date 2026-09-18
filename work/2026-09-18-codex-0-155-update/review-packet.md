# Review packet: Codex 0.155.0 rollout

## Requested outcome

Update the generic runtime, vpsFree extension, consuming workspace and aitherdev
configuration so that the system package, workspace profile, portal and shared
Codex App Server converge on Codex 0.155.0. Deploy only aitherdev from the
configuration feature branch. Keep branches unmerged and retain rollback
profiles/generations.

## Review scope

This is a high operational-risk rollout because it deploys configuration and
restarts the shared App Server after clients are idle. The committed changes are
otherwise dependency pins only: no hand-written service, API, state, protocol,
or configuration-module logic changed. At the user's explicit direction, this
is a shortened review: one General lane reviewer using `gpt-5.6-terra` with
`xhigh` reasoning. Risk/architecture/scope lanes are deliberately omitted;
protocol/model catalog validation and the real profile switch are the concrete
compatibility gates.

## Initiative and revisions

- Initiative: `2026-09-18-codex-0-155-update`
- Tracking: `work/2026-09-18-codex-0-155-update/{plan,state}.md`
- `dev-workspace`: `fe67863a2b8fcf3bb10e1b3a74220582e3283fa3` to
  `18817f4bf60f9918932d980d5c91b92852ba3cfa`
- `vpsfree-dev-workspace`: `ab74ed67b83f488f7825884b12a58c17c3ca3e2b` to
  `e170ea0ead2babef823aa415e2d1b354d1648173`
- `vpsfree-cz-configuration`: `6ac2068b3aea8c3669bb9fa81dc713034ea501bd` to
  `c7ed1210fc90434e50de2b1e4752a7ae38d9a491`
- consuming `workspace`: `e4bfa8d34074951792398aabed10d5c299c9ae01` to
  `1042c1f66106059c1f4b8378712e11a6d2d32a50`

The source target is `llm-agents.nix` lock revision
`ddc89534b9a73cd99ff4d33656569ce3be6e6490`, which evaluates Codex to
`0.155.0`. The generic flake input intentionally remains on the upstream default
branch; its lock file selects that exact tested revision.

## Commit split

- Generic runtime: one input/lock update.
- Extension: one downstream runtime-lock update.
- Configuration: one generated `confctl` commit for independent `llm-agents`,
  then one generated commit for `devWorkspace`.
- Consuming workspace: one extension-lock update.

Each pin is independently reversible and corresponds to its dependency edge.
Configuration commits retain confctl-generated messages unamended.

## Compatibility, deployment and rollback

The configuration's independent `llm-agents` supplies the system Codex binary;
its `devWorkspace` input supplies the host module. The consuming workspace is
the sole source for `workspace-host switch`, so it carries the extension pin.
Deploy configuration first, then switch the user profile. `workspace-host`
validates the selected Codex protocol and model catalog before activation and
keeps the old 0.154.0 profile available. Existing active clients delay the
App Server restart; normal pending reconciliation waits for them to become idle.

No persistent format, schema, API, or module interface changes are introduced.
The local operator is trusted to administer aitherdev; remote portal and Codex
clients remain untrusted under the runtime's normal validation/authentication
boundaries.

## Documentation

Checked `dev-workspace` README and `docs/dev-sessions.md`, which already cover
paired profile/App Server activation, idle reconciliation and rollback. No
lasting documentation change is useful for this exact input bump. The session
plan/state own site-specific rollout, verification and recovery evidence.

## Quick verification completed

- `git diff --check origin/master..HEAD` passed in all four worktrees.
- Generic runtime, extension, configuration, and consuming workspace Nix
  evaluations each returned `0.155.0`.
- Configuration input commits ran declared Nixfmt and commit-message hooks.
- The configuration worktree checkout initially failed because its overcommit
  gems were unavailable outside the declared Nix shell. Running
  `nix develop --command overcommit --install` restored the declared hook
environment; no tracked files changed.

Long flake checks, aitherdev build/dry activation, deployment, profile switch,
and live App Server verification remain after this review.
