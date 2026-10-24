# Incident2 prepared-plan delivery and HTTP runtime wait: independent FINAL review

Report from retained reviewer0 to lead, 2026-10-23. Saved by lead from the
reviewer's delivered report; no reviewer source/session edits.

## Findings and disposition

No Blocking, Important or Advisory findings in the exact final A ac62eeeb/B7b8c6469 deliverables. General, architecture/repetition, scope/proportionality and risk/compatibility lanes are complete. These source units are suitable for the separately planned post-review verification phase.

This conclusion does not certify native/package/build results, W/C composition, deployed recovery of the user's original submission, live usability or integration readiness. Prior retention review is context; the changed prepared-send/HTTP admission and runtime-wait boundaries were independently inspected.

## Identity and reviewed source

Retained reviewer0, gpt-6.1-sol/xhigh/read_only, verified ready/review-purpose in the live same-session roster; no overrides or fallback. dev-session current from the tracking directory returned2026-10-22-codex-thread-retries. Both DEV_SESSION markers were absent and the trusted exact session/workspace binding matched. Mandatory skill and all four full lane references, applicable workspace/repository guidance, the RELEASED packet and accepted design Incident2 section were read.

I inspected committed source, complete histories/final diffs, adjacent callers, actual Handler/managed-client regressions, owner final receipts and retained quick evidence. No source/session-file edits, tests/build/native execution, CI wait, live ledger inspection, nested agents, claims, deployment, integration, release or lifecycle action.

| Repository | Base | Final head | Final tree |
| --- | --- | --- | --- |
| A codex-web | ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5 | ac62eeeb9d8b1fa7b8ed8fb95ba8160acb7efa1c | c0066833953974d27019c40754301a45a58868b0 |
| B dev-workspace | bf6d4b0c49600c15e17fe71248807ef43424e932 | 7b8c646974df72e0df3e576d10f09d79823ae004 | 9a409e0eb0003d1e3cefd6874d0cae028506d368 |

Exact heads/trees, clean status, bases, whitespace and full series were independently confirmed. Fresh SSH reads matched published feature heads and unchanged remote defaults at the stated bases. A c1f and B ed2 are actual deployed predecessors; their preserved bundles independently verify. No current source equivalence with the substantive successor is claimed.

## A: exact prepared proof and locking

Commit ac62eeeb, codex/client.go:3053 and :5250:

- IsPreparedSendWithOptions normalizes original options and checks the exact thread/UUID/text/action/options digest inside the existing per-thread queue lock and reloaded ledger transaction.
- Only an existing prepared entry without a queue-attempt marker returns true. Absent, submitting, accepted or queue-owned work cannot acquire this first-execution grant. Changed identity and unreadable ledger error. Stored steering/options and ledger bytes remain untouched.
- RequireSubmissionAttemptsKnownExceptPreparedSend holds the same per-thread queue lock across positive exact validation and the existing requireSubmissionAttemptsExcept primitive. It excludes only that one prepared UUID; other unresolved sends, queue attempts and queue deletions receive ordinary checks.
- The methods issue no native mutation, do not authorize dispatch or settings changes, and do not change SendAttempted's existing prepared-inclusive meaning.

The helper reuses the existing submission/queue owner rather than exposing a private ledger snapshot or duplicating downstream parsing. Its queue lock is local; the documented common application admission fence remains necessary across proof and later effects. The generic writer still reloads ledger state, preserves steering intent and persists submitting before start/steer; the new observation is not a replacement for that final delivery boundary.

A tests cover restart, zero/nonzero options and both steering flags; full identity changes; all relevant negative delivery states including executed/deleted queues; second unresolved requests and queue deletion; known/executed queue receipts; stale cross-client reads; unreadable state; unchanged ledger bytes; and a deterministic queue barrier verifying the queue lock remains held throughout the known-submission check. Existing reconciliation/no-resend and active-turn refusal tests remain.

## B: exact prepared-plan recovery through HTTP

Commit9fe56d2b:

- portal/internal/workspacecodex/turn_retry.go:257 retains generic exact reconciliation/history recovery first. Only when an existing exact attempt has no managed snapshot can A's positive prepared/nonqueued predicate permit its first capture. It never upgrades submitting/accepted/queue-owned work from missing retry evidence.
- capture remains after the explicit Plan-to-Default update, so newly admitted evidence uses the current epoch. Existing old-epoch snapshots are preserved rather than rewritten/rebound. Root generic zero options remain zero; member options/context/policy stay immutable.
- portal/internal/web/plan_delivery.go:21 constructs only the exact bounded same/recover root tuple. It takes no browser-provided socket/thread/directory. Trusted current tracking/runtime identity, provider, observation receipts, tmux and native identity are checked before and again inside roster-operation/conversation locks.
- reconcilePlanDelivery at:38 performs only exact generic receipt/history reconciliation before ordinary activity and plan freshness. Accepted originals return their receipt; unknown remains unknown. It never sends, changes mode, resumes or discards uncertain work.
- A positively prepared request selects only a request-local root observation exception. teamruntime/observation.go:70 and workspacecodex/observation.go:174 factor the existing observation owner; only the root's known-submissions check changes. Root metadata/persistence/activity/queue/prompt checks, the exact retained set, every member and all other unknown work still use ordinary proof.
- The normal implement-plan handler then rechecks the current proposal turn/digest, mode/activity and immutable generic preparation. It updates mode explicitly when needed and sends the original UUID through ordinary managed admission. Generic final receipt/steering checks remain mandatory. Receipt recovery precedes stale-plan checks; obsolete prepared retirement stays on its existing positively unsubmitted path.

Lock order remains transition -> runtime -> roster operation -> conversation -> retry admission -> generic ledger/queue. Early receipt reconciliation releases roster/conversation locks before retained observation reacquires its own operation lock. The low-level prepared exception and send path do not acquire outer roster locks while holding the conversation or retry fence. No recursive roster acquisition or new inversion was found.

The full actual Server.Handler fixtures use the real managed client/generic ledger over synthetic native wire. They exercise fresh plan, deployed prepared Plan and Default states across restart, failed mode update, exact accepted and acknowledged-history replay after newer work, changed text/action/options, another root/member unknown request, stale plan, original steering intent, submitting uncertainty and accepted retry-save failure. Before/after admission-save injection verifies native0/settings1 before recovery and native1/settings1 using the original preparation after client recreation. Root/member wrapper tests preserve original option/context/policy and old-epoch evidence. Retention pressure/FIFO/replay tests remain, with their former blanket prepared refusal deliberately changed to the accepted positive-first-execution boundary.

## HTTP runtime contention and fresh authority

Commit7b8c6469, portal/internal/session/authority.go:52:
LockRuntimeSharedContext uses the same private owned directory/file validation and one descriptor. It retries only EWOULDBLOCK/EAGAIN with an interruptible10ms timer, checks context before attempts and after acquisition, and closes on failure/cancellation. Existing fail-fast shared/exclusive/creation APIs remain unchanged. No holder termination, downgrade or ownership transfer exists.

portal/internal/web/server.go:2030 establishes the session mutation20s parent budget before the runtime wait; nested handler contexts cannot extend it. Conversation resolution uses the existing conversation operation deadline. Waits occur under the outer transition fence before roster/conversation/admission locks. Automatic-retry resolution deliberately retains fail-fast runtime acquisition.

After the wait, both HTTP paths check the current host profile and creation/lifecycle state, reload tracking, normalize interactivity and repeat provider/retained authority proof. The plan path's exact identity checks and later ordinary proof remain fresh. Conversation resolution preserves member identity, cold/recovery behavior and final client VerifyThread; waiting does not itself grant activation.

The18 actual HTTP route/outcome combinations cover plan, root/member messages, queue addition and queue reconciliation. A real exclusive runtime flock holds the request before release; it produces no native mutation while waiting. Release permits normal delivery, while deadline prevents it. Plan tests change package generation, authority, lifecycle or cold identity while waiting and require refusal with no native mutation/settings effect. Descriptor reacquisition checks cover release on all outcomes; focused session tests also preserve old fail-fast behavior. The synthetic checks establish the intended composition but do not claim a live historical holder or native campaign success.

## History, consolidation and deployed lineage

Complete A base-to-final series:

1. df00fa36c820fc7a62ee5b8dd6e1745940ff8e15 client/context/predicate.
2. 6c828759440705c632e1902fa8309ccac446b050 optional retry HTTP/UI.
3. c1f415ad5602c23e6443cced73cb59267a796f05 native fixture, deployed boundary.
4. ac62eeeb9d8b1fa7b8ed8fb95ba8160acb7efa1c additive prepared proofs.

A's first three commits are unchanged; the successor changes only client.go, prepared_send_test.go and reference docs. No dependency-update stream exists in A.

Complete B base-to-final series:

1. 7262c24e4fbe9dbf8604e73590f9b5ef3d5dce99 core.
2. b3c7187c6e26e269994433716a0ee719d0a7edf7 capability.
3. aafaf4195d695c4641ce4f9342d56a1786f237c3 original runtime.
4. a708f4011d33e7df6b73256b9a3873c24d03bbe7 sole final A pin.
5. f856549e54e2dbe56cc91548d2ea9b588c7e6633 accepted-only retention.
6. 9fe56d2b031928ed18a8fa7bde61dc5edadef24e prepared-plan recovery.
7. 7b8c646974df72e0df3e576d10f09d79823ae004 bounded HTTP runtime wait.

The complete histories/final diffs were assessed with prior full review and current deployed-to-final changes. Original core/capability/runtime commits remain exact. I independently confirmed f856's retention patch ID equals deployeded2's4850f62fbfc3bb6569f25a5a4f946bcebce73a7f; ed2-to-f856 product diff is empty outside the five A selection files. The H1 protected-Pending correction and coordination fixture support therefore remain in the retained product patch.

B's A dependency stream is correctly consolidated to one final update, a708. Oldd819 pin and intermediate A updates do not remain as redundant commits. Exact deployeded2 is preserved as a ref/bundle/rollout receipt, not a literal ancestor of current B. No state recovery contract requires that ancestry. This establishes preserved lineage evidence and a retained product patch, not equivalence of the substantive Incident2 successor or a claim that deployeded2 was merged.

Commit separation is coherent: shared library proof, one dependency update, supported retention behavior, prepared-plan delivery and independent HTTP contention correction. Tests/docs belong with their contracts. No obsolete unmerged approaches, fixups, abandoned shims, transitional behavior/migrations or redundant pin streams remain. Mechanical pin changes did not displace the supported deployed boundary.

B selects Aac62 consistently in Nix source/lock and Go pseudo-version v0.0.0-20261023170628-ac62eeeb9d8b, sumh1:z09uGj1nKIn7CYBPZ7YZ5rsGF3MwN98tbyHqQln24ds=, with source NARsha256-tCfdy/lh9LHbvEd6BYO0trM1pUelyv2T63KsQ1iEK90= and vendorHashsha256-NZ9hapJobbhvEdxWTtzYJ/3ZeMkSZAqOdewJCsZoL2o=. Independent lock comparison against deployeded2 changes only codex-web; all nodes/edges outside that selection remain unchanged.

## Migrations, scope, consumers and documentation

No migrations: no database migration, retry-state conversion, eager rewrite, ledger reset or new persisted format. Deployed A c1f/B ed2 schema1 retry and schema3 native records are real supported predecessors. The new readers/proofs operate directly on them; original UUID/action/options/steering and unknown/queue identities remain. Native0.163, runtime capabilities and HTTP payload/error schemas are unchanged. Older software can decode the formats but retains this delivery bug; forward package recovery remains appropriate.

A owns generic immutable delivery-state proof; B owns trusted managed authority and the actual HTTP plan workflow. This matches actual imports/wrappers/pins without a private ledger parser or upstream protocol reimplementation. The context-aware lock owner remains session authority, adopted only by the affected HTTP admission paths. No speculative registry, new fallback/generalized recovery framework, native patch or deferred UI redesign entered scope. Scope and proportionality are acceptable for the two demonstrated failures and their required replay/concurrency consequences.

A docs/reference.md accurately explains prepared versus absent/queued/submitting, unchanged SendAttempted semantics, queue-lock scope and application-fence limitations. B docs/turn-retry-recovery.md explains exact plan first admission, receipt-first recovery, current-epoch capture, bounded HTTP waiting and post-wait checks. The scheduler-only no-sleep wording avoids falsely forbidding HTTP waits under the transition fence. Existing README/portal links keep owning contracts discoverable; incident/source/rollout evidence stays in session records. Documentation placement and adequacy are acceptable.

W/C final mechanical source graphs/history were not inspected in this review. They remain a separate frozen supplement and have no stale approval from this A/B disposition.

## Verification evidence and remaining gates

Owner final receipts bind exact committed/tested trees. A receipt SHA2566a7882c9bf9408e0e86a8f68c66d92dd111a3a321e215ec9a992cfaeca302d02 matches the packet. Independently parsed A final normal/race JSON:48 passing test/subtest events each, no selected fail/skip; output hashes match the receipt.

B final focused logs pass web8.927s/workspacecodex5.720s/session0.072s/teamruntime1.159s. Inspected race receipts cover web14.658s/session1.130s, corrected wrapper/options/retention57.401s, core2.136s and actual Handler persistence boundaries2.052s. I verified the saved log hashes against implementer1-incident2-final.json. Original failed wrapper/fake and nested metadata-RPC fixture diagnoses remain preserved; corrected fixture scope removes the reentrant RPC and validates explicit authorized resume without changing product checks. No test was rerun by this reviewer.

The required post-review exact A/B packaged checks, targeted native contract/controller/recovery and runtime/package/lifecycle exclusion regression remain necessary. Derivation/input-based reuse must separately justify any unchanged check. W4/C8, scoped system/profile builds and fresh activation/user-original-submission proof remain later gates. No native/package success or unrelated full VM repetition is inferred from source/fake tests.

Disposition: independent FINAL source review passes with no findings for exact Aac62/B7b8c6469. Lead may save this as incident2-prepared-plan/review.md and continue the separately authorized verification workflow. Retain this reviewer for material related revisions. No integration, deployment, claim/release or session lifecycle action is authorized by this report.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/
