# 2026-09-09-workspace-components

## Goal

I'd like to evaluate whether it would make sense to split vpsfree-cz-workspace into three components:

- web interface for codex (what is shown in the development portal), this could be a reusable library with an example integration
- workspace session tooling, i.e. dev-session tools, vpsadminos/vpsadmin cluster management and the web portal itself
- vpsfree-cz-workspace would be using the independent session tooling and this repo would from now on contain only the work sessions, I don't like how we mix the tooling with the work sessions)

as such, the workspace integration into aitherdev in vpsfree-cz-configuration still seems too heavyweight, I'd imagine something more plug&play with the complexity hidden away (the workspace flake can provide nixosconfigu).

the codex web interface or the session tooling can bring their own codex, but definitely based on numtide/nix-agents.nix, so that we don't have to rebuild it and have a fresh version available.

suggest solutions.

## Affected repositories

- `vpsfree-cz-workspace`: inspect the shared `master` checkout, portal,
  session/runtime helpers, cluster tooling, packaging, and workspace data.
- `vpsfree-cz-configuration`: read canonical Git objects for aitherdev's host
  integration and Codex packaging; no configuration changes are requested.
- Potential new repositories for a reusable Codex browser component and
  independent session tooling. Names and interfaces are proposals only.

## Approach

1. Map current ownership and coupling using code and deployment configuration.
2. Verify Codex App Server integration and numtide agent packaging upstream.
3. Compare repository boundaries, library versus service integration, host
   module composition, and independent application deployment.
4. Record a recommendation, alternatives, migration order, and unresolved
   product choices in an assessment artifact.

This initiative is an evaluation. It does not authorize implementing the split,
creating remote repositories, deploying, or modifying another session.

## Compatibility and deployment

- Preserve tracking paths, Git history, session/thread identity, portal URLs,
  private runtime authority, operation journals, and cluster socket ownership.
- Assess old/new package contracts and rollback without changing live state.
- Keep application updates in the user profile; consider an exported NixOS
  module for stable host prerequisites and a separate optional complete host
  configuration for examples or dedicated machines.
- Source Codex from numtide's agent packaging, with one runtime owner and
  compatibility checks before activating upgrades.
- No database/API/node protocol migrations or coordinated node updates are
  part of this assessment. A later implementation must test mixed versions.

## Testing plan

- Read-only source inspection and upstream documentation verification.
- Check proposed boundaries against actual imports, helper invocation paths,
  state contracts, and Nix derivation composition.
- No builds, integration tests, or service transitions are needed to compare
  solutions. Any implementation will require the mandatory change review and
  focused compatibility tests before integration testing.
