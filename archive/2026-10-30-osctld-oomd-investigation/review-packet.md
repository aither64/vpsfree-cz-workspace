# Final review packet: stale OOM daemon misses

User first requested root-cause investigation, then explicitly said
"ok, implement the fix". Review the completed fix; no deployment or default
branch integration is authorized. Tracking: `plan.md`, `state.md`; architect
brief/evidence: `design.md`; independent incident source proof: `source-trace.md`.

## Exact deliverable and history inventory

- Repository: `vpsfreecz/vpsadminos`, integration target `staging`.
- Worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-osctld-oomd-investigation/vpsadminos`.
- Branch: `2026-10-30-osctld-oomd-investigation`.
- Base: `8ce6234db194ccb934db724c7262aeab7fd26915`.
- Head: `4642beb9c37c558e1d0b74e285fecdda16d62eca`.
- Complete series: one commit, `4642beb9c37c558e1d0b74e285fecdda16d62eca`
  (`osctl-oomd: ignore queued misses after pruning`).
- Final diff: `git diff BASE..HEAD` in this worktree. Two files, +101/-1:
  `osctl-oomd/lib/osctl/oomd/killer.rb` (+4/-1) and existing
  `osctl-oomd/spec/osctl/oomd/killer_spec.rb` (+97).
- Source and its focused tests/comment are one logical fix. No obsolete
  approach, follow-up commit, shim or temporary compatibility path retained.
- No migrations; no merged/released/deployed/externally consumed new schema.
- No repeated dependency/channel/input/generated update streams. Required
  `make osctl-oomd` metadata refresh produced no diff. No pin/lock changes.
- Worktree clean; implementer is publishing the same final head.

Review the complete series and final diff independently. Explicitly conclude
whether obsolete history remains, migration lineage is sound ("no migrations")
and repeated update streams require consolidation (inventory says none).

## Acceptance and boundaries

Only hits create tracking records under the existing mutex. A miss for an
absent record is ignored. Prove that a queued miss delivered after pruning
cannot recreate a zero-counter record with nil `last_hit`. Real hits,
counter decay/clamping and old/recent/positive-counter pruning remain correct.
Existing restart/stop thresholds and action result behavior are preserved.

The original bug is process-fatal (`Thread.abort_on_exception`). Exact production
interleaving and deployed source revision were not proven; the local regression
must independently establish the reachable state transition. Avoid broadening
the fix into event queue, watcher, shutdown, restart or logging redesign.
Rejected: nil guard in pruning that leaves malformed miss-only records alive.

Owning component: osctl-oomd. Watcher supplies internal hit/miss events; killer
owns record construction, counters and pruning. The packaged runit service
consumes the daemon. No public API/CLI, protocol, database, persisted state,
Nix module option or dependency contract changes. No downstream pin updates.
Independent per-node rollout is possible; rollback restores the defect without
state incompatibility. No fleet coordination is needed or planned.

Documentation: brief source comment explains why a miss can outlive a record;
tests preserve the invariant. Incident details remain session-owned. No new
manual, operations procedure or release guide is useful for this small internal
correction. Existing incident findings are context, not a new product document.

## Quick checks complete before review

Prepared repository Nix environment. Commands/evidence:

- `make osctl-oomd`; `git diff --exit-code -- os/packages/osctl-oomd`: no diff.
- Original source loaded with `git show BASE:.../killer.rb` into a separate
  Ruby/RSpec process: four new examples, expected two failures; unknown miss
  retained a malformed record and stale-miss-after-prune raised exact nil/<
  exception. Corrected worktree was never replaced with old bytes.
- From osctl-oomd with component bundle: `bundle exec rspec
  spec/osctl/oomd/killer_spec.rb`: 14 examples, zero failures.
- `bundle exec rspec`: 41 examples, zero failures.
- Root bundle `bundle exec rubocop osctl-oomd/lib/osctl/oomd/killer.rb
  osctl-oomd/spec/osctl/oomd/killer_spec.rb`: two files, no offenses.
- `overcommit --run`: Nixfmt and RuboCop pass (about three minutes).
- Normal commit hooks: pre-commit and commit-msg pass. TextWidth warning >72
  characters only; all message lines satisfy workspace <=80 rule.
- Logs: `oomd-quick-checks.log`, `oomd-final-quick-checks.log`, `oomd-commit.log`.
  `oomd-quick-checks.sh` records commands. Initial root lint launch failed from
  inherited component BUNDLE_PATH; corrected by selecting root bundle and
  unsetting BUNDLE_PATH. Scoped lint initially flagged subject stubbing; final
  test spies on Kernel.system, then final component specs/lint passed again.
- No long VM/integration tests started. CI will be assessed after publication.

## Reviewer selection and required lanes

Current verified roster selects independent ready retained `reviewer0`, saved
`gpt-6.1-sol` / xhigh, read-only review instructions; no fallback or override.
Risk: high under skill classification because host/node policy is affected,
despite localized compatible implementation. Lanes: general, architecture and
repetition, scope and proportionality, risk and compatibility.

Read mandatory-change-review SKILL.md and all four lane references in full.
Perform the review directly, without nested reviewers or source edits. Read
applicable workspace/project instructions, inspect committed diff/history and
surrounding source/tests. Review scope/proportionality before detailed concerns.
Report concrete Blocking/Important/Advisory findings or explicitly none, test
gaps and residual risk; return actual identity/model/effort and reviewed range.
Save concise final conclusions to `review.md` here and report to the lead.
