# 2026-10-22-haveapi-release

## Goal

Prepare HaveAPI 0.30, the first release containing rewritten JavaScript
clients, the Rust client generator and Python client. Audit release processes,
prepare version metadata and release documentation, verify package artifacts,
and identify exact pending trusted-publisher registrations.

## Affected repositories

- `haveapi`: release metadata, packaging, workflows and release documentation.
- Workspace: this session's coordination records only. No downstream pin changes.

## Approach

1. Architect audits current release paths, compatibility, package names and
   registry bootstrap constraints, then records the design and execution packages.
2. Implementers prepare independent release packages with serialized Git work.
3. Commit intended changes, pass quick checks, inventory the complete branch,
   and run independent final review before longer verification.
4. Publish the development branch and provide an actionable release checklist,
   trusted-publisher reminder, verification results and remaining operator steps.

## Decisions

- This request authorizes release preparation. Default-branch integration needs
  explicit direction for the repository and target under workspace rules.
- No registry publication, release tags or GitHub release publication during
  preparation. Describe the concrete ready result before asking for any final
  release/integration direction that is required.
- A crates.io credential is available locally. Never include its value in
  output, notes, prompts or commits; use only if an authorized registry action
  actually requires it.
- Retain the current session and saved team settings; leave the session open.

## Compatibility and deployment

Assess package version alignment, generated clients and runtime dependencies,
JavaScript upgrade behavior, Python/Rust minimum versions and first publication
ordering. Preserve old-client/server compatibility and document intentional
breaks. No production deployment or database change is planned.

## Documentation

- Readers: release operator, SDK consumers and future maintainers.
- Repeatable release instructions belong in HaveAPI; exact release evidence and
  pending registry registrations belong in this session.
- Lead owns final user-facing release prose after technical facts are settled.

## Testing plan

Use HaveAPI's declared Nix environment, hooks and release checks. Quick checks
must precede committed-deliverable review; longer builds/tests use a fresh
utility watcher. Validate package contents and dry-run paths without publishing.
