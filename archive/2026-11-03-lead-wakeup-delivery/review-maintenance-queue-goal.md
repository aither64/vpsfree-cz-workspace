# Final affected review: queue and goal metadata

## Findings

**No new Blocking, Important or Advisory findings** in `94eb2380bc3527863d7f712ff914717146cc963c..f168b9d4bc1141dc66c27042dc31e7385dfedbd8`.

The two exact notification classifications are supported by selected-native schema/producer evidence and the actual current consumer. They preserve separate execution/effect proofs. The added close diagnostic changes no acceptance rule. This conclusion does not establish a normal actual close, resolve all native blockers or release another run.

## Exact scope, settings and source evidence

- Repository/worktree: `git@github.com:aither64/dev-workspace.git`, `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-lead-wakeup-delivery/dev-workspace`.
- Head: `f168b9d4bc1141dc66c27042dc31e7385dfedbd8`.
- Tree: `30368c3cb1134dec7c730db3b18af6436ee5b17a`.
- Parent: `3145caa8fcf23b1e825eb54fe9176258f58c6b7f`.
- Affected delta: three files, +87/-10.
- Complete range: `3bb08df22aa4a36b7ff23ef62aaad586f4c59bb7..f168b9d4bc1141dc66c27042dc31e7385dfedbd8`: five commits, 127 paths, +26455/-161. Exact merge base is3bb.

I checked HEAD/tree/parent and clean worktree/index directly. Actual affected/full Git diffs equal the supplied comparisons. I also reconstructed B's differently ordered plain unified diff exactly from the baseline/current bytes: its header/order difference is not source drift.

Main receipt SHA256 `e55adead2de64d2e4dadb3dfb76af43e285eb9e591d86b1ee0c1334dac954dec` and B packet SHA256 `f31fba6da1054c5147b7e7a4d4d39309c8cab8a06797fd34f44881227e42f3b2` match. All nine main artifacts, 26 B artifacts, three source hashes, twelve unchanged inputs and thirteen retained94eb raw artifacts match. All six primary-source SHA256s and five available Git blob IDs were independently recomputed and match.

Before owned records, exact tracking-directory `dev-session current` matched `2026-11-03-lead-wakeup-delivery`. Both shell identity markers were absent under the matching trusted developer binding. Capacity was confirmed. Reviewer0 retained saved **gpt-6.1-sol / xhigh / read_only**, without overrides, fallback or nested reviewer.

I read the current bounded packet/state, mandatory skill/four lane references, relevant implementation/tests, primary sources, failure projections and quick logs. Applicable unchanged guidance and full5e68/diagnosticc79/goal15f review conclusions were reused only within their unchanged scope. Main's R1–R3 step-9 closure and narrow owner-reason closure remain separate accepted evidence, not a new full implementation audit.

This review was read-only: no tests/evaluation/builds, native/browser/VM, Git mutations, publication, CI, live/claim/profile operations, peer-state access or lifecycle actions.

## General lane: actual defect and refusal invariants

The actual94eb result receipt `f9f910bddcae968268861f2303fe195c554cba30ef894b1fdbc87afc7a7042a9` records a failed aggregate: three refusal-path passes and two positive-path failures. It is not full maintenance acceptance.

For the sleep case, the retained pre-HUP projection names the same actor/owner/epoch, generation1, first unknown-event origin at sequence19 `thread/queue/changed`, and uncovered snapshot sequence20. That exact event entered the old unknown-thread-event branch and poisoned coverage. The empty digest projection on an uncovered Snapshot is not proof that the completed sleep item itself disappeared.

The fixture immediately calls queue/add and active goal/set. Selected native source proves the latter can emit `thread/goal/updated`, also previously unknown to this reducer. The captured first-origin value does not identify the actual sequence20 method; the goal correction is justified by the actual adjacent consumer and pinned producer, not an invented second captured event.

Production changes only the existing explicit inert branch at `portal/internal/maintenance/observation.go:391–398`: add exact `thread/queue/changed` and `thread/goal/updated` equalities and update the rationale comment. No wildcard, poison reset, item retirement, sequence/generation admission, source-turn logic, digest logic or Snapshot authority changes.

The regressions inspect ordered queue then goal metadata while the reducer has a real completed-sleep digest and pending maintenance MCP item. All Snapshot fields and membership stay unchanged except the expected sequence increment. They then complete the original item/turn and prove a valid successor starts fresh; proof for the superseded turn still fails. Other tests preserve:

- No coverage/readiness from metadata alone; foreign starts cannot establish coverage.
- Unknown queue/goal/item sibling poison and first-origin identity.
- A genuine unresolved command hold and next-start refusal.
- Malformed known-metadata frame invalidation.

The tests therefore preserve the safety boundary rather than merely removing the observed assertion. I read the original red package failure (0.014s), final observation/activity pass (0.265/1.360s), and tagged compilation pass (0.048s, **no tests run**). I did not rerun them.

## Architecture and repetition lane: metadata is not execution

I inspected retained immutable primary sources at native revision `360319d8dee62d87e2d59fc0c21805d79519cfed`:

- [Queue API](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/app-server/src/request_processors/thread_queue_processor.rs#L77) delegates add to enqueue. [Queue service](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/ext/queue/src/service.rs#L265) persists the item, emits changed state and then performs an idle-only wake; actual dispatch uses native turn admission.
- [Goal processor](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/app-server/src/request_processors/thread_goal_processor.rs#L242) emits goal metadata and applies runtime effects. Its source explicitly notes active goals can inject an objective or start idle work.
- [Resume snapshot](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/app-server/src/request_processors/thread_lifecycle.rs#L972) can emit the same goal update from a stored-state read.
- [Protocol types](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/app-server-protocol/src/protocol/v2/thread.rs#L2163) give queue changed only thread identity, and goal updated thread/optional turn/goal state; the exact method mappings were also inspected.

The underlying mutation APIs **can schedule work**. Treating these notices as metadata neither certifies those APIs as passive nor proves their effects ended. Notification delivery is not an owned execution record or admission barrier.

The unchanged actual consumer still validates the exact active source turn before and after cleanup, the direct pending MCP item/ack identity, descendant/current-item cleanup, and final observer generation/item/digest membership. Lease/Stop and native drain/exit checks remain separate. Any scheduled work must satisfy those existing checks; metadata alone cannot substitute for them. Queue/goal preservation and activation-only continuation remain unchanged.

The classification belongs in the reducer's existing finite explicit list. No second registry, SDK API, observer, callback, protocol framework or downstream policy duplication is introduced.

## Scope and proportionality lane

This is a bounded correction to a demonstrated current-consumer compatibility failure. Two exact names address the observed queue notification and the adjacent supported goal producer; no future-event family or sibling expansion is added. The fixture's accepted queue/goal setup, ordering and preservation assertions are retained, rather than hidden or reordered to avoid notifications.

The additional seven fixture lines execute only inside the existing failed-close assertion. They call existing in-process Snapshot/PriorOrigin projection and log actor/source/operation/retained owner/socket epoch plus `separateNonAtomicReads=true`. No new native request, subscription, hook, await, timeout, retry, seed or acceptance branch is introduced.

The nearby exact-method comment correctly distinguishes state metadata from APIs that schedule work. Existing maintenance/update docs still own queue/goal preservation and effect/close limits. No new operations document or optional framework is warranted.

## Risk and compatibility lane

The independent execution proof remains necessary: source-turn changes, unknown effects, pending commands/children, lost observation, invalid identity and missing digest membership still refuse. The metadata branch creates no lease, readiness, terminality, idle proof or continuation permission. Metadata does not erase preexisting poison or carry prior tool/digest membership into a successor turn.

The failure-only close diagnostic is non-atomic and records only the existing local bounded reducer projection and known disposable fixture identities. It does not retain frame payloads, arguments, commands or settings. It may reveal an earlier first poison or a first loss boundary while still leaving low-level transport subtype unknown.

The94eb second positive failure reported `observation-lost` after successful source drain/exit. Both outer and embedded reason fields now agree, which supports the separate owner-reason transport closure. That does **not** prove the actual WebSocket close was normal. Earlier abnormality and later read/retirement loss remain distinct possible causes; the new failure projection has not executed yet.

I matched main's narrow closure SHA256 `112286689312e16877780691c980a8b81362e5a910d4f2362a9eb5ba7517cff8` and its unchanged production files. No close classification, owner/control contract or refusal precedence changes in this delta.

SDK/module/sums, Nix graph/vendor/native/model/catalog, host/startup/claims, diagnostic accessor and ordinary admissions are unchanged. Existing unreported-cell, archive and deferred-R5 limits remain. Neither a terminal turn nor source exit proves global cell/descendant quiescence.

## Complete history, consolidation and migration/state lineage

The complete current series remains:

1. `e18a1e8de4d599df830e6ac390c9ab306d23d891` — independent tracking-directory deadline fixture.
2. `58e87f9d3ccc1aac262b29f587a1d0553257a554` — durable monitor capability.
3. `f161ede8a6ea4cf540edcb7ece81ebb76f064a05` — adopted passive archive-hydration diagnostic.
4. `3145caa8fcf23b1e825eb54fe9176258f58c6b7f` — final SDK and genuine independent historical fixture dependency.
5. `f168b9d4bc1141dc66c27042dc31e7385dfedbd8` — coherent final maintenance implementation.

The first four commits are unchanged; only the owning maintenance commit was amended.94eb and prior failed/reviewed heads remain refs/receipts rather than fixup ancestry.

**Obsolete history:** no obsolete approach, superseded fixup chain or transitional compatibility behavior introduced or retained by this amendment. Whole-series coherence/consolidation conclusions continue within the reused full review and inspected affected boundary.

**Repeated update streams:** none. There remains one final production SDKc3 selection and the intentionally independent original3bb fixture SDKd3 graph, with distinct consumers. No new pin, dependency or generated-input update occurs here.

**Migrations:** **no DB migrations or seeds**. No new persisted diagnostic format, conversion step or intermediate reader. Existing final maintenance schema1/readers/recovery and public/monitor/submission/service/retry/claim formats remain unchanged. Historical donor external consumption is still unproved; no absence assumption or private-state inspection is used to justify compatibility.

These are source/history conclusions, not literal-merge or deployment acceptance. W/C still consume historicalf161; final consumer composition and artifacts remain separate.

## Verification limits and disposition

The quick evidence uses canonical published SDKc3, with no module override. The final observation/activity selector records an absent provider-catalog fixture environment; this is isolated test setup, not a product-policy change. Dirty-tree/system warnings and the ignored Nix cache-busy warning remain in original logs. Current source is clean and matches tested-tree/source receipts.

No actual native call, VM/browser, application build or full suite has run for this patch as part of the reviewed package.94eb's failed aggregate and case/effect evidence retain their exact scope. It remains unproved whether the classification correction removes all subsequent blockers or whether the close failure was caused by prior metadata poison versus transport/retirement loss.

A future exact-source run must retain all existing acceptance assertions. No older SDK/runtime/donor/W/C result substitutes for final maintenance/native/VM/browser/full-check/composition/live acceptance. This review makes no normal-close or global-effects guarantee.

**Disposition:** all-four-lane affected final source review complete with no new findings. Main owns subsequent execution release and any finding disposition. Publication, native execution, live activation, claims, default integration and lifecycle actions are not authorized by this report.

Session remains open: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-lead-wakeup-delivery/
