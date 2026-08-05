# 2026-08-05-vpsadminos-test-disk-image-reuse

## Goal

Add evaluation-only regression coverage proving that vpsAdminOS test machines
reuse the same squashfs image when only test or machine labels change, while
different machine configurations still produce different images.

## Affected repositories

- `vpsadminos`

## Approach

- Add a dedicated vpsAdminOS disk image reuse check alongside the existing
  NixOS check.
- Compare the `squashfs` machine output because osvm attaches it to vpsAdminOS
  test VMs as the read-only root filesystem drive.
- Assert reuse across test-name and machine-name changes and separation when a
  deterministic `/etc` marker changes the system closure.
- Export the check from the flake and run it as a separate CI step before the
  main OS build without realizing the squashfs outputs.

## Compatibility and deployment

This is test-only. It adds one flake check and does not change runtime code,
persisted state, APIs, protocols, image formats, or deployment behavior. The
existing NixOS check remains unchanged, so current check consumers continue to
work. No coordinated machine or node update is required.

## Testing plan

- Build both disk image reuse checks with `--no-link`.
- Run the repository Overcommit checks from the Nix development shell.
- Run the mandatory standalone change review after committing the intended
  change and before relying on long CI validation.
- Push the feature branch and monitor GitHub Actions through completion.
