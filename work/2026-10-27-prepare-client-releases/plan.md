# 2026-10-27-prepare-client-releases

## Goal

I'd like to release haveapi 0.31.0 and vpsadmin-typescript-client. haveapi-typescript-client is a new gem, so we'll need a pending trusted publisher. vpsadmin-typescript-client will need a manual publication, I believe... so you'll have to prepare it and instruct me.

## Affected repositories

- `haveapi`: coordinated 0.31.0 release of every maintained component: Ruby
  server/client, Go/Rust/TypeScript generator gems, npm client and browser bundle,
  Python, and PHP/Composer. Includes first haveapi-typescript-client publication.
  User explicitly reconfirmed this full scope; Elixir is unmaintained/excluded.
- `vpsadmin-typescript-client`: independent repository, default `main`; prepare
  its first public npm release as 0.1.0 with the MIT license.
- `haveapi-client-php`: existing coordinated HaveAPI PHP mirror destination,
  default `master`; prepare exact retained snapshot/provenance for approved
  atomic master/tag synchronization under a short repository claim.

## Approach

1. Architect investigates current release procedures, versions, registry state,
   and publisher identity; records the smallest execution packages in design.md.
2. Implementers prepare independent repository release changes, artifacts and
   technical publication instructions, with hooks and quick checks.
3. Lead checks user-facing release text and accepts evidence. Run independent
   final review of committed substantive changes, then required longer checks.
4. Publish feature branches and prepare exact release actions. Obtain explicit
   repository/target integration approval if default-branch changes are needed.
5. Execute the authorized HaveAPI release when prerequisites permit; provide
   the user the pending publisher fields and manual vpsAdmin client commands.

## Decisions

- Keep scope to these releases; avoid unrelated generator or workflow redesign.
- The user owns manual vpsAdmin TypeScript client publication and account-only
  authentication steps. Never record registry credentials.
- Release authorization does not imply default-branch integration approval.
- User explicitly selected MIT license and version 0.1.0 for the SDK and
  confirmed that the pending RubyGems publisher has been saved.
- Retain SDK generator/schema inputs and exact haveapi-client@0.30.2 runtime;
  regeneration and runtime upgrades are outside this release milestone.
- The first HaveAPI tag run failed before retaining artifacts or publishing
  packages because maintenance-lineage tests used the checkout's current minor
  version while constructing synthetic 0.30 fixtures. Correct fixture isolation
  and retain a synthetic future-minor regression; preserve production guards.
- Latest user direction keeps 0.31.0 and authorizes fixing/retrying the failed
  unaccepted tag, superseding an interim 0.31.1 decision. Preserve the original
  tag identity/source in a recovery ref and records; replace only that exact
  failed tag with an old-object lease after checks and affected final review.
- Completed milestone: HaveAPI 0.31.0 published/verified at every maintained
  destination; SDK 0.1.0 published by user and exact integrity verified.
- New user milestone: release SDK 0.1.1 through trusted publishing to verify its
  configuration. Limit changes to standard version/lock/provenance metadata;
  keep the genuinely published 0.1.0 source boundary. Automation requires source
  on main, so explicit SDK/main integration approval remains a separate gate.

## Compatibility and deployment

Confirm component version consistency, generated client/package contracts and
release ordering before tagging. New publisher registration must match the exact
repository, workflow and environment. No infrastructure deployment is planned.
Registry releases are persistent: verify final source and artifacts before
publication; recovery normally requires a subsequent version rather than reuse.
Architect will identify any schema or mixed-version constraints; no migration
changes are requested.

## Documentation

Readers are the release operator and future maintainers. Keep version-specific
commands, artifacts and publisher fields in this session; update owning project
release documentation only where the existing procedure needs a lasting fix.

## Testing plan

Use each owning repository's declared Nix environment and hooks. Bound checks to
version/package metadata, artifact contents, and documented release checks. Run
quick checks before final independent review, then required long checks through
the monitoring skill. Verify actual registry state after publication.
