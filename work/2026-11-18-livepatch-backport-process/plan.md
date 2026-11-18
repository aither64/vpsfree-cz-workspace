# Selective security livepatch backports

## Goal and current scope

Investigate the existing security-advisory selection policy and vpsAdminOS
livepatch workflow, then suggest a reusable process joining them. The process
must present CVEs and source fixes for user approval before backporting and must
surface important skipped fixes and residual exposure. Do not import all stable
patches. The first later execution targets 6.12.113 using fixes through 6.12.118.
This turn delivers investigation/design and a solution proposal, not a deployed
batch or vpsAdmin writes.

## Affected repositories

Read-only investigation: vpsadminos, security-advisories, linux as necessary.
Choose permanent procedure ownership from existing documentation; no project
changes until the proposal is settled.

## Approach and decisions

Architect owns bounded investigation and design.md. Lead coordinates scope,
acceptance and user communication. Existing team is retained; user explicitly
requested daybreak-blue for the team. Apply it through supported configuration,
preserving role purposes, access and effort. No merge/deployment authorization.

## Compatibility and deployment

Design must bind each batch to exact kernel source/configuration and existing
cumulative livepatch state, assess patch dependencies and runtime safety, retain
unsupported/uncertain cases, and describe rollback limitations. Later deployment
uses existing approval and verification procedures.

## Documentation

Readers: kernel/livepatch maintainers and advisory operators. Current proposal
and evidence live in design.md. Reusable runbooks should remain with their owning
projects and link the existing selection and livepatch procedures.

## Verification

Inspect current documented commands and contracts. No kernel builds or runtime
changes for this proposal. Candidate selection and technical safety are separate
conclusions; builds alone must not prove CVE remediation.
