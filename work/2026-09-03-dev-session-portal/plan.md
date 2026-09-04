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
  nginx configuration, VPN firewall access, internal DNS record, and a
  narrowly scoped root deployment key for aitherdev.

## Approach

- Keep the existing Go portal and responsive embedded UI. It reads validated
  active and archived initiative manifests, shows GitHub comparisons and
  workflow state, renders sanitized tracking files and curated artifacts, and
  exposes only the required Codex App Server operations.
- Replace the side-by-side session layout with one full-width tab set for
  Codex, handoff commands, repositories, plan, state, and curated artifacts.
  Open the Codex tab by default when a thread is available and keep responsive
  behavior for narrow screens.
- Sort active and archived session cards by the date at the start of their
  slug, newest date first. Within one date, use recorded update time and then
  the slug for deterministic ordering. This keeps a newly dated session above
  an older initiative whose tracking files were edited more recently.
- Keep the `dev-session` integration that creates and resumes one persisted
  Codex thread per initiative and shares it between the browser and terminal
  client through the supervised host App Server.
- Keep empty pending-request collections as JSON arrays across the Go and
  browser boundary, with a browser fallback for a rolling deployment that
  briefly combines an older API response with the corrected asset. Treat an
  absent caller `TMUX` value as an empty string when attaching from a normal
  shell. Install one host-configured `dev-session` command on aitherdev, matching
  the checkout's `./bin/dev-session`, and remove the separate
  `workspace-dev-session` name. Display exact known slugs without the
  unnecessary `--as-is` option; unique short-name lookup and explicit
  `--as-is` remain available.
- Treat a fresh Codex thread as unmaterialized until its announced rollout path
  exists. Before the one allowed first-turn RPC, atomically write an in-flight
  schema-2 manifest with a durable attempt marker. A retry of the same
  unmaterialized thread must fail closed even when its metadata still looks
  idle; after materialization it must verify exactly one matching initial user
  request without sending anything. Limit working-directory reconciliation and
  replacement to a validated creating, unsent session; ready sessions resume
  only their authoritative thread ID.
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
- Use an unencrypted custom CA key protected by filesystem permissions. On
  first aitherdev activation, create the CA and leaf directly in root-owned
  `/var/lib`, install the nginx pair, and retain a user-readable public CA copy.
  Renew leaf certificates automatically under the same CA and reload nginx.
- Remove the specialized rollout/rollback helper and its deployment machinery.
  Use ordinary confctl/NixOS generations for deployment and rollback.
- Add the existing local ED25519 public key to the shared key data without
  including it in the broad `aither.all` set. Authorize it only for root on
  aitherdev, restrict it to local source addresses, and disable SSH forwarding
  and PTY features so later portal iterations can be deployed locally with
  `confctl` without creating a reusable remote login credential.

## Compatibility and deployment

- Existing schema-1 portal manifests remain readable. Stored Codex versions
  remain diagnostic history; they do not prevent a compatible newer Codex from
  resuming the same thread or validating the same tmux/App Server endpoint.
- Pending-response normalization and shell attachment do not change manifests,
  runtime authority, Codex history, or tmux ownership. A corrected portal can
  serve existing live sessions without recreating them. Rolling back the
  aitherdev generation restores the pending-response and attachment defects,
  the sidebar layout, the previous index order, and the former
  `workspace-dev-session` command; the intentional command rename has no
  compatibility alias.
- The Codex 0.153 materialization boundary temporarily uses manifest schema 2
  only while initial-goal delivery is unresolved. Exact-history verification
  atomically removes the attempt marker and returns the completed session to
  schema 1, so older portals can read completed sessions. A rollback rejects an
  in-flight schema-2 session and cannot progress it; redeploy the corrected
  portal and retry the same recorded request. Existing schema-1 sessions remain
  readable, and a legacy ambiguous creating session fails closed until an App
  Server restart permits a fresh replacement.
- The portal remains useful for status and files when GitHub or Codex is
  unavailable and reports integrations as unavailable without failing pages.
- Active sessions use live branch comparisons. Finalized sessions preserve
  immutable comparison metadata and remain read-only at the same URL.
- The CA, password, and generated nginx hash persist across redeployments and
  ordinary rollbacks. Repeated activation validates and reuses them instead of
  rotating credentials. The leaf renewal timer replaces only the server pair.
- No password, CA private key, or server private key is committed or placed in
  the Nix store. The portal process cannot read the root-owned CA or nginx key.
- The portal, Codex App Server, and terminal Codex share the `aither` account,
  which owns the local deployment private key. Authenticated browser control of
  Codex is therefore intentionally equivalent to local aitherdev root command
  execution after bootstrap. Basic Auth and VPN reachability protect that
  boundary.
- The user completed the one-time aitherdev bootstrap and both internal DNS
  deployments. The restricted local deployment key is active, so the agent can
  deploy later aitherdev iterations. The activation and browser-origin
  corrections have been deployed and validated. Client installation of the
  public custom CA remains user-owned.
- The first aitherdev activation failed before authentication and PKI state was
  created because a wrapped helper retained an env-based Bash shebang. The
  package now uses direct store interpreters and tests its installed helpers
  with an empty ambient `PATH`. Repeating activation creates the missing state
  atomically and reuses any complete state.
- The initial rollout ordered aitherdev before DNS. The follow-up corrections
  redeployed only aitherdev and left the working DNS deployments unchanged.
  Standard confctl generation rollback is sufficient; portal state is additive
  and can remain on disk if the configuration is rolled back. Rolling
  aitherdev back before the deployment-key generation also removes that
  authorization. Such a rollback is user-owned unless another root credential
  is available, and another user bootstrap is required before agent deployment
  can resume.

## Testing plan

- Extend Go protocol contract tests to validate every request, response, and
  notification shape used by the adapter against the currently supplied Codex
  schema. Test a non-matching diagnostic version without rejecting it.
- Extend `dev-session` tests for compatible version upgrades, runtime endpoint
  authority, session reuse, browser creation, terminal attachment, cleanup,
  and existing manifest compatibility.
- Cover attachment from a shell with no `TMUX` value, the concise exact-slug
  attach command shown by the portal, and an empty pending-request response in
  both the Go API and browser contract.
- Cover newest-first index ordering for active and archived sessions.
- Test PKI initialization without a passphrase, repeated activation, file
  ownership and modes, missing or malformed input, leaf renewal, nginx
  installation, and public CA export.
- Test Basic Auth bootstrap for initial generation, idempotent reuse, hash
  verification, permissions, and fail-closed malformed credential state.
- Verify that the configured deployment-key fingerprint matches the local
  public key and that the key is authorized only for aitherdev root.
- Exercise or inspect the installed wrapped helper entry points under an empty
  ambient `PATH`, so portable source shebangs cannot survive in makeWrapper's
  hidden executables and fail during NixOS activation.
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
