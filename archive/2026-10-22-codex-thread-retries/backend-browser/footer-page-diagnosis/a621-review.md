# Retained affected FINAL review — lost-policy-reply fixture correction

Findings: no Blocking, Important or Advisory findings in the assigned general, architecture/repetition and scope/proportionality lanes. The test-only correction is acceptable within this reviewed boundary. Actual browser/package/native and operational readiness remain unproved.

Reviewed exact B bf6d4b0c49600c15e17fe71248807ef43424e932..a62166a87658e16baa0efdddfea3a448ebebcc28, tree49dee759cd203a94eb898c6af5f67fbe99474028. Owning changed commit15 is5ddd74159a18f82c058a4d61c7e4dc58a5deb537. Comparison predecessor is preserved f75f79e545c29ec9e741d33504c3ce741a3a9dd4/treec3f0b49b920ad4d8778f711014cb37dba4296e4c.

Identity/guidance: dev-session current matches2026-10-22-codex-thread-retries; environment markers both absent, trusted developer binding matches. Verified live roster34 reviewer0 ready/independent/thread01a162d6-4bf1-7142-bb04-7b871eb2d1af, saved gpt-6.1-sol/xhigh/read_only; no override, fallback or nesting. Read authoritative affected-review-release.md fully, mandatory skill/three applicable full references, current B AGENTS and retained applicable workspace procedures. Inspected actual source/consumer assertions, diagnosis/source evidence, quick results and complete history. Medium risk affected fixture; prior high-risk production/recovery conclusions retained only at exact-content boundaries.

## General

portal/internal/web/retry_backend_browser_test.go:685–719 still executes the unmodified real Handler to completion before losing transport delivery. The correction at:703 copies actual response headers, sets Content-Length to the actual recorded JSON body length, writes actual status and flushes before hijacking/closing without sending the body. No fabricated policy/token/body, handler replacement, application retry or filter relaxation is introduced. The HTTP/1 TLS fixture supports the existing Flusher/Hijacker boundary.

The owning new root/member TLS regression at:422–483 reads actual policy, posts one real choice/revision, requires committed200 JSON headers/positive body length, zero received body and io.ErrUnexpectedEOF, then verifies real changed policy/new revision by GET. Exact one additional POST/drop, zero native starts and unchanged retry ledger are asserted. Existing constructor/manual checks remain. It verifies the failure after durable mutation and distinguishes it from the old no-header EOF; it does not claim to execute browser UI recovery.

Inspected unchanged CJS lost-reply consumer at retry_backend_browser_test.cjs:185–206 and:383–389: exact uncertainty copy, readback, onePOST/drop, replay/no-write and all32 case semantics remain. Production app.js:2798–2821 consumes response JSON and observes uncertain results through GET without repeating the preference write. The new truncated response exercises that intended seam.

Pinned Chromium147.0.7727.15 source/SHA matches its receipt. HandleIOError/ShouldResendRequest permit resend on reused connections without received headers; the new fixture supplies the real headers first. Original attempt7 failures for all4 variants show Saved instead of uncertainty after policy-scope. They do not empirically prove the internal resend count; no product bug or final browser pass is inferred.

## Architecture/repetition

No finding. Transport fault injection stays in the existing private TLS adapter, with real backend mutation and policy persistence owned by production. The regression reuses the same fixture/control/diagnostics rather than adding a new fake policy provider, generalized failure framework or separate implementation of policy behavior. The root/member table is appropriate coverage of the actual consumers.

## Scope/proportionality

No finding. Exactly one Go test file changes versus f75. CJS, product/service/lifecycle source, docs, assets, A and dependency pins remain byte/mode identical. The eight-line transport correction plus owning regression directly addresses the observed fixture failure. No optional native investigation, production policy redesign or broader browser exception was introduced.

## Evidence independently checked

All267 final quick input hashes match committed source before/after; tested candidate tree equals final tree. All75 referenced artifact hashes match. Raw final selector records8 test/subtest PASS, zero failure/skip, package0.773s/command10.329s. Raw baseline records both new root/member loss leaves failing with no-header EOF, while four construction leaves pass. Its bound Go source differs from final by exactly the eight-line transport correction; other baseline/final inputs are equal. These are inspected owner executions; reviewer ran no tests.

## History/consolidation

Independently reconstructed the complete18-series, messages, path inventory and base-to-head final diff; saved series/full-final.diff/f75.delta.diff match SCM byte-for-byte. First14 commit IDs are exact. Commit15 contains the fixture correction. Replayed16=99f19afc,17=2812c586 and18=a62166a8 each have byte-identical raw patches and messages to predecessor service16/deletion17/corrected recovery18. Across all586 tracked paths, only retry_backend_browser_test.go changes blob/mode versus f75;585 others are identical.

The transient fixup is folded into owning15. No obsolete unmerged approach, redundant follow-up or transitional migration remains in the final series. Logical commit boundaries remain appropriate. Sole A update stream is9ccb4b11->A5743f94c2fbd01b65438847d2e2bab0f01df32ae, with the full locked graph unchanged; no repeated/redundant pin stream. Prior D1 and R1 direct step9 closures remain retained, with no confirmation-only rerun or new production audit. Existing deployed7b8c provenance remains a supported nonancestor lineage through retained exact patch/receipt evidence, not literal merged ancestry.

## Migrations/documentation

No new migrations, persisted format, schema, API or runtime-contract change. Whole-branch prior no-database-migration conclusion remains: direct final retry/policy schema1, preserved generic submission3/MaxSnapshots64 and existing lifecycle/start/removal formats; no branch-iteration conversion/reset is introduced. Production/recovery content equality preserves prior risk/compatibility conclusions at their recorded limits.
The nearby fixture comment explains the lasting transport invariant. Product docs require no change because production behavior is identical; diagnosis and failed-attempt execution history appropriately stay in session records.

## Limits/disposition

Recorded SSH publication matches exact a621/masterbf6d; local source was clean. NAR/build/derivation reuse is not certified. Browserattempt7 remains failed/preserved; attempt8 is prepared-only/held and has not established the32-case browser result. Prior fork/pressure passes retain their original scope; historical CI failures remain unwaived. W/C still select stale e914 and are excluded. No tests/build/browser/native/CI/live-state/prompt/history queries, source/tracking writes, claims, integration, deployment or lifecycle actions performed. This report supplies no operational/deletion/integration permission.

Same reviewer retained for material followups.
Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/
