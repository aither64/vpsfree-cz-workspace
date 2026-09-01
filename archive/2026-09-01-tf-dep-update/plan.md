# 2026-09-01-tf-dep-update

## Goal

Refresh the Terraform provider's complete Go and GitHub Actions dependency
stack, remove known reachable vulnerabilities from the provider release,
retire the unsupported Go 1.25 build baseline, and publish provider version
`v1.5.0` after local, integration, review, and default-branch verification.

## Affected repositories

- `terraform-provider-vpsadmin`

## Approach

Use three focused commits:

1. Update both Go module graphs, set the minimum toolchain to Go 1.26.6,
   replace `get-token`'s deprecated `x/crypto/ssh/terminal` import with
   `x/term`, refresh the Nix vendor hashes, and document the new build
   requirement.
2. Test Go 1.26 and 1.27, build releases with the latest Go 1.27 patch, and
   update imported GitHub Actions to their latest compatible releases.
3. Set the provider version to `1.5.0` in the Makefile and Nix package.

Run the mandatory standalone change review after all commits and quick checks,
then run the full provider integration suite because the generated vpsAdmin
client and its request-origin validation change.

## Compatibility and deployment

Terraform resources, data sources, schemas, state formats, and provider
protocol remain unchanged. Existing configurations and mixed provider versions
remain compatible, and v1.4.0 can read state written by v1.5.0. There is no
server, database, protocol, generated configuration, or deployment ordering
change.

Source builds will require Go 1.26.6 or newer instead of Go 1.25.8. Release
binaries remain self-contained and retain the existing target matrix. Releases
will use the latest Go 1.27 patch.

## Testing plan

- Run formatting, module tidiness, provider and helper unit tests, builds,
  vet, generated-documentation idempotence, actionlint, GoReleaser validation,
  Nix package builds, evaluated version checks, and `git diff --check`.
- Run `govulncheck` for both modules using the release toolchain. Require zero
  reachable vulnerabilities and verify that `get-token` no longer depends on
  `x/crypto`.
- Run the mandatory standalone review with all commits and quick results.
- Run the full integration suite, then require branch and default-branch Go and
  integration workflows to pass on the exact tested commits.
- Publish lightweight tag `v1.5.0`, verify release assets, checksums and GPG
  signature, then verify Terraform Registry and OpenTofu Registry publication
  with clean pinned initializations.
