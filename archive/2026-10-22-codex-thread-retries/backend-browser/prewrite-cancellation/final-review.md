# Retained affected FINAL A+B review — pre-write cancellation, adoption and fixture diagnostics

Findings: no Blocking, Important or Advisory findings in the four assigned lanes. Completed independent source review of the exact committed deliverable. This does not establish browser/package/native/composition or operational readiness, and does not resolve attempt9's unrecorded inner cause.

## Reviewed ranges

A codex-web ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5..11ec57d2203fc735696fe75a837d47da55a5c6af, tree407762bc074c009540a6e2b5ca363fef1cc178f6,8 commits.
B dev-workspace bf6d4b0c49600c15e17fe71248807ef43424e932..e06578e4ad03cd6c023dcdd9685a678cd64339cc, treec1a8e9740a45c9e63549fd774dacb54a68b20abc,18 commits.
B comparison boundaries: reviewed e22eecab01a691225f7464f0c8965526648f442a and preserved adoption10182241096fc999f3636b7335cbd5eede835eed. Both final worktrees clean at inspection; recorded SSH proofs select assigned feature heads with default branches unchanged.

## Identity/guidance

Verified dev-session current/session2026-10-22-codex-thread-retries; markers both absent and trusted workspace/thread binding matches. Live roster34 reviewer0 ready, independent, thread01a162d6-4bf1-7142-bb04-7b871eb2d1af, saved gpt-6.1-sol/xhigh/read_only. No override/fallback/nested reviewer. Read final-review-release.md fully, mandatory skill/all4full references, current A/B AGENTS and applicable workspace/project/verification/documentation guidance; unchanged previously read routes retained. Read accepted design1582–1764, actual code/callers/tests/docs and evidence. Overall HIGH risk is appropriate for shared RPC transport, prompt identity and unknown mutation outcomes.

## General

A11ec57d2/codex/client.go:1188–1195 checks ctx.Err after writeMu/connectionMu and existing generation/prompt-claim revalidation, immediately before connection.Write. It releases pendingMu when applicable and connectionMu before returning the existing TransportError wrapping the context error. It does not call Write or markDisconnected at this positive no-write boundary. The deferred writer unlock, stale-generation/prompt checks and actual Write error/disconnect path remain intact.

Inspected requestOn's pending registration/removal, finishResponse's claim release, markDisconnected's generation checks and mutation send/reconciliation callers. The guard does not convert a failed mutation into success, retry an RPC, clear a durable attempt, detach its context or infer that an actual Write failure had no effect. Existing prompt/unknown outcome handling remains conservative; no new public “not sent” promise is introduced. Cancellation after the check/during actual Write can still disconnect; this remains an explicit limit.

A codex/write_cancellation_test.go:22 onward deterministically keeps a live sibling RPC outstanding, holds writeMu, waits for canceled request registration, cancels before lock release and uses a later wire barrier. Both already-canceled and canceled-waiter cases require existing error/context identity, zero canceled method frames, unchanged connection/generation/readiness, sibling success and one physical connection. This checks the intended boundary without relying on browser scheduling. Existing stale disconnect/generation, changed prompt claim and genuine write-failure guards remain in the focused evidence.

B sole adoption65e58006 selects A11ec in flake input, Go module/sums and vendor digest. Imported module v0.0.0-20261024144044-11ec57d2203f, Sumh1:cod93lovFHu5adtEqQy7QyE1E5YIFJrTkCnjB3phFgw= and unchanged GoModSum agree. Independently matched77 imported Go/module file hashes to both the module cache and A final source. Only codex-web locked node changes; other nodes/root edges/follows and native version remain unchanged. Vendor-hash raw receipt matches sha256-GcniWcl+4lS5swtWoGZYG04oa5uNtBjfYrKxVaiW1us=. No reviewer build/Nix hash computation or derivation-equivalence claim.

B diagnostic commit15=9ff433b33c726cd125fa1d2778be998f3e6f37e7:

- retry_backend_browser_test.go:125–171 records context states and typed categories around exactly one delegate;:182/:188 overrides forward ObserveThreadIdentity/VerifyThread directly to embedded real planDeliveryClient.
- :1089–1122 wraps the real resolver once and attaches a private context plus X-Retry-Fixture-Request only for four exact retry-host queue/page method+paths. It passes the original writer, Handler, result/error/Target/Release/capabilities and lock ownership. teamService uses this same adapter, so typed observation failure is captured before production's generic refusal. No observation is repeated.
- .cjs:32–84 associates lifetime records with the actual Playwright Request via WeakMap, page/document ordinals, monotonic start/end phases/times and exact Response.request header join. Missing headers stay unjoined. No request header, network interception, new fetch/RPC/wait, retry or queue suppression.
- The private retry wire records accepted/closed socket ordinals and fixed termination categories only. These are not A generations or RPC-to-HTTP attribution.
- The4096-event sink retains visible incomplete/active-at-snapshot state; overflow does not affect the delegate and fails the later gate. :1224–1240 saves server diagnostics after child return and before child-error Fatal, on success or failure. Browser artifacts retain the diagnostic array on either path.

## Architecture/repetition

No finding. A fixes the common owning writer boundary used by observation RPCs and prompt writes rather than adding consumer-specific suppression. Existing lock ordering and error types are preserved.
B uses one fixture-local sink and private request context, with short append locks never held over delegated work. One generic diagnostic call preserves original values/errors; no global current-request variable, production hook, shared manual-wire change or duplicated admission implementation. The bounded native intervals, server stage records and browser/server header join have distinct documented meanings. Actual root/member consumers and unchanged required interfaces remain coherent.

## Scope/proportionality

No finding. A production delta is eight lines in the owning transport plus its focused regression. A first7 accepted commits/assets remain exact. B final delta versus reviewed e22 is exactly five adoption paths plus two private fixture paths. No B product/ledger/lifecycle/fence/queue/UI rewrite, new framework/provider or production logging API was introduced.
Independently compared CJS: all scenario/action/control/assertion/error-gate bytes from policy-scope through the final negative gate, and the ancillary-policy prefix, are byte-exact versus pinhead. Original32 cases, onePOST/readback/unknown/native-negative/footer/draft assertions remain required; no POST404 exemption. Private fields/comments suffice for the diagnostic invariant; product docs need no expansion.

## Risk/compatibility

No finding in the new boundary. Positive cancellation before Write no longer retires unrelated healthy calls; actual write failures retain shared disconnect and uncertain submission behavior. Generation/prompt authority wins before the cancellation return. The new error does not authorize a new UUID, changed options or resend; durable reconciliation remains with the existing mutation owner.
Diagnostics preserve unknowns: errors.Is cancellation/deadline, errors.As TransportError and ObservationError.Code are recorded without raw error text/native payloads/prompts/options/configuration. Parent/stage context snapshots distinguish live transport from caller cancellation. Simultaneous states remain ambiguous. Browser and server clocks are not assumed interchangeable; native ordinals cannot establish sibling causation. The original attempt9 FAIL and the particular inner queue-reconciliation cause remain qualified; a future pass cannot retrospectively prove that cause.

## Verification evidence independently bound

A normal/race source manifests116 entries match final bytes before/after; raw logs show7 normal PASS and7 race PASS, no failure/skip. Red-before-guard shows both new cases fail while five existing guards pass. Recorded command times6.657s/12.854s are owner executions, not reviewer reruns.
B final diagnostic input maps274 entries match committed source before/after normal/race; raw JSON shows13 normal and13 race test/subtest PASS, zero failures/skips, Go0.386s/1.764s and wall2.209s/32.959s. Source inspection of owning tests covers actualTLS root/member queue200/exact body/one joined header with unchanged policy+ledger/zero starts; exact once/value/error/Release; barrier-overlapped context isolation; success/cancellation/deadline/live transport/semantic/simultaneous classification; overflow forwarding. Format/Node syntax/compile receipts are retained.
Pre-diagnostic11-test adoption quick binds10182241 only. Its two fixture inputs differ from final; no claim it executed on final diagnostic bytes.
Independently checked83 A artifact hashes,117 adoption artifact hashes and111 diagnostic packet artifact hashes with zero mismatches. Recorded immutable source/NAR/bundle supplements remain scoped source evidence; absence of the old pinhead Nix store copy is honestly recorded and does not undermine the hash-bound preserved lock comparison.

## Complete histories and update streams

A complete8 series/messages/full-final/new-unit diffs match SCM. First7 through5743 are exact; eighth11ec is a separate logical transport correction. Only codex/client.go and new write_cancellation_test.go differ versus5743; accepted assets/docs/other paths are unchanged. No obsolete approach, redundant fixup or repeated dependency stream found.

B independently reconstructed complete18 series/messages/full-final and both delta diffs. Adoption preserves first3 IDs versus e22 and replays5–18 with byte-exact raw patches/messages; consolidated pin4=65e58006 is the sole A update. Diagnostics preserves first14 IDs versus10182241, folds into owning15 and replays16–18 with byte-exact raw patches/messages. Across586 paths, exactly7 blobs/modes differ versus e22, exactly2 versus adoption; all remaining content/modes stay equal. No obsolete unmerged iteration, redundant pin/fixup stream or transitional migration remains. Historical preserved refs/bundles/failed evidence retain their own scope, without retaining redundant pin commits.

## Migrations/provenance/documentation

No NEW database/data migration, schema, API, protocol/catalog/native version, ledger/options/UUID or persisted format change in these packages. Whole-branch prior direct final retry/policy schema1/deployed retry1/generic submission3/MaxSnapshots64 and existing start/removal/recovery conclusions remain at exact-content boundaries. No transitional conversion/reset is introduced. D1/R1 closures and prior product/lifecycle assessments are retained without confirmation-only or unrelated re-audit.
Verified deployed Aac62 is an ancestor of finalA. B deployed7b8c is nonancestor; supported lineage continues through preserved exact patch/receipt provenance, not a literal merged-ancestry claim. The substantive runtime successor needs its own deployment and acceptance.

A README/reference TransportError/mutation-reconciliation and prompt contract remain applicable; the near-code no-write comment explains the local invariant. B forwarding/join/classification/overflow limits are documented with the private fixture/session evidence. No public error/UI/help copy changed; prior owning recovery docs remain unchanged.

## Limits/disposition

No reviewer tests/build/browser/native/CI/live-state/prompt/history query, source/tracking write, nested agent, claim, integration, deployment or lifecycle action. Source review supplies no operational/deletion/integration permission.
Prepared attempt10 guard hashb78705d14de89eeabe5c407b3204eb6c7bf4983994a6958ab3b2442c5a6247cf/output absence verified; it is not execution evidence. Actual32 browser cases/four complete manifests/zero unexpected failures and final package/native/composed/deployment gates remain unproved and lead-owned. Prior fork/pressure passes keep their original scope; historical CI failures remain unwaived. W/C stale e914 are excluded. All long/live execution remains subject to the lead's separate release.

Retain reviewer0 for relevant material followups.
Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/
