# 2026-09-30-portal-review-improvements

## Goal

Implement the approved dev-workspace portal plan: migrate workspace Sol defaults to gpt-6.1-sol; make live Codex model/reasoning edits atomic and stable across refresh; retain loaded diffs and add Load all diffs; abstract repository origin with GitHub as the only provider; review staged, unstaged, and untracked changes; apply role-based team-member defaults; and add vpsadmin-webui beside the legacy UI in the vpsAdmin development cluster. Preserve compatibility, complete required review and verification, deploy the portal through the user profile, and leave default-branch integration for explicit approval.

## Affected repositories

- `dev-workspace`: repository review, Codex settings, team defaults and generic
  origin support.
- `vpsfree-dev-workspace`: vpsAdmin development-cluster integration and the
  downstream runtime pin.
- `workspace`: GPT-6.1 Sol team defaults, policy/docs, cluster domain and the
  downstream vpsFree extension pin; update its transitive `llm-agents` lock so
  the user-profile package contains a Codex build that exposes the requested
  model.
- `vpsfree-cz-configuration`: deploy `aitherdev` from the registered
  feature worktree at the existing head, which already pins the required
  `llm-agents` revision; do not make a redundant input update or integrate the
  configuration branch without separate approval. Prepare the bounded fourth
  repository edit: one internal DNS CNAME and a monotonic SOA serial in
  `configs/internal-dns/zone.vpsfree.cz.`. Shared DNS publication is pending
  exact-target user approval and is outside the aitherdev/profile deployment
  authorization; no input or system host code changes are included.
- `codex-web`: read-only protocol dependency; its existing settings request is
  atomic, so the portal draft and refresh fix belongs in `dev-workspace`.
- `vpsadmin-webui`: read-only package/module dependency at reviewed head
  `534caa83a5f97d2b40b4a126886649b14dc9e8d3`.
- `vpsadmin`: read-only same-session worktree required by the cluster runner;
  its selected API source must support the new nondefault OAuth client seed.

## Approach

1. Design the repository snapshot and origin-provider boundaries, the atomic
   Codex settings draft, role-default resolution and the side-by-side WebUI
   service before application edits.
2. Implement generic portal behavior in `dev-workspace`, then update the
   vpsFree extension and workspace configuration/policy consumers.
3. Run focused quick checks, commit each coherent repository change and perform
   the mandatory independent review before long Nix and cluster checks.
4. Prove the newer Codex model catalog and protocol compatibility, update the
   workspace package lock, then build and deploy the existing aitherdev
   configuration head whose configuration-owned `llm-agents` channel already
   selects that revision.
5. Deploy the reviewed portal package through the user profile. Keep feature
   branches unmerged until the user explicitly approves each default-branch
   integration.
6. Prepare, check and independently review the internal DNS candidate locally,
   then ask for publication approval naming both internal ns1 hosts and both
   monitoring copies listed in the design. Cluster/profile work continues
   independently; neither successful service probes nor this preparation
   authorizes shared DNS deployment.

## Decisions

- Base work on current `dev-workspace/master` at or after `7c133c5`; the portal
  performance and automatic-history work is already integrated.
- Use `gpt-6.1-sol` for new lead, implementer and reviewer defaults while
  retaining the existing effort levels. Existing rosters keep saved settings.
- Codex model and effort changes use a local draft plus an explicit Apply
  action; background reads cannot overwrite a dirty or saving draft.
- Loaded diff editors remain mounted. `Load all diffs` expands and fetches all
  eligible previews. Native browser find is retained, with CodeMirror's DOM
  virtualization limitation accepted.
- Unstaged review includes untracked non-ignored files. Staged and unstaged
  views use immutable temporary snapshots and never modify the real index,
  refs or worktree.
- Keep the persisted `github` manifest field for rollback compatibility while
  exposing an origin-neutral internal/API representation. GitHub is the only
  provider in this change.
- Run the React WebUI beside the PHP WebUI at
  `newadmin.aitherdev.int.vpsfree.cz`, using a separate newadmin container and
  loopback-only private listeners behind the existing services TLS edge.
- The cluster declares `newadmin` for guest hosts/resolution, but selected
  configuration `ee99382c` lacks its site internal DNS record. Prepare
  `newadmin.aitherdev.int IN CNAME frontend.aitherdev.int.vpsfree.cz.` next to
  the existing aliases, with a strictly increased SOA serial. Public production
  `newadmin.vpsfree.cz` is unrelated. Hostname/browser readiness requires normal
  host and intended VPN-client resolution; `--resolve` checks prove only the
  service path. Publication remains pending user approval.
- Codex 0.155.0 does not expose `gpt-6.1-sol` for the active account, while an
  isolated 0.159.2 App Server using the same account does. Update the user-profile
  package lock to the proved `af40d966` revision and deploy configuration head
  `ee99382c`, which already selects it. The running system is still 0.158.0
  because that head has not been deployed. Preserve exact model validation.
- `check-dev-workspace-deployment` rejects unequal complete generic revisions
  (`41c648c` in workspace, `ec05cb9` in configuration). Their consumed host
  module and paths are unchanged. Record this helper limitation and verify
  actual host contracts; do not bump unrelated configuration `devWorkspace`.

## Compatibility and deployment

- No database, API resource, node protocol or vpsAdminOS change is planned.
- Existing session manifests and saved team rosters remain readable by the
  previous portal generation. Temporary uncommitted-change snapshots are
  process-local and are discarded on eviction or shutdown.
- Member-add requests may omit model and effort together; explicit callers and
  older clients remain valid. Supplying only one remains an error.
- The development cluster seeds a separate non-default OAuth client and keeps
  its credentials/session secret outside the Nix store in ignored cluster
  state. The legacy PHP client and hostname remain active.
- User-profile switches are forward-only. Portal recovery requires a newer
  compatible forward switch, not selecting an older profile generation. If the
  new cluster UI fails, update services with a known-good matching build or
  disable only React while retaining its credentials and BFF session state;
  reverting an older API/schema generation needs separate compatibility proof.
- The portal is deployed from the workspace user profile. Deployment does not
  authorize integration of any feature branch.
- The Codex update must pass the exact App Server protocol/schema contracts and
  package-transition preflight before activation. Deploy aitherdev from the
  configuration feature worktree with dry activation first. Retain the previous
  system generation as recovery evidence; its use requires separate host and
  Codex-state compatibility proof and does not roll back the user profile.
  The user-profile application remains a separate forward-only transition with
  its own generation and recovery journal, using the documented candidate entry
  and failure boundaries in the design addendum.
- DNS publication is a separate operation on the approved shared targets.
  Preserve existing records and use a newer SOA serial for any correction or
  removal after publication. Account for negative caching; do not reset or
  restart the development cluster to repair a missing DNS record.

## Documentation

- The accepted technical and verification brief is [design.md](design.md).
- Update workspace team-policy documentation for GPT-6.1 Sol.
- Update generic portal and cluster documentation for origin links,
  uncommitted comparisons, atomic Codex settings and the new WebUI component.
- Apply the vpsFree user-facing writing workflow to visible labels, errors and
  help before committing.

## Testing plan

- Portal unit/browser tests for retained editors, load-all behavior, staged and
  unstaged snapshots, origin links, role defaults and the atomic Codex settings
  draft across polling, failures and active turns.
- Repository edge cases: combined staged/unstaged files, untracked/ignored
  paths, rename/delete/symlink/binary/oversized/submodule content, concurrent
  writes, eviction and archived sessions.
- Cluster source/override tests, Nix evaluation and builds, then a booted-cluster
  check of TLS, build metadata, health/session endpoints, OAuth callback, local
  source override and the unchanged PHP WebUI.
- Compare live model catalogs from the old and candidate Codex builds using the
  same account, run the candidate package's protocol and flake checks, build and
  dry-activate aitherdev, deploy it, and verify the running system and candidate
  user-profile package use the intended Codex revision before switching the
  portal profile.
- Use the required Luna/low watcher for long builds and cluster verification.
- DNS: verify the one-record/serial diff, validate each rendered zone, build the
  four explicit consumers under the review/watcher gates, and prepare their
  deployment evidence before asking for shared-DNS publication approval.
  After approval and publication, check each authoritative copy, normal host
  and VPN-client resolution, then strict-CA HTTPS and browser OAuth/refresh
  without `--resolve`; handle negative caches and recovery as in the design.

## Approved repository-review follow-up (2026-10-01)

- Empty committed and working-tree comparisons must encode `files` as a JSON
  array. The browser also treats legacy `files: null` as an empty comparison so
  a mixed or rolled-back portal generation remains usable.
- The Repositories overview shows one full-width repository card per row. The
  Compare, Staged changes, Unstaged changes and Refresh commits controls remain
  visible above a native **Local commits** disclosure.
- Local commits starts closed on each full page load. History continues loading
  in the background so Compare and branch-change monitoring remain available;
  the retained card node preserves an opened disclosure during periodic details
  refreshes.
- Add raw JSON and browser regressions for an empty staged/unstaged snapshot,
  legacy null compatibility, the single-column desktop layout, one-line desktop
  actions and disclosure state. Preserve the existing lazy/load-all diff tests.
- Append the generic fix to the already deployed branch history, update the
  extension and workspace pins, repeat whole-branch review and long checks, then
  deploy the rebuilt workspace package through the aitherdev user profile. No
  schema migration, configuration-repository change or default-branch
  integration is included.
