---
lifecycle: active
---

# 2026-09-03-dev-session-portal

## Current status

The implementation remains on development branches and has not been deployed.
The initiative stays active until the user deploys aitherdev and both internal
DNS containers and installs the public CA on client devices.

- Portal URL after deployment:
  `https://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/`
- Workspace branch: `2026-09-03-dev-session-portal`.
- Configuration branch: `2026-09-03-dev-session-portal`.
- The configuration lock is the authority for the exact workspace revision
  selected through `aitherVpsfreeWorkspace`. Exact heads are reported at
  handoff rather than embedded in this same-repository tracking file.
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
- Commit subjects:
  - `pki: add workspace portal certificate tooling`
  - `auth: add workspace portal password derivation`
  - `dev-session: share workspace sessions across clients`
  - `portal: add authenticated development interface`
  - `workspace: develop reusable changes on feature branches`
  - `review: standardize mandatory lanes on xhigh`
  - `docs: explain workspace portal operation`
  - `flake: package the workspace portal at its source`

### vpsfree-cz-configuration

- Repository: `vpsfreecz/vpsfree-cz-configuration`
- Branch: `2026-09-03-dev-session-portal`
- Initial base: `248e2fc614bb3bc29c0a9c9f910330ade0b3cb80`
- Worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-03-dev-session-portal/vpsfree-cz-configuration`
- Commit subjects:
  - `inputs: add aither workspace source`
  - generated exact `aitherVpsfreeWorkspace` pin
  - `aitherdev: host authenticated development workspace portal`
  - `internal-dns: publish workspace portal`

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
  contract. It also publishes worst-case form and JSON transport expansion;
  Ruby, Go, HTML, nginx, and their boundary tests consume that contract.
- The generated schema supplied by the configuration's normal `llm-agents`
  Codex package is checked against every App Server shape consumed by the
  adapter. An incompatible ordinary Codex update fails the aitherdev build;
  there is no initiative-specific Codex pin.
- nginx provides HTTPS and Basic Auth. Application mutations additionally
  require the exact HTTPS origin and all application responses are `no-store`.
- The custom CA and nginx key material are root-owned and absent from the Nix
  store. Certificate/key pairs are validated and switched atomically, with a
  predecessor retained. The packaged, directly tested reconciler updates its
  applied marker only after successful export and nginx reload, so partial
  failures retry.
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

Completed on the current workspace candidate:

- `nix build .#workspace-portal --no-link -L`
  - generated Codex schema contract passed
  - all Go packages passed
  - 121 packaged dev-session tests and 924 assertions passed; 10 real-tmux
    cases were intentionally skipped by the package build
  - the ambient suite passed all 121 dev-session tests and 1,021 assertions
  - 14 PKI tests and 92 assertions passed, including failed CA export, failed
    nginx reload, retry, atomic marker publication, and inactive nginx
  - 2 password tests and 18 assertions passed
  - output: `/nix/store/vihxms8wyh9431vb48q8cn9ji46rmi4h-workspace-portal-0.1.0`

Completed on the previous pushed configuration candidate; repeat after its
final workspace repin:

- `nix flake check --no-build -L` passed.
- `named-checkzone vpsfree.cz configs/internal-dns/zone.vpsfree.cz.` loaded
  serial `2026090300` successfully. It reports the repository's existing
  `@fqdn@` template-name warning.
- Feature-branch GitHub Actions queries returned no runs at that checkpoint.

Still pending:

- final mandatory-review rerun after the current remediation is repinned;
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

The first remediation rerun reviewed workspace `0ae37664` and configuration
`5d4e9eaf` with fresh General, Architecture, and Risk xhigh lanes. It found:

- the workspace branch needed rebasing after tracking advanced `master`;
- the review-effort policy needed its own commit;
- percent-encoded form and escaped JSON requests could hit independent
  transport caps below the semantic message limit;
- `thread/start` had to verify its returned working directory before sending
  the initial turn;
- the TLS applied-marker retry state machine needed direct regression tests.

The branch is rebased, the policy commit is split, transport ceilings and all
numeric messages derive from the runtime contract, `thread/start` validates
the returned cwd, and the tested PKI reconciler now owns the export/reload
state machine. Final affected-lane review waits for the configuration repin.

## Handoff and cleanup

- User deployment instructions: `deployment.md`.
- Reusable first-input bootstrap lesson:
  `notes/vpsfree-cz-configuration/2026-09-04-confctl-add-new-input.md`.
- Keep both feature branches after integration unless the user explicitly asks
  for deletion.
- Do not finalize or archive this initiative until deployment, CA installation,
  live smoke tests, and worktree cleanup are complete.
