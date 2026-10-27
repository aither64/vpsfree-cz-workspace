# 2026-10-27-api-copy-regression

## Goal

i'm told client examples in haveapi ruby server repeatedly copy the whole API description. The same performance regression was caused when we introduced the rust client, which prompted me to introduce performance tests. now tell me how is it possible that we have introduced the same bug in a different component. how come the performance test didn't catch it?

## Affected repositories

- HaveAPI: read-only investigation of TypeScript client example generation in the Ruby server, Rust-client history, performance tests and CI wiring. User clarified that TypeScript examples are the new problem.

## Approach

- Architect `architect0` owns source/history investigation and may delegate an independent test-coverage question to an existing implementer.
- Lead owns scope, acceptance inspection, tracking and user explanation.
- Acceptance: identify the concrete copy call path, establish chronology, explain exactly what performance tests measure and why they miss this behavior, and distinguish evidence from inference.
- Milestone 1: deliver findings explaining the recurrence and coverage gap.
- Milestone 2 (user addition): integrate/rework the supplied TypeScript documentation patch on this session's feature branch, add meaningful regression coverage and address the workload/routing gap. User additionally requested Go inclusion; architect audits Go examples and identifies necessary coverage without assuming a Go defect.
- Architect owns design.md before substantive implementation. One implementer owns the bounded fix, tests and technical docs unless independent packages justify another.
- Independent final review after committed deliverable and quick checks; then appropriate longer checks and feature-branch publication. No master integration, release or deployment authorized.

## Decisions

## Compatibility and deployment

Preserve generated example output, authorized per-request data boundaries and mixed string/symbol-key semantics. No API, schema, protocol, version or deployment changes intended. Implementation must avoid shared cross-request mutable caches; rollback is code-only.

## Documentation

Audience: the user and future maintainers investigating this recurrence. Preserve evidence in this session; no product documentation changes needed for an explanation-only investigation.

## Testing plan

Inspect existing test assertions, workloads and CI entry points. Regression tests must reject recursive work proportional to unrelated schema descendants and exercise real generated TypeScript examples. Verify Go path and performance inclusion. Bound checks to the changed Ruby adapter, profile/fixture/runner and relevant CI selection contracts; preserve authentication filtering and immutability. Use mandatory independent review and monitoring procedures for final checks.
