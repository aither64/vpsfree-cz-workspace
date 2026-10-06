# 2026-06-07-vpsconf-nixpkgs

## Goal
Answer whether `nixpkgsProduction` and `nixpkgsStaging` in
`vpsfree-cz-configuration` used to stay in sync with `nixpkgsStable`, then move
production/staging to up-to-date 26.05, commit, and push to `master`.

## Affected repositories
- `vpsfree-cz-configuration`

## Approach
- Inspect `flake.nix`, `flake.lock`, the daily update workflow, and git history
  for the nixpkgs channel inputs.
- Change `nixpkgsProduction` and `nixpkgsStaging` sources to `nixos-26.05`.
- Use `confctl inputs channel update` to update `nixos-stable`, `production`,
  and `staging` nixpkgs locks to the current 26.05 revision.
- Commit on a feature branch, fast-forward to `master`, and push.

## Compatibility and deployment
- All three channel inputs remain separate for deployment control, but now
  resolve to the same 26.05 revision.
- This is a nixpkgs channel change for stable NixOS hosts and production/staging
  vpsAdmin/vpsAdminOS inputs. Deployment should still be controlled through
  normal configuration rollout.

## Testing plan
- Run Overcommit hooks.
- Verify `confctl inputs channel ls '{nixos-stable,production,staging}'`.
