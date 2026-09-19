---
lifecycle: complete
---
# Current status

Implemented mandatory procedure routing in the workspace, HaveAPI and vpsAdmin.
Every original nonblank paragraph is retained verbatim. Four fresh Astra/xhigh
review lanes completed; findings were fixed and focused final diffs checked.
All twelve read-only live routing scenarios (thirteen turns) and both packaged
workspace checks passed. All seven registered exact local/remote feature heads
are proven ancestors of their remote default branches. No work remains.
The user authorized both initiatives to merge into all default branches and
waived waiting for CI. No host deployment is needed for instruction files.

## Scope and repositories

Audited sixteen canonical repositories with instruction files plus the workspace,
and eleven canonical repositories without them. Two renamed clone pairs were
deduplicated. Fourteen cohesive repository instruction files remain unchanged.
The vpsAdminOS extraction was dropped after measuring a normal test-task context
increase; its original instructions and base branch were restored without a
repository-wide reset, clean or stash. Security-advisories uses a nonstandard
remote default branch; its complete assessment workflow remains inline.

All worktrees are under `worktrees/2026-09-17-agent-instruction-routing/` and
all retained branches use `2026-09-17-agent-instruction-routing`.

| Changed project/worktree | Final head | Target |
| --- | --- | --- |
| haveapi | a2fc755452db60dac919205829fda6db362e3fce | master |
| vpsadmin | 941451cffe415850e15b29813937fc5e035456c0 | master |
| workspace | c8889ea85682f5e673ac243e27f533ecc7ef3700 | master |

Inspection-only worktrees: terraform-provider-vpsadmin, vpsadminos,
vpsfree-cz-configuration and vpsfree-kb-contracts. Their feature branches retain
original upstream bases with no content changes. These retained refs were published;
merge-proof.json covers every registration. Initial bases, canonical
defaults and decisions are in inventory.json and portal.yml.

## Documentation and verification

- [Plan](plan.md), [coverage](coverage.md), [source inventory](inventory.json),
  [repositories without instructions](repositories-without-instructions.json).
- [Review packet](review-packet.md), [findings and remediation](review-results.md),
  [verification results](verification.md), [behavioral plan](verification-plan.md),
  [task context sizes](context-sizes.json), [merge proofs](merge-proof.json).
- Workspace procedures: `docs/agent-instructions/`; HaveAPI:
  `doc/agent-instructions/`; vpsAdmin: `docs/agent-instructions/`.
  Repository README/docs indexes link their procedures. Project guidance stays
  with its owner; test fixtures, source mappings and rollout evidence stay here.
- No API, schema, protocol, persisted-state, module-option or runtime change.
  Entry files and their procedures are atomic commits. Existing conversations
  need to reread changed guidance; unrelated sessions were not interrupted.

Static coverage checks preserve all 123 original paragraphs in the three changed
files and validate every route. Workspace guard: 2 tests, 32 assertions, no
failures; formatting, whitespace and declared commit hooks passed. Final
workspace core is 11,056 bytes (45,697 before), HaveAPI 4,018 (6,823 before), and
vpsAdmin 4,907 (10,052 before). Bytes are not token charges; tasks add their
applicable procedure reads and skills. Some broad tasks load more than before.

The original workspace file exceeded the installed Codex automatic 32 KiB
instruction limit. Earlier live evidence retained exactly 32,768 bytes, omitting
later KB, commit and project-map rules. The new entry file fits with headroom;
procedure routing preserves these requirements without relying on truncation.

## Operational evidence and ownership

Initial plan/state committed at c62285f before project commits or external
mutation. The external conversation owns both requested initiatives. Managed
thread `01a0aeb9-78c1-7211-b673-4cae59d580cb` was initialized harmlessly and remains
available. Session creation recovered its own App Server terminal disconnect.

Worktree creation completed even when post-checkout hooks initially failed.
VpsAdmin/vpsAdminOS hooks required re-signing; configuration needed its Nix
bundle. VpsAdmin's required i18n hook needed the API dependency bundle: a bounded
Luna/low watcher prepared it, then the parent retried the commit with hooks
passing. Existing worktree and Nix-environment notes document these cases.

No archive, delete, branch deletion or session shutdown is authorized. Retain
clean feature worktrees/branches for follow-up. Unrelated shared-root changes
remain untouched. Consolidate tracking under the existing cadence; source
changes are independently committed and reviewed.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-17-agent-instruction-routing/).

## Integration and final checks

HaveAPI and vpsAdmin were fast-forwarded into remote master through fresh temporary
worktrees at their exact tested commits, then the temporary worktrees were
removed. Shared workspace master was fast-forwarded to `c8889ea85682f5e673ac243e27f533ecc7ef3700`
and pushed, preserving all unrelated index/working-tree changes. Comparison
captures were refreshed before integration. The workspace feature update used an
exact force-with-lease; no CI runs existed on the branch to cancel. CI was not
awaited. All seven registered local/remote feature heads are merged, including
inspection-only branches that remained at their original upstream bases.

The comparison tool refuses identical base/head pairs for unchanged inspection
branches. Recorded their exact unchanged bases and merge proofs instead of
inventing a comparison. No integration was needed for these branches. A broad
root whitespace check found unrelated daily-report HTML whitespace; the check
was narrowed to this initiative's feature diff and the unrelated files preserved.

Final packaged checks caught two test-harness defects: duplicate dynamic Nix
system attributes and locale-dependent Ruby reads. Grouped checks and explicit
UTF-8 fixed them; evaluation, C-locale local tests and both packaged checks
passed. Details and focused review rationale are in review-results.md and the
new instruction-check Nix-environment note. All behavioral fixtures used the
unchanged final instruction content. No runtime deployment was needed.

Both sessions remain open, with clean feature worktrees and retained branches.
A single final handoff consolidates the curated records and durable notes; no
per-poll/test/deploy checkpoint commits were made. Raw test artifacts are stored
outside Git under `~/.local/state/dev-workspace-evidence/` in this initiative's
subdirectory. The tracking directory contains only intentionally retained
curated evidence. No operator action remains.
