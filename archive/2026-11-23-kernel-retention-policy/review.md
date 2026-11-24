# Final change review: kernel retention

- Repository: `vpsadminos` only. Feature worktree `worktrees/2026-11-23-kernel-retention-policy/vpsadminos`; target `staging`. The complete diff and commit messages are `$base..$head` in that worktree. No merge, push or rollout performed.
- Base `b86287c105b749827cd63632ac35936533910f63`; review head `43cfd7763ded25789dd9972156f95bf68b29dba4`; clean index/worktree.
- High risk for destructive repository automation, GitHub token trust/permissions, boot/test compatibility and rollback. Review general, architecture/repetition, scope/proportionality, risk/compatibility. Reviewer0 saved `gpt-6.2-sol` / `xhigh`.

## Requested behavior and scope

Required UTC `dateAdded` from introduction commits, optional inclusive hold, strict UTC age >30 days, protect stable/unstable and live use on reconciled vpsFree.cz fleet. Abort writes on incomplete evidence; retire owned livepatches and release-specific tests with their kernel rather than retaining repo references. Reusable tests follow stable. Shared offline checker for Overcommit/required PR check/pruner. Trusted weekly direct FF after exact candidate verification and fresh usage; no PR, bypass, force push, production node mutation, API/DB change, branch settings or automatic activation. See `plan.md` and `design.md` for detailed contract.

## History and checks

1. `726de81563317ac2e6e7b67b09e07a35d20d783d` — backfill + per-key record discovery, shared staged/tree validator, PR check, maintainer guide. [A evidence](package-a-evidence.md) includes introduction SHA/date map and exact build-neutral comparison in both ZFS paths.
2. `6a5c0cf49b8af3e1ce394d615aec9716e198f352` — stable RTNL/ZTS, dedicated exact ZFS regression, test owner discovery and authoring guidance. Offline enumeration (168 original IDs + one new opt-in), `.110` AMD/Intel behavior/ownership, altered stable-selector proof and 39 source substitutions. Kernel runtime not claimed.
3. `feac129e2570bbd4df55c364eb24d63be3aa711f` — owned payload locations and check coverage, deploy predicate evaluation, native .110 patch move, real NFS acceptance split; [C evidence](package-c-evidence.md). Nine Linux/ZFS identities and existing numbered producer preserved; legacy/eBPF package paths intentionally rerouted. Dormant/single/multiple batch cases and docs strict check; generic aggregate not built fully.
4. `43cfd7763ded25789dd9972156f95bf68b29dba4` — read-only production adapter and deterministic planner, typed removal, offline exact-tree verification, staged writer and runbook. Local bare-remote and mocked GH/curl admission; real-tree simulated retirement/revert. Exact all-key no-build smoke surpassed an initial short bound; GitHub production rules/coverage unverified.

All four commits ran required actual hooks in a worktree-local trust setup without changing common trust. Lead verified clean status, `git diff --check b86287c10..HEAD`, `python3 -B -m unittest discover -s tools/kernel_retention_tests` (19), `python3 -B tools/test-kernel-entry-check.py` (7). No DB/schema/data migrations; none merged, released, deployed or externally used. No repeated dependency/input update streams: new Actions pins scoped to the new workflow, not lockfile changes. Inspect any obsolete iteration, repeated streams, commit cohesion and exact migration lineage independently. Diffstat 74 files (3709 insertions/1330 deletions, some moves and extracted existing checks); evaluate proportionality, especially the writer verification, status/API contracts, and release-qualified coverage.

## Documentation and compatibility

| Topic/readers/class | Authoritative location | Evidence/limits |
| --- | --- | --- |
| Catalog registration/holds, staged and PR checks; kernel maintainers; procedure | `docs/os/kernel-updates.md` | Shared CLI and check, active branch settings remain unverified |
| Weekly operation and rollback; repo administrators; repeatable operation | `docs/os/kernel-updates.md` | Report-only until conditions verified; no project or production activation initiated |
| Stable test and exceptions; contributors; how-to | `docs/os/testing.md`, short `AGENTS.md` rule | No retained real release pin without reason/ownership; prior userspace upgrade policy stays intact |
| Qualification ownership and legacy/bounded ranges; livepatch maintainers; procedure | `docs/os/livepatches/process.md` | Whole-commit revert; strict docs/evaluation, no full runtime certification |

## Independent review outcome

`reviewer0` reviewed the exact range above with all four lanes. No migrations, obsolete approach or repeated dependency streams. Documentation ownership and supported userspace upgrade coverage were preserved. Findings:

- Blocking: independently join the writer's staging base to the candidate's sole parent, declared evidence and fresh recheck. Fixed in `79efa90fd96f636543e9abfd4f5220ded5d2c6bd` with actual publisher refusal fixtures for mismatched bases.
- Important: preserve disabled/open-ended eBPF records without failing unrelated retirement. Fixed in the same amendment, with owned-subset fixtures.
- Important: safe operational pause must drain/cancel queued or running publishers, not rely on a variable change revoking a running job. Fixed in the runbook.
- Important: keep package-field validation in the authoritative checker; narrow the planner to retention metadata and canonical native catalog keys. Fixed and covered by fixtures.
- History: Python moved into the mandatory hook commit (A); old and new tip trees were identical for the history-only rewrite.
- Advisory: date provenance clarified in the kernel guide and disposable refs clarified in the test README. The stale manual ZTS dispatch description remains an advisory, without impact on the selected kernel.

Focused follow-up accepted exact `380c5f30180f816fa70135eb5ff078bb3bbb0c61`: no Blocking or Important findings, no obsolete commits, no repeated update streams and no migrations. All 29 fixture tests and the synthetic full no-build retirement/revert passed on that head.

## Remaining deployment evidence

Provider remains the public anonymous `nodes/public_status` contract in vpsAdmin; no source change in vpsAdmin or configuration repos. OS public catalog/runner interface should be preserved except intentionally removed keys/tests; existing pinned OS revisions still build subject to cache. No host update order, reboot, DB/schema/generation migration. Existing `daily-update` / `flake-update` direct writers must be verified compatible before GitHub enforcement. Potential push/node boot race remains operationally managed (holds/pause). The session does not authorize integration or settings/production writes.
