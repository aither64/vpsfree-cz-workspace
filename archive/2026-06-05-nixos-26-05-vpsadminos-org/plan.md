# Upgrade vpsadminos.org to NixOS 26.05

## Goal

Upgrade `vpsadminos-org-configuration` from NixOS/nixpkgs 25.11 to 26.05
for both direct NixOS host configuration and the vpsAdminOS input consumed by
the vpsadminos.org machines.

## Affected repositories

- `vpsadminos-org-configuration`
  - Branch: `2026-06-05-nixos-26-05-vpsadminos-org`
  - Worktree:
    `worktrees/2026-06-05-nixos-26-05-vpsadminos-org/vpsadminos-org-configuration`

`confctl` is used as the tool source and provided the
`confctl-configuration-update` skill. No `confctl` code changes are planned.

## Current inventory

- `nixpkgs` input: `github:NixOS/nixpkgs/nixos-25.11`, rev `25f53830`
- `vpsadminos` input: `github:vpsfreecz/vpsadminos/staging`, rev `62de2d8b`
- Channels:
  - `nixos-stable`: role `nixpkgs`
  - `os-staging`: role `vpsadminos`
- Machines:
  - `org.vpsadminos/int.builder`
  - `org.vpsadminos/int.cache`
  - `org.vpsadminos/int.docker-registry`
  - `org.vpsadminos/int.gh-runner1`
  - `org.vpsadminos/int.gh-runner2`
  - `org.vpsadminos/int.gh-runner3`
  - `org.vpsadminos/int.images`
  - `org.vpsadminos/int.iso`
  - `org.vpsadminos/int.www`
  - `org.vpsadminos/proxy`

All listed machines currently have `spin = "nixos"` and consume both
`nixos-stable` and `os-staging`. vpsAdminOS is present as a release-coupled
input used by profiles and artifact/doc/ISO builds.

## Release notes checklist

Official sources read:

- NixOS announcement:
  https://nixos.org/blog/announcements/2026/nixos-2605/
- NixOS 26.05 release notes:
  https://nixos.org/manual/nixos/stable/release-notes
- Nixpkgs 26.05 release notes:
  https://nixos.org/manual/nixpkgs/stable/release-notes.html

Items to watch during evaluation/build:

- systemd stage 1 is now the default; old scripted stage 1 is deprecated and
  scheduled for removal in 26.11.
- `nixos-rebuild-ng` is enabled by default; remove or avoid stale
  `system.rebuild.enableNg` handling if encountered.
- GCC 15, Node.js 24 LTS, and Ruby 3.4 are defaults and may affect local
  packages, scripts, documentation generation, or hooks.
- Large package removals and deprecated aliases may affect overlays and
  vpsAdminOS documentation/manual builds.
- NetworkManager VPN plugin defaults, Syncthing 2, Keycloak, Varnish/Vinyl
  Cache, MinIO deprecation, and OPA 1.0 changes are checked if any of those
  services appear in the configuration.

## Approach

1. Update `flake.nix` release URL for `nixpkgs` from `nixos-25.11` to
   `nixos-26.05` as a manual configuration edit.
2. Use `confctl inputs channel update --commit --no-changelog --no-editor`
   for `nixos-stable nixpkgs`.
3. Use Confctl to refresh `os-staging vpsadminos`, because the vpsAdminOS input
   follows `nixpkgs` and should be validated against 26.05.
4. Build representative machines first:
   - `org.vpsadminos/int.iso` for vpsAdminOS ISO/artifact paths.
   - `org.vpsadminos/int.www` for docs/manual generation paths.
   - `org.vpsadminos/proxy` for public NixOS service configuration.
5. Build the full fleet with `confctl build -y`.
6. Fix release warnings/evaluation failures in separate commits from generated
   input updates.

## Compatibility and deployment

- Persisted state: no schema or on-disk format edits are intended. Existing
  service state should be compatible unless release notes or builds reveal a
  service-specific migration.
- Database schemas: no database migrations are expected from the configuration
  change itself.
- API/protocol contracts: no public API shape change is intended.
- Generated configs and modules: NixOS option deprecations/removals must be
  fixed before merge unless explicitly deferred.
- Mixed-version operation: machines can be rolled one at a time because this
  update does not change cross-host protocols. The vpsAdminOS artifacts built
  by `int.iso`, `int.www`, and related hosts should be deployed after those
  hosts build successfully.
- Rollback: rollback should be possible to earlier NixOS generations as long
  as no service-specific state migration is introduced during validation.
- vpsAdminOS fleet coordination: this repository publishes/builds vpsAdminOS
  artifacts, but does not directly update all running vpsAdminOS nodes. If a
  vpsAdminOS release-coupled change requires coordinated node updates, record
  it before merge.

## Testing

- `nix develop -c confctl inputs ls`
- `nix develop -c confctl inputs channel ls`
- `nix develop -c confctl ls`
- Representative `confctl build -y` targets listed above.
- Full `nix develop -c confctl build -y` sweep, unless blocked by local-only
  secrets or operator paths. Any blocker must be recorded in `state.md`.
