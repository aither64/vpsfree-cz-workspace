# HaveAPI 0.32 and generated vpsAdmin client releases

## Goal

Prepare an implementation plan for HaveAPI 0.32.0, followed by regeneration
and conditional minor releases of the vpsAdmin generated clients. This request
covers planning. Implementation, integration, tags and publication are future
execution steps.

## Affected repositories

- `haveapi`: coordinated release components and generators.
- `haveapi-client-php`: automatically maintained Composer distribution mirror.
- `vpsadmin`: committed-source API-description export, without production changes.
- `vpsadmin-go-client`, `vpsadmin-rust-client`,
  `vpsadmin-typescript-client`: regenerate and release only when changed.

## Approach

The architect-owned [design and verification brief](design.md) records the
repository evidence, exact commands, version inventory and execution boundaries.

1. **Preflight and prepare.** Refresh authoritative remote heads/tags and check
   registry availability. Create this session's feature worktrees; read local
   instructions and activate hooks/Nix environments. Inventory HaveAPI changes
   since v0.31.2 and distinguish its current master VERSION (0.31.0) from the
   previous release tag. Check publication prerequisites without changing them.
   Resolve Rust's divergent v0.1.0 tag/main history and Go's remote tag baseline.
2. **Prepare HaveAPI 0.32.0.** In the top-level Nix shell run
   `make release-deps`, then `make version VERSION=0.32.0`; update release notes
   for the five Ruby gems, npm/browser client, Python package
   and Composer client. Elixir is excluded by the existing release procedure.
   Retain prepared library dependency locks locally, without adding ignored
   library locks or generated documentation/build output to Git.
   Keep changes focused on packaging the existing intended release content.
   Run quick checks, commit, and obtain independent final review of the entire
   branch/history before longer tests and package checks. Publish the feature
   branch and validate CI.
3. **Integrate and publish HaveAPI.** After explicit named-target integration
   direction, fast-forward the reviewed metadata into HaveAPI master. Follow
   the documented `haveapi-0.32` branch and annotated `v0.32.0` release process
   from the exact approved commit. Publication includes the protected workflow
   environment and PHP mirror master/tag updates. Verify every distribution
   before dependent client publication; reconcile partial releases first.
4. **Regenerate clients, preserving their versions during comparison.** Use
   exact HaveAPI 0.32.0 source. Capture public API 7.0 once for Go/Rust and reuse
   it offline; use the established full-plugin committed-source fixture export
   for TypeScript. Review source/input changes separately, retain hashes and
   provenance, and compare generated code, public types and copied runtime.
   Check file removals as well as additions. Update only necessary generator
   tooling; TypeScript may need pinned Prettier 3.9.10 available to regeneration.
5. **Apply the conditional release gate.** A client gets a minor release only
   for meaningful generated code/type/runtime changes. Provenance, formatter,
   pin, ownership-manifest or version-only churn does not qualify. For changed
   clients, bump versions and applicable locks/configuration/changelogs, then
   regenerate and verify deterministic output. For unchanged clients, retain
   the version and record that publication was skipped. Required handwritten
   tooling changes still receive checks and independent review.
6. **Verify, integrate and publish changed clients.** Commit all intended
   changes, pass quick checks and independent final whole-branch review, then
   run applicable longer checks/CI. Integrate each named default only on
   explicit direction. Release Go by semver module tag, Rust through its
   protected release workflow, and TypeScript from the validated npm archive.
   Verify public artifacts, integrity/provenance where provided, and clean
   consumer installation/builds. Record exact integrated heads and releases.

| Client | Inspected source version | Conditional target |
| --- | --- | --- |
| Go | No version or tags in local clone | Next minor from authoritative tags; if none, propose first v0.1.0 |
| Rust | 0.1.0 | 0.2.0 |
| TypeScript | 0.1.1 | 0.2.0 |

These are source-ref findings, not claims of registry publication. Actual
generated diffs and current remote versions remain execution-time evidence.

## Owners, dependencies and acceptance

| Package | Planned owner | Dependencies | Acceptance |
| --- | --- | --- | --- |
| Technical design | architect0 | Read-only investigation | Evidence and verification brief saved |
| HaveAPI release preparation | implementer0 | Ref/registry preflight | Coordinated metadata, hooks/checks, committed reviewed branch |
| Schema capture/export | implementer1 | Exact HaveAPI source and committed vpsAdmin source | Reviewed per-profile inputs with provenance |
| Go regeneration/release preparation | implementer0 | HaveAPI package complete; public snapshot | Meaningful diff or documented skip; inventory and compile checks |
| Rust regeneration/release preparation | implementer2 | Same public snapshot; tag/main lineage resolved | Meaningful diff or skip; provenance, default/blocking and package checks |
| TypeScript regeneration/release preparation | implementer3 | Full-fixture export and exact generator/tooling | Meaningful diff or skip; deterministic generation, consumer/package checks |
| Independent final review | reviewer0 | Committed deliverables and passing quick checks | Findings reconciled; whole-history and migration conclusions |
| Integration/publication coordination | lead | Explicit scope approvals and accepted evidence | Remote ancestry, workflow/artifact and consumer verification |

Owners are planned assignments, not active implementation tasks. Recheck the
live roster/access before assigning them. Client packages become independent
after their exact generator and schema inputs are settled; serialize changes
and Git operations within each repository. All long/uncertain verification is
launched and monitored through the required fresh utility.

## Decisions

- Treat 0.32 as 0.32.0, following HaveAPI's coordinated release conventions.
- Compare regenerated clients before editing their versions or release notes.
  Version-only changes do not qualify an unchanged client for a release.
- Preserve each client's established generation-input profile unless a change
  is explicitly justified. Record API-description and generator provenance.
- Confirm registry/tag availability during execution; local refs alone do not
  establish which artifacts are published.
- Keep TypeScript's exact HaveAPI runtime peer/dev requirement at 0.30.2 unless
  a demonstrated generated-runtime contract requires a change. Generator 0.32
  alone does not require consumers to upgrade their runtime.
- Preserve published release tags. Rust's inspected v0.1.0 release commit is
  not an ancestor of inspected main; reconcile source and release-workflow
  differences before preparing 0.2.0 rather than treating the tag as main.

## Compatibility and deployment

- Assess generator/runtime compatibility and old-server/new-client behavior.
- API remains version 7.0; Go/Rust copy their runtime, while TypeScript depends
  on the HaveAPI npm runtime. Additive API fields, removed actions, required
  parameters and public type changes need explicit diff assessment.
- No production deployment, persistent-state migration, downstream Terraform
  provider update or configuration-pin update is proposed by this plan.
- Integration into named remote defaults requires separate explicit direction.
  HaveAPI's automated PHP mirror update must be included in publication scope.
- Public versions and tags are durable release boundaries. Handle partial
  publication through the documented release recovery process, preserving
  published artifacts and recording exact results.
- Old and new client packages may coexist against compatible API 7.0 servers.
  Roll back consumers by their prior version and lockfile; already submitted
  API actions are unaffected by a software rollback. No DB/on-disk format or
  node protocol change is proposed, and no coordinated fleet update is needed.

## Documentation

- Readers: release operator, implementers and independent reviewer.
- Session delivery order and decisions live here; technical commands and
  acceptance criteria live in `design.md`; progress/evidence lives in `state.md`.
- During implementation, update affected package release notes and existing
  release documentation only where the final changes require it. The lead owns
  final member-facing release prose after technical facts are settled.

## Testing plan

- Planning checks: reconcile repository instructions, versions, generation
  commands, release dependencies and conditional-release criteria.
- Execution: use repository Nix environments/hooks, pass quick checks, commit
  intended changes and obtain independent final review before longer checks.
- Review the complete base-to-head history, final diff and migration provenance;
  apply the mandatory-review skill's generated-content exemptions precisely.
- Delegate checks/builds of uncertain duration or over one minute to the fresh
  verification utility under `dev-session-monitor`.
- Verify each published artifact and clean consumer installation after release.
