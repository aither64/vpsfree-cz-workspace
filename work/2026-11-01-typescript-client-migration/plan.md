# 2026-11-01-typescript-client-migration

## Goal

Implement full adoption of `vpsadmin-typescript-client` in vpsadmin-webui,
replacing the custom endpoint/request solution. The user accepted the assessment,
authorized regeneration with current HaveAPI, permitted SDK changes for clarity
and separation of concerns, required those changes to come from its generator,
and authorized autonomous implementation in isolated worktrees. The user may
steer the work while it proceeds. Merge, registry publication and deployment
have not been requested.

## Affected repositories

- `haveapi`: TypeScript generator, generated public APIs and focused regression
  tests. Reusable transport remains HaveAPI-owned.
- `vpsadmin-typescript-client`: schema/provenance refresh, regeneration from the
  exact generator revision, current runtime alignment, package consumer checks.
- `vpsadmin-webui`: shared request policy and full migration of vpsAdmin calls,
  capabilities, outputs, tests, documentation and reproducible dependency pins.
- `vpsadmin`: clean full-fixture schema export input; API behavior changes are
  not planned.

## Approach

Architect `architect0` owns `design.md`, stable contracts and package boundaries.
Lead owns acceptance, tracking, coordination and user communication. Eight
retained implementers own complete execution packages through source, tests,
technical docs, hooks, commits and follow-up fixes. Preserve retained settings.

Generator foundation and clean schema capture precede final SDK regeneration;
the shared WebUI policy/pilot must pass before dependent domain migrations run
in parallel. Temporary compatibility wrappers are transitional only. Final
acceptance removes `haveApiCall`, `CallOpts`, historical unwrapping and duplicate
wire DTOs. SDK functionality improvements originate in the HaveAPI generator;
never patch generated SDK files directly.

Provisional owners: implementer0 generator; implementer1 schema/SDK package;
implementer2 WebUI foundation/pilot/shared integration; implementer3 VPS/storage;
implementer4 networking/DNS; implementer5 users/settings; implementer6
infrastructure/operations; implementer7 finance/content. Activate packages only
when their dependencies and file boundaries are settled in `design.md`.

## Decisions

- Prefer a clean separation of reusable SDK mechanics and WebUI application
  policy; SDK changes are authorized when needed for that separation.
- Preserve authentication, server authorization, capability discovery, error
  semantics and transport behavior in any proposed solution.
- Do not treat generated TypeScript types as runtime validation.
- All vpsAdmin operations and descriptions/capability queries use SDK APIs in
  the final tree. BFF/session/OAuth and external downloads remain their own
  protocols, not invented vpsAdmin SDK operations.
- Serialize Git operations and overlapping edits per repository. Rebase at
  phase boundaries and before final review, inspect upstream additions, and
  migrate new custom call sites too. Preserve colleagues' commits and behavior.

## Compatibility and deployment

Preserve old/new supported API combinations, live field/permission checks,
public isolation, OAuth BFF boundaries, uncertain-write handling, no automatic
write replay, action-state receipts and pagination completeness. No persistent
state/schema or node protocol migration is intended. Rollback restores the
previous frontend/dependency artifact; already accepted server writes still
require reconciliation. No integration or deployment approval is inferred.

## Documentation

Readers are implementers, reviewers, maintainers and operators. `design.md`
contains the architect-owned implementation/verification brief and assessment
evidence. Lasting SDK contracts go in HaveAPI/SDK docs; final WebUI architecture,
API/provenance/package docs and work log change with implementation. Temporary
phase/revision/rebase evidence remains in session records.

## Testing plan

Run focused generator/SDK consumer and WebUI quick checks per package. Complete
and commit intended changes, consolidate transitional history and pass quick
checks before mandatory independent final review by retained reviewer0
(Astra/xhigh). Then run the risk-appropriate longer build/integration/browser
checks, using fresh verification watchers for long/uncertain operations. Record
exact commits, schemas and dependency inputs. Verify real isolated API behavior
separately from fixtures. No new validation framework or unrelated API fixes.

## Execution records

- [Architect-owned implementation brief](design.md): exact generator contract,
  64-file domain partition, phase dependencies and verification.
- [Source-backed contract dispositions](contract-dispositions.md): unsupported
  current request shapes and minimal direct-consumer corrections.
- [Execution backlog](backlog.md) and [milestones](implementation-milestones.md).
- [Original feasibility assessment](assessment.md): evidence and scope before
  the user authorized full implementation.

The first foundation source changes are underway. A fresh full-fixture capture
is byte-identical to the prior schema; source/tooling provenance is refreshed.
Generator changes add reusable SDK facilities and retain current0.32 runtime
support. Later domain fixes address real unsupported controls and advisory
revision checks, preserving supported semantics without backend expansion.
