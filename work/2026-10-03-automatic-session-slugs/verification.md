# Release verification evidence

Current status (2026-10-04): this page preserves historical verification at the
exact revisions below. The fixed-profile source and managed-child fixture have
newer reviewed commits, but no new assembled candidate, managed VM execution or
deployment pass. See [state.md](state.md) and
[static-profile-native-observation.md](static-profile-native-observation.md)
for the current failed native gate and pending diagnostic-logging choice.

## Native observation fixture checkpoint

Provider local4651d764 adds bounded tool/SQLite metadata and the accepted
owned-probe/actual-question fixture corrections. Public helper/policy are
unchanged from reviewed d371a772. Parent full diff inspection, gofmt/whitespace,
and the owning Nix tagged pure `-race` selector passed11top-level groups/90tests
and subtests,0fail/skips,2.759s. Evidence:
`/tmp/automatic-session-slugs-native-observation-quick.jsonl`.
Retained reviewer0 completed the related four-lane assessment with no new
findings at turn01a1046d-9d61-7f80-995f-534b7b142c0f. See
[native-observation-review.md](native-observation-review.md).
Fresh catalog Luna/low utility `/root/native_observation_proof` completed one
authorized actual native diagnostic run at4651d764, retaining unchanged strict
assertions: exit1/20s. All35 recorded first/final deny samples were2->2, with
actual question cancellation and both designated preflight faults reached.
The mismatch now identifies native code-mode exec/wait wrappers, and SQLite
diagnostics identify logs_2.sqlite/table logs. FreshMCP and later gates remain
uncompleted. See[native-observation.md](native-observation.md). No publication.
Native diagnostic logging preference, final pins/resources, deployment and
retained live canaries remain pending.

## Earlier package and verification checkpoints

Status: earlier full package checks passed; fixed-file exact-head CI passed;
related independent review and native proof remain gated.
Deployment has not run. Feature branches remain unmerged.

Earlier fully checked package composition:

- codex-web `ca0f3bc980ca99454d000761aeee37b4b9bbafc3`.
- dev-workspace `42be6ee588f5770c4ed324c676b82758b932ba1e`, tree
  `6b4520e9307465e7077fcd3b30fe65eb6012c80b`.
- vpsfree-dev-workspace `2e3733ade1bac712f0b852d1960a681e5bca5076`.
- workspace `f5d30e291929bdf771f0d3842b84db1f08640131`.

[Related review](recovery-review.md) covers the complete cleaned histories,
final diffs, intended consumer pins and migration provenance. The final narrow
GET snapshot correction was directly inspected and verified under mandatory
review step9; all Important findings are resolved. Consolidation preserved
the checked final runtime tree exactly. No migrations or format changes were
added by the recovery corrections.

## Fixed instruction-file checkpoint, 2026-10-04

Current provider d371a7721819ddc7becbd41eabd0486664e1edcd and runtime
8acd722029f3c1d0abd8c2801b734a554a4a2eef are clean and published. The exact
nonempty instruction-file contract replaces the unsupported empty-file contract.
Quick provider12top-level/74test-and-subtest passes, tagged pure fixture5top/47passes
and adapter5top/12passes all completed with zero failures or skips. The adapter
also passed against the exact published dependency without a local replace.
Protocol coverage,55restriction schema checks, pin fixtures and the generated-hash
Go modules build passed. Vendor hash discovery used the intentional fake hash;
that expected build failure is recorded separately from the successful real-hash
build. No unexpected kernel build occurred.

Exact provider CI37162566014 and runtime CI37162928425 passed. The runtime fast
job took6m23s; its host job was skipped by the normal selector. The actual earlier
host VM remains separate evidence for unchanged host/module behavior. Logs:
`/tmp/automatic-session-slugs-fixed-file-{provider,fixture,adapter}-quick.jsonl`,
`/tmp/automatic-session-slugs-fixed-file-real-pin-quick.jsonl`, and
`/tmp/automatic-session-slugs-fixed-file-runtime-ci.json`.

The retained reviewer completed all lanes; the lead closed the three diagnostic
findings by direct inspection and7group/61case -race checks at local5f6c7e2.
The subsequent native run failed; see[native-fixed-file-observation.md](native-fixed-file-observation.md).
No deployment has launched. The older
package supplies the identical pinned Codex ELF for the next native run; its
installed provider resources are stale and must be refreshed before activation.

## Focused verification

All checks used owning Nix environments and explicit selectors:

- R1/R2 Go checkpoint:25top-level tests, no failures/skips, web2.364s, plus
  uploads.19pure preparation browser cases and five JS/CJS syntax checks passed.
- Post-snapshot Go checkpoint:22top-level tests, no failures/skips,2.561s,
  including two new groups/four leaf cases and shipped browser contracts.
- Portal/CLI/fork Ruby:16runs/223assertions, no failures/errors/skips.
- Final extension authority contract:2runs/149assertions, no failures/errors/
  skips; complete contract JSON equals the deployed predecessor.
- Final workspace deployment contract:4runs/19assertions, no failures/errors/
  skips.
- Packaged Git-warning control with synthetic author/committer identity:
  one archive-head test/20assertions, no failures/errors/skips. Full packaged
  Ruby evidence remains357runs/3759assertions with12skips; the focused result
  does not turn those into full-suite coverage.

Logs and commands are linked from [state.md](state.md). Pure contracts and
quick tests do not establish real browser or native Codex isolation.

## Packaged and CI checks

Fresh catalog watcher `/root/final_package_ci` owns full runtime, extension and
workspace flake checks, complete workspace default package and exact normal
CI runs37153598662/37153668457. Runtime host VM actually ran; it is separate
from the skipped feature-branch host CI job. All three flake checks and complete default build passed, exit 0 in 1202 s.
Built candidate: `/nix/store/a9z46ikp6w1gnm2hxx8fd4rbzsjc6ywj-dev-workspace-0.2.0`.
Both specified normal CI runs passed at the exact source heads; extension
devcluster-check also passed. No unexpected kernel compilation.
See [binary-identity.json](binary-identity.json) for actual assembled native
identity and original Luna metadata; the native isolation fixture is pending.

## Integration, activation and retained canaries

Two fresh catalog watchers stopped the batch before real isolation proof:

- `/root/final_integration`: firewall fixture rejected by nftables 1.1.7. The
  retained implementer corrected block separators only; parent nft --check,
  formatting and 12 tagged quick groups passed. Local test-only commit
  `13f85921bb8db2e0b04ebc2aa04f876ef3c079eb` is not yet folded or consumer-pinned.
- `/root/integration_nft_corrected`: firewall loaded, then ordinary control
  thread setup failed before the naming helper. The fixture omitted the
  underlying RPC error. Pinned-source null-to-TOML conversion suggests its nil
  environment is invalid; a bounded non-null control-map and diagnostic
  correction is assigned. This diagnosis remains subject to actual rerun.

Complete logs: `/tmp/automatic-session-slugs-final-integration.log` and
`/tmp/automatic-session-slugs-integration-nft-corrected.log`. No later race,
older-source compatibility or real-browser cases ran. No native isolation pass
is inferred from schema, mocks, compilation or these prerequisite failures.

Exact entry points and prerequisites are in
[verification-plan.md](verification-plan.md); prepared activation and recovery
contract are in [rollout.md](rollout.md). The canary script is syntax checked
only, and has issued no requests.

The control-map correction is local test-only commit
`4f20c94a662cc1ff84e2a152a53ff8a85afc7db0`; parent inspected the three-line diff,
formatted it and passed 12 tagged quick groups with no failures/skips. Fresh
catalog watcher `/root/integration_control_corrected` owns the next batch;
log `/tmp/automatic-session-slugs-integration-control-corrected.log`.

Third native attempt `/root/integration_control_corrected` stopped after 10 s,
exit 1: the ordinary thread started but made no Responses request in 5 s.
Source inspection found app-server disables environment API-key admission,
while the fixture supplied only an OPENAI_API_KEY environment value; it needs
a synthetic private API-key auth.json. Both inherited synthetic MCP servers
also lacked startup budgets; the pinned default is 30 s and the HTTP sentinel
is deliberately blocked by the firewall. The retained implementer owns these
fixture-only prerequisites and a bounded synthetic thread-read diagnostic.

The independent race/compatibility/real-browser portion is now assigned to a
fresh watcher `/root/runtime_release_integration`, while native fixture setup
is corrected. It uses unchanged production sources and owning environments,
log `/tmp/automatic-session-slugs-runtime-release-integration.log`. No pass is
inferred; all original native failures remain retained separately.

Private synthetic auth, 0.2 s MCP startup budgets and bounded diagnostic
thread reads are local test-only commit
`1a25313dccc3d6db0270418ed34b5580c1663b9e`. Parent inspected the exact diff,
confirmed the pinned-source contracts, formatted it and passed 12 tagged
quick groups with no failures/skips. No production behavior or isolation
assertion changed. Native proof awaits the separate utility slot.

The next native prerequisite attempt (`native_prerequisites_corrected`) still
stopped before inference: the synthetic ordinary turn remained inProgress,
thread/read succeeded and its error was null. Log
`/tmp/automatic-session-slugs-native-prerequisites-corrected.log`; no native
isolation is proven. The retained implementer now adds bounded synthetic
stderr/HTTP metadata and a positive permitted-endpoint probe to identify the
remaining setup gap without weakening isolation assertions.

Independent full race results: provider passed (476 test/subtest pass actions,
3 skips); runtime had 933 pass actions/2 skips and failed in
TestAssignmentSerializesWithMemberRemoval on the unchanged test client event
slice. Parent reproduced both race stacks on an exact git-archived baseline
924c0ec (including its original module files), focused exit 1;
`/tmp/automatic-session-slugs-baseline-member-race.log`. OS flock serializes
production operations but does not provide a Go-race-detector happens-before
for the fixture slice. A recording-only mutex is assigned; its send handshake
stays outside the mutex so the serialization assertion remains meaningful.

Older-source preparation fixture passed all three selected package invocations
(web writer, baseline upload reader/collector, new web recovery). Real Chromium
then stopped on a single-fetch versus observed transport-POST count (3 versus1)
after TCP reset; log `/tmp/automatic-session-slugs-release-compat-browser.log`.
A bounded browser fetch recorder will test the application submission count
while requiring all wire attempts to preserve exact body and identity.
Existing team-settings browser coverage is independently assigned to fresh
watcher `/root/release_team_browser`.

Existing team-settings Chromium test passed, actual selected leaf
TestQuestionBrowser/team_settings_browser_test.cjs, 26.89 s, no skips. Log
`/tmp/automatic-session-slugs-release-team-browser.log` includes self-signed
fixture TLS handshake errors; source explicitly uses ignoreHTTPSErrors and
the browser assertions and Go test passed. This is separate from live HTTPS,
which must validate through the installed CA after activation.

Bounded follow-up quick checks: 13 tagged provider groups (including diagnostic
bounds), no failures/skips; runtime member-removal race selector passed 10
repetitions (2.125 s); real-browser fixture syntax passed. Coordinator inspected
all diffs and committed test-only corrections. The production helper, policy,
runtime member operation lock and all browser request/identity protections are
unchanged. The send handshake is outside the fixture recording mutex.
Fresh watcher `/root/native_diagnostic_proof` now owns native proof with the
new bounded evidence; log `/tmp/automatic-session-slugs-native-diagnostic-proof.log`.

Local test checkpoint codex-web: `45869c3252e699d351cbdc03ba7d3bec61221e7f` (not yet published or final-pinned).

Local test checkpoint dev-workspace: `a025aab4a8e4adfb212de4cb2e06af3d96048f55` (not yet published or final-pinned).

Native diagnostic run (provider45869c3) identified12 actual WebSocket GET
upgrades rejected404; the positive permitted-provider firewall probe passed.
This pinned version enables WebSockets from provider capability/fallback state,
not retired feature flags. The architect's accepted source-based supplement
in design.md defines valid-upgrade426 to exercise its supported native HTTP
fallback, preserving builtin provider capabilities and original metadata.
Owning provider reference prose now labels HTTP/SSE coverage and requires a
positive unchanged-serving-transport model call. Successful WebSocket framing,
continuation caching, reconnects and hostile delivery over WebSockets remain
outside this fixture's coverage. The bounded transport correction will receive
independent review before native proof.

Full runtime race rerun at a025aab passed924 test/subtest actions,1 skip and no
failed packages; `/tmp/automatic-session-slugs-corrected-runtime-race.jsonl`.
Creation Chromium then passed the duplicate-fetch/immutable-wire-replay and R2
no-opener/retained-original/new-scope flows, before stopping on a legacy-draft
assertion that still expected old fixture catalogb after preceding cases changed
it tod. The implementer now freezes the external fixture catalog at scenario
start for that exact acknowledgement assertion. This changes test expectation
setup, not shipped browser behavior. Complete failure log retained at
`/tmp/automatic-session-slugs-corrected-runtime-race-browser.log`.

## Accepted native HTTP-fallback fixture checkpoint

Architect accepted genuine WebSocket upgrade426 with real POST evidence and
explicit HTTP/SSE coverage limits. Main reviewed all frozen edits and applied
visible-doc writing guidance. Quick14top/95test-and-subtest passes, no skips or
failures, recorded in /tmp/automatic-session-slugs-http-fallback-quick.jsonl;
browser syntax passed. Consolidated source heads8db6adfd/d05e7527 retain exact
checked trees4133363d/d81d7af7. New independent four-lane review is assigned before
native integration. No native/browser-final/deployment/live pass claimed.

Rechecked installed17publicGo files plus ephemeral_policy.json after consolidation: all18byte-equal current source. Native binary/model unchanged. Exact-head remaining native/browser batch prepared, not launched before review.

## Planned final package refresh scope

After native proof and exact consumer refresh, run provider full flake checks,
runtime all evaluated checks and every fast build, complete extension/workspace
checks and complete assembled package. Runtime host-module-idempotency actual
VM already passed on the unchanged production/host sources at packaged42/2e/f5.
Its expensive rerun is excluded for fixture/docs/hash-only refresh; this matches
the repository's ordinary CI selector and carries forward precisely that earlier
VM evidence, without claiming a VM run on later hash-only heads. Any production
host/runtime edit invalidates this reuse. Prepared script
/tmp/automatic-session-slugs-post-fixture-package.sh has exact-head/clean guards
and saves separate final artifacts; it has not run.

Related four-lane independent review completed by retained reviewer0 at turn
01a103e1-a466-7973-8588-a6805c54d8b2, actual gpt-6.1-sol/xhigh/read_only,
no override/fallback. No new findings. Explicit whole-history/no-migrations
conclusions and current-default workspace comparison qualification recorded
in fixture-review.md. Parent accepts the source gate and launches the prepared
actual native/creation Chromium batch once through a fresh Luna/low utility.
No native/release/deployment success is inferred from the source review.

## HTTP-fallback real inference, control eligibility failure

Fresh Luna watcher ran exact guarded8db/d05 batch once, exit1 about7s. Schema
and55restrictions passed; native1.57s inner/2.10s outer reached2accepted upgrades
and1decodedResponsesPOST, then GLOBAL_POLICY_SENTINEL control eligibility failed.
Native utility cases/final creation browser did not run. Complete log
/tmp/automatic-session-slugs-http-fallback-native-browser.log retained. Parent
assigned only test prerequisite diagnosis/evidence to retained implementer0;
no assertion relaxation, manually injected sentinels or helper change authorized.

## Final actual creation Chromium PASS

Fresh final_creation_browser Luna/low utility ran the exact guarded runtime
 d05e75270a9bed417d07e9be8bc082c906f6846a script once, exit0 about32s.
/tmp/automatic-session-slugs-final-creation-browser.log reports complete creation
browser acceptance: generated/custom names, immutable recovery, separate tab
scopes/no-opener, attachments/attachment-only, storage, progress and legacy plans/
receipts. This is actual Chromium153/rev1243 with pinned Playwright1.63.0,
not syntax or partial-scenario evidence. No serving instance/lifecycle action.
Native source-only eligibility diagnostic remains independent and pending.

Control fixture quick15top/105test-and-subtest passes0fail/skips; source-supported marker/exact native identity selection/bounded synthetic diagnostics committed and folded into provider 23d1aaa67574c849b933178400058f46d53ef3e1. Public sources unchanged; narrow related reviewer0 assessment requested before another native observation.

Control related independent review completed at23d1aaa6 by saved reviewer0 gpt-6.1-sol/xhigh/read_only, no new findings, all4affected lanes and coherent-history/no-migrations conclusions. Parent accepted the source gate and launches only actual native proof through a fresh Luna watcher; browser gate remains closed as passed.
# Latest native checkpoint: control passed, utility setup failed

The reviewed provider23d1aaa native-only run completed exit1 in about10s;
log `/tmp/automatic-session-slugs-control-native.log`. All eight ordinary
instruction/tool sentinels and exact Luna/low eligibility passed: two accepted
native upgrades and one decoded Responses POST. All36 utility leaves entered.
Most then failed with generic `ErrEphemeralServer` in approximately0.07s, before
utility inference. The preflight timeout leaves reached their deadlines and
also detected increased denied-egress counts. The log does not reveal the
native RPC error or establish which activity produced the denied packets.

Retained implementer0 was assigned bounded test-proxy diagnostics and exact
pinned-source setup diagnosis at turn01a1040d-efda-7c72-bf64-c4680864e139.
No isolation, transport, deadline or persistence assertion is relaxed. The
actual browser, race and compatibility passes remain applicable to unchanged
production sources. Deployment remains gated on successful native proof.
