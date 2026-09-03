---
lifecycle: active
---

# 2026-09-03-webui-vps-ipv6

## Repositories

- `vpsadmin`
  - branch: `2026-09-03-webui-vps-ipv6`
  - worktree: `worktrees/2026-09-03-webui-vps-ipv6/vpsadmin`
  - base: `origin/master` at `cbd0fa16434947a4273610389d84216bcde35e72`
- `vpsfree-kb-contracts`
  - branch: `2026-09-03-webui-vps-ipv6`
  - worktree: `worktrees/2026-09-03-webui-vps-ipv6/vpsfree-kb-contracts`
  - base: `origin/master` at `46466e83c2293f47bfef3fe516a3b51c2de14c70`

## Status

Implementation starting. Root cause and historical session provenance have been
confirmed. No project code has been changed yet.

## Commands run

- Inspected the Location resource, WebUI consumers, API specs, requests-plugin
  overrides, repository history, historical Codex sessions, and KB contract.
- Fetched workspace, vpsAdmin, and vpsfree-kb-contracts upstream `master` refs.
- Created both initiative worktrees with `bin/dev-session worktree add` from
  current `origin/master`.

## Results

- `has_ipv6` is required by ordinary-member route and interface-address forms,
  but the non-admin Location output whitelist removes it.
- `Location#domain` is read directly only by administrator-only WebUI cluster
  pages. Member-visible Node names are derived separately; the user chose to
  keep the raw Location field restricted.
- The responsible pre-workspace worker was session
  `019e557f-e037-7682-bba1-964135736018`, overseen by parent session
  `019e548d-3620-7b71-a99a-6f8e85cc9810`.
- `bin/dev-session current` returned a false negative from tool execution:
  the tmux Codex frontend has the correct initiative environment, while the
  long-lived external app-server that launches tool shells does not. Use the
  explicit slug with session helpers.

## Open questions

None.

## Cleanup

- Both worktrees are active and must remain until review, CI, integration, and
  any separately authorized merge are complete.
- The initiative is not eligible for finalization or archival.
