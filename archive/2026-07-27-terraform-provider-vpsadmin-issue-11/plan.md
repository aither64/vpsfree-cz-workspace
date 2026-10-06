# 2026-07-27-terraform-provider-vpsadmin-issue-11

## Goal

Verify the diagnosis in terraform-provider-vpsadmin issue #11, prove that the
current provider no longer sends an empty `hypervisor_type` while resolving an
OS template, and prepare the next provider release for review. Stop before any
tag, GitHub release, issue mutation, or Terraform/OpenTofu registry
publication. The user subsequently authorized pushing the development branch
to obtain GitHub Actions results.

## Affected repositories

- `vpsadmin`
  - branch: `2026-07-27-terraform-provider-vpsadmin-issue-11`
  - worktree:
    `worktrees/2026-07-27-terraform-provider-vpsadmin-issue-11/vpsadmin`
- `terraform-provider-vpsadmin`
  - branch: `2026-07-27-terraform-provider-vpsadmin-issue-11`
  - worktree:
    `worktrees/2026-07-27-terraform-provider-vpsadmin-issue-11/terraform-provider-vpsadmin`

## Approach

1. Confirm the versions published by GitHub, Terraform Registry, and OpenTofu
   Registry, and compare release `v1.2.0` with current `origin/master`.
2. Trace request serialization in the vpsAdmin Go client pinned by each
   provider revision and reproduce the failure/success against a controlled
   HTTP endpoint and the public live API endpoint.
3. Determine the repository's versioning and release process and choose the
   next semantic version based on all changes since `v1.2.0`.
4. Add only the tests or release metadata needed to make the fix and release
   readiness durable. Repair release-blocking development-shell failures found
   on current `origin/master`, then run quick local verification.
5. Commit intended changes, run the mandatory fresh-context change review,
   resolve significant findings, and run the relevant full test/build/release
   checks.
6. Backport only the API example corrections from vpsAdmin branch
   `2026-06-15-vpsadmin-events`, without taking any event work. Update the
   provider's vpsAdmin flake input to the isolated fix branch.
7. Push both development branches, inspect every GitHub Actions result and any
   failed-attempt evidence, then present the exact candidate commits, proposed
   tag/release notes, and remaining publication commands for review without
   publishing a release.

## Compatibility and deployment

The provider is a client-side executable. No database, persisted server-side
state, API contract, protocol, NixOS module, or vpsAdminOS on-disk format is
changed. The vpsAdmin correction changes documentation examples only, aligning
them with the output schemas that already govern actual responses.
The effective request change is backward compatible: the provider uses the
API's maximum accepted page size of 1000 instead of the rejected value 10000.
The optional `hypervisor_type` was already omitted by v1.2.0 and remains
omitted, letting the API select vpsAdminOS templates. Existing Terraform state
must remain readable by the current provider; this will be covered by the
existing unit and integration suites.

Because `origin/master` contains multiple provider behavior fixes and dependency
updates after `v1.2.0`, the next release will be assessed as a minor release
unless repository history or compatibility checks show that a patch release is
the established policy. Deployment is an opt-in provider upgrade; no
coordinated server or node rollout is required. Rollback consists of pinning the
previous provider version, though v1.2.0 remains unable to create VPSes against
the current API.

## Testing plan

- Controlled request capture comparing `OsTemplate.Index` in v1.2.0 with the
  client pinned by `origin/master`.
- Public live API checks for limits 10000, 1000, and 100, plus explicit empty
  `hypervisor_type`.
- Regression test asserting both the valid page limit and omission of
  `hypervisor_type`.
- `nix develop -c make test`
- `nix develop -c make test-get-token`
- Provider build and release snapshot/package check using the repository's
  documented release tooling.
- `nix build` and `nix flake check` to cover the pinned Nix package and shell
  after removing the stale exact Go patch assertion.
- Existing integration suite when quick checks and mandatory review pass.
- vpsAdmin API smoke specs with packaged HaveAPI 0.29.8, proving that the
  complete API can mount and serve its description.
- Provider integration suite with its vpsAdmin input pinned to the isolated
  correction branch.
- Verify clean worktree, commit contents, proposed semantic version, and that no
  release tag or external publication state changed.
