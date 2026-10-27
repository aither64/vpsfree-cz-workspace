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
- Milestone 2 (user addition): integrate/rework the supplied TypeScript documentation patch on this session's feature branch, add meaningful regression coverage and address the workload/routing gap.
- Milestone 3 (explicit user expansion): all registered client example renderers and supported modes must be included in meaningful performance tests, with registry coverage checks that fail on omissions. This includes generated TypeScript and Go, full-page rendering and authentication/action examples. Do not infer that Go needs a production fix.
- Architect owns design.md before substantive implementation. Implementer0 owns TypeScript adapter and direct regression specs. Implementer1 owns all-client performance fixture/runner/routing/tests and technical docs. Boundaries are independent; Git mutations in the shared session worktree are serialized by the lead.
- Independent final review after committed deliverable and quick checks; then appropriate longer checks and feature-branch publication.
- User subsequently explicitly authorized after verification: integrate HaveAPI into `master`, backport all new commits into `haveapi-0.31`, and release HaveAPI 0.31.1. Preserve source/backport/release-metadata commit separation, required hooks, short repository integration claims and protected release workflow gates. No host deployment requested.
- Necessary release blocker C: existing paired-performance preparation/live/replay rejects synchronized internal package version changes on the 0.31 line. Architect addendum defines narrow validated own-version normalization while preserving exact external dependencies/runtime/source proof/budgets and historical 0.30 lineage. Implementer1 owns this required correction, committed quick checks and same-reviewer affected-lane review before backport and final release review. No general baseline/replay redesign.

## Decisions

- The recurrence is a missing workload/assertion integration, not evidence that stricter timing thresholds would have detected an unconfigured renderer. Preserve the source/history distinction from inferred author intent.
- Use selected-subtree normalization from the supplied patch. Keep per-request authorization fresh and retain mixed-key, alias and selected-provider equality semantics; introduce no shared request cache.
- Enforce complete live renderer inventory and real Go/Rust/TypeScript profiles in a required current-source work/allocation and full-page contract. Preserve the older paired timing reference and budgets, which predate generated TypeScript.
- Support synchronized own-package version metadata in preparation/live/replay with source-bound raw evidence. Preserve all other manifest bytes, external dependencies/runtime/locks and historical 0.30 rules.
- Keep all source backports before one release metadata commit, prove equivalence independently, and publish only the exact tagged candidate validated by the protected workflow.

## Compatibility and deployment

Preserve generated example output, authorized per-request data boundaries and mixed string/symbol-key semantics. No API, schema, protocol, version or deployment changes intended. Implementation must avoid shared cross-request mutable caches; rollback is code-only.

## Documentation

Audience: the user and future maintainers investigating this recurrence. Preserve evidence in this session; no product documentation changes needed for an explanation-only investigation.

After implementation scope expanded, update HaveAPI's TypeScript documentation invariant, performance guide and existing client-example/development entry points. Preserve final investigation in findings.md, design in design.md, independent review records and release evidence in this session. Lead owns final user-facing changelog and summary.

## Testing plan

Inspect existing test assertions, workloads and CI entry points. Regression tests must reject recursive work proportional to unrelated schema descendants and exercise real generated TypeScript examples. Cover all registered renderers, modes, initialization/authentication/action paths and complete pages; an inventory guard must reject omissions. Bound checks to changed adapters, profile/fixture/runner and CI selection contracts; preserve authentication filtering and immutability. Preserve honest fixed-reference support without silently skipping missing client profiles or inventing measurements. Use mandatory independent review and monitoring procedures for final checks.
