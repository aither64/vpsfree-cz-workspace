# 2026-11-01-typescript-client-migration

## Goal

I'd like you to check what would it take for vpsadmin-webui to use vpsadmin-typescript-client instead of the dynamic haveapi-client. Would be beneficial for correctness? Would it be difficult to implement? How about maintainability? Suggest a solution.

## Affected repositories

- `vpsadmin-webui`: consumer architecture and current dynamic client use.
- `vpsadmin-typescript-client`: generated client/runtime and release workflow.
- `haveapi`: current dynamic runtime and TypeScript generator contracts.
- Read-only assessment of fetched default branches; no implementation, merge or
  deployment is requested.

## Approach

Architect `architect0` owns the code investigation and recommendation in
`design.md`. Lead owns scope, acceptance inspection, session records and the
user-facing assessment. Compare concrete call patterns, shared types and runtime
behavior, identify confirmed gaps, and propose incremental adoption with bounded
effort estimates. Use existing implementers only for independent read-only
inventories if the architect needs them.

## Decisions

- Assess correctness, implementation effort and maintenance together.
- Preserve authentication, server authorization, capability discovery, error
  semantics and transport behavior in any proposed solution.
- Do not treat generated TypeScript types as runtime validation.

## Compatibility and deployment

Assess generated schema/API drift and old/new consumer/server combinations.
No persistent-state migration or deployment is being performed. A future
proposal must retain the OAuth BFF boundary and account for rollback.

## Documentation

Readers are the maintainer and a future migration implementer. Investigation
findings and the proposed solution belong in this session's `design.md`; no
product documentation changes are needed for this assessment.

## Testing plan

Inspect source and existing tests at exact fetched revisions. Do not run builds
or integration tests for a read-only feasibility assessment. State confidence
limits and the checks required for a later implementation.
