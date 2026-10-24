# Presentation milestone final-review packet

Status: RELEASED for final independent presentation review. Both owners completed
their intended presentation deliverables, committed and passed quick checks.

Session: 2026-10-22-codex-thread-retries. Workspace:
/home/aither/workspace/ai/vpsfree.cz. Owners are implementer0 (A codex-web) and
implementer1 (B dev-workspace). Architect0 owns the accepted UI successor section
in ../design.md. Lead owns acceptance and copy. Retained reviewer0 is the intended
independent reviewer, Sol/xhigh/read_only, subject to fresh roster verification.

## Requested outcome

Review the completed presentation slice: optional generic activity API and notice,
Session Settings switches, stable footer inside the actual transcript viewport,
and real-template controlled browser fixtures. The durable session-policy backend,
controller and deployment guards are later work. Production must not advertise
working policy/actions until their actual capability/provider exists. Fixture
responses must not be mistaken for delivery evidence.

Accepted UI behavior and screenshot cases are in acceptance.md. Inspect actual
consumers rather than only the generic module. Both full and incremental message
renderers must preserve the footer, scroll position and composer. Validate token
input boundaries, stale action handling, concurrent refresh/destruction, local
dismissal identity/reload/newchain behavior and honest partial/unknown metrics.
Terminal elapsed freezes; active execution remains visible. Idle is zero height.

## Scope and source identities

Worktrees beneath /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries:

| Repository | Historical feature base | Deployed baseline | Final head/tree |
| --- | --- | --- | --- |
| codex-web | ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5 | ac62eeeb9d8b1fa7b8ed8fb95ba8160acb7efa1c | f86290673d752c77b56c70228c3d26aced75e177 / 0ed8092438d2f0a70838828573bbfd187b73393f |
| dev-workspace | bf6d4b0c49600c15e17fe71248807ef43424e932 | 7b8c646974df72e0df3e576d10f09d79823ae004 | 39497062e0da98a70386355384fa922c0eaa0168 / 28a9d72044dc3ffa7eb4f817cbb2c4d6c9614d18 |

Both worktrees are clean; lead SSH reads matched exact published feature heads.
Owner full inventories/diffs/remote proof are under ../ui-a/ and this directory's
b-*. Final A selection in B is one update stream including Go/Nix/vendor metadata.
Lead inspected the full lists, final delta scope and whitespace. Reviewer must
independently assess the complete histories, deployed lineage and migrations.

B full eight-commit series: original7262c24e,b3c7187c,aafaf419; sole A pin67b354e8;
retention6dba4c39,plan6435f157,runtimewaitb8967dfe; presentation39497062. Full messages
are b-final-history.json. b-lineage-proof.json binds old/new patch IDs, exact
deployed preserved ref and five-path-only preparation difference. Final candidate
tree equals preconsolidation tested tree. Range diffs: b-consolidation-range-diff.txt
and b-deployed-final-range-diff.txt; final/deployed bundles verified. Deployed7b8c
is preserved source evidence, not a literal ancestor of final reconstructed B.
No product-equivalence claim for the substantive presentation successor.

B deployed-to-final has fourteen paths: five A selection metadata files; two
guides; app.js,style.css,session.html; question/retry activity browser fixtures;
server_test.go module-copy list; one stale paging source assertion. No server,
managed-client, controller, policy/sidecar or lock implementation delta.
Final vendor hash sha256-x0Qrgfvcn74v0E6zJ7JKgwBnOGuJNUNTZQz0JdFIqcU=.
B final packet b-final.json SHA256
977f30c6f55b40c5074eeb96e7f5aafdad9ed30c4380e86e5d42ffaed76a04cd.
Its final source is /nix/store/945qwb93ggqnwgrrdlgg0pkwwrmphdv3-source,
NAR sha256-q05iiwXXkcIyD1zStXof4+fkItIFpyBhJK3DBz8VC48=. Owner compared all561
tracked blobs/modes to the commit. Capture script checks frozen B head and clean
source before execution. New UI source is frozen pending this review.
Exact commands and owner handoff: quick-commands.md and b-review-handoff.md.

A's full series retains df00fa36,6c828759,c1f415ad,ac62eeeb unchanged and appends
one optional activity successor f8629067. Ten successor paths: README, reference,
flake Node list, handler, retry_activity.go/test, conversation.js/css,
retry_activity.js and its Node contract. No codex/ or native/ledger delta.
Source NAR sha256-jOEXFTr55N88YbPakjlMw/7wsH8ZKr51Ag+Z1QaM25A=,
Go v0.0.0-20261023192737-f86290673d75,
sum h1:5iVFEW9ghXtccbfhFB2swLC+UqZYIqEPaRfNOh1bsMM=.
Owner complete packet ../ui-a/final.json SHA256
6672e61c99c62de3f38b882a57310303c45b3cb25e10edff508f45dabd8fd6e1.
Full history/diffs are ../ui-a/base-to-final.history and .diff, and deployed-to-final
counterparts; source identity and verified bundles are linked in the packet.
Tested tree equals final tree. Final all-conversation Go0.106s, retry race1.119s,
Node102PASS/0fail/0skip. Lead inspected recorded exits and exact SSH feature ref.

## Compatibility and provenance

Preserve deployed retry schema1/native ledger3 and all original IDs/options.
No native Codex changes or upgrade. No new policy sidecar in this presentation
milestone. Existing RetryProvider remains source-compatible for other embeddings;
new activity capability is optional. Fixture-only backend responses are explicit.

Previous complete source/history reviews live in
../incident2-prepared-plan/review.md and review-downstream.md. Deployed c1f/ed2 and
older W/C sources remain in exact bundles/rollout records. They are not described
as literal ancestors after earlier accepted consolidation. The incident2 and
ed2 behavior must survive: receipt-first plan recovery, exact prepared distinction,
bounded runtime wait/fresh revalidation, protected provenance and >64 replay.

Inventory migrations explicitly. Expected: no database migration, native protocol
change, ledger rewrite or retry schema change. Browser-local dismissal is new
presentation persistence. Check actual final source rather than relying on this
expected inventory. Whole-branch history conclusions remain required.

## Quick-check correction provenance

B's initial focused Go/fixture compile passed17.074s and read-cycle Node17 cases
passed. Owner identified two auxiliary command/assertion issues: the browser
contract script requires its serverURL harness, and the paging source assertion
expected an older callback than deployed7b8c's stronger read-cycle/identity gate.
Inspect the bounded assertion correction and final supported harness results;
no production gate may be weakened to satisfy that check. Original failure logs
remain in the owner evidence. Final receipt paths are pending.

B corrected quick checks passed: syntax, paging contract, read-cycle17 tests and
actual TestShippedBrowserClientMatchesSessionAPI (0.99s). QuestionBrowser fixture
compiled; execution was deliberately skipped pending this review. A focused Go
and new+legacy retry Node checks passed (exit0,14.446s/11.141s; Node16/0fail/0skip),
receipts at ../ui-a/go-retry-activity.* and node-retry-activity.*. Exact tested-tree
bindings for A are in its final packet. B final quick log b-final-quick.log passes
actual shipped-browser HTTP and incident2 PlanDelivery/EXwait cases5.965s; compile
all browser fixture source0.042s, syntax/paging/read-cycle17PASS in b-final-syntax.log.
No actual Playwright run yet. b-presentation-boundary.json links earlier checks.

Capture is not yet run. B supplies a focused TestQuestionBrowser subtest using
the actual httptest template/CSP/assets, with controlled API responses and fixed
time. Only retry_activity_browser_test.cjs is selected; no full unrelated browser
campaign. Lead will release this after committed quickchecked review through one
fresh Luna/low watcher. Exact final command and output paths remain pending.

## Review lanes and limits

Risk: high for cross-project API, browser persistence and mixed-version behavior.
Assign general, architecture/repetition, scope/proportionality and risk/compatibility
lanes to the same independent reviewer. Read mandatory-change-review/SKILL.md and
all four lane references, plus actual repository AGENTS and applicable procedures.
No nested agents or edits; no tests/builds/native/live state/claims/deployment.

Report findings with severity and source references; explicitly conclude on full
history consolidation, update streams and migration lineage. This review certifies
the presentation deliverable only. Later completed backend and final composition
require their applicable final review. No integration, deployment, release or
lifecycle authorization follows from this packet.
