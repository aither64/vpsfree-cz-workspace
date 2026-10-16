# Independent final runtime review

Reviewer: retained `reviewer0`, GPT-6.1 Sol/xhigh/read_only, all four mandatory
lanes, no nested agents or source edits. Exact range:
`ba8669b14536f72b559abc912bba8eac430111e4` ->
`a7000a2ae803c21274eb65d23ee63d2097fb8829`. Completed committed-deliverable
review before long integration. Report delivered to lead, saved here by lead.

Amended reviewer report supersedes the initial report. No Blocking findings.
Four Important and two Advisory findings:

1. **Important, general/risk:** `static/session-attention.js:56` adopts any new
   API identity and immediately acknowledges/publishes presence from the retained
   old document. Bind to rendered observation identity and root; mismatch must
   stop ack/presence/settings and require reload. Reviewer reproduced actual
   module in read-only Node VM. Cover same-root replaced directory and new root.
2. **Important, general/risk:** `attention.go:64` clears a committed unread done
   event after observer gap >90 seconds, even if exact identity and completed turn
   remain relevant. Preserve known current events across downtime without creating
   notifications for completions first discovered after a gap. Test restart beyond
   90 seconds and both delivery TTLs; existing continuous TTL test was insufficient.
3. **Important, general/architecture:** `notifications.go:109` capacity check
   before assigning existing delivery key prevents coalescing at 512 entries.
   Cleanup then removes old delivery after emission is consumed. Prune irrelevant
   work before admission and permit existing-key replacement at capacity. Test
   new input replacing completion in a full outbox.
4. **Important, general/history:** dependency-only commit `0bddd694` changes
   vendorHash to the final feature tree's closure before it introduces webpush
   imports. Ordinary go mod vendor follows imports, so cached final output can
   conceal an unbuildable intermediate boundary. Verify each source closure/hash
   or combine inseparable module/import/hash changes with documented rationale.
5. **Advisory, general/risk:** `browser-notifications.js:19` disables Disable when
   local subscription exists but registration ID was lost. A lost /register reply
   can leave delivery active with no disable/recovery action. Reflect incomplete
   local subscription and allow explicit unsubscribe/removal recovery. Reviewer
   reproduced actual module with rejected registration response.
6. **Advisory, architecture/general:** `notification-worker.js:8` accepts only
   `[a-z]+[0-9]+` member routes, narrower than supported digit-containing roles.
   `gpt6reviewer0` receives fallback instead of member link. Match bounded roster
   grammar and cover representative address. Actual worker reproduction confirmed.

Lead disposition: fix all six as narrow corrections inside accepted contracts;
delegate source to implementer, focused verification by lead. No new design or
scope expansion intended, so no automatic full review rerun. Reassess if fixes
expand behavior beyond these recommendations. Fold fixes into owning unmerged
feature commit before publication. Consolidate the original dependency and
feature commits because Nix vendoring follows imports: module/import/vendorHash
are one inseparable packaged feature boundary. Nothing published/deployed or
externally consumed. Final composition/history review will confirm new series.

## History and compatibility conclusions

Complete own series exactly dependency `0bddd69473c1c18d7574fa195215910e680484e0`
then coherent interdependent feature/docs/tests
`a7000a2ae803c21274eb65d23ee63d2097fb8829`. Merge base and final diff match packet;
diff SHA256 `0bec427d96d8c506216a73c1c2c8ced445f5c4a0936a6960d8aa1a061a772279`.
Worktree clean during review. No obsolete approach/fixup series/transitional
schema/repeated update streams. The amended report identifies the dependency
source/hash boundary requiring correction or independent verification; no
redundant update commits otherwise require consolidation.

No database, lifecycle, roster or runtime-contract migrations. Private schema1 is
initial, no predecessor/conversion. Optional strict boolean preserves omitted old
receipt serialization/digest and explicit false. Both Ruby readers and Go accept
omitted/true/false, reject malformed; unfinished creation fences preserved.
Predecessor rejection of new flagged receipts is documented paired-generation,
forward-only recovery. Unmerged/unpublished/unreleased/undeployed/unconsumed.

Upstream sensitive behavior preserved. Observation identity semantics support mute
preservation on moves and reset on replacement; finding 1 is browser enforcement.
dev-workspace owns policy, pinned codex-web stable identities suffice, no shared
library change. Reviewer inspected exact dependency, observer, authenticated
nginx/router topology and reservation holder projection. Final generated workspace
and configuration pins remain outside this runtime gate and need history review.

## Evidence and remaining verification

Reviewer read instructions, packet, complete history/diff/source/tests/docs and
ran three read-only Node reproductions using declared Node 24.19.0. Quick suite
PASS comes from lead/member packet; no long tests, network push or deployment.
Endpoint allowlist/literal dial/TLS/origin/key/private persistence/failure fencing
and no authenticated worker caches fit selected remote trust boundary. Mutex/body
concern was not demonstrated remote exploit: nginx buffers bodies and app listens
on private Unix socket; no local-operator hardening expansion requested.

After fixes: packaged suite, real template/CSP/worker integration, actual browser
subscription/background/click display proof; distinguish synthetic/provider
acceptance from macOS OS display. Full creation/sensitive and old receipt fixtures
must remain covered. No merge/deployment readiness or lifecycle completion claimed.

Original complete report arrived in this conversation as reviewer0 final review;
this durable record preserves findings, evidence, conclusions and lead decisions.

## Narrow remedies verified by lead

Frozen replacement head e91f22f7bc027245f6efbea9b87c907461d7ecb0 directly
parents ba8669b14536f72b559abc912bba8eac430111e4. Clean worktree. One logical
feature commit includes source imports, module graph and vendorHash, explicitly
explaining the inseparable Nix vendor closure. Original two unpublished commits
are superseded. All six findings fixed inside their reviewed boundary.

Lead directly inspected a7000a2..e91f22f (12 files, 316 additions/74 deletions):
rendered identity+root checks precede storage/ACK/presence/settings and stop on
mismatch; known exact relevant events survive downtime without new replay;
baselines/pruning precede bounded outbox admission; local subscription recovery
uses the existing idempotent register and disable endpoints; worker roles include
digits with bounds. Main-agent copy pass applied to affected docs and UI text.
No new design, public API or private schema was introduced by remediation.
Mandatory-review narrow-fix policy applies; no automatic reviewer confirmation.

Lead verification at exact consolidated head: focused Go restart-gap/full-outbox/
push-expiry tests PASS0.092s; nine actual-module Node contracts PASS68ms; diff
checks PASS. Implementer reran all attention/notifications Go tests PASS0.395s
and changed JS syntax. Forced final tracked-tree vendoring again yielded
sha256-iyydGWryLmh8P+YxQcQ2SqGIj1Lds+WBDgsKQV4uFqA= (expected mismatch
exit1, vendor-hash-consolidated.log/.status). No migration/state lineage change.
Long runtime integration now authorized; source publication and mechanical
composition follow. Final composition/history conclusion remains required.

Test-only integration correction: e91f22f..e414ed3 changes two stale test
expectations (asset version and default fork preference), no product behavior.
Lead inspected patch and ran exact two affected Go tests PASS1.222s. Broader
member quick suite PASS44.017s. Same single feature commit amended, not a new
follow-up commit. No new review lane or design boundary introduced.
