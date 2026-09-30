# 2026-09-30-portal-review-improvements

## Goal

Implement the approved dev-workspace portal plan: migrate workspace Sol defaults to gpt-6.1-sol; make live Codex model/reasoning edits atomic and stable across refresh; retain loaded diffs and add Load all diffs; abstract repository origin with GitHub as the only provider; review staged, unstaged, and untracked changes; apply role-based team-member defaults; and add vpsadmin-webui beside the legacy UI in the vpsAdmin development cluster. Preserve compatibility, complete required review and verification, deploy the portal through the user profile, and leave default-branch integration for explicit approval.

## Affected repositories

- `dev-workspace`: repository review, Codex settings, team defaults and generic
  origin support.
- `vpsfree-dev-workspace`: vpsAdmin development-cluster integration and the
  downstream runtime pin.
- `workspace`: GPT-6.1 Sol team defaults, policy/docs, cluster domain and the
  downstream vpsFree extension pin.
- `vpsadmin-webui`: read-only package/module dependency at reviewed head
  `534caa83a5f97d2b40b4a126886649b14dc9e8d3`.

## Approach

1. Design the repository snapshot and origin-provider boundaries, the atomic
   Codex settings draft, role-default resolution and the side-by-side WebUI
   service before application edits.
2. Implement generic portal behavior in `dev-workspace`, then update the
   vpsFree extension and workspace configuration/policy consumers.
3. Run focused quick checks, commit each coherent repository change and perform
   the mandatory independent review before long Nix and cluster checks.
4. Deploy the reviewed portal package through the user profile. Keep feature
   branches unmerged until the user explicitly approves each default-branch
   integration.

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
  `newadmin.aitherdev.int.vpsfree.cz`.

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
- Portal rollback restores the previous UI/API together. Cluster rollback uses
  the previous generation while retaining credential and BFF session state.
- The portal is deployed from the workspace user profile. Deployment does not
  authorize integration of any feature branch.

## Documentation

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
- Use the required Luna/low watcher for long builds and cluster verification.
