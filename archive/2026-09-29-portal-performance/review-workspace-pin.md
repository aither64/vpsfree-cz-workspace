# Mandatory review packet: workspace package pin

## Assignment

- Reviewer: retained `reviewer0`, GPT-6 Sol, xhigh, read-only.
- Risk: medium configuration and deployment risk.
- Lanes: general, risk and compatibility, and scope/proportionality for the lock graph.

## Repository and change

- Repository: `worktrees/2026-09-29-portal-performance/workspace`.
- Base: `979ef666099a678b7738826169e7fa6cf0a2f1a7`.
- Head: `238ee9a684579e732fd3bab3c37409c892a05ebe`.
- Commit: `flake: pin portal performance runtime`.
- Files: `flake.nix` and `flake.lock` only. The worktree is clean and unpushed.
- There are no migrations or independent application edits in this repository.

## Intended result

- Pin pushed `vpsfreecz/dev-workspace` revision `7e6fdd140e144611658acb6e7610a5ccf668a0f2` with `lastModified` 1790712941 and `sha256-7IuXL9Q/PAUFcm+fTatIetbsPZqj0cja7aRDhWcUffk=`.
- Carry its exact `dev-workspace` revision `9db7bc844a0332b7e00d21536c3bebf835928ece` and `codex-web` revision `d210d3f7cc93981d0ab163b1fcf0718f9587f47e` into the consuming lock.
- Preserve all follows relationships, unrelated lock nodes, workspace metadata, and the deployment package composition.

## Evidence and deliverable

- Nix syntax, lock JSON, exact direct/transitive metadata, structural lock comparison, and `git diff --check` pass.
- Review complete pin-chain coherence, unchanged unrelated inputs, package/deployment compatibility, and commit scope. Report findings by severity or explicitly state none.
- Consuming build, deployment, live acceptance, and final whole-chain readiness are later gates. No default branch integration is authorized.
