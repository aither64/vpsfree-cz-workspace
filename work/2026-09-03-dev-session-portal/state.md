---
lifecycle: active
---

# 2026-09-03-dev-session-portal

## Current status

The implementation is committed, clean, and pushed on development branches.
It has not been deployed. The initiative remains active until the user deploys
aitherdev and both internal DNS containers and installs the public CA on client
devices.

- Portal URL after deployment:
  `https://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/`
- Workspace head: `0ae37664d211adc4ccf608544ccccbaa0e1d7d5e`
- Configuration head: `5d4e9eafa67c27ef1ef4913794250806431f1153`
- The configuration lock pins the exact workspace head through
  `aitherVpsfreeWorkspace`.
- No GitHub Actions runs exist for either feature branch.
- The Basic Auth password is prepared at
  `/home/aither/.local/state/vpsfree-workspace-portal/password`, owned by uid
  1000 at mode 0600. Its value has not been printed or recorded.
- Current Codex thread:
  `01a0678c-baae-7600-bcf6-9a0cb6c83232`.

## Repositories and worktrees

### Workspace

- Repository: `aither64/vpsfree-cz-workspace`
- Branch: `2026-09-03-dev-session-portal`
- Initial base: `ac651305d935e3e78768567b4f18b498037f985a`
- Worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-03-dev-session-portal/workspace`
- Commits:
  - `471ca91` PKI and certificate lifecycle tooling
  - `7f0fd37` Basic Auth password derivation
  - `b220ffd` shared browser/terminal development sessions
  - `841d755` authenticated portal and App Server adapter
  - `639a7a5` workspace development-branch policy
  - `f9a805e` operator and native-client documentation
  - `0ae3766` source-owned Nix package and checks

### vpsfree-cz-configuration

- Repository: `vpsfreecz/vpsfree-cz-configuration`
- Branch: `2026-09-03-dev-session-portal`
- Initial base: `248e2fc614bb3bc29c0a9c9f910330ade0b3cb80`
- Worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-03-dev-session-portal/vpsfree-cz-configuration`
- Commits:
  - `01f9ec39` declare the `aitherVpsfreeWorkspace` input
  - `6ff183fe` pin the exact workspace feature revision with `confctl`
  - `d259432a` configure the aitherdev services and HTTPS proxy
  - `5d4e9eaf` publish the internal DNS record

The top-level shared checkout remains on `master`. Its unrelated modified
`AGENTS.md` and unrelated untracked files are preserved and are outside this
initiative.

## Supported design

- The workspace repository owns the Go portal, embedded responsive UI,
  `dev-session` integration, PKI/password helpers, handoff skill, documentation,
  and Nix package.
- The portal validates active and archived manifests, renders sanitized
  tracking files and curated artifacts, and enriches repository entries with
  GitHub comparisons and workflow status.
- A root-supervised Codex App Server listens only on a local Unix socket. The
  portal and tmux terminal client share the same persisted thread. The App
  Server is never exposed on the network.
- Browser-created sessions use a retry-safe creation journal. Terminal attach
  goes through `workspace-dev-session attach`, which reconciles the tmux client
  after an App Server restart.
- The initial and follow-up message limit is one shared 20,000-byte runtime
  contract consumed and tested by the Ruby session helper, Go portal, HTML
  forms, and configuration.
- The generated schema supplied by the configuration's normal `llm-agents`
  Codex package is checked against every App Server shape consumed by the
  adapter. An incompatible ordinary Codex update fails the aitherdev build;
  there is no initiative-specific Codex pin.
- nginx provides HTTPS and Basic Auth. Application mutations additionally
  require the exact HTTPS origin and all application responses are `no-store`.
- The custom CA and nginx key material are root-owned and absent from the Nix
  store. Certificate/key pairs are validated and switched atomically, with a
  predecessor retained. A successful-applied marker makes export or nginx
  reload failures retryable.
- Only the VPN interface can reach the HTTPS listener. Internal DNS maps the
  portal name to aitherdev at `172.16.106.40`.

## Compatibility and deployment

- Existing schema-1 manifests remain readable. Recorded Codex versions are
  diagnostic only, so compatible ordinary upgrades can resume old sessions.
- Portal status and local files remain available when GitHub or Codex is down;
  the unavailable integration is reported without failing the page.
- Active sessions compare live feature branches with repository default
  branches. Finalized sessions retain immutable comparison metadata and become
  read-only at the same URL.
- The CA, password, nginx password hash, portal state, and Codex state persist
  across ordinary NixOS redeployments and generation rollbacks.
- Deployment order is aitherdev first, then both DNS containers. Rollback uses
  ordinary previous NixOS/confctl generations. See `deployment.md` for CA
  trust removal and compromise recovery.
- No persisted database, API, protocol between production services, or
  vpsAdminOS node format changes are involved. Mixed versions are safe because
  the portal and DNS entry are additive and a missing portal only makes the
  name unavailable.

## Verification

Completed on the current workspace head:

- `nix build .#workspace-portal --no-link -L`
  - generated Codex schema contract passed
  - all Go packages passed
  - 121 dev-session tests and 1,021 assertions passed
  - 11 PKI tests and 76 assertions passed
  - 2 password tests and 18 assertions passed
  - output: `/nix/store/l7yjrrp0pfvq0jvz4cdc4khlb5wswbig-workspace-portal-0.1.0`

Completed on the current configuration head:

- `nix flake check --no-build -L` passed.
- `named-checkzone vpsfree.cz configs/internal-dns/zone.vpsfree.cz.` loaded
  serial `2026090300` successfully. It reports the repository's existing
  `@fqdn@` template-name warning.
- Feature-branch GitHub Actions queries returned no runs.

Still pending:

- mandatory-review rerun of the affected General, Architecture, and Risk lanes
  with fresh `gpt-5.6-sol` xhigh reviewers;
- sequential `confctl build` of aitherdev, prg/int.ns1, and brq/int.ns1;
- user-owned deployment and live HTTPS, authentication, DNS, browser, and
  terminal-attach smoke tests.

## Mandatory change review

The final full review used fresh `gpt-5.6-sol` reviewers at xhigh, never max or
ultra. Its General, Architecture, Scope, and Risk lanes reviewed workspace
`ed58a077` and configuration `4022ff8d`.

Resolved Blocking and Important findings:

- split the password helper from the PKI commit;
- changed all displayed attach commands to the reconciliation wrapper;
- published the 20,000-byte request boundary as one cross-layer contract;
- replaced permanent nginx restart behavior with a one-time restart trigger;
- persisted the last successfully applied TLS target so failed exports or
  reloads retry;
- corrected and condensed operator tracking to the supported implementation.

Resolved low-cost advisory work adds permanent CA decommission and compromise
recovery instructions. The in-memory GitHub/session caches remain intentionally
unbounded because this is a single-user, VPN-only service with a small set of
workspace initiatives. The native ChatGPT section remains because the user
explicitly asked about desktop and mobile access; it clearly describes a
separate SSH-based workflow rather than claiming access to the portal thread.

The affected review lanes are being rerun against the exact current heads.

## Handoff and cleanup

- User deployment instructions: `deployment.md`.
- Reusable first-input bootstrap lesson:
  `notes/vpsfree-cz-configuration/2026-09-04-confctl-add-new-input.md`.
- Keep both feature branches after integration unless the user explicitly asks
  for deletion.
- Do not finalize or archive this initiative until deployment, CA installation,
  live smoke tests, and worktree cleanup are complete.
