---
lifecycle: active
---

# 2026-09-09-workspace-components

## Repositories

- Coordination checkout: `/home/aither/workspace/ai/vpsfree.cz`, branch
  `master`.
- Workspace source baseline:
  `3580e60bb035c2d0ba5be6f0d2489bbbf30ded3d`.
- Configuration source baseline:
  `7481618dacab04bfd5b09bc730c373c2d2bf14d7` from remote `master`.
- Initial tracking commit:
  `58ccb4da27d6e1ef26c330662b2471d559d2c437`.
- New public repository:
  `git@github.com:aither64/dev-workspace.git`, empty before bootstrap.
- New public repository:
  `git@github.com:aither64/codex-web.git`, empty before bootstrap.
- Planned feature branch in every affected repository:
  `2026-09-09-workspace-components`.
- No feature worktree has been created yet.

## Status

- The user accepted the three-component split and requested implementation.
- The user created the two public repositories. Both are empty and have no
  default branch. The selected default branch is `master`; both use the MIT
  license.
- The user selected a staged cutover: extract and deploy `dev-workspace`, then
  extract `codex-web` and port the portal.
- `dev-workspace` will ship core tooling and a separate vpsFree compatibility
  output containing KB commands and packaged workspace skills.
- `codex-web` will provide the Go App Server integration and framework-free ES
  module. It will not run as a separate service.
- The NixOS host module will use the secure local preset: basic authentication,
  local-CA TLS, nginx and no firewall opening without configured source ranges.
- This standalone Codex CLI owns implementation. It is intentionally not a
  managed development session and does not use the retained portal thread.
- No service, remote branch or repository content has been changed yet.

## Commands run

- Read `AGENTS.md`, the prior plan, state, assessment and independent handoff.
- Verified `/proc/self/cgroup` is
  `/user.slice/user-1000.slice/session-614.scope`, outside
  `workspace-codex@vpsfree-cz.service` and
  `workspace-tmux@vpsfree-cz.service`.
- Verified this shell has no inherited `VPSFREE_*` variables and
  `dev-session current` reports no current managed session.
- Read official OpenAI App Server documentation and the OpenAI Docs,
  vpsFree user-facing writing, mandatory change review and session handoff
  skills.
- Inspected the current portal, Codex adapter, lifecycle helpers, package,
  cluster flakes, aitherdev configuration, runtime contract and project map.
- Fetched workspace `origin`; local `master` remains one scoped tracking commit
  ahead of `origin/master`.
- Verified both new GitHub repositories are public, reachable over SSH, empty
  and have no default branch.
- Ambient Python lacked PyYAML for the tracking check. Ruby's standard YAML
  library validated the portal manifest instead; the scoped staged diff also
  passed `git diff --check`.

## Compatibility decisions

- Preserve all existing manifest, journal, authority, operation receipt,
  submission ledger, registry, profile and cluster-state formats and paths.
- Preserve `VPSFREE_*` environment names, current commands, systemd unit names,
  portal URLs, thread IDs, working directories and tmux identities.
- Pin Numtide `llm-agents.nix` revision
  `c2a308c84bbfa9f30827344219b7284f8104bdd8` and Codex 0.153.4 for the first
  cutover. Do not override Numtide's package or nixpkgs.
- Keep aitherdev's existing credentials, local CA and TLS material during the
  NixOS module migration.
- Keep shared bridge, DHCP and NAT configuration in
  `vpsfree-cz-configuration`; the reusable module accepts existing bridges.
- Default-branch integration, releases, archival, deletion and session stop
  are not authorized. aitherdev deployment is authorized.

## Review and testing

- Risk classification: high, because the change affects authentication,
  persisted runtime state, public interfaces, destructive lifecycle helpers,
  host deployment, rollback and mixed package generations.
- Mandatory review will use General, Architecture, Scope and Risk lanes with
  `gpt-5.6-sol` at `xhigh` after committed changes and quick checks, before
  long integration tests.
- Test and deployment results will be added as implementation proceeds.

## Open work

1. Commit this implementation and ownership checkpoint without staging
   unrelated shared changes.
2. Bootstrap the two new repository histories and canonical bare clones.
3. Create and register the four feature worktrees.
4. Implement, review, test and deploy the two stages.

## Cleanup

- Session remains active. No lifecycle action or delayed cleanup is authorized.
- Stable portal URL:
  https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-09-workspace-components/
