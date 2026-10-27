# 2026-10-27-prepare-client-releases

## Goal

I'd like to release haveapi 0.31.0 and vpsadmin-typescript-client. haveapi-typescript-client is a new gem, so we'll need a pending trusted publisher. vpsadmin-typescript-client will need a manual publication, I believe... so you'll have to prepare it and instruct me.

## Affected repositories

- `haveapi`: prepare the 0.31.0 release and its component gems, including the
  first `haveapi-typescript-client` gem publication.
- `vpsadmin`: inspect the owning client-generation/release package for
  `vpsadmin-typescript-client`; confirm its location and version in design.

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
