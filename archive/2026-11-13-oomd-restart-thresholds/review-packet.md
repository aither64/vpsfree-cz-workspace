# Final configuration review

Outcome: node25.prg oomd restart hits 8 → 4 and load multiplier 2.0 → 1.5.
User explicitly selected 1.5x median, clarified configuration-only scope, and
authorized merging when done. No deployment, node access or machine reservation
belongs to this task. No fleet defaults or daemon implementation changes.

## Exact range and complete deliverable

- Repository: `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`, target master.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-oomd-restart-thresholds/vpsfree-cz-configuration`.
- Branch: `2026-11-13-oomd-restart-thresholds`.
- Base: `1a948a872f84bdb4643926b357cf15534de1d313`.
- Head: `08d68a85f24a95b70b2d806f995f04b236e4d89a`, committed and SSH-published.
- Complete series: one commit, `cluster: lower oomd restart thresholds on node25.prg`.
- Complete diff: five added lines in
  `cluster/cz.vpsfree/nodes/prg/node25/config.nix`, ordinary
  `osctl.oomd.settings = { restart_hits = 4; load_multiplier = 1.5; };`.
- Clean worktree; quick checks pass. Full commit/diff are available from Git.
- No migrations, prior deployments, release/external-use boundaries, generated
  clients, repeated dependency/input-update streams, obsolete branch approaches
  or transitional history. One focused configuration commit needs no split.

## Evidence and accepted checks

[Plan](plan.md), [state](state.md), architect-owned [design](design.md), and
implementer [evidence](implementation.md) carry source references and logs.
Implementation evidence includes the complete 64-node input graph and current
node25 role mapping. This patch changes no pins/lockfiles. Current pinned OS is
`c0ad0ad8f970e04099830ff1c2ebfda01e8c9d62`; architect reconciled semantics after
upstream master advanced during preparation.

Passed in pinned `nix develop`: changed-file parse, nixfmt, diff whitespace,
actual active Overcommit commit/commit-message hooks. No push-triggered CI exists
for this branch; repository workflow is scheduled/manual input maintenance.
The commit's single >72-column message warning is nonfatal and all lines meet
the documented 80-column requirement.

Post-review required check: `nix develop -c confctl build cz.vpsfree/nodes/prg/node25`
at the exact final head under a fresh watcher. Inspect actual built runit command
and generated JSON for exactly
`{"load_multiplier":1.5,"restart_hits":4,"verbose":true}`. Pinned confctl keeps
full module config private; accepted sequencing uses the real build instead of
reimplementing its evaluator. No long integration check has started.

## Risk, compatibility and documentation

Overall high risk under the skill's host/node-behavior criterion, despite the
small compatible change. Lanes: general, architecture/repetition,
scope/proportionality, risk/compatibility. Selected independent reviewer0 is
retained Sol `gpt-6.1-sol`, saved xhigh, read-only, ready and independent.

Existing freeform JSON options are supported by the pinned daemon/module;
ordinary merging retains shared verbose=true. Sampling stays 15 seconds, stop
hits 40, memory 95%, conditional CPU 90%, load top 5. Host gate uses 1-minute load
>= multiplier times a buffered median of up to 5760 samples. Scores accumulate
and decay; inactive rounds skip misses. Lower host activation can also accumulate
unchanged stop scores sooner. No state format/API/protocol/migration changes or
coordinated updates are needed. Operator can restore previous settings through
ordinary configuration deployment, but completed container actions are not undone.

Documentation routing: node-specific choice/rationale → operator/maintainer,
individual execution context → design.md and implementation.md. Existing settings
need no new repository reference/runbook; no documentation moves, new public
behavior contract or reusable mechanism is introduced. Pinned module/daemon is
the owning source contract, configuration is its existing consumer. All rollout
and verification artifacts stay in session records per repository policy.

Reviewer: read repository AGENTS and all four lane references in the
mandatory-change-review skill; inspect complete range and actual source directly.
Report findings and explicit whole-branch history, migration, repeated-stream and
documentation placement/preservation conclusions. Save review.md here and report
to lead. Do not edit source, run long builds or spawn reviewers.
