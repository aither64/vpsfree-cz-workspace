# NixOS 26.05 Port Plan

## Goal

Port vpsAdminOS to NixOS/nixpkgs 26.05. vpsAdminOS itself must build
against `github:NixOS/nixpkgs/nixos-26.05`; compatibility with 25.11 is
not required.

After the vpsAdminOS port is complete and merged or otherwise available at an
exact revision, port `vpsadmin` onto that vpsAdminOS/nixpkgs 26.05 input
graph. Then update `nixos-stable` and the vpsAdmin inputs in
`vpsfree-cz-configuration`.

NixOS 26.05 "Yarara" was announced on 2026-05-30. The announcement says
26.05 receives bugfix/security updates until 2026-12-31 and that 25.11 reaches
end of life on 2026-06-30:
https://nixos.org/blog/announcements/2026/nixos-2605/

## Affected Repositories

- `vpsadminos`
  - Primary port of flake input `nixpkgs` from `nixos-25.11` to
    `nixos-26.05`.
  - vpsAdminOS NixOS module import compatibility.
  - Native/package compatibility for nixpkgs 26.05, including Ruby 3.4 and
    GCC 15 fallout.
  - NixOS container templates under `os/lib/nixos-container`.
  - Image repository defaults that expose NixOS template versions.
  - Build and VM test coverage.
- `ruby-lxc`
  - vpsAdminOS `osctld` native dependency.
  - Needs a Ruby 3.4-compatible gem before vpsAdminOS packaged gems can be
    regenerated on nixpkgs 26.05.
- `vpsadmin`
  - Port vpsAdmin packages/modules/tests to the vpsAdminOS 26.05 input graph.
  - Update the `vpsadminos` flake input using the repository-local script.
  - Validate API/web UI packages, nodectl/nodectld packages, and integration
    tests against nixpkgs 26.05.
  - Refresh packaged gems if the vpsAdminOS gem build inputs change.
- `vpsfree-cz-configuration`
  - Follow-up channel/input update after vpsAdminOS and vpsAdmin are buildable
    on 26.05.
  - `nixos-stable` channel, plus related inputs that intentionally track the
    stable release (`home-manager`, possibly custom stable branches).
  - vpsAdmin input pins for services, staging, and production as needed.
  - Build checks for stable NixOS containers/machines, vpsAdmin services, and
    staging vpsAdminOS nodes.
- `confctl`
  - Flake-mode machine metadata loading for health checks.
  - Needed because `nix eval .#confctl.machines` serialises Nix store paths
    without realising derivation outputs used by local builder health-check
    commands.

## Current Workspace

- Initiative: `2026-06-03-nixos-26-05-port`
- `vpsadminos`
  - Worktree: `worktrees/2026-06-03-nixos-26-05-port/vpsadminos`
  - Branch: `2026-06-03-nixos-26-05-port`
  - Base: `origin/staging`, currently `a0adfcf74`
  - Feature head: `0ac745ae3`
- `ruby-lxc`
  - Worktree: `worktrees/2026-06-03-nixos-26-05-port/ruby-lxc`
  - Branch: `2026-06-03-nixos-26-05-port`
  - Base: `vpsfree`, currently `df19e1f`
- `vpsadmin`
  - Worktree: `worktrees/2026-06-03-nixos-26-05-port/vpsadmin`
  - Branch: `2026-06-03-nixos-26-05-port`
  - Base: `origin/master`, currently `ad03f5cad`
  - Feature head: `4f413dfd0`
- `vpsfree-cz-configuration`
  - Worktree:
    `worktrees/2026-06-03-nixos-26-05-port/vpsfree-cz-configuration`
  - Branch: `2026-06-03-nixos-26-05-port`
  - Base: `origin/master`, currently `1f1532af`
  - Feature head: `92982a0c`
- `confctl`
  - Worktree: `worktrees/2026-06-03-nixos-26-05-port/confctl`
  - Branch: `2026-06-03-nixos-26-05-port`
  - Base: `origin/master`, currently `771aacd9`
  - Feature head: `eb26c228`

## vpsAdminOS Approach

1. Update the flake baseline.
   - Change `inputs.nixpkgs.url` in `flake.nix` to
     `github:NixOS/nixpkgs/nixos-26.05`.
   - Refresh `flake.lock`.
   - Keep `nixpkgsUnstable` on `nixos-unstable` unless evaluation shows a
     reason to change it.

2. Evaluate vpsAdminOS against 26.05 before doing broad edits.
   - Run `nix flake check --no-build` or focused `nix eval` probes for
     `checks.x86_64-linux.os-eval`, `packages.x86_64-linux.toplevel`, and
     template outputs.
   - Fix module import path changes from nixpkgs first, especially files
     listed in `os/modules/nixos-modules.nix`.
   - Search and remove/update any 25.11-only compatibility shims where 26.05
     has made them invalid.

3. Handle likely NixOS 26.05 migration points.
   - Stage 1: NixOS 26.05 uses systemd initrd by default, while vpsAdminOS has
     its own stage-1 implementation and a read-only compatibility option in
     `os/modules/nixos-compat.nix`. Decide from evaluation failures whether
     vpsAdminOS should continue forcing the custom stage-1 surface or update
     compatibility stubs.
   - `system.rebuild.enableNg`: release notes say the old Bash
     `nixos-rebuild` path was removed. Search showed no existing use, but
     keep this on the check list for generated configs and tests.
   - Filesystems: release notes say `fileSystems.<name>.fsType` has no
     default. Existing vpsAdminOS test/machine paths mostly set it explicitly;
     verify generated container templates do too.
   - D-Bus: 26.05 defaults to `dbus-broker` for NixOS. vpsAdminOS has its own
     dbus module and an overlay setting `dbus = null`; verify this still
     builds and does not pull incompatible assumptions from nixpkgs modules.
   - Kernel: NixOS 26.05 defaults to Linux 6.18, but vpsAdminOS currently
     pins its own 6.12.91 kernel/ZFS pair in
     `os/packages/linux/available-kernels.nix`. Keep that pin unless a build
     failure requires a kernel/ZFS bump, then split that bump into its own
     focused commit.
   - Ruby: nixpkgs 26.05 uses Ruby 3.4 in this build graph. Rebuild
     vpsAdminOS gems and update native dependencies such as `ruby-lxc` when
     extension ABI/API checks fail.
   - Toolchain: nixpkgs 26.05 uses GCC 15. Fix local C package failures in
     vpsAdminOS overlays/packages when they are source-level issues, rather
     than weakening compiler checks globally.

4. Update NixOS container templates.
   - `os/lib/nixos-container/stable/minimal.nix` and
     `stable/impermanence.nix` derive the module name from
     `lib.trivial.release`, so 26.05 should naturally become
     `container_26_05`.
   - Add/import `stable/vpsadminos-26.05.nix` if the image repository should
     expose a versioned compatibility module, following the existing
     `vpsadminos-25.11.nix` pattern.
   - Point `os/lib/nixos-container/stable/vpsadminos.nix` at the current
     26.05-compatible module surface.
   - Update flake `nixosModules` exports and any aliases that currently stop
     at `container_25_11`.
   - Update `os/configs/image-repository.nix` so NixOS `26.05` and
     `26.05-impermanence` receive `latest`/`stable` tags. Keep old versioned
     entries only if still useful for the repository, but do not spend effort
     preserving 25.11 as the active stable target.
   - Regenerate or refresh template lock contents if the current flake lock
     clone logic needs 26.05 inputs.

5. Build and test.
   - Hook setup before commits: install/sign Overcommit in the repo shell;
     `git worktree add` reported that `.overcommit.yml` needs signing.
   - Initial checks:
     - `nix flake lock --update-input nixpkgs`
     - `nix flake check --no-build`
     - `nix build .#toplevel --no-link`
     - `nix build .#template-stable`
     - `nix build .#template-impermanence-stable`
   - Targeted tests:
     - `./test-runner.sh test 'driver/nixos'`
     - `./test-runner.sh test 'osctl/image-repository-build-service'`
     - `./test-runner.sh test 'dist-config/*'`
     - one smoke test that boots a NixOS container from the generated 26.05
       template, if available in the existing suite or easy to add.
   - Broader confidence before integration:
     - `./test-runner.sh test 'osctl/*'` or the CI subset if the focused tests
       pass and changes touch shared container/build behavior.

## vpsAdmin Approach

Start this after the vpsAdminOS 26.05 branch is buildable and has a concrete
revision to pin.

1. Update the vpsAdmin flake input graph.
   - `vpsadmin/flake.nix` follows `vpsadminos/nixpkgs`, so pinning the
     ported vpsAdminOS revision moves vpsAdmin to nixpkgs 26.05.
   - Use the repository-local `tools/update_vpsadminos_flake.sh`; do not edit
     `flake.lock` manually for this input. The script is the local rule for
     producing the isolated `flake.lock` commit.
   - If the vpsAdminOS branch is not merged yet, temporarily point
     `vpsadminos.url` at the feature revision/branch for validation, then
     normalize to the merged `staging` input when available.

2. Evaluate and fix 26.05 fallout in vpsAdmin.
   - Build/evaluate Nix packages that are consumed from
     `vpsfree-cz-configuration`: API, database package, web UI, supervisor,
     console router, download mounter, client, nodectl, nodectld, and
     libnodectld.
   - Check vpsAdmin NixOS and vpsAdminOS modules under `nixos/modules`,
     especially service module options affected by NixOS 26.05 changes.
   - Watch package changes that commonly affect vpsAdmin services:
     Ruby 3.4, PHP/Composer dependencies, MariaDB/MySQL clients, RabbitMQ,
     Redis, Node tooling for the web UI, and systemd service option changes.

3. Refresh packaged gems when required.
   - If Ruby code packaged for Nix changes, or if the vpsAdminOS gem build id
     changes and packaged nodectl/nodectld/libnodectld inputs must follow it,
     run `rake vpsadmin:gems` from the repository shell.
   - Keep generated gem rebuilds separate from functional changes, following
     the workspace rule for Nix-packaged Ruby gems.

4. Build and test.
   - Hook setup before commits: enter `nix develop` and sign/install
     Overcommit. The worktree checkout reported that `.overcommit.yml` needs
     signing.
   - Initial checks:
     - `nix flake check --no-build`
     - `nix build .#test-runner`
     - `nix develop .#api --command bundle exec rubocop`
     - `nix develop .#api --command bundle exec rspec`
     - `nix develop .#libnodectld --command bundle exec rspec`
   - Targeted integration checks:
     - `./test-runner.sh ls 'tag=ci'`
     - `./test-runner.sh test services-up`
     - at least one node/VPS lifecycle smoke test that exercises API,
       nodectld, and vpsAdminOS together.
   - Add or update CI selection metadata only if runtime paths, integration
     tests, or web UI Playwright scripts move or change shape.

## Configuration Repository Approach

Start this only after the vpsAdminOS and vpsAdmin 26.05 branches are buildable
and either merged or pinned to exact revisions.

1. Update channels through `confctl`, not by manually editing `flake.lock`.
   - Use `confctl inputs channel set --commit os-staging vpsadminos <rev>` if
     the vpsAdminOS port must be tested before merge.
   - Use `confctl inputs channel set --commit vpsadmin vpsadmin <rev>` or the
     matching staging/production channel command when the vpsAdmin port must be
     tested before merge.
   - Use `confctl inputs channel update --commit nixos-stable` for the stable
     NixOS channel when ready.
   - Use `confctl inputs set --commit confctl <rev>` if the ConfCtl metadata
     fix is required before it reaches the default branch.
   - Also review stable-following inputs in `flake.nix`:
     `home-manager` currently uses `release-25.11`; likely update it to
     `release-26.05` with the `home-manager` channel.
   - `nixpkgsMunin` currently points to `aither64/nixpkgs/25.11-munin-fastcgi`;
     decide whether a 26.05 equivalent branch is needed or whether the local
     override can be removed after evaluation.
     Decision: remove the custom input. NixOS 26.05 still lacks the Munin
     FastCGI module options, but the needed `munin-cgi-graph` service is small
     enough to define directly in the `int.munin` container configuration.
   - `nixpkgsStaging` and `nixpkgsProduction` still point at 25.11. Their
     upgrade is a separate production/staging channel decision unless the
     user asks to combine it with `nixos-stable`.
   - Update `vpsadminServices`, `vpsadminStaging`, and `vpsadminProduction`
     in the order chosen for the rollout. `vpsadminServices` follows
     `nixpkgsStable` and is the direct consumer for many stable NixOS service
     hosts.

2. Evaluate known consumers of `nixos-stable`.
   - Stable NixOS containers under `cluster/cz.vpsfree/containers/**`.
   - `cluster/org.vpsadminos/*` hosts using `nixos-stable`.
   - NixOS machines such as `build`, `em1`, `aitherdev`, APU hosts, and
     `nixos-live`.
   - vpsAdmin services that follow `nixpkgsStable` through `vpsadminServices`.

3. Build validation.
   - Enter `nix develop` so `confctl` and hooks use repository-pinned tools.
   - Run `confctl build` on a focused stable sample first:
     - `cz.vpsfree/machines/build`
     - `cz.vpsfree/machines/nixos-live`
     - `org.vpsadminos/*`
     - representative stable containers, including DNS, web/proxy, monitoring,
       and vpsAdmin services.
   - Expand to `confctl build "cz.vpsfree/nodes/stg/*"` after vpsAdminOS is
     pinned and the stable channel evaluates.
   - Use `dry-activate` only for nodes/hosts where runtime activation risk
     needs checking and secrets/network access are available.

## Compatibility And Deployment

- vpsAdminOS no longer needs to build with nixpkgs 25.11. The port can remove
  25.11-specific compatibility when it blocks the 26.05 build.
- Persisted host/container state should not change as part of this port unless
  a migration is explicitly identified. Do not change ZFS feature defaults,
  osctld state formats, dataset attributes, or image metadata formats without
  separate compatibility notes.
- Existing vpsAdminOS nodes may run older revisions while the image builder or
  staging nodes run the 26.05-capable revision. Avoid changing protocols
  between vpsAdmin, osctld, osctl-image, and image repository services unless
  coordinated deployment is documented.
- vpsAdminOS `osctld` now depends on the Ruby 3.4-compatible `ruby-lxc`
  release produced for this port. Deploy the vpsAdminOS gem/package update
  together with that gem availability; no osctld state format change is
  expected from this native-extension fix.
- vpsAdmin API/web UI/services and nodectld may not update at exactly the same
  time. Avoid API, RPC, database schema, queue payload, and nodectl/nodectld
  protocol changes unless they are explicitly backward/forward compatible or
  the deployment order is documented.
- vpsAdmin database migrations are not expected for a pure NixOS 26.05 port.
  If a migration becomes necessary, record rollback behavior and mixed-version
  behavior before implementation.
- NixOS container template images are versioned by NixOS release. New 26.05
  templates can be added without forcing existing containers to rebuild. The
  `latest`/`stable` tags should move to 26.05 only when the templates build
  and boot.
- Rollback from a vpsAdminOS 26.05 build should remain possible if no new
  on-disk format is introduced. If a kernel/ZFS bump is required, check ZFS
  feature flags and explicitly avoid enabling features that block rollback.
- The production `nixos-stable` channel update in
  `vpsfree-cz-configuration` should happen after vpsAdminOS 26.05 is
  available, because stable NixOS hosts and services may consume the updated
  vpsAdminOS input graph.

## Commit Shape

- `vpsadminos`
  - Commit 1: flake/nixpkgs 26.05 baseline and module compatibility fixes.
  - Commit 2: NixOS container template/image repository 26.05 updates.
  - Optional separate commit: kernel/ZFS bump, only if required.
  - Optional separate commit: generated gem rebuild, only if Ruby code or
    packaged gem inputs change.
- `vpsadmin`
  - Commit 1: isolated vpsAdminOS flake input update via
    `tools/update_vpsadminos_flake.sh`.
  - Commit 2+: Nix package/module/application compatibility fixes, if needed.
  - Optional separate commit: generated gem rebuild via `rake vpsadmin:gems`.
- `vpsfree-cz-configuration`
  - Automated `confctl` input update commits as generated.
  - Separate manual commits only for compatibility fixes discovered by builds.

## Open Questions

- Does a 26.05 replacement exist for `aither64/nixpkgs/25.11-munin-fastcgi`,
  or can that override be removed after the stable update?
- Should production/staging vpsAdminOS channels remain on 25.11 initially
  while only `nixos-stable` moves to 26.05, or should staging be moved to the
  vpsAdminOS port revision as part of the same rollout?
- Should `vpsadminServices` be updated first for stable service hosts, before
  `vpsadminStaging`/`vpsadminProduction`, or should all vpsAdmin inputs move
  together after validation?
- Do we want to keep all historical NixOS template versioned modules in
  `os/lib/nixos-container/stable`, or prune old ones now that 25.11
  compatibility is not required for vpsAdminOS itself?
