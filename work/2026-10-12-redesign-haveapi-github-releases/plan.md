# 2026-10-12-redesign-haveapi-github-releases

## Goal

I'd like to redesign haveapi releases (server and clients) to be done using github actions. Change also release documentation as appropriate. Exclude elixir server/client, it is not maintained. Suggest a solution.

## Affected repositories

- `haveapi`: release workflow, packaging helpers, Makefile and release docs.
- `vpsfreecz/haveapi-client-php`: existing publication destination. No independent
  library development or default-branch update is performed during this proposal.
- No downstream configuration, vpsAdmin or generated Go module changes.
- Exclude both Elixir implementations from versioning, builds and publication.

## Approach

Investigate the current release procedure and suggest an implementable design
first, as requested. The lead owns investigation and design in the retained
`lead_reviewed` mode. See [design.md](design.md) for the proposed implementation
and verification brief. Repository code and release documentation remain
unchanged at this proposal checkpoint.

Keep shared versions and `haveapi-X.Y` release branches. A manually pushed
`vX.Y.Z` tag starts validation, maintained-component tests and packaging on
GitHub-hosted runners using the top-level Nix shell. Publishing consumes the
exact checked artifacts after approval through a protected `release` environment.
Create the public GitHub Release only after all publication steps succeed.

## Decisions

- Continue releasing all maintained components together under one version.
- Use RubyGems and npm trusted publishing with short-lived OIDC credentials.
- Automate PHP synchronization to its existing root-layout Composer repository
  over SSH with a repository-scoped write deploy key.
- Provide a manual build-only workflow path for testing the release pipeline.
- Retain artifacts and make partial-publication recovery explicit. An existing
  version can be skipped only after verifying its content against the saved
  artifacts; never treat arbitrary publication errors as success.
- Keep version/changelog commits under maintainer control. The workflow neither
  prepares release commits nor invents the next version.

## Compatibility and deployment

No runtime/API/schema/protocol changes or database migrations. Preserve gem and
npm names, Composer package identity, PHP repository and tag scheme. Consumers
continue installing from their existing destinations; mixed server/client
deployments are unaffected by this tooling change. Add the workflow to master
and the currently supported release line before tagging a new automated release.
Integration into either branch needs explicit repository/target direction.

One-time operator setup: protected release environment, RubyGems trusted
publishers for three gems, npm trusted publisher, PHP SSH deploy key, and verified
Packagist synchronization. Writing this procedure does not execute publication.
Always obtain explicit authorization before publishing a new version.

Published versions and pushed tags are immutable. Recovery resumes missing
destinations with the same artifacts; defective published content requires a new
version. Consumers can select a previous package version without state conversion.

## Documentation

Readers: HaveAPI release maintainers and future contributors. Update the owning
repository's `doc/agent-instructions/releases.md` as the authoritative release
procedure, with a README pointer and aligned AGENTS.md instructions. Cover normal
releases, one-time setup, build-only checks, approvals and partial failure.
Keep proposal status, rollout revisions and review evidence in session records.

## Testing plan

Before implementation: confirm package identities, branch policy, toolchain and
published baseline; consult official trusted-publishing documentation.

After implementation: quick version/content checks, workflow lint and meaningful
release-helper checks; commit all intended changes; retained independent final
review including complete branch history and an explicit no-migrations conclusion;
then fresh Luna/low watcher for full maintained-component tests and package smoke
checks. Exercise safe build-only GitHub Actions before enabling publication.
Do not publish a test version without the user's explicit authorization.
