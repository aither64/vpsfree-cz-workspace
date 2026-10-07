# Network availability and IPv4 counter implementation

## Goal and authorization

Implement the final plan accepted in this conversation. The user requested
implementation on 2026-10-06, selected both configuration channels, and explicitly
confirmed that Network.role is sufficient for public/private classification.
No RFC1918/CIDR classification or filtering is part of this feature.

## Affected repositories

- vpsadmin: enabled state, allocation policy, counter, legacy UI, docs and tests.
- vpsadmin-webui: state/control and address selectors, translations and docs.
- vpsfree-cz-configuration: exact reviewed source pins for vpsadmin and
  vpsadmin-webui channels, deployment/recovery preparation.
- vpsfree-kb-contracts: required external documentation impact verification;
  revise only evidence required by the actual UI impact.

## Design and ownership

Architect0 reconciles [design.md](design.md) before substantive implementation.
Implementer0 owns source/configuration edits; lead owns coordination, review,
verification and final user-facing English/Czech copy. Reviewer0 remains
independent and receives final committed deliverables after quick checks.
Existing default-true inventory remains visible. Disabled pools prohibit new
use, including explicit IDs and owned detached reuse, while preserving existing
service, trusted assigned-address continuity, release and rollback. Counter is
unowned/unassigned/unreserved rows from enabled public_access IPv4 pools only.
Do not infer pool retirement from purpose, location or maintenance flags.

## Compatibility and deployment

Additive NOT NULL/default-true migration; omitted updates preserve state.
Expose admin-only write and readable status, with optional list filtering.
All writers must enforce policy before first disable; already admitted chains
may complete. Preserve existing routes and ownership; no coordinated node
upgrade is needed. Old API rollback ignores disabled state and is unsafe while
retired pools remain disabled. No production activation, database mutation,
network retirement, default-branch integration, or lifecycle action is included.

## Configuration and verification

Use confctl within the configuration dev shell to pin final published feature
SHAs through channels vpsadmin/role vpsadmin and vpsadmin-webui/role
vpsadmin-webui. Preserve generated commits and inspect lock changes.
Run relevant quick checks and hooks, then commit all source/UI/config/docs.
Inventory full branch history, final diffs and migration deployment provenance;
final independent review precedes long integration tests and affected-host builds.
Fresh verification watchers own long/uncertain runs. Correct substantive review
findings and run focused verification under the narrow-fix policy.

## Documentation

Keep lasting enabled/admission/continuity semantics and upgrade guidance with
vpsadmin, UI design/work log with vpsadmin-webui, rollout evidence in session
records, and required KB impact evidence under the external contract workflow.
Production KB writes require approval of exact staged changes. Preserve unrelated
shared workspace work and keep the session open after handoff.

## Independent dependency prerequisite found during CI

Current W CI fails its BFF production dependency audit before the required
quick/unit gates. Both the original 02ac0c7 base and final e4c49bcd lock
proxy-addr 2.0.7; network work changed neither package manifest nor lockfile.
Upstream GHSA-jqcg-44mw-7w3h identifies 2.0.8 as patched. Prepare this one
transitive dependency update in a separate W worktree/branch and review PR,
without bundling it into the network feature or changing the currently tested
W/C heads. Verify production audit and owning BFF/package checks. It is a
separate prerequisite for green CI/integration; no default merge or deployment
is authorized. All network runtime work continues at its recorded heads.

## User-requested workflow correction (2026-10-06)

Update workspace AGENTS.md and the Git procedure to make development branches
the ordinary deliverable, without creating or managing pull requests unless
the user explicitly asks or that repository's own instructions require them.
The vpsadmin-webui PR requirement remains local to vpsadmin-webui. Preserve
fast-forward-only default integration, explicit integration authorization,
independent source review, hooks and verification. Do not use GitHub merge
commits to integrate workspace projects. No change to existing application
branches, PR state, pins, package selection or deployments is part of this edit.

This bounded instructions-only change uses the registered workspace feature
worktree at the current shared master base 9b37d3900045f965ebc6581cec6c114d0064e696.
Implementer0 owns the edit; lead owns final wording and scope; reviewer0 performs
the independent final general-lane review after commit and existing quick
instruction checks. No migration or long build is needed.

## Accepted user-list visibility follow-up

User requested implementation after selecting “Keep owned IPs visible”.
Network Index for non-admins lists enabled networks only. IP Index applies
existing access permissions, then keeps enabled-network addresses, the caller's
owned addresses and currently assigned addresses they may access. Disabled free
inventory is hidden before count/pagination. Explicit filters cannot widen this
visibility. Admin inventory remains unchanged. Show and association permissions
remain independent of enumeration; assigned hosts/export endpoints and history
retain current access. No model-wide default scope, migration, new field, numeric
classification or allocation/counter change. Both UIs must retain owned/assigned
disabled addresses and included network details without client-side removal.

Architect0 reconciles the owning brief; implementer0 owns source/tests/docs and
prepared pin helpers. Lead owns final prose, review, checks and publication.
Refresh the vpsadmin configuration role and KB V revision to final source; W pin
changes only if W actually changes. Keep application/configuration/KB/dependency
changes in existing feature branches; do not create/manage PRs outside W, merge,
deploy, retire production networks or mutate lifecycle/package state.
