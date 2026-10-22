# 2026-10-12-redesign-haveapi-github-releases

## Completed follow-up: resolve pending draft tags and test publication

The approved0.29.11 job failed before registry writes. The lead replaced REST tag
matching with the GraphQL pending-tag-to-ID lookup used by GitHub CLI, retaining
visible API errors and immutable source/artifact behavior. Masterc58704a and
release355c299 passed complete independent review, local/package checks and11safe
Actions. The user's logged-in gh diagnostic resolved the actual pending draft.

The user authorized both target integrations and0.29.12, then approved the human
GitHub release gate. Master is integrated; haveapi-0.29 and annotatedv0.29.12 point
to355c299. Tag run39313082898 passed all tests/build and published successfully.
Fresh read-only verification confirms all registry-served package bytes, PHP tag
snapshot/provenance, finalized GitHub assets and Packagist indexing match the
retained originals. npm now identifies vpsfreecz/haveapi as the repository and
latest is0.29.12. The requested release-process test is complete.

See state.md, release-0.29.12.md, pending-tag-review.md and
patch12-publication-verification.json. No runtime, migration or Elixir changes.
Original failed tags/drafts/files remain preserved. Session remains open.

## Original accepted follow-up: 0.29.10

The user requested a real patch release, chose automation-only 0.29.10 and
directed implementation of the proposed release plan. Prepare and review a
separate candidate from `haveapi-0.29`; preserve its fixes and tests. Backport the
release implementation/docs, use the verified current master Nix lock, and
commit the maintained-component version/changelog separately. Validate locally
and through safe Actions before updating the release branch and annotated tag.
Publication waits for the user's protected-environment approval in GitHub.
Record execution in [release-0.29.10.md](release-0.29.10.md); the design brief is
in [design.md](design.md). No unrelated runtime changes or Elixir publication.

## Goal

I'd like to redesign haveapi releases (server and clients) to be done using github actions. Change also release documentation as appropriate. Exclude elixir server/client, it is not maintained. Suggest a solution.

## Affected repositories

- `haveapi`: release workflow, packaging helpers, Makefile and release docs.
- `vpsfreecz/haveapi-client-php`: existing publication destination. No independent
  library development or default-branch update is performed during this proposal.
- No downstream configuration, vpsAdmin or generated Go module changes.
- Exclude both Elixir implementations from versioning, builds and publication.

## Approach

The user accepted the proposed approval flow and directed implementation. The
lead owns investigation, design and application edits in the retained
`lead_reviewed` mode. See [design.md](design.md) for the implementation and
verification brief. The workflow, helpers and repository docs are committed;
independent review precedes full verification and publication of the feature
branch. Preparing the implementation does not authorize a new package release
or integration into master/the supported release branch.

Outcome, 2026-10-19: the user subsequently authorized the HaveAPI master merge.
The exact reviewed and tested head `c14e7d3158b91c134c2817b489cd29772fc09f82`
is now integrated there. Supported release-line integration and a new version
remain separate future work; see [state.md](state.md) for receipts and limits.

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
