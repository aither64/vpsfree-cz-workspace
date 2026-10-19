# Final review: frozen fork recovery remediation

Reviewed clean runtime head `901cff7db8f816cad12d8bbc2b39fa477fbd786a`, complete range `7ceb6b943c7fa6e6db2b42b1fc2d9732c6413e03..901cff7db8f816cad12d8bbc2b39fa477fbd786a`, and the remediation delta from `a7bd54445b5920916270c8eff01787dddd0e5f42`. The supplied full and delta artifacts exactly match Git output; whole-range whitespace checking passed. Earlier accepted conclusions remain applicable outside this delta.

Reviewer: same independent standalone `/root/creation_final_review`, `gpt-6-astra` / `xhigh`, installed-catalog fallback. Session identity and matching environment were verified; the live roster is null. This actual follow-up covers all four affected lanes under the mandatory review skill and its references, applicable workspace/repository guidance, the packet, updated design, earlier report, committed source/tests/docs, pinned client implementation, and full series. Only this report was written; no source edits, nested agents, long checks, deployment, integration, or lifecycle actions occurred.

## Findings

- **Blocking:** none.
- **Important:** none remaining in the reviewed change.
- **Advisory:** none.

Both Important findings in `final-review-fork-settings.md` are resolved by the inspected implementation.

The completed-fork path now supplies the journal's model/effort, creates a missing terminal without launching Codex, and routes through `reconcile_fork_terminal!`. Both existing-terminal recovery paths use that same helper. An older running client therefore cannot bypass correction solely because its pane already runs Codex.

Recovery quiesces the exact owned native pane with existing identity/process checks, proves the root idle, invokes `thread ensure-settings`, validates its exact returned model/effort, and relaunches with frozen CLI arguments. Settings refusal, malformed/mismatched output, or launch failure occurs before journal deletion and preserves the root/source identities. Idle refusal uses the existing terminal-restoration path and retains the journal; it does not claim successful recovery. Unexpected terminal processes are refused before settings mutation.

## Affected-lane assessment

**General.** The new host action checks required runtime arguments and both frozen values, then uses `RequireThreadIdle` to verify the requested thread and exact directory, completed latest turn, pending prompts, queue, and unresolved submission attempts. The subsequent update is verified twice: by the pinned client and by the command/Ruby result checks. The existing missing-terminal recovery test retains its one-native-fork proof and now checks the frozen arguments and deferred launch. The added recovery test exercises native and shell panes, settings refusal, active-root refusal/restoration, and unexpected processes while checking journal and source/root preservation.

**Architecture.** Generic dev-workspace owns the bounded journal recovery and host CLI action. It delegates settings transport and confirmation to the existing pinned `codex-web` implementation at `c064ce09cfce`; no duplicate native protocol implementation or dependency change was added. I inspected `UpdateThreadSettings`: it subscribes, obtains stable current settings, issues `thread/settings/update` when needed, and waits for a newer settings revision matching the requested fields. An already-matching stable read is returned directly. This avoids treating ignored `thread/resume` overrides as successful correction. The runtime argument tuple is shared without changing existing create/fork semantics, and native launch arguments retain their shared owner.

**Scope.** The additional helper is justified by the observed older-package interrupted-fork state. Its Ruby callers remain inside unfinished fork recovery and the existing creation/session locks. Ordinary ready-session reconnection is unchanged. Root-only idle validation is appropriate here: the operation changes neither retained members nor their settings, and the existing team-fork continuation accepts destination members still in `creating` state. Requiring the whole destination team to be ready would prevent valid partial-fork recovery. No new team, generalized recovery framework, native patch, or browser mutation endpoint is introduced.

**Risk and compatibility.** The exact thread/directory check and existing journal, manifest, provenance, tmux identity and pane checks preserve the supported ownership boundary. Host CLI arguments come from the trusted local orchestration; this action adds no remote authorization surface. Reassertion changes only model and reasoning effort using the existing native settings operation, retaining collaboration mode and other settings. Failures remain retryable without replacing the fork. The deployed `95cc08d` unfinished-fork journal and running-terminal case is now handled explicitly. Old and new packages still share existing persisted formats; rollback can read the state, though old code can reintroduce the settings bug.

## Verification and remaining acceptance

The packet reports the final focused Ruby selector passing 26 tests / 275 assertions in 10.815 seconds, focused Go CLI/creation-roster checks passing in 0.071 seconds, and gofmt, Node syntax, Nix parsing, and whitespace checks passing. I inspected the changed tests and their real call boundaries; I did not rerun those checks or launch native integration.

The new packaged subtest changes a usable fork to `xhigh` through the shipped browser, checks native state, rejects an incorrect directory without changing effort, invokes the real host helper to restore `high`, then runs the existing root/roster/provider/identity proof. It exercises the stock settings operation independently of the Ruby stub tests. The full nondefault-effort creation and causal follow-up suite remains intact. Actual execution must still establish that the shipped terminal/native combination behaves as expected; this review is not a packaged or live acceptance result. Documentation correctly describes the intended guarantee and refusal behavior.

## Complete history and migration conclusion

The final complete series remains six coherent units:

1. `98ae6b38b2830b612f68d3d5a84f96c1d7caf5ca` — optional provider journal reader contract.
2. `bc29fab704f1cff34f2435710585d063e0419d87` — packaged usable-creation acceptance and CI.
3. `95cc08dbbeaafcc264a9af0e452b832b16d68e82` — all-provider retirement discovery.
4. `11620fc9793083a8ba2a8ac25cc4cf7357c3c489` — terminal preparation retry refusal.
5. `814568f3a28ae916ef193fd0be129a9f28fe1ffd` — actual HTTP readiness after fixture restart.
6. `901cff7db8f816cad12d8bbc2b39fa477fbd786a` — frozen fork startup/recovery settings and supporting verification/docs.

The unpublished partial `a7bd544` unit has been replaced by the complete final unit, rather than retained as a fixup chain. Exact consumed `95cc08d` and published/verified `814568f` remain ancestors. No obsolete intermediate protocol, abandoned implementation, or redundant compatibility path remains in the reviewed series. The latest helper, orchestration, tests, and documentation support one settings-preservation behavior and are appropriately bundled.

**No migrations:** the complete range introduces no database migration, journal schema/version transition, or state conversion; there is no migration lineage to consolidate or preserve for intermediate schemas. **No repeated runtime dependency/input/pin update streams** exist in this range.

The previous consumer conclusions are retained: workspace `3d638f9b0cf535e75ee08ce0f8f7d63efb9ec324` and configuration `102b9520ba00ec9bfdb4562869e40170d5347b31` each contain one consolidated selection from their original bases, with no migrations or redundant pin stream. They still select `814568f`, so they do not yet compose this corrected runtime. Their next refresh must again leave one final selection per stream and retain deployment provenance separately.

No review finding prevents proceeding to the authorized long verification. Exact positive packaged/CI acceptance, actual old-reader negative control, final matching consumers and deployment, live acceptance, and conditional integration/release remain the parent's responsibility. This report does not waive any of those gates.
