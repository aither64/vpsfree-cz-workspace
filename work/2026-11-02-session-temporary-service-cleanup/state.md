---
lifecycle: active
---

# Session service cleanup and portal resources implementation

User authorized implementation and identified vpsfree-cz-configuration for
aitherdev deployment. Default-branch integration is not authorized. Existing
unregistered services remain excluded; no session archive/delete/stop is requested.

## Phase checklist

- [x] Identity, retained Full-team roster and workspace-write access reverified.
- [x] Registered-service and Resources/Team design accepted; user authorized implementation.
- [x] Architect reconciled feature base and froze execution interfaces/boundaries.
- [ ] Implementation: registered service lifecycle, portal navigation/counts, compatibility/docs.
- [ ] Intended changes committed and quick checks pass.
- [ ] Mandatory independent final review and finding reconciliation.
- [ ] Long integration/VM/package checks and feature CI.
- [ ] Matching workspace/configuration pins and deployment preparation.
- [ ] Authorized aitherdev deployment, disposable verification and portal usability.
- [ ] Separate approved integration and exact remote-head evidence.

## Backlog and owners

| Owner | Package and acceptance | Dependency / checks |
| --- | --- | --- |
| architect0 | Reconcile existing design with current source and publish exact source/reader/lock/file boundaries; no new framework. | Needed before dependent implementation; existing-source diagnosis first. |
| implementer0 | Registered service owner/CLI and pre-prune archive/delete gate; known-state recovery, native stop proof and focused Ruby/docs. | Architect contract; quick checks before final review. |
| implementer1 | Independent Resources/subtabs/counts and Team membership; then service projection/compatibility/docs. | Existing source establishes UI independence; service reader and persisted contract must be frozen before dependent edits. |
| reviewer0 | Final independent general, architecture, scope, risk/compatibility and whole-history review. | All intended changes committed, quick checks passed; retained Sol/xhigh. |
| lead | Tracking, acceptance, public wording, test/review/deployment coordination and approval boundaries. | Exact graphs/heads and required claims for activation/integration. |

## Repositories and rollout

Reusable dev-workspace owns functionality. Workspace feature worktree owns its
nested runtime selection; vpsfree-cz-configuration owns matching host/module input
and aitherdev deployment. No vpsFree extension runtime edits are currently needed.
Registered feature worktrees all use branch
`2026-11-02-session-temporary-service-cleanup`:

- dev-workspace: worktrees/2026-11-02-session-temporary-service-cleanup/dev-workspace,
  initial base c2182254d29c4175c3e9fe4267e5a92dd1da6b79.
- workspace: worktrees/2026-11-02-session-temporary-service-cleanup/workspace,
  initial base 6383e8848c92c06a9d817f8109853b5b61305c89.
- vpsfree-cz-configuration:
  worktrees/2026-11-02-session-temporary-service-cleanup/vpsfree-cz-configuration,
  initial base c040c14cdbacc07998700b524996a89306188d7f.

Configuration checkout is clean and registered. Ambient post-checkout Overcommit
initially failed on missing bundled gems; fresh pinned Luna/low watcher verified
`nix develop --no-write-lock-file -c bundle check` at c040c14c (exit 0, ~40 seconds),
with evidence in config-shell-check.log. Its declared Nix shell satisfies the
Gemfile. No files were discarded or hooks bypassed; the original post-checkout
hook was retried under that shell with original checkout arguments and passed
(exit 0). Configuration preparation is usable without bypassing hooks. User profile application deployment remains
separate from system configuration.

## Evidence and constraints

Selected proposal package was /nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0.
Its archive prunes tracking before ordinary journal preparation; durable service
cleanup must precede first prune. Detailed evidence, supported boundaries and
fixture criteria are in [design.md](design.md). Prior initial proposal checkpoint:
4c91a16e4. Design/plan updates since then remain in the working tree under tracking cadence.

No live example services may be inspected/stopped/adopted, and no live lifecycle
experiment may archive/delete a session. Use disposable fixture state only.
Unregistered services get no discovery/migration/gate. Registered uncertain state
fails before file deletion. Ordinary completion/handoff does not trigger cleanup.

## Current milestone and next action

Both implementers confirmed exact current identity from the trusted tracking
directory; shells lacked both markers at workspace root, so verified literal
markers may now be propagated per sessions.md. Retained settings unchanged.

Implementer0 completed source diagnosis and waits for architect's frozen first-
registration/registry/prelude/public reader contract before core code. Implementer1
confirmed portal navigation/counts are independent through existing detail and
incarnation-bound reservation readers and can proceed in owned files. Service
projection/host compatibility wait for that contract. Initial Git lane belonged to A. At head c2182254 A confirmed no staged/unfinished
Git effects and transferred it; lead granted B the lane for an independent UI/count
commit with precise owned staging. A continues source-only until return. B must
preserve all dependent and A edits and verify its exact staged/committed tree.

Selected/pinned catalog digest:
495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7.
Watcher utility is gpt-6-luna/low, one fresh operation, native identity
`dw_af6ea530112c2a5e816254d08d217be90f4f5c713a51db96`, installed full_access;
actual TOML danger-full-access/never verified. Final reviewer is retained
reviewer0 Sol/xhigh. Announced documentation, monitor and final-review workflows.

Read configuration's aitherdev coordination guide and selected runtime guide.
The config guide's older release/idle wording conflicts with current runtime and
thread instructions: apply current verified-deployment + integrated-lineage
release conditions, without waiting for separate UI acceptance. No claims held.

Milestone: implementer1 completed independent Resources/nested navigation,
cluster presence/counts and Team roster count source with focused JS tests;
16 focused JS count/coordination checks and selected Go cluster/count/Team/
template/details/assets checks passed in the Nix shell; no Git mutation. B retains
integer count API with additive snapshot certainty and is finishing observation
fences/incarnation cache isolation. Final-head checks will bind committed source. Service/host integration still waits for
architect's execution appendix. Implementer0 diagnosed pre-prune and deletion
recovery boundaries, with A now owning archive-check and auto-archive launch-token
integration. No core source edits until contract frozen.

Frozen contract is published at the top of design.md and accepted by lead/A/B.
It specifies initializing→ready registration marker, registry/prelude paths,
public schema-1 JSON, pure host validator, same-ID ordinary-journal handoff,
delete-force retry semantics and two runtime capability keys. Global nonreused
resource UUIDs avoid redundant epoch state. Both implementers resumed dependent implementation. A drafted the core owner and
is wiring lifecycle/CLI. B drafted safe service reader/template with 1MiB bound,
coalesced cache and exact profile/session/incarnation checks. Its receipt hash
handoff seam is under architect support; ordinary matching stays strict meanwhile. Architect now prepares bounded read-only deployment/check command
brief independently; this is not a further gate.

Next: core/service-reader/host implementation and quick-check evidence. B's full cluster Go package and focused resource/Team/
details/template/header checks plus 16 JS tests pass. Browser navigation fixture
changes are authored but not run before required review. Lead applied the writing
skill to current UI/docs; B applied exact wording edits. Dependent service/host
code was waiting for the execution contract and is now underway. Package A
explicitly retains safe refusal for a lost uncertain launch with no positively
observed native unit/cgroup identity; missing unit/PID is not proof of shutdown. Use watcher policy
for long checks; independent review precedes long integration tests.

## Rollout evidence

[rollout.md](rollout.md) records user direction, predecessor system/profile/package
identities, canonical repo/machine aliases, graph preservation, preparation and
activation sequence, and current integration-bound machine release rules.
No claims acquired or runtime deployment performed.

## Cleanup and authorization

Implementation is authorized; no merge, session lifecycle operation or unrelated
service cleanup is authorized. Machine deployment follows the user's aitherdev
direction and required deployment procedure. Keep this session open and active.
Preserve unrelated shared files/index, roster settings and all recovery contracts.

Stable session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/
