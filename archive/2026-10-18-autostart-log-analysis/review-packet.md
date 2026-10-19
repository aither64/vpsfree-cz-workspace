# Final review: osctld descriptor cleanup before process limits

## Request and outcome

Review completed committed osctld-only repair, independent final review before long VM integration. User narrowed scope to urgent osctld error; swap/kernel/histfile, deployment, node recovery and merging are excluded. Goal: fix child EMFILE during inherited descriptor cleanup by ordering preparation before parent-applied target limits and workload release, preserve descriptor/socket/identity/limit behavior, clean up failed handshakes without leaks/hangs. No blanket retry redesign.

## Repository / complete history inventory

- Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-18-autostart-log-analysis/vpsadminos
- Branch: 2026-10-18-autostart-log-analysis
- Base: d531fc90888e3eabf17889b0dff94c648866cea4 (origin/staging; fetched unchanged before commit).
- Head: 21e4dfb24 (resolve full exact SHA with git rev-parse).
- Complete series: one commit `osctld: prepare child descriptors before applying process limits`.
- Final diff: 4 files,497 insertions/1 deletion: switch_user.rb, switch_user_spec.rb, VM test and registration. No other intended application changes; local libosctl/tmp is generated native build output, not staged/committed.
- One logical repair includes its deterministic unit and packaged runtime regressions, avoiding a failing test-before-fix intermediate. No prior project commits, obsolete approaches, fixup/WIP residue, repeated dependency/pin/metadata update streams or transitional compatibility paths. No migrations; no database/schema changes and therefore no merged/released/deployed/external migration provenance to preserve.
- No kernel/package/dependency pins, version bumps or configuration changes. Source-gem wiring packages the current local source directly.

## Design, evidence and documentation

Session plan.md/state.md/design.md in work/2026-10-18-autostart-log-analysis. Logs from reboot show child EMFILE at10:22:53 -> parent EOF;48starts,25success markers,23failures. Source race established deterministically below; no descriptor leak claim. Runtime node state/limits unavailable (direct SSH denied); no node mutations performed. Owning project invariant comment explains why preparation ack precedes parent limit application; private helper change needs no separate public guide. Prepared future rollout checklist remains in session design, not product docs.

## Quick verification already passed

- Root patched ruby_vpsadminos shell; local libosctl native rebuilt with matching Ruby. Focused SwitchUser RSpec:30examples,0failures seed19302 (unit-check-patched-ruby.log).
- Isolated control (ordering-control.log): corrected targeted example1/0; exact base helper loaded only in separate test process fails expected `:applying_limits` vs `:waiting_for_preparation`; overall control exits0. Shared source/index never overwritten.
- VM Nix evaluation passed (vm-eval-resume.json), same kernel as baseline plain-tank test. Kernel output /nix/store/0lgvd22dlh9l0pn8vafx15wklbmvkcrc-linux-6.12.113 is remotely cached, no local kernel build authorized.
- Nix parse/Nixfmt and embedded VM Ruby syntax passed; final commit hooks Nixfmt/RuboCop passed (repair-commit.log). Commit-message warning threshold60/72 differs from repository's80 requirement; no hook bypass.
- Full VM test not run: awaits this review, then one osctld/switch-user-prlimits run. Unexpected kernel build must stop.

## Review classification and lanes

High risk: privileged host child setup, descriptor cleanup, prlimits and container isolation. All lanes apply: general, architecture/repetition, scope/proportionality, risk/compatibility. Reviewer0 retained read-only independent purpose-review member uses saved gpt-6.1-sol/xhigh (no override).

Inspect complete base-to-head commit history and final diff, source/callers/tests directly; explicitly conclude obsolete history, repeated update streams and no migrations. Read applicable AGENTS.md, docs/os/patch-series-policy.md and mandatory-change-review skill plus all4 lane references. No nested reviewer, edits or test/build launches. Review source failure paths, exact-PID cleanup, child/parent FD ownership, release ordering and coverage. Flag scope or VM correctness concerns concretely; no rubber stamp.

Public helper signature/PID return and callers remain unchanged; cross-node API/CLI/protocol/on-disk state unchanged. Private handshake peers come from same daemon invocation. Configured container limits and namespace/socket semantics must remain intact. Rollback compatible, old binary reintroduces race; no fleet-synchronized update required. No deployments or integration authorized by this review.
