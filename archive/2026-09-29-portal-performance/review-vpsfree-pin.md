# Mandatory review packet: vpsfree-dev-workspace pin

## Assignment

- Reviewer: retained `reviewer0`, GPT-6 Sol, xhigh, read-only.
- Risk: medium configuration/deployment risk.
- Lanes: general and risk/compatibility, with scope/proportionality for the lock graph.

## Repository and change

- Repository: `worktrees/2026-09-29-portal-performance/vpsfree-dev-workspace`.
- Base: `bd961682cecb0b3b2bf729a53d2e08bda3d48eb2`.
- Head: `7e6fdd140e144611658acb6e7610a5ccf668a0f2`.
- Commit: `nix: pin the updated workspace runtime`.
- Files: `flake.nix` and `flake.lock` only. The worktree is clean and unpushed.
- There are no migrations, interface changes, or independent runtime edits in this repository.

## Intended result

- Directly pin reviewed and pushed `aither64/dev-workspace` revision `9db7bc844a0332b7e00d21536c3bebf835928ece` with `lastModified` 1790712621 and `sha256-bjPRiEdnlwKUTlo+SrjVZq9xv/WxChEx/qAAhadosD4=`.
- Update the transitive `codex-web` node to the runtime's exact reviewed dependency `d210d3f7cc93981d0ab163b1fcf0718f9587f47e` with `lastModified` 1790710401 and `sha256-jp6nOqpINJIzj9iKWqkmWDlSefRRZ7uTLM6y0BuiZns=`.
- Preserve every follows relationship and all unrelated lock nodes.

## Evidence and deliverable

- Nix syntax, lock JSON, structural lock comparison, exact direct/transitive metadata, and `git diff --check` pass.
- Review pin coherence, lock-graph scope, deployment compatibility, and stale or unintended inputs. Report findings by severity or explicitly state none.
- Full builds and live rollout are later gates. No default branch integration is authorized.
