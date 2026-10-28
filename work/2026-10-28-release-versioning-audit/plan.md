# HaveAPI release versioning investigation

## Goal and scope

Explain why HaveAPI master reports 0.30 after publication of 0.31, and recommend
a correction grounded in Git history and actual release tooling. This request
initially covered investigation and a proposal. The user subsequently requested
"implement it", authorizing the accepted major/minor policy and its checks.
Publication and default-branch integration are not authorized by that request.

## Affected repositories and ownership

- `haveapi`, canonical read-only investigation via `repos/haveapi.git`.
- Architect `architect0` owns release-history/tooling investigation and the
  proposed design in `design.md`. Lead owns acceptance inspection, records and
  user-facing conclusions. Implementer0 owns the accepted HaveAPI execution package through fixes, checks,
  documentation, commits and feature-branch publication. Reviewer0 owns independent
  final review after committed completion and quick checks.

## Approach and acceptance criteria

1. Fetch current upstream refs, identify master and release/tag heads, and
   compare every relevant version source and ancestry.
2. Trace release preparation, publication and branch synchronization tasks.
3. Separate observed defects from unproven historical operator actions.
4. Recommend the smallest immediate repair and durable process safeguards,
   including how to verify the correction without publishing packages.

A successful report explains the mismatch with exact evidence, identifies
whether released source changes are missing as well as metadata, and states
remaining uncertainties and a bounded follow-up package.

## Compatibility and deployment

Implementation synchronizes maintained package identities and dependency
constraints to 0.31.0, enforces master patch zero and release major/minor floors,
and repairs a historical test fixture. No API, protocol, schema, persistent-state,
configuration or fleet change is intended. Preserve published tags/artifacts and
their original recovery tooling. Existing releases remain supported; new release
validation applies to future tagged tooling. Integration and publication retain
their separate approval requirements.

## Documentation and checks

Audience: HaveAPI maintainers. Preserve evidence and proposed design in this
session's `design.md`; maintain phase and acceptance evidence in `state.md`.
Update HaveAPI release instructions with the selected policy and recovery
constraints. Prepare dependencies in the Nix shell; run focused release/lineage
specs, metadata checks and declared hooks. Commit intended changes, inventory the
full branch and obtain independent final review before longer release checks.
Use fresh verification watchers for uncertain or long operations. Publish the
feature branch and verify its CI, leaving it ready for integration approval.

## Findings and recommendation

See [design.md](design.md) for accepted evidence and the unimplemented package.
The release branch received new metadata while master retained 0.30.0; the
procedure and checks permit this omission. Following the user's clarification,
master carries the latest major/minor base version with patch zero: catch up to
0.31.0, while haveapi-0.31 retains patch versions such as 0.31.2. Restore release
notes and the already-released test-fixture adaptation. For subsequent major/minor
releases, update master before cutting the release branch; patch version bumps
stay on release branches. Validate master patch == 0 and compare only numeric
major/minor pairs against the release candidate. Preserve a higher major/minor
master version and original published tags, artifacts and recovery tooling.
The earlier full-version floor/catch-up proposal is superseded. Historical
operator intent is unknown. No implementation or publication was performed.

## Authorization and delivery

User instruction: "implement it" after the major/minor-only proposal. Implement
the accepted design.md package on the session feature branch. No merge, release,
deployment, session archival or deletion is requested. Keep one implementation
owner because metadata, validation, fixtures and workflow checks are coupled.
