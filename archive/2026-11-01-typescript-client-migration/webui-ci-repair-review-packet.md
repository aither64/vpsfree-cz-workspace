# Committed CI repair review

Session: 2026-11-01-typescript-client-migration.
Repository: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-typescript-client-migration/vpsadmin-webui.
Branch: dev/typescript-client-migration; PR126 remains at the published checkpoint.

Complete range: `63d484fc070dbee633d32624de545e834d483701..4279c2384c2a9e74fd11f6b41e4a33686edeab23`.
Affected delta: reviewed/published `14cfdcb6d2a3bc337fd445932fd38916b3dcd9ab..4279c2384c2a9e74fd11f6b41e4a33686edeab23`.
Final tree: `d37a454e2bb996a61d7ccc0b6811429da0e6d489`; index/worktree clean.

Retain reviewer0's saved Astra/xhigh/read_only settings. Overall migration risk
remains HIGH because authentication, authorization and uncertain destructive
writes are in the supported contract. Apply all four lanes to the affected test
and metadata delta: general/history, architecture, scope, risk/compatibility.
Read the current mandatory-change-review skill and all four references. Perform
the review directly; no nested reviewers, source/Git mutations or checks.

## Requested outcome and scope

The user authorized full generated SDK migration and temporary unpublished SDK
consumption. Prior source and final-history reviews remain in
webui-final-review-result.md, webui-packaging-review-result.md,
webui-readiness-review-result.md and webui-final-history-review-result.md.
This packet requests independent assessment of the completed CI repair delta
and the resulting whole-series history. Reuse unaffected source conclusions;
do not repeat the 440-file source audit without a concrete discrepancy.

Core CI41366168908 passed at14cfd. Broader Playwright run41366168907/attempt1
timed out at native40minutes in all three jobs after real assertions. Full logs
contain32/35/42 observed case headings across30specs, not terminal suite totals.
See w-final-ci-diagnosis.md and ci-41366168907-diagnosis/test-failure-summary.json.
All exact-run artifacts were retained and API-digest verified; no rerun was used
as diagnosis. Unknown passed/skipped/unrun totals remain unknown.

Architect-owned design.md section "Broader CI browser repair after the published
migration" defines six disjoint owner packages. Every observed path is assigned
once. Original traces establish explicit leaf fixture or assertion defects;
cluster summary is explicitly source plus native-log evidence, with no claimed
original HTTP trace. No valid payload rejected by the product was demonstrated.

The repair changes only30E2E specs and two E2E coverage metadata files:
32files,+251/-234. Product src/bff/public, fixtures/helpers, runners, workflows,
browser configuration, dependency manifests/locks, vendor archive/provenance,
Nix packages/checkers and integration inputs have no delta from14cfd.
No default normalizer, output decoder, permissive guard, SDK/runtime/API repin,
test skip, timeout increase, new browser or new framework was introduced.

## Contracts and assertions to assess

- Success handlers use generated resource namespaces, included resource objects,
  numeric account identity/level and declared boolean/string values. Empty output
  objects remain empty; existing receipt metadata is retained without inventing
  asynchronous receipts for synchronous actions.
- News fixtures supply the scenario's localized message while preserving cs/en
  editor fields. Income uses payment_stat and instructions use user.instructions.
  Transaction JSON content is supplied in the declared string form.
- Request eligibility fixtures explicitly provide enabled/supported templates
  and the lookup routes needed to reach the intended submit/preflight boundary.
  Stale-preflight, server rejection, uncertain outcome and zero-write tests keep
  their original intent and counts.
- Mail-log queries compare the exact complete pair multiset independent of order;
  duplicates and unexpected pairs still fail. Reminder clear asserts the accepted
  expiration-only setter and faithfully emulates its reminder reset. Populated
  paid_until clear remains refused without dispatch.
- Missing-action-state negative fixtures retain absent receipts inside valid
  resource framing; explicit transport aborts and malformed/rejected branches
  remain negative. No replay, identity, permission, retry, frozen intent, receipt,
  exact write count and touch geometry assertions are to be relaxed.
- Centered-dialog scenarios retain all27routes:26supported Advanced dialogs and
  one current user-data template editor. The removed user-data Advanced control
  is replaced by inline format/clear URL assertions and editor centering/open/close.
  Four observed cluster routes get explicit empty namespaced collection replies.

## Commits, provenance and history

The original nine reviewed migration commits remain intact and published.
Repository AGENTS.md forbids rewriting published history without exact user
authorization; none was given. These six ordinary logical correction commits
preserve14cfd ancestry and replace no implementation or dependency candidate:

1. 1cf3a95ef89c984e18691baa27e7567723e9f6bb — C5 users, five specs.
2. 814930f4a6c65f972ced3bf37c4d474602d89f12 — C7 finance/content, five specs.
3. 479cf605f9c8b7ec1db5beb7fa0d022a5cbb6216 — C4 network/DNS, five specs.
4. dba717baca940580a9076e16490c7f481501ae77 — C3 VPS/storage, eight specs.
5. 77fb7d24db190c31f58e2eaff76863aaec7737ad — C6 infrastructure, six specs.
6. 4279c2384c2a9e74fd11f6b41e4a33686edeab23 — CW centered dialogs and strict adoption.

Complete series has15commits,469files,+14154/-9520. The prior nine owner split,
original34-commit fold proofs and their independent conclusions remain retained;
this patch does not claim global equivalence to pre-remedy aef. Full messages,
authors/dates and paths are in webui-ci-repair-series.txt,
webui-ci-repair.paths and webui-ci-repair-full.diffstat. Six follow-ups are
coherent post-publication fixes rather than another SDK pin stream. Assess that
history conclusion independently against repository instructions.

There is still exactly one SDK archive/manifest/lock/provenance/Nix support
stream. SDK99ee0665, generator eea3ae5e, HaveAPI0.32.0 and frozen API610a96 remain.
No DB/schema/persisted-format migrations, intermediate consumed state boundary,
default integration, release, SDK publication or deployment occurred.

## Quick checks and documentation

Each owner passed scoped pinned-Nix ESLint and strict TypeScript rooted in its
assigned spec files/imports with unchanged repository E2E options, plus diff checks.
C4 fixed four actual strict diagnostics without casts or guard weakening.
W formatted its three paths. Parent combined gate passed exit0:
`nix develop -c npm run typecheck:e2e:core`,118checked/164deferred, zero diagnostics.
Fourteen edited deferred specs are adopted completely; the original baseline
SHA2567bdc6a363a2706be14533e05712bda641aa709ce2413a4bd68ebe427ecec3317 and
sourceRevision remain unchanged. No deferred hash/cap refresh hides errors.

webui-ci-repair-strict.log records the combined check on settled source bytes
subsequently committed unchanged. webui-ci-repair-acceptance.json and owner commit
receipts bind final paths/blobs/hashes and foreign-byte preservation.
See c5-ci-repair-evidence.json, c5-ci-repair-commit-receipt.json,
ci-repair-commit-proofs/, w-ci-e2e-adoption-source-manifest.json and
w-ci-repair-commit-receipt.json. The lead independently inspected the affected
diff, final clean state, complete ancestry and protected-path zero delta.

No product behavior, UI prose or KB change is introduced; existing project
contracts remain applicable. Current repair decisions and evidence belong in
design.md/state.md/backlog.md and linked CI records. W's later dated work-log
append will record actual outcomes only, after browser results, rather than
inventing new feature contracts or anticipating a pass.

## Remaining verification and acceptance

No browser or CI rerun has started on4279. After review clearance: first the two
dashboard news locale cases, then existing representative and originally observed
cases with retries0/max-failures1, preserving touch-only cases in mobile-chrome.
The actual WebKit project remains CI acceptance; local Chromium does not certify
WebKit. Use the retained durable per-operation PID/exit capture and native process
effects proof. Do not relaunch an operation to recover an observation handle.

Earlier A124/B8, API23/cleanup and literal14cfd five-output Nix results retain
their exact source/input scope. New final-head package/provenance and complete CI
remain pending; source equality is not derivation equality. Historical API2
deletion remains externally unconfirmed. No merge/deployment/lifecycle action is
authorized by this review.

Return findings by severity or no findings; explicitly assess the affected
contract/negative coverage, strict adoption, proportionality, published-history
boundary, repeated-input stream and no-migration lineage. Record the report in
webui-ci-repair-review-result.md and report to lead. State residual test limits.
