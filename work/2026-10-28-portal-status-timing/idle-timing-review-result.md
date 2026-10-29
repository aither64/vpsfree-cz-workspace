# Independent idle-timing review

**No Blocking, Important or Advisory findings.** The bounded display change is
acceptable for the deferred browser verification and final package checks.
It does not authorize deployment or integration by itself.

## Scope, behavior and execution safety

Reviewed runtime `cc0d452a0653a112c8a013492c1734d9554bb909`, on top of
previously reviewed `7d1163585a51da684be0f5cdd500a64822165839`, directly across
all four lanes: general, architecture/repetition, scope/proportionality and
risk/compatibility. Reviewer remains `/root/final_review`, gpt-6.1-sol/xhigh.
No delegation, build, native execution or live operation was performed.

The original task includes repairing unavailable timing/status. Allowing a
historical activity read after recovery verifies idle addresses that task
without expanding execution permission. `refreshActivity` continues to refuse
a held conversation unless its recovery state is `idle`; hidden/paused pages
and the existing read scheduler retain their guards. The idle-state transition
explicitly refreshes timing even when the conversation remains held and no
conversation-sync restart occurs.

I traced the activity request through the existing HTTP read capability, trusted
conversation resolution, activity provider and codex-web `ReadActivity`/
`historyRequest`. It reads thread metadata and history without subscribing,
resuming, answering requests or changing settings. The browser change does not
clear `executionHeld`, alter the recovery store, enable live events or call
message-dispatch drain while held. Existing server-side retained-input identity,
mutation locking and explicit-input admission remain authoritative. Failed,
unavailable and waiting holds continue to suppress browser activity reads.

The browser fixture now expects timing while idle/held, checks absence of
execution HTTP calls before the explicit original retry, and covers failure,
recovery without reload, accepted delivery, unknown delivery and reload without
replay in Chromium and Firefox. Its Go handler additionally checks that the
native wire has no execution calls and that the recovery hold still exists
immediately before the explicit message request. That is relevant coverage of
the new boundary rather than a mirror of the JavaScript predicate. The owning
portal guide accurately documents the distinction between recorded timing and
execution permission.

The change reuses existing state, endpoint, client and refresh scheduling. No
new abstraction, duplicated admission policy, schema, native launch argument or
public execution capability was introduced. The display fix is small enough to
remain separate from the native-home cutover while sharing its final package.

## Complete runtime history, dependency streams and migration lineage

I enumerated the complete runtime range
`d0e4318cb1872feb69f3109f032870c310f14bdf..cc0d452a0653a112c8a013492c1734d9554bb909`
and checked the final changed-path inventory and new committed diff. Its exact
series is:

1. `7d1163585a51da684be0f5cdd500a64822165839` — private native home, matching
   Codex 0.165/package selection and related fixtures; prior review retained.
2. `cc0d452a0653a112c8a013492c1734d9554bb909` — verified idle historical timing,
   its browser/native-safety assertions and owning documentation.

**Whole-branch conclusion:** the two commits have distinct, coherent purposes.
No superseded design, unused interim compatibility path or redundant fixup
sequence remains. The newly discovered timing defect is independently
reviewable and appropriately separate from the retained home/native commit.

**Repeated-pin conclusion:** there is no repeated dependency-update stream in
this runtime series. The new commit changes no dependency pins or generated
artifacts; the first commit retains the previously checked final codex-web,
llm-agents and vendor selections. Consumer locks are still at `7d116358` at this
checkpoint. Their proposed mechanical refresh to exact runtime `cc0d452a`
remains a subsequent verification step: preserve the extension and input graph,
consolidate each consumer's earlier pin update, and check the final committed
composition. This report does not certify consumer heads that do not yet exist.

**Migration-lineage conclusion:** no new project-owned SQL migrations or
persisted-state changes. The prior upstream native schema-62 and unexecuted
one-time partition lineage conclusions remain unchanged. The display commit
does not add a migration predecessor or require old/new state translation.

I also inspected the narrow operational retry correction committed at
`abe63598915ffa30a75d8976500761ca30ab5495`: lock acquisition now changes mode only
when the existing descriptor's permissions differ, avoiding the spurious
`ctime` change. The revised fixture retries the actual outer runner after
publication intent and before the first exchange. Together with the reported
passing outer-retry test, this resolves the remaining Blocking finding in
[review-remediation-result.md](review-remediation-result.md). It introduces no
new observation/recovery design requiring another full review.

## Verification and remaining gates

Committed diff whitespace is clean. The packet reports passing JavaScript
syntax and focused recovery/retained-input Go checks, plus native 0.165 naming,
0.164-to-0.165 saved-state resume/fork, namespace and provider-routing checks for
unchanged native code/binaries. Prior runtime CI `40854716525` passed its
creation/archive/package checks. Final runtime CI `40858490632` and the updated
browser fixture remain pending in the supplied packet; I did not run or monitor
them. A completed old-head build does not verify this changed JavaScript or the
final composed application output.

Before live use, complete the updated browser checks, applicable final-head
CI/package checks, mechanical consumer refresh and exact composition proof,
final system/application builds and the existing claimed migration/deployment
acceptance. That acceptance still includes timing/status for both reported
sessions, stock/portal isolation, conserved native history, retained execution
holds and the same-attempt original message reconciliation/retry. No master
merge, forced interruption, reboot or backup deletion is authorized by review.
