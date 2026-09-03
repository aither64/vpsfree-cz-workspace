# 2026-09-03-dev-session-portal

## Goal

Provide a VPN-only HTTPS web interface for development initiatives at
`workspace.aitherdev.int.vpsfree.cz`. Each initiative must have a stable page
with GitHub comparisons and workflow runs, rendered tracking files and curated
artifacts, live interaction with its Codex thread, and a browser action for
starting an ordinary `dev-session` that can also be attached from a terminal.

## Affected repositories

- Coordination workspace (`aither64/vpsfree-cz-workspace`): portal service,
  `dev-session` integration and tests, PKI helper, documentation, handoff skill,
  and tracking.
- `vpsfree-cz-configuration`: pinned workspace source input, portal package and
  aitherdev service/nginx configuration, VPN-only firewall access, and internal
  DNS record.

## Approach

- Build a small Go service with an embedded responsive UI. It will read active
  and archived initiative manifests, inspect registered worktrees, query GitHub
  through `gh`, render sanitized tracking files, and proxy only an allowlisted
  subset of the local Codex App Server protocol.
- Extend `bin/dev-session` to create and resume one named Codex thread per
  initiative through the managed local daemon, persist `portal.yml`, expose the
  stable URL, and launch the tmux TUI against the same daemon. Browser creation
  will start an empty session and send the supplied goal as the first turn;
  Codex remains responsible for selecting repositories.
- Add single-user password authentication, secure cookies, CSRF and origin
  checks, rate limiting, strict artifact containment, and no raw shell,
  filesystem, or App Server RPC endpoint.
- Add an OpenSSL-based PKI helper. The encrypted CA key and unencrypted nginx
  leaf key live under `/home/aither/.local/state/vpsfree-workspace-pki`, never
  in git. The helper supports initialization, inspection, renewal, verification,
  and public CA export.
- Add a compact `dev-session-handoff` skill and workspace rule so handoffs after
  material changes include the stable portal URL.
- Package an exact coordination-workspace revision as a non-flake input in
  `vpsfree-cz-configuration` and configure the service, HTTPS virtual host, DNS,
  and firewall declaratively.

## Compatibility and deployment

- Existing work/state directories and standalone Codex processes are not
  migrated. New manifests are additive; older helpers ignore them.
- The portal remains useful for status and files if GitHub or Codex is offline,
  and reports those integrations as unavailable without failing the page.
- Active sessions use live branch comparisons. Finalization preserves metadata
  and leaves the same URL read-only under `archive/`.
- No database, API, protocol, or persistent project state is changed. Rolling
  compatibility is limited to the local workspace helper and portal protocol;
  explicit schema and control API versions will reject mismatches cleanly.
- The implementation will prepare and verify configuration only. The user owns
  deployment of both internal DNS servers and the aitherdev NixOS generation,
  as well as CA trust installation on client devices.
- Rollback consists of reverting the aitherdev generation and normal git
  reverts. Tracking files and Codex histories remain readable.

## Testing plan

- Unit-test manifests, git/GitHub metadata, authentication, CSRF, containment,
  Markdown sanitization, App Server event mapping, and PKI generation/renewal.
- Extend `dev-session` tests for thread reuse, URL/JSON output, browser-style
  start, terminal attach, worktree metadata, and finalization.
- Exercise a disposable shared Codex thread through the portal adapter and tmux
  TUI, including messages, steering, interruption, questions, approvals, and
  reconnects. Verify ChatGPT macOS discovery when the user can participate.
- Run Go and Ruby tests, skill validation, hooks, Nix checks, internal DNS zone
  validation, and `confctl build` for aitherdev and both internal DNS servers.
- Run the mandatory change review after intended commits and quick checks, then
  prepare a deployment runbook with exact user-owned deployment and smoke-test
  commands.
