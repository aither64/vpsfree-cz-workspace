# Final configuration review

## Channel update I2 final history review (2026-11-23)

Current unmerged range:
`4fa3c97b83f2b9368b2d4bdb9f7b9630afcdd278..11d6d55924d531d6311dc5a98283d980c9818bb0`.
The base is the already integrated oomd move (receipt in state.md); do not
re-review that accepted change. Only generated flake.lock changes, +15/-15:

1. `fe530b123f7d8d7bcfdcdb8ce621abd2644b6b30`: three OS pins to
   `b86287c105b749827cd63632ac35936533910f63`.
2. `11d6d55924d531d6311dc5a98283d980c9818bb0`: two vpsAdmin pins to
   `4062a8da3314aa7b48170b0d6f441446bad9b207`.

User requested both roles in production/staging/os-staging. Only five mappings
exist; do not create missing os-staging vpsadmin role. [D2 design](design.md)
and [complete I2 evidence](channel-update.md) give exact commands, all old/new
source revisions/NAR hashes, 105-path semantic graph comparison, 38 unchanged
follows edges, 19 root inputs and final lock SHA-256. Only five selected source
identities changed; original URLs, mappings and other source identities unchanged.
Services source remains fixed but its existing follows dependency advances to
new staging OS. Both upstream default heads/old-revision ancestry confirmed.

Both commits are confctl-generated with unedited useful changelogs and normal
hooks; generated-message width warnings are permitted by repository instructions.
Quick JSON/diff/bundle/channel-metadata checks passed; published remote head exact,
master remains base, feature clean and comparison captured. No push CI applies.
No superseded/repeated local update streams or transitional local migrations;
each role updated once. Preserve separate role commits; integrated oomd history
is immutable. Assess complete history/consolidation independently.

Mechanical generated dependency updates are exempt from standalone source-content
review under the skill; required whole-branch history/migration assessment still
applies. This bounded independent review covers general/history and applicable
scope/risk checks for exact input selection and recorded compatibility limits,
not an upstream implementation audit. No architecture changes or handwritten
logic. High downstream host/node compatibility context, saved reviewer0 Sol/xhigh.

Distinguish no migrations created/rewritten/run in this configuration branch from
upstream published migration `20261030180000_add_incident_escalation.rb`, which
is already present in unchanged services source. Runtime schema uninspected.
Future rollout must match schema-2 Top, oomd, osctld and nodectld, reconcile pending
actions, and establish compatible incident backend/schema/RPC prerequisites.
Design/evidence preserve rollback/data constraints. No deployment or runtime
verification is authorized; new pins have not been approved for integration.

Known full-node build gap remains external missing initrd host key; no unchanged
retry or synthetic secret. Channel metadata is not full machine/system evaluation.
Lead will run bounded read-only machine metadata evaluation for nodes and one
os-staging container, without building/activating full systems. No successful
system realization is claimed. Reusable project docs are unchanged because these
are routine generated pins; source contracts remain in upstream docs linked by
D2 and individual execution/review evidence stays here, per repository policy.
Return explicit findings/history/migration/documentation conclusions read-only;
lead preserves report. No further edits, builds, claims or integration.

## Refreshed review M (2026-11-23)

Current final range is
`baf73377af387a8ef1c90e20b17bb559fcd15c45..4fa3c97b83f2b9368b2d4bdb9f7b9630afcdd278`.
See [merge preparation](merge-preparation.md) for the complete one-commit series,
full +2/-5 diff, passing current-shell quick checks/hooks, unchanged pin fingerprints,
prepared target and actual pinned consumers. Original range below is historical;
`range-diff` says equal, with stable patch ID
`a394a3dbb5ea2fbfc7c3ff54d4c7500611230940`. No source conflicts or new source
behavior, migrations, repeated update streams or deployed lineage.

Fresh applicable independent review is required because the new base already pins
production OS `ccd51ed38ebffa2e744f7f8847668bc2e3413378` and staging OS
`e9d55bada43c888ae91139d549d156a0831817de`. They materially changed oomd
controllers/readings since the original review. Assess the move against their
actual setting semantics and imports; do not audit unrelated upstream history.
All four original lanes apply; high host/node classification; retained independent
reviewer0 Sol/xhigh, no fallback. Quick checks and feature publication complete.

User now directs "merge this" for the existing oomd move into this repo/master,
following disclosure of the missing-initrd-key full-build gap. No build success
is inferred and no unchanged retry is requested. Lead owns short claimed merge.
The same message separately requests OS/vpsAdmin channel updates; those are not
in this range and will be a separate deliverable after original integration.
No deployment. Documentation remains appropriately unchanged; original report
and current execution evidence remain in session records. Explicit current
history/migration/documentation conclusions are required. Return report read-only;
lead will preserve it in review.md.

## Original review R (2026-11-13)

User request: move node25.prg's lowered osctl-oomd restart hits and load threshold
into common configuration for all nodes. User clarification: "just change
configuration, no deployment". Acceptance: numeric restart_hits=4 and
load_multiplier=1.5 apply once in the common settings; node25 duplicate removed;
all 13 existing node consumers covered, with enablement/verbose/unrelated policy
and input pins unchanged.

Session: `2026-11-13-osctl-oomd-common-config`.
[Plan](plan.md), [state](state.md), [design](design.md),
[implementation and quick-check evidence](implementation.md).

- Repository: `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`; target master.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-osctl-oomd-common-config/vpsfree-cz-configuration`.
- Branch: `2026-11-13-osctl-oomd-common-config`.
- Base: `08d68a85f24a95b70b2d806f995f04b236e4d89a`.
- Final committed/published head: `48e94d18b467d1a3999fb906f0fd726968146267`.
- Complete series: one commit, `48e94d18b467d1a3999fb906f0fd726968146267`
  (`cluster: share osctl-oomd tuning across nodes`).
- Complete diff: `git diff 08d68a85f24a95b70b2d806f995f04b236e4d89a..48e94d18b467d1a3999fb906f0fd726968146267`.
  Two files only: common/all.nix +2; prg/node25/config.nix -5. One atomic policy
  relocation; splitting removal from addition would temporarily change node25.
- No superseded source approaches, follow-up fix series, unused compatibility
  paths, migrations or repeated dependency/channel/generated update streams.
  No schema, release, deployment or external-state migration provenance exists.
  Reviewer must independently conclude on whole history and migration lineage.

Quick checks passed in pinned `nix develop --no-write-lock-file`: nixfmt --check,
nix-instantiate --parse for both files, git diff --check, exact full diff, source
import coverage. Installed Overcommit 0.76.0 Nixfmt and commit-msg hooks passed.
Documented worktree hook dependency issue resolved without bypass. Worktree clean;
fresh remote feature equals head, master equals base. No push CI applies (only
scheduled/manual daily-update workflow). Long node builds remain pending review.

Inputs unchanged: flake.lock SHA-256
`d6a45cb62482eb2f321d551595325da1b44b1095284abe2acf6f4af57f487877`;
both production/staging vpsAdminOS pin
`c0ad0ad8f970e04099830ff1c2ebfda01e8c9d62`, with existing option support.
Owning module: cluster/cz.vpsfree/nodes/common/all.nix. Existing consumers/import
routes and exact input fingerprints are in implementation.md/design.md. No new
interface or import. All 13 nodes include backuper2 and both staging nodes.
Node25's effective settings remain the same; the other 12 gain these values.
No state format or binary change; mixed deployed configurations supported,
no coordinated rollout required. Reverting the move restores previous config.

Non-goals: deployment (including dry-activate), runtime checks, integration,
new imports/modules/options, daemon changes, pin changes, synthetic assignment
tests or broad tuning audit. No merge approval exists. After review run the
repository-required all-node build through a fresh watcher, not deployment.

Documentation routing/fidelity: node policy → maintainers/reference → existing
shared settings block; self-explanatory relocation, no project-doc addition
useful. Intent and compatibility → maintainers/session design → design.md.
Actual checks and revisions → maintainers/individual execution → implementation.md
and state.md. No project documentation is moved or deleted; temporary execution
evidence stays out of the configuration repository. Verify placement conclusion.

Overall risk: high under the skill's host/node-behavior trigger, despite tiny
reversible diff. Review lanes: general, architecture/repetition, scope/proportionality,
risk/compatibility. Selected eligible retained reviewer0: gpt-6.1-sol/xhigh,
read-only, independent, ready. No fallback or settings override.
