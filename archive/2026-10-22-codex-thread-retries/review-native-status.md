# Loaded native status affected independent final review

## Findings and disposition

No Blocking, Important or Advisory findings in the completed A/B protocol correction. The source units are ready for the planned disposable native run3. This conclusion does not certify native success, final downstream composition, deployment, live use or integration.

Prior B1/I1/I2/I3 and unchanged optional UI/scope conclusions remain valid. The material native-status correction was assessed independently rather than treated as patch-equivalent or as a narrow test-only refresh.

## Protocol correctness and authority

A owns the additive TurnState.IsLoadedFailedTurn(expectedTurnID) observation in codex/turn_state.go. It requires a nonempty expected ID, exact latest-turn identity, failed terminal status and raw native idle or systemError. It rejects cold, active, missing/unknown, wrong/newer and nonfailed observations. Raw TurnState.Status remains unchanged. The helper neither classifies errors nor proves queue, prompt, ledger, binding or execution authority.

I independently inspected pinned rust-v0.163.0:
- bespoke_event_handling.rs:1034-1055 calls note_system_error before affects_turn_status, so the error flag alone cannot establish a failed turn.
- thread_status.rs:147-191 clears the error flag on new turn start but not completion; :447-468 distinguishes notLoaded, active flags/running, systemError and idle.
- resolve_thread_status at :290-303 upgrades in-progress idle/notLoaded, not systemError. This makes the separate latest-turn terminal check necessary.
- The native system_error_sets_idle_flag_until_next_turn test at :619 confirms error-flag persistence.

Thus accepting the exact failed tuple under systemError is supported by the selected native source. Run2 did not retain that tuple; this report makes no empirical systemError claim from it.

Both existing ContinueFailedTurn preflights consume the shared helper through continuationIdle. Reconciliation of the exact accepted/submitting identity still precedes fresh admission. The queue mutex, stable text/action/options identity, pending-request and queue checks, foreign unresolved-ledger gate, final reread, atomic submitting claim and unknown-outcome reconciliation remain intact. No normalization, reset, resume, policy write or dummy turn was added.

B retryBackend.Check delegates to the same helper and retains current epoch/binding, socket generation, execution permission, provider, policy/common instructions and exact historical native context checks. Automatic failure classification remains the separate exact serverOverloaded/cyberPolicy allowlist. General retained observation and managed lifecycle/admission fences were not relaxed. The I3 warm witness still requires active/inProgress and is unchanged; the loaded-failed helper is not reused to promote settings authority. Managed-only/no-native-CAS limitations remain explicit.

The helper belongs in A because it describes selected native protocol observations and is used by both provider preflights and the concrete B consumer. It adds no required interface member or persisted format. Existing callers and embeddings remain source-compatible. Corrected B must ship with corrected A; an older A would continue to hold systemError failures and lacks the new method.

## Verification and fixture integrity

Inspected A's table/raw-status/continuation tests and B's actual managed-admission -> exact native-style receipt/context -> backend/controller -> continuation-wire matrix. Positive idle/systemError cases cover both eligible codes. Negative cases retain cold/active/unknown status, wrong/newer/nonfailed turns, unknown failure code, missing/changed binding/provider, queues, pending questions and foreign submission-ledger holds. These tests verify no extra resume/settings/policy mutation, exactly one accepted continuation and preservation of competing work. Protocol corpus assertions bind the exact four ThreadStatus variants, activeFlags requirement and flag values. Accepted/uncertain receipt behavior remains tested independently of fresh admission.

A's native setup now uses a private project, the existing managed BootstrapHeadlessThread single developer marker and persisted identity verification before any original user input, with no user turn or terminal failure fabricated. It then subscribes and proves a fresh loaded thread with no latest user turn. Helpers receive the current subtest T; explicit plan selection precedes the original turn, and actual original native model/effort/default-or-plan context is asserted before comparing continuation settings. This fixes setup/observability instead of weakening the continuation assertion.

The six intended native subcases remain: default/plan nonempty continuation, exact cyber terminal, actual queue execution settings, lost accepted reply with recreated client, and forced native-direct busy race. Partial command item/output, deterministic side-effect contents, original/continuation message counts, actual settings, application context, provider request counts and busy-race refusal remain asserted. B retains genuine accepted-start proof, real schema3 submitting ledger inspection, exact source/UUID/action/content, recreated client, actual retained resolver and exactly one native continuation input. Its barrier hides only successful nonempty native turn receipts; RPC rejection or missing receipt cannot masquerade as acceptance. Controller-restart before dispatch retains its native subscriber; the actual client restart occurs after acceptance and tests reconciliation, without repairing a cold execution hold.

Bounded diagnostics now retain status/latest-turn/error information, setup persistence/subscriber evidence and RPC identities without dumping arbitrary prompts/configuration. Read-only B native ledger inspection does not seed or rewrite authority. The unchanged recovery fixture gained process start/stop diagnostics only.

Reviewed owner quick evidence, without running tests:
- A focused races passed8.024s; generated pinned protocol/status/flags/corpus coverage passed; native compile/list succeeded.
- B exact final-head52-case matrix passed4.447s; focused races passed core4.058s/workspacecodex18.330s/web7.402s; fake receipt barrier passed1.225s; affected notification/browser checks passed0.207s/1.088s; tagged compile/list included both expected native top-level tests.
- Current worktrees are clean and exact final trees match the packet.

Run1/run2 remain failed/incomplete records. A run2 stopped before its first original user turn because the fresh thread lacked physical rollout; parent-T FailNow also hid the remaining subcases. B timed out without retaining the actual failed status. Source proof, fixture repairs and fake tests do not turn those runs into empirical passes. Run3 must retain named PASS evidence, actual status tuple and native acceptance/reconciliation evidence. Native-direct busy behavior remains a compatibility gate and does not establish global exclusion.

## Exact identity and branch history

Same retained independent reviewer0, gpt-6.1-sol/xhigh/read_only, verified ready review-purpose identity through the live roster; no override/fallback. dev-session current returned2026-10-22-codex-thread-retries, both environment markers were absent and the trusted thread/workspace binding matched. HIGH risk; affected general/architecture/risk lanes performed directly using the skill/references and applicable unchanged guidance. No source edits, tests/native execution, builds, nested agents, claims, deployment, merge or lifecycle actions.

Reviewed full base-to-head histories and final diffs together with the prior full reviews and current substantive deltas:

| Repository | Base | Final head | Final tree |
| --- | --- | --- | --- |
| codex-web | ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5 | 665fd35e3b29e07c29cd990c2067a3dba295fbf7 | 8ae62055147b638658d57aaddf0e3af795a2ab80 |
| dev-workspace | bf6d4b0c49600c15e17fe71248807ef43424e932 | 731bb742e07b4374cb8ee9a3a1379eb751cf44c4 | 67a58609dd374702984ae871b47e08977ca9abf8 |

A retains three logical commits: c27cd986 client/context/predicate; acfc950d optional UI;665fd35e native fixture. Optional UI stable patch ID independently remains4f906eb1dd62001465e5419ac67d8f97b8af592a. Predicate/protocol tests/docs are folded into the owning client commit, fixture/bootstrap/diagnostics into the test commit.

B retains four logical commits:7262c24e core and b3c7187c capability unchanged exact;0f752d7e owning runtime;731bb742 sole final A pin. Production delta is limited to shared predicate use/diagnostic; test/docs/pin support is appropriate. Previously reviewed epochs/quota/I3/lifecycle code and schema have no delta. Small earlier notification/browser fixture changes supply required provider/module dependencies and do not change application authority.

Commit split and messages remain adequate. No obsolete approaches, fixup/transitional commits or branch-iteration compatibility shims remain. Original reviewed/diagnosed ranges are preserved as evidence; no product-equivalence claim is made for the corrected status behavior.

B's one codex-web update stream remains consolidated in its final dependency commit, selecting665fd35e across Go module/sums, Nix source and vendor hash. Direct lock comparison against diagnosed3f shows only codex-web changed and all input edges unchanged. No superseded pins remain in the reviewed B series; A has no dependency-update stream. C's final workspace/configuration pin stream must still be consolidated to the verified final source pair after native source-unit success. Frozen old C selections are not certified ready by this review.

## Migrations, consumers and documentation

No migrations: no database migration, retry-state conversion or transitional private format. Final retry schema1/capability1, keyed charges/provenance epochs, native ledger3 and roster/history formats are unchanged. Supplied provenance remains unmerged/unreleased/undeployed with no external retry-state predecessor. No intermediate compatibility path is required.

Consumer discovery remains imports/wrappers and actual Go/Nix/composition pins, with B as the concrete helper consumer and workspace/extension/configuration composing it. Source-unit native verification uses the matching B shell/private A/B fixtures and is independent of pending mechanical C selection. Final C source/input graphs and full composition/builds remain separate gates before deployment.

A docs/reference.md correctly defines loaded quiescence, raw systemError and the helper's limited meaning. B docs/workspace-portal.md explains the same status distinction while retaining all independent admission gates. Lasting protocol behavior is documented with its owner; failed-run diagnoses and per-run evidence remain in session records. Placement and adequacy are acceptable; prose does not claim a successful rollout/native run.

Disposition: affected final source review passes with no findings. Proceed through the existing native run3 gate with the exact reviewed A/B heads. Preserve all prior reports and use the same reviewer for any material protocol/authority follow-up. Full-composition readiness and live use remain unproved.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/
