---
lifecycle: active
---

# 2026-09-23-storage-redesign

## Current status

The read-only backup inventory is ready on the published
`vpsfree-maintenance-tasks` feature branch, awaiting merge approval. The
operator can capture the production vpsAdmin database and ZFS on
`backuper2.prg` using the [task guide](../../worktrees/2026-09-23-storage-redesign/vpsfree-maintenance-tasks/2026-09-24-storage-inventory/README.md).
This session has not accessed production or run a live capture. A report from
separate DB and ZFS observations is diagnostic, not proof of one consistent
instant or permission to delete a snapshot.

The broader physical-topology reconciliation, safe user snapshot deletion,
and bounded backup dispatcher remain proposals in [investigation.md](investigation.md)
and [plan.md](plan.md). No schema, service, or live storage state changed.

## Repositories and ownership

- `vpsfree-maintenance-tasks`: worktree
  `worktrees/2026-09-23-storage-redesign/vpsfree-maintenance-tasks`, branch
  `2026-09-23-storage-redesign`, base `2fdc9f2`, final one-commit head
  `4ff9b48362b7e53a644c3b0ba8881395cbd2eda9`, pushed to `origin`.
  The worktree is clean. No merge or deployment occurred.
- `vpsadmin` canonical bare HEAD `9fc0648accd4`: source review only.
- `vpsadminos` canonical bare HEAD `2166e5934fe1`: reference review only.
- `architect0` supplied physical graph and migration design; `implementer0`
  supplied scheduler feasibility. A fresh writable implementation agent wrote
  the task code. The lead handled coordination, review, and tracking.

This conversation is bound to `2026-09-23-storage-redesign`, as checked with
`dev-session current` and the environment identity. The older session named
in the request was not accessed. Retained specialists' read-only shells could
not complete `dev-session current` because its lock path was read-only, so
they only inspected canonical bare source. The writable implementation agent
verified its session identity before editing.

## Verification and review

- Final offline Minitest run: `ruby 2026-09-24-storage-inventory/test_inventory.rb`,
  18 tests and 62 assertions passed. Ruby syntax and `git diff --check` passed.
- Fetched `origin/master`; it remained at base `2fdc9f2`. Captured the
  repository comparison at base `2fdc9f2` and head `4ff9b48`.
- The repository has no GitHub Actions workflows. `gh run list` returned no
  branch runs after push.
- Mandatory review classified the change **high risk** because it reads a
  production database and storage host and emits sensitive topology. A fresh
  independent standalone reviewer from the installed default development
  team's review role, GPT-6 Sol/xhigh, covered general, architecture, scope,
  and risk lanes. Retained read-only peers had reported `dev-session current`
  EROFS failures, so the retained reviewer was treated as unverified.
- Initial review found a blocking missing DB-to-ZFS branch-origin comparison
  and important host-scope, metadata-integrity, and ZFS-type checks. The
  implementation agent fixed them and broadened scoped lock capture. A review
  rerun confirmed those fixes, then found short hostnames could collide and
  asked for one cohesive unpublished commit. The final focused fix requires
  a qualified hostname and rejects short aliases; collision and failure tests
  pass. The two unmerged commits were folded into the single final commit.
  Review covered original `69dac3e` and remediation `86a7612`; their final
  equivalent plus the narrow host-scope reduction is `4ff9b48`. The narrow
  final fix did not require another review rerun.

No live MariaDB or ZFS validation has occurred. Scan duration and SQL cost at
the reported scale of roughly 20,000 snapshots remain unmeasured. Two ZFS
scans can miss a change that reverts between them. Version 1 draft captures
are incompatible with the final version 2 format and must be recaptured.

## Next actions

1. Operator: follow the private capture and offline comparison procedure in
   the task guide. Use a SELECT-only account, exact backup pool roots, and
   private output paths. Preserve the two capture windows and any volatility
   findings when sharing results; do not commit raw artifacts.
2. Analyze observed discrepancies and scan cost, then refine the additive
   physical topology migration and safe snapshot-deletion design. Do not infer
   deletion eligibility from one inventory match.
3. Obtain explicit direction before merging the feature commit into
   `vpsfree-maintenance-tasks` `master`. Keep this session active.

The task guide owns repeatable operator instructions. The source investigation
and proposed future compatibility/deployment sequence remain in this session;
they are not executed rollout records.
