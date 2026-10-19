# Final review: frozen fork terminal settings

Reviewed runtime `7ceb6b943c7fa6e6db2b42b1fc2d9732c6413e03..a7bd54445b5920916270c8eff01787dddd0e5f42`, with affected-code inspection concentrated on `814568f3a28ae916ef193fd0be129a9f28fe1ffd..a7bd54445b5920916270c8eff01787dddd0e5f42`. The worktree remained clean at the requested head. The supplied delta and full diff match the committed Git ranges. Previous accepted conclusions remain applicable outside this delta.

Independent reviewer: retained standalone `/root/creation_final_review`, `gpt-6-astra` / `xhigh`, installed-catalog fallback because the verified same-session roster is null. Session identity was checked. This review covers general, architecture, scope, and risk lanes under the mandatory review skill and all four references, together with applicable workspace/repository guidance. No source changes, native patch/build, long tests, deployment, integration, or lifecycle actions were performed.

## Findings

### Blocking

None.

### Important

1. **Completed-fork recovery still launches with host model/effort defaults.** General and risk lanes; `libexec/dev-session:1726` and `:1734`.

   `fork` tries `recover_completed_fork` before reaching the newly corrected main path. Once an interrupted attempt has written the destination manifest/thread, this recovery path launches a missing terminal through `create_tmux_session`, or restarts a shell through `reconcile_native_client!`, without either frozen keyword. Both helpers therefore receive their new `nil` defaults. The recovery then writes ready authority/evidence and deletes the journal. A failure after native fork creation but before terminal completion can still lose the journal's accepted model/effort, even when the entire attempt uses the new package.

   Forward `journal.fetch('model')` and `journal.fetch('effort')` to both recovery calls. Extend existing fork recovery coverage, especially `test_fork_resumes_after_thread_creation_and_tmux_failure`, to assert these values on retry and retain its one-native-fork/unchanged-thread proof. Cover the shell relaunch branch as well. The new fresh-fork and command-array assertions do not exercise these calls.

2. **An already-running terminal from an interrupted older fork bypasses correction.** General and risk lanes; `libexec/dev-session:8937`, reached from completed-fork recovery and the main existing-terminal branch.

   The deployed `95cc08d` can launch a fork terminal with host defaults, then fail during later synchronization, team/evidence work, or journal completion. Its journal still freezes the accepted settings. After upgrading, a retry finds that owned native process and `reconcile_native_client!` returns immediately, before using the supplied model/effort. Fixing finding 1 alone leaves this case unchanged: neither subsequent synchronization nor journal deletion reasserts the frozen settings. This is an unfinished journal-owned creation, so it belongs to the supported interrupted-retry boundary, without expanding ordinary ready-session reconnect semantics.

   Reconcile the frozen settings and the owned terminal before completing that journal. Reuse existing identity-scoped terminal/idle mechanisms where appropriate; preserve refusal for unexpected ownership/processes or active work. The effective native settings must be established before recording success. A plain additional `thread/resume` is insufficient while a client remains subscribed: stock 0.163 only rebuilds a loaded thread for mismatching overrides when it is idle, has no running agent, and has no subscribers; otherwise it preserves the loaded thread and ignores the overrides. This behavior is explicit in upstream `resume_running_thread`. [Stock native thread processor](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/app-server/src/request_processors/thread_processor.rs).

   Add a focused recovery case with an existing owned native pane, a retained high-effort journal, and stale host-default settings. Require either successful settings reconciliation or a recoverable refusal that retains the journal; do not silently mark the fork complete. Preserve the existing root/thread and do not create another fork. Ordinary completed-session reconnect behavior need not change.

### Advisory

No additional findings.

## Native startup assessment and coverage

The fresh-launch argv correction fits the stock native boundary. The executable/provider arguments remain intact; `--model` and the JSON-quoted TOML effort override are escaped as arguments before remote `resume`. The upstream CLI merges root arguments into resume configuration. The TUI treats an explicit model, provider, or effort setting as a request to use current configuration for model settings, and constructs resume parameters containing the selected model/provider and effort. Thus the existing explicit provider argument explains why relying on restoration from the stored thread was unsafe, and adding the frozen selections is a supported correction. [Native CLI](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/cli/src/main.rs), [resume override selection](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/tui/src/app/config_persistence.rs), [resume request construction](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/tui/src/app_server_session.rs).

This source assessment does not prove that the observed live regression is resolved. The loaded-thread behavior described in finding 2 is a material limit. Actual packaged and live acceptance must still establish effective settings and a successful causal follow-up at the exact corrected head.

Selecting `high` while the host default remains `xhigh` makes the prior silent reset observable. The browser/native root checks and persisted roster checks are appropriate additions. The shared argv test independently checks model forwarding even though the packaged model remains the fixture's standard model. Previously reviewed causal follow-up, provider, attachment, root/member inventory, fork/plan, restart, retry, and deletion assertions remain intact. The packet's 25 Ruby tests / 222 assertions and syntax/Nix/whitespace results are quick evidence; the earlier successful `814568f` VM and CI do not cover this new behavior. No new native acceptance is claimed here.

## Lane conclusions

- **General:** fresh launch and shell command construction are consistent, but the two interrupted-fork cases above remain incomplete. Documentation describes the intended frozen-settings guarantee and becomes accurate once recovery satisfies it.
- **Architecture:** `native_client_arguments` is a proportionate shared owner for launch/relaunch argv. Runtime orchestration stays in generic dev-workspace; no downstream duplication, new native patch, or alternate settings authority was introduced. Recovery should use the frozen journal and existing owned-terminal mechanisms.
- **Scope:** the live failure and nondefault-effort regression justify the change. Repairing unfinished forks across the deployed-to-new package boundary is within scope. No general reconnect redesign, new team, speculative native abstraction, or exhaustive upstream conformance suite is required.
- **Risk:** no new persisted schema, provider-selection format, public API, or package dependency is introduced. Older readers can still read the state. Reverting software can reintroduce the settings bug; compatibility of stored data does not imply preservation of this behavioral fix. The old-package interrupted-fork case needs finding 2 addressed before the upgrade/retry guarantee is accepted.

## Whole-branch history, migrations, and consumers

The complete six-commit series was inspected against the final diff:

1. `98ae6b3` — existing optional provider fields in creation journal readers and their contract tests.
2. `bc29fab` — packaged creation acceptance, fixture infrastructure, CI, and owning documentation.
3. `95cc08d` — all-provider retirement discovery.
4. `11620fc` — terminal preparation retry refusal.
5. `814568f` — HTTP readiness after fixture restart.
6. `a7bd544` — frozen fork terminal selections, focused tests, stronger packaged assertions, and documentation.

These remain independently understandable behavior or verification units. The exact deployed `95cc08d` source remains in ancestry, and `814568f` remains available for its published consumer selection and completed verification evidence. The latest behavior fix and its supporting tests/docs form one coherent unit. Narrow remediation of findings 1 and 2 should be folded into this latest unmerged unit when practical, preserving the consumed source boundaries. I found no abandoned protocol/schema implementation or obsolete compatibility path requiring removal.

**No migrations** exist in the complete runtime range: no database/schema conversion, journal-version transition, or migration lineage to retain or consolidate. There are **no repeated dependency/input/pin update streams** in this runtime series.

The prior independently checked consumers each contain one consolidated final-selection commit from their original bases: workspace `3d638f9b0cf535e75ee08ce0f8f7d63efb9ec324` and configuration `102b9520ba00ec9bfdb4562869e40170d5347b31`. Their no-migration and no-repeated-stream conclusions are retained, but they select `814568f` and are not final consumers of this new runtime. Regeneration must again leave one final update per stream and preserve exact deployment evidence separately. This report does not certify consumer composition for `a7bd544` or its remediation.

The prior urgent deployment authorization remains separate. Full corrected packaged acceptance, the old-reader control, matching final consumers/deployment, actual live acceptance, and conditional master integration/release gates remain with the parent. The two Important findings require remediation or an explicit recorded disposition before proceeding under the mandatory review workflow.
