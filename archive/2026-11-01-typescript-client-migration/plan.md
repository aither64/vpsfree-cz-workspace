# 2026-11-01-typescript-client-migration

## Goal

Implement full adoption of `vpsadmin-typescript-client` in vpsadmin-webui,
replacing the custom endpoint/request solution. The user accepted the assessment,
authorized regeneration with current HaveAPI, permitted generated client changes for clarity
and separation of concerns, required those changes to come from its generator,
and authorized autonomous implementation in isolated worktrees. The user may
steer the work while it proceeds. HaveAPI/master integration is complete. The
user subsequently supplied the released client and requested adoption plus a
session-owned vpsAdmin preview. That milestone is delivered at WebUI4ed519b6
using exact registry0.3.0, with a running bridge cluster and verified OAuth login.
The earlier unpublished-input stage remains historical; the standard optional
local pack/no-save workflow is retained. The follow-up below authorizes conditional WebUI/main integration after semantic
adaptation, review and passing tests; production deployment remains separate. No registry publication or session cleanup is authorized.

## Current follow-up scope (2026-11-03)

Adopt the exact verified public0.4.0 client release. Semantically
rebase the migration onto current WebUI main and handle all legacy request usage
newly introduced upstream, beyond Git-conflict paths. Preserve upstream security,
optimistic concurrency and lifecycle behavior through generated operations and
retain supported request-policy/output boundaries. Keep actual deployed4ed
lineage and evidence available while consolidating obsolete unpublished approaches
within the user-authorized feature rewrite. Final design/history conclusions,
quick checks, committed independent review and full required tests/CI precede
conditional WebUI/main integration. Then use the configuration repository's
ordinary confctl WebUI channel update, bound to the actual merged remote revision.
No production deployment, configuration-default merge or session cleanup follows
without its applicable authorization. The existing preview stays running.

### Authorized cluster conclusion (2026-11-04)

The later user direction “merge it when you're done. then stop & release the dev
cluster” supersedes keeping the preview running. WebUI/main is now verified and
merged atbabe5142; the exact session cluster has been stopped and publicly
released, with absence independently verified. Session remains open. The already
requested configuration channel update is being refreshed to this merged source;
configuration/master and production activation still need separate authority.

### Follow-up after automatic broad-CI failures

The user explicitly requires fixing the observed failures and making broad smoke
run on PRs and other branches, so failures are detected before default integration.
Retain the already-merged670 history. Add reviewable follow-up commits for the
minimal evidenced fixture/product corrections and for automatic pull_request plus
all-branch push triggers, keeping manual dispatch and existing broad selections.
Do not change branch protection, weaken assertions or add a new runner framework.
The complete follow-up must pass quick checks, independent final affected review,
and broad premerge verification before any further WebUI/main integration.
The configurationb466 deliverable stays separately preserved; no configuration
master integration, deployment or preview change is inferred.

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

Generator foundation and clean schema capture precede final generated client regeneration;
the shared WebUI policy/pilot must pass before dependent domain migrations run
in parallel. Temporary compatibility wrappers are transitional only. Final
acceptance removes `haveApiCall`, `CallOpts`, historical unwrapping and duplicate
wire DTOs. generated client functionality improvements originate in the HaveAPI generator;
never patch generated client files directly.

Provisional owners: implementer0 generator; implementer1 schema/generated client package;
implementer2 WebUI foundation/pilot/shared integration; implementer3 VPS/storage;
implementer4 networking/DNS; implementer5 users/settings; implementer6
infrastructure/operations; implementer7 finance/content. Activate packages only
when their dependencies and file boundaries are settled in `design.md`.

## Decisions

- Prefer a clean separation of reusable generated client mechanics and WebUI application
  policy; generated client changes are authorized when needed for that separation.
- Preserve authentication, server authorization, capability discovery, error
  semantics and transport behavior in any proposed solution.
- Do not treat generated TypeScript types as runtime validation.
- All vpsAdmin operations and descriptions/capability queries use generated client APIs in
  the final tree. BFF/session/OAuth and external downloads remain their own
  protocols, not invented vpsAdmin generated client operations.
- Serialize Git operations and overlapping edits per repository. Rebase at
  phase boundaries and before final review, inspect upstream additions, and
  migrate new custom call sites too. Preserve colleagues' commits and behavior.

## Temporary unpublished generated client consumption

The optional development workflow remains useful after this migration. Document
the existing client build/pack commands and a temporary WebUI install with
`--no-save --package-lock=false --ignore-scripts`; `npm ci` restores the committed
dependency graph. Do not add an installer, Vite alias or persistent local switch.
The install may also change other temporary dependencies, so verify the actual
client and peer and restart Vite with `--force` when entering or leaving it.
Building does not regenerate source or bypass the exact generator revision check.

Before merge, select an actually available compatible released client and move
the committed dependency to that release. The user explicitly selected “Keep the
release transition pending” on2026-11-02; do not begin that dependency transition
or registry publication during the current verification milestone. This is not registry publication
authorization, and no suitable published version has been established yet. Keep
the current exact archive until that separate dependency transition, then remove
its Nix adapter and archive-specific inputs. The documented development override
survives that removal.

The architect will select the smallest conventional reproducible npm/Nix path
using the verified generated client candidate, and record files, provenance/update
procedure, checks and removal path in design.md before edits. W owns WebUI
manifest/lock/source-filter/Nix hash and guidance; generated client owner is involved only if
the selected design requires actual generated client packaging changes. No machine-local
absolute dependency, expiring artifact URL, invented registry version/integrity,
or new distribution service/framework. Generated source remains generator-owned.
Later registry adoption may remove temporary support when separately authorized;
this task does not authorize publication, release tags or default merges.

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
evidence. Lasting generated client contracts go in HaveAPI/generated client docs; final WebUI architecture,
API/provenance/package docs and work log change with implementation. Temporary
phase/revision/rebase evidence remains in session records.

## Testing plan

Run focused generator/generated client consumer and WebUI quick checks per package. Complete
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

The generator/client/WebUI foundation and domain migration are complete. The
full-fixture schema capture retained the prior schema bytes while refreshing
source/tooling provenance. Generated facilities retain runtime0.32 support; domain
corrections preserve supported semantics without backend expansion. Optional
local-client validation, scoped fixture repairs and exact-head Nix verification
are complete. See state.md for current published heads and required CI; the user
explicitly keeps the released dependency transition pending.

## Released-client adoption and development preview (user release)

The user now confirms that the generated client has been released and directs
using that release and starting a vpsAdmin development cluster to view the new UI.
Verify the actual published package/version/provenance, transition the WebUI from
its temporary tracked archive to the normal registry dependency, and remove the
archive-specific Nix adapter/checks/artifacts. Keep the documented optional
standard npm pack override. No generated source or application guards change
without evidence. Preserve published branch history and prior evidence scopes.

Architect0 owns the brief, implementer1 the release proof, implementer2 the complete
WebUI transition, and implementer6 the session cluster preparation. The lead owns
acceptance/review, long-operation utility release and user-facing preview handoff.
Use the final reviewed/verified candidate in the session-owned cluster; prefer
bridge networking and retain existing cluster state. Starting the preview does
not authorize production deployment, registry publication, default integration,
cluster reset, or session lifecycle cleanup.
