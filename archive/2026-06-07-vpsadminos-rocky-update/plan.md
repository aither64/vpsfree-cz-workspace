# 2026-06-07-vpsadminos-rocky-update

## Goal

Update Red Hat-family vpsAdminOS image build scripts, with priority on the
outdated Rocky Linux 9 and Rocky Linux 10 release RPMs. Use the
`update-redhat-family-image-releases` skill and upstream HTTP directory
listings rather than guessed versions.

## Affected repositories

- `vpsadminos`

## Approach

1. Reuse the active initiative slug
   `2026-06-07-vpsadminos-rocky-update`.
2. Work in
   `worktrees/2026-06-07-vpsadminos-rocky-update/vpsadminos` on branch
   `2026-06-07-vpsadminos-rocky-update`, based on `origin/staging`.
3. Run `ruby skills/update-redhat-family-image-releases/scripts/discover_release_updates.rb all`
   from the vpsAdminOS repository root.
4. Update only release-related lines in changed
   `image-scripts/images/*/build.sh` files:
   `POINTVER`/`RELEASE` for Rocky, AlmaLinux, and CentOS Stream; Fedora
   release suffix lines for stable releases; rawhide variables for rawhide.
5. Run `./test-runner.sh test image-scripts/test@<image-name>` for every
   changed image.
6. Keep commits split per changed image directory.

## Compatibility and deployment

These image scripts affect newly built container images. They do not change
running hosts, the vpsAdminOS runtime, database schemas, API contracts,
protocols, generated NixOS/vpsAdminOS options, or persistent on-disk state.
Existing deployed containers keep their current root filesystems until
operators explicitly rebuild or replace them. Rollback is possible by building
images from the previous script versions.

Mixed-version operation is expected: old image artifacts and newly generated
image artifacts can coexist. No coordinated update of all running machines or
nodes is required.

## Testing plan

- Run the skill discovery script for scope `all`.
- For every changed image directory, run:
  `./test-runner.sh test image-scripts/test@<image-name>`.
- Before committing, ensure Overcommit hooks are available and pass, using
  repository tooling or `nix develop --command overcommit --run`.
