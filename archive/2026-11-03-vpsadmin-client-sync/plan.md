# vpsAdmin generated client synchronization

## Goal and current request

Bring Go, Rust and TypeScript clients up to date with vpsAdmin, release updated
client versions first, then establish ongoing synchronization rules. The user
will merge the in-progress WebUI TypeScript-client adoption after those releases.
The current request is to revise this plan; no execution starts in this turn.

All three clients were proven stale in the initial investigation. Findings and
source identities are preserved in [design.md](design.md) and the linked client
evidence. Refresh upstream identities before implementing; the inspected heads
are investigation evidence rather than frozen execution inputs.

## Phase 1: update and release clients

1. Recheck the API and HaveAPI defaults, client defaults, published versions and
   each repository's release procedure. Export a reviewed source-based API 7.0
   schema with the existing tools/export-api-schema and retain full provenance.
2. Regenerate Go, Rust and TypeScript in separate owned feature worktrees using
   pinned generators. Review the full contract diff, including removals and the
   missing advisory actions/state guards. Assess the move from public snapshots
   to the complete source-fixture profile for Go and Rust.
3. Prepare release metadata under each client's conventions. Default
   vpsadmin-typescript-client releases to a new minor version unless the user
   explicitly specifies otherwise. The inspected package is 0.3.0, so 0.4.0 is
   the tentative next release; verify tags/registry state before selecting it.
   Do not apply this versioning default to Go or Rust without their own policy.
4. Commit intended changes and pass quick checks, then independent final review
   of the complete branch histories and provenance, followed by the required
   language, regeneration, packaging and consumer checks. Use verification
   watchers for long or uncertain checks. Publish feature branches and inspect CI.
5. Integrate reviewed client updates into their defaults under explicit
   repository/target approval, then publish updated client releases using their
   native release procedures and verify published artifacts/tags. Keep these
   operations distinct from plan revision and preserve exact final-head evidence.
6. Hand released versions and artifact evidence to the user. The user owns the
   separate WebUI WIP merge; this plan does not take over that work or inspect
   another session's worktree.

Acceptance: all three regenerated client defaults cover the reviewed API
contract; applicable checks and independent review pass; updated releases are
available and verified. The TypeScript release uses the next minor by default.
This milestone must complete before Phase 2 begins; rule work must not delay it.

## Phase 2: institute future rules

- API-contract work must assess all three clients and finish with updated client
  defaults or source-tied no-generated-change evidence. Ordinary source
  synchronization alone does not require releases.
- When WebUI changes require new API support through vpsadmin-typescript-client,
  merging WebUI requires a published client release containing that support and
  final manifest/lock resolution to its registry artifact. Feature-branch/Git/local
  dependencies are allowed during development and removed before merge.
- A required TypeScript client release defaults to the next minor version;
  explicit user version/bump instructions override this default. An incompatible
  change still needs its compatibility impact stated before execution.
- Put the authoritative sync procedure in vpsAdmin's schema-export documentation
  and route it from AGENTS.md. Link client contributor guides and HaveAPI
  generator-change guidance. Add the release prerequisite to WebUI's existing
  maintainer/review instructions. Update workspace project routing as needed.
- Reuse existing regeneration/provenance checks. Go needs fresh-output comparison
  including deletions. Any added enforcement should extend existing tooling;
  distinguish saved-input reproducibility from current-API freshness.

Acceptance: reviewed and tested rules express the above completion and release
requirements, the minor-version default and the user override. Avoid circular
cross-repository merge gates and unbounded follow-up obligations.

## Owners and dependencies

The lead owns scope, plan/state, acceptance and release/integration coordination.
Architect0 owns the design and verification brief. Client execution packages go
to saved same-session implementers after checking live roster/access, with
independent client file boundaries. Phase 2 packages follow Phase 1 acceptance.
WebUI WIP integration remains with the user. No team changes are planned.

## Compatibility and recovery

Use API source rather than production discovery as the intended contract.
Retain source/profile/schema/generator identities and distinguish framework,
generator and runtime package versions. New client calls require compatible
API deployment or capability checks; publication alone does not establish server
availability. Review removals, type changes and mixed versions. Roll back input
snapshots, provenance, generator pins and generated trees together; retain
published releases. No database migrations or machine deployments are planned.

## Documentation and records

Readers are the user and future maintainers. Keep execution status and exact
release/merge/check evidence in state.md and linked receipts. Lasting rules and
release instructions belong in their owning repositories during Phase 2.

## User correction: site policy and conditional integration

The user rejects placing vpsAdmin-specific workflow rules in generic HaveAPI
instructions/development documentation. Withdraw the unmerged HaveAPI policy
commit; preserve its former review and lineage as rejected proposal evidence.
Site-specific coordination belongs with the vpsFree workspace/site extension,
if existing routing does not already cover it. Architect0 owns this bounded
placement reassessment; owner1 owns removing HaveAPI changes. No generic
framework policy, new enforcement system or runtime/deployment work is authorized.

Integration is conditionally authorized only when session
`2026-11-01-typescript-client-migration` finishes its current work. The user
states it is still working on broken WebUI behavior. A source integration
milestone is not terminal task completion; wait for explicit terminal dependency
evidence and refresh current public main before using this authorization.

Placement reassessment accepted: existing workspace verification routing already
covers HaveAPI generator changes affecting vpsAdmin clients. Remove only the
rejected HaveAPI proposal; add no site-extension feature. Remaining feature scope
is six repositories, with conditional integration authority retained.
