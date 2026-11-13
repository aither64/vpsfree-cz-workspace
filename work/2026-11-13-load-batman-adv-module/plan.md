# Load batman_adv in vpsAdminOS

## Goal and scope

Load `batman_adv` by default in vpsAdminOS, with its kernel module dependencies.
Affected repository: `vpsadminos`; no configuration pin updates, mesh setup,
production deployment or default-branch integration is authorized by this request.

## Approach and ownership

Architect0 investigates the existing module inclusion/loading path and records
one sufficient brief in [design.md](design.md). Implementer0 owns the narrow
source change, meaningful checks, commit and evidence after lead release.
Reviewer0 independently reviews the final committed branch after quick checks.
The lead owns acceptance, tracking and publication coordination.

## Compatibility and deployment

Use the existing module loader and dependency mechanism. Establish that the
selected kernel provides the module and dependencies without a kernel change.
No persisted state, API, protocol or migration changes are expected. Record
activation and rollback implications in the design. Staggered updates should
remain supported; no coordinated fleet update is expected. Deployment is a
separate operation; integration requires explicit approval for vpsadminos/master.

## Documentation and checks

Readers are OS maintainers and operators. Keep short rationale with the existing
module list if useful; retain commands, rollout limits and evidence in session
records. No separate product guide is expected for a default module list entry.
Use the repository Nix environment and required hooks. Verify evaluated module
inclusion/loading and dependencies with bounded checks, then independent final
review before any longer runtime test. Stop unexpected local kernel builds.
Publish the feature branch and inspect applicable CI feedback.
