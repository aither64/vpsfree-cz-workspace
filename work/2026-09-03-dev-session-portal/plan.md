# 2026-09-03-dev-session-portal

## Goal

Provide a VPN-only HTTPS web interface for development initiatives at
`vpsfree-cz-workspace.aitherdev.int.vpsfree.cz`. Each initiative has a stable
page with GitHub comparisons and workflow runs, rendered tracking files and
curated artifacts, live interaction with its Codex thread, and browser creation
of a session that can also be attached from a terminal.

## Affected repositories

- Coordination workspace (`aither64/vpsfree-cz-workspace`): portal service,
  `dev-session` integration, tests, flake packaging, PKI helper, credential
  preparation, documentation, handoff skill, and workspace rules.
- `vpsfree-cz-configuration`: workspace flake input, aitherdev services and
  nginx configuration, VPN firewall access, and internal DNS record.

## Approach

- Keep the existing Go portal and responsive embedded UI. It reads validated
  active and archived initiative manifests, shows GitHub comparisons and
  workflow state, renders sanitized tracking files and curated artifacts, and
  exposes only the required Codex App Server operations.
- Keep the `dev-session` integration that creates and resumes one persisted
  Codex thread per initiative and shares it between the browser and terminal
  client through the supervised host App Server.
- Make the workspace repository a flake and the sole owner of the portal Nix
  package. Export `packages.x86_64-linux.workspace-portal`; remove the copied
  package expression and package output from `vpsfree-cz-configuration`.
- Rename the configuration input to `aitherVpsfreeWorkspace`. Its `nixpkgs`
  and `llm-agents` inputs follow the configuration's existing inputs, so the
  ordinary configuration `llm-agents` update remains the only production Codex
  update path. The workspace flake lock is only the standalone development
  default.
- Remove the hard-coded Codex 0.152.1 runtime rejection. Keep detected version
  values only for diagnostics, not as session authority. Build the portal
  against the configuration-provided Codex and validate every App Server RPC
  shape consumed by the adapter. An incompatible Codex update must fail the
  aitherdev build before deployment.
- Keep HTTP Basic Authentication in nginx. Prepare a random password in
  `/home/aither/.local/state/vpsfree-workspace-portal/password`, readable only
  by `aither`, and generate the nginx hash from it during activation.
- Use an unencrypted custom CA key protected by filesystem permissions. Prepare
  the CA and first leaf certificate in a mode-0700 staging directory under
  `/home/aither/.local/state`, outside every Git checkout. On first aitherdev
  activation, validate and import private material into root-owned `/var/lib`,
  remove the staged private CA key, and retain a user-readable public CA copy.
  Renew leaf certificates automatically under the same CA and reload nginx.
- Remove the specialized rollout/rollback helper and its deployment machinery.
  Use ordinary confctl/NixOS generations for deployment and rollback.

## Compatibility and deployment

- Existing schema-1 portal manifests remain readable. Stored Codex versions
  remain diagnostic history; they do not prevent a compatible newer Codex from
  resuming the same thread or validating the same tmux/App Server endpoint.
- The portal remains useful for status and files when GitHub or Codex is
  unavailable and reports integrations as unavailable without failing pages.
- Active sessions use live branch comparisons. Finalized sessions preserve
  immutable comparison metadata and remain read-only at the same URL.
- The CA, password, and generated nginx hash persist across redeployments and
  ordinary rollbacks. Repeated activation validates and reuses them instead of
  rotating credentials. The leaf renewal timer replaces only the server pair.
- No password, CA private key, or server private key is committed or placed in
  the Nix store. The portal process cannot read the root-owned CA or nginx key.
- The implementation prepares the user-owned staging credentials on aitherdev.
  The user only deploys `cz.vpsfree/machines/aitherdev` and the two internal DNS
  containers. Installing the public custom CA on each client is an unavoidable
  one-time client action.
- Deploy aitherdev before publishing DNS so the hostname does not resolve until
  HTTPS is ready. Standard confctl generation rollback is sufficient; portal
  state is additive and can remain on disk if the configuration is rolled back.

## Testing plan

- Extend Go protocol contract tests to validate every request, response, and
  notification shape used by the adapter against the currently supplied Codex
  schema. Test a non-matching diagnostic version without rejecting it.
- Extend `dev-session` tests for compatible version upgrades, runtime endpoint
  authority, session reuse, browser creation, terminal attachment, cleanup,
  and existing manifest compatibility.
- Test PKI initialization without a passphrase, staging import, repeated
  activation, file ownership and modes, missing or malformed input, leaf
  renewal, nginx installation, and public CA export.
- Test Basic Auth bootstrap for initial generation, idempotent reuse, hash
  verification, permissions, and fail-closed malformed credential state.
- Run Go tests, race tests, vet, JavaScript tests, Ruby tests, workspace flake
  checks/builds, repository hooks, Nix formatting, internal DNS validation, and
  `confctl build` for aitherdev plus both internal DNS servers.
- Commit intended changes and quick checks before running the mandatory change
  review. Use fresh `gpt-5.6-sol` reviewers at `xhigh` only. Resolve Blocking
  and Important findings before the long confctl integration builds.

## Cleanup

- Rewrite and force-push the two unmerged feature branches. Remove the
  configuration-owned package and the initiative-specific `llm-agents` commit
  from configuration history while preserving the normal upstream pin.
- Keep the initiative active until the user deployment handoff is complete.
  Do not archive it while deployment and client trust installation remain.
