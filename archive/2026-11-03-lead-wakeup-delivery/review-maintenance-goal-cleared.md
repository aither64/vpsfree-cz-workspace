# Final affected review: exact goal-cleared notification

## Findings

**No new Blocking, Important or Advisory findings** in `1285b9640fbbf3aba08491f548aee3b5a0914cce..4dc0bee2681d3b0e4007f3cfe0915e46f4df99e8`.

The exact `thread/goal/cleared` classification is supported by the captured first origin and immutable selected-native schema/producer evidence. The correction does not grant coverage/readiness, reset prior poison or retire effects. No further classification expansion is needed for this change.

## Exact boundary, identity and evidence

- Runtime head: `4dc0bee2681d3b0e4007f3cfe0915e46f4df99e8`.
- Tree: `c88a3ed2992b80d60bc18df9b8a9e73d46f2354e`.
- Parent: `3145caa8fcf23b1e825eb54fe9176258f58c6b7f`.
- Affected delta: only `portal/internal/maintenance/observation.go` and `observation_test.go`, +64/-1.
- Complete range: `3bb08df22aa4a36b7ff23ef62aaad586f4c59bb7..4dc0bee2681d3b0e4007f3cfe0915e46f4df99e8`: five commits, 127 paths, +26235/-161.

I checked the exact head/tree/parent and clean worktree/index. Both supplied affected.diff and full.diff equal the actual Git comparisons. Main receipt SHA256 `dc638b857b2be274bb6cd80eb812cbd661b01866c7e6ccb8689beaa8b72752c1` and B packet SHA256 `bdbef39bfdfa6f336049342158e0d630c74bd6e30c5447c35587fb916528e21f` match; all five main and 22 B artifact hashes, both source hashes, nine frozen inputs and the three retained raw evidence hashes match.

Before owned records, `dev-session current` from the exact tracking directory printed the bound `2026-11-03-lead-wakeup-delivery`. Both shell markers were absent; trusted developer workspace/session binding matched. Capacity was confirmed to the lead. Reviewer0 retained **gpt-6.1-sol / xhigh / read_only** without overrides, fallback or nested reviewer.

This is the affected final protocol-classification review across all four mandatory lanes. I read the current packet/state, mandatory skill/four references and relevant source/tests/primary evidence, reusing applicable unchanged guidance and the prior full review5e68, diagnostic reviewc79 and main R1–R3 closure within their unchanged boundaries. No unrelated implementation/SDK audit was repeated.

No tests, evaluations, builds, native/VM/browser calls, Git mutations, publication, CI, claims, live actions, peer records or lifecycle operations were performed. Evidence/hash inspection was read-only.

## General lane: actual cause and correctness

The 1285 one-case diagnostic receipt `0e1a23169e9fc1c1137a014a98408180b84f41bee23441b47e5e04513bac5606` and raw projection retain the same actor, generation1 and first origin at sequence5: method `thread/goal/cleared`, reason `observation-event-unknown`, no turn/item identity, no truncation. That origin appears before the source start at snapshot sequence9 and remains alongside later sequence11/13 prior-effects refusals.

In the old reducer, that scoped method reaches the unknown `thread/*` branch and sets sticky prior effects. A valid matching start subsequently preserves the prior-effects refusal. This is a source-backed sufficient initial reducer cause. The separate diagnostic/Snapshot reads do not prove a unique native emitter, an atomic state or absence of subsequent blockers.

The production change at `observation.go:391–397` adds one exact equality to the existing explicit inert branch, with two rationale lines. It remains after JSON decoding and watch lookup. It changes no parser, wildcard, poison-reset path, item handling, generation/sequence admission or Snapshot authority.

The added regressions at `observation_test.go:321–380` cover:

- The observed cleared-before-start sequence: metadata alone remains uncovered/not-ready; a later valid observed start can establish coverage but still cannot establish wait readiness.
- Unknown goal/item siblings and existing poison remain refusing after this notification.
- A genuine unfinished command remains a wait blocker and poisons next-start coverage; its first-origin identity survives.
- Malformed known-event JSON still invalidates observation.

The retained red run failed on the old reducer at the expected behavior (0.010s), and final canonical observation/activity checks passed (0.273/1.359s). The red/green evidence uses the same test additions. I read those logs; I did not rerun them.

## Architecture and repetition lane: provider contract and consumer ownership

Primary sources are pinned to native revision `360319d8dee62d87e2d59fc0c21805d79519cfed`. I inspected the retained bytes and independently recomputed all three Git blob IDs and SHA256s:

- [Protocol type](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/app-server-protocol/src/protocol/v2/thread.rs#L2172): `ThreadGoalClearedNotification` contains only camelCase `threadId`; no turn/tool/effect ownership.
- [Exact method mapping](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/app-server-protocol/src/protocol/common.rs#L1991): that type maps to `thread/goal/cleared`.
- [Goal-clear path](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/app-server/src/request_processors/thread_goal_processor.rs#L275), with the emitter at501–521: notification follows successful clearing.
- The retained [resume snapshot path](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/app-server/src/request_processors/thread_lifecycle.rs#L972), SHA256 `eed1cc9bf38608be6ff2aa7a812b988fa9ecdcd5802944feda6839fe9361656e`: reading an absent stored goal also emits this notification.

Thus the notification describes goal metadata, including an absent-goal snapshot; it is not an instruction to execute new work or proof that an owned effect finished. The actual captured emitter cannot be distinguished from the method/thread projection, and the correction does not depend on guessing it.

Classification belongs in this maintenance reducer's existing explicit protocol list. No secondary registry, new SDK API, alternate observer or generic goal-event framework is introduced. The exact pinned provider contract, actual callback consumer and existing prior-origin diagnostic remain separate owners.

## Scope and proportionality lane

The observed failure and primary contract justify this one-event compatibility correction. It is the smallest conventional change: one equality and its focused regressions. It does not classify every goal notification, add future schema variants, or use a blanket goal wildcard.

The owning code comment explains the non-obvious absent-goal replay behavior. That is sufficient documentation for this bounded implementation correction; there is no new operational procedure or product guarantee to document. Existing maintenance/update docs and the diagnostic's in-process limits remain applicable.

No optional hardening or further implementation expansion is recommended by this review.

## Risk and compatibility lane

A goal-clear notification does not create authority. The unchanged reducer still requires a watched, valid exact turn start for coverage, then the existing pending-call/effects/identity proof for readiness. This equality neither erases an earlier poison nor treats goal disappearance as terminal command/child/cell evidence.

Unknown goal siblings remain conservative unknown events. Existing item/turn handling, unresolved-command holds, malformed-frame behavior, observation loss and first-origin lifetime/bounds remain. Neither this notification nor a successful subsequent fixture can establish global cell/process quiescence.

SDK/module/sums, Nix graph/vendor selection, native/model/catalog, host/startup/claims, fixture/deadlines and Snapshot/control wire contracts are unchanged. No settings, queues/goals or submission records are mutated by this classification. Later native/goal observations still own their existing admission and continuation decisions; this callback does not replace them.

Earlier full-review findings remain covered by the accepted step-9 corrections. This affected review introduces no waiver or new acceptance claim for those paths.

## Complete history, consolidation and migration/state lineage

The current series remains:

1. `e18a1e8de4d599df830e6ac390c9ab306d23d891` — independent tracking-directory deadline fixture.
2. `58e87f9d3ccc1aac262b29f587a1d0553257a554` — durable monitor capability.
3. `f161ede8a6ea4cf540edcb7ece81ebb76f064a05` — adopted passive archive-hydration diagnostic.
4. `3145caa8fcf23b1e825eb54fe9176258f58c6b7f` — final SDK and genuine independent historical fixture dependency.
5. `4dc0bee2681d3b0e4007f3cfe0915e46f4df99e8` — coherent final maintenance implementation.

Only the final maintenance commit was amended; the first four commits remain unchanged. Earlier reviewed/failed heads, including1285, remain provenance refs/receipts, not extra fixup ancestry.

**Obsolete history:** none introduced or retained by this amendment. The correction and regression are folded into their owning unmerged capability. Existing whole-history coherence/consolidation conclusions continue within the reused implementation and inspected delta.

**Repeated update streams:** none. There remains one final production SDKc3 selection and the intentionally separate original3bb fixture SDKd3 graph. This delta changes no dependency/pin/generated stream.

**Migrations:** **no database migrations or seeds**. No persisted format changes, new migration, diagnostic schema or transitional reader path. Final private maintenance schema1, existing monitor/public/submission/service/retry/claim formats and recovery readers remain unchanged. Historical donor external-consumption uncertainty remains; no global absence claim or private-state inspection is used to justify compatibility.

These are source/history conclusions, not deployment acceptance or a claim that amended old commits were literally merged.

## Remaining verification limits and disposition

The actual1285 diagnostic remains a failed original90s observation wait. It now supports the named first reducer cause, but not unique emitter identity, absence of later blockers, successful maintenance readiness/drain/activation or full runtime acceptance.

No native run on4dc0 was performed as part of this package. The unchanged fixture, deadlines and prior acceptance assertions still need their separately released exact-source execution. Existing SDK successes and old runtime/W/C/donor evidence do not substitute for final maintenance/native/VM/browser/full-check/composition/live proof.

Original dirty-tree/system warnings, failures and raw evidence remain retained. Current source is clean and matches the tested-tree receipt. No check replay was needed for this read-only review.

**Disposition:** affected all-four-lane final source review complete with no new findings. Subsequent capture, acceptance, publication, deployment, integration, claims or lifecycle actions require their existing separate lead/user authorization. The report itself grants no execution.

Session remains open: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-lead-wakeup-delivery/
