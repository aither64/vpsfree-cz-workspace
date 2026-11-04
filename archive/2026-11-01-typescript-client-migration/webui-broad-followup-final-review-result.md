Important — R670-B1: the repaired action-state fixture still asserts a member response that the API does not provide, and relies on an undeclared result field.

Lanes: general; risk/compatibility. Owning commit e938939bc7c7dcf0893cb6f8dcee354746c1e8ca, retained at frozen final ebfdc1e320a80a1a08380ce0fd80b75b25c4baf1.
References: e2e/specs/app/action_state_detail_page.spec.ts:56–60, :98–109, :131–133 and :170; API942c6eaed41331f823d8e0f670ed239e2b308440 api/lib/vpsadmin/api/resources/transaction.rb:44–48 and :79–83; selected installed client0.4 dist/generated/resources/transaction/actions/index.d.ts:13–33.

The role loop serves the same transaction to level1 member and level99 administrator, including user/type/priority/input/output, and then requires dataset input, worker and mounted text in both views. The actual API blacklists user/type/urgent/priority/input/output for non-admins. The generated Transaction output also has no result field; mounted is supplied only by invented result:{mounted:true}. Stringifying input/output removes the original reader failure but leaves these false wire/role assumptions. The member deep-reload fixture also supplies forbidden input. A mocked broad pass could therefore be reported as canonical member verification even though the real member response cannot satisfy those assertions. This is an inherited assumption within the expressly repaired and newly strict-adopted leaf, not a demonstrated production authorization defect.

Smallest remedy: keep the member and admin cases, shape their responses according to their actual roles, retain rich input/output/user assertions in the administrator case, and assert member expansion/navigation with supported fields plus absence of privileged payloads. Preserve the mounted/content intent using declared administrator output rather than result. Keep the deep-reload member response canonical. Do not weaken production readers, change backend policy, or turn the member case into another administrator case. Focused inspection/checks can confirm that direct fixture-only remedy under skill step9.

No Blocking findings and no additional Important or Advisory findings supported by this review. R670-B1 must be fixed or explicitly dispositioned under the mandatory-review policy before long verification is released. This report does not grant merge, deployment or lifecycle approval.

Please persist the complete report as work/2026-11-01-typescript-client-migration/webui-broad-followup-final-review-result.md. Reviewer access remains read_only; no report file was written by me.

Identity, scope and evidence

Verified dev-session current = 2026-11-01-typescript-client-migration in /home/aither/workspace/ai/vpsfree.cz. Both DEV_SESSION_SLUG and DEV_SESSION_WORKSPACE are absent, consistent with the trusted thread binding. Same-session live roster61 identifies ready review-purpose reviewer0, gpt-6-astra/xhigh/read_only, thread01a19801-c630-7971-b7b9-cc178b6ced88. Settings retained; no override, fallback, nested reviewer or source authorship.

Read mandatory-change-review and all four references directly, current WebUI AGENTS and applicable workspace guidance, accepted design.md:2002 onward, localization procedure/resolved terminology, owning workflow/API/package contracts and relevant KB workflow. All four lanes performed directly at HIGH overall risk: unintended clearing of persisted notes, role-dependent API evidence, uncertain writes and premerge CI execution.

Reviewed the complete ordinary follow-up:
  base670cf286daf9bddb65594035507ca112a9e6d397
  head ebfdc1e320a80a1a08380ce0fd80b75b25c4baf1
  tree c53eb2197a2fdb845b972b11baf4bee311069669
Canonical session WebUI worktree; seven commits, 27 modified paths, +1149/-445. HEAD/tree and clean index/worktree remained exact at final inspection.

Packet SHA256 fca3bc187a10c8233ae020b6330a1b706d3b28a6042fbf22edc52d7deeae4f22, commit receipt3b2414255f6989344cc79b7154f62678c19e8bfc06ccd2cecb4335a676770fa3, seriesc2b4bd46a391fa806e75e796d5b97b69d273eb5b906b5f6cd85c90ae6137ba2b and committed-bindingsb05fec7d3f92c1a231f93fca44d418bf202e486c06c611250b78effc547341cc match the supplied values. Independently compared all2595 committed blobs/modes/SHA256 and live bytes with the final binding inventory: no mismatch. Actual seven raw commit objects and pathsets match the series receipt.

The full tracked pathset is unchanged. The explicit production selector yields1140 paths at this boundary; this is not evidence of a new file versus an older1139 census. The production delta is precisely Form/Panel plus EN/CS catalogs. All74 API production files and package/lock/flake/BFF/Nix package inputs are unchanged. I retained the completed670 review and R040 acceptance for unchanged source rather than repeating its unrelated517-path audit.

General/correctness and negative-path assessment

The product fix matches the original failure. Independently opened the retained advisory retry0 trace in memory: the individual501 update returned its English note, then bulk501/502 sent both notes null and received null notes. The fixture really cleared them; treating that as a mock-normalization problem would be incorrect. All99 retained context/trace SHA256 values match the local archives, with33 original project cases across12 files and the diagnosis's retained causal matches. These are historical670 failures, not executions of this final candidate.

SecurityAdvisoryNodeForm.tsx:58–63 validates supported language codes before omission. An absent map keeps the ordinary editor comparison; a present map requires explicit true for each language. Selected nonblank text is trimmed; selected blank becomes null; unchecked languages are omitted. The map is initialized only on successful bulk open at SecurityAdvisoryNodesPanel.tsx:187. No second payload implementation was added.

Rendered controls at Form:193–217 use the existing labeled Checkbox and Textarea. Language codes are visible and in their accessible names; the localized explanatory text states preservation and clearing. Unchecked textareas are disabled, focus does not select, and unchecking retains the draft while cancelling its write. Cancel/reopen resets through openBulk; confirmation cancel keeps current form choices. Ordinary editor presentation remains checkbox-free.

runBulk at Panel:193–239 captures the parsed payload once, preserves active-node targeting and captured statuses, increments revisions sequentially and performs bracketed readbacks. Control changes during an awaited write cannot alter the remaining payload. Existing failure/progress/writeBlocked behavior is unchanged. The tests cover untouched omission, both locales, independent clear/set, whitespace, uncheck/recheck, confirmation cancellation, bulk reopen, existing/missing row Update/Create, sequential guards, in-flight payload capture and retained no-replay after failed readback. Helpers preserve unsupported-language refusal and ordinary-editor unchanged/set/clear behavior.

The advisory browser edit changes only three expected_state assertions. Exact body/count/revision and both later stored-note assertions remain (security_advisories_admin.spec.ts:408–440), as do retired-node exclusion and subsequent publication/update/outage/negative paths. This is meaningful preservation, not acceptance of null loss.

Other inspected fixture corrections are proportionate to observed failures or necessary subsequent declared response contracts:
- dataset/snapshot/DNS/export Show and mutation namespaces, resource relations, explicit idle preflights, resolver-null inheritance and VPS empty output receipts;
- actual manual rollback reconciliation with typed snapshot200 and a fresh busy refusal, keeping the operation count at one and retaining readback/lock assertions;
- supported OS-family filter while preserving editor enabled/supported bodies;
- canonical node/status/transaction frames and full outage lookup-user levels; later entity fields/Delete frames match their readers;
- authenticated eligible approval templates/locations; explicit queue opt-out in the list-return case; successful WebAuthn Delete namespace.
No assertion removal, timing/cap relaxation or shared fixture normalizer was introduced. The request leaf's substantive changes match its retained minimal patch; the larger diff is formatting. R670-B1 is the exception to accepting the transaction fixture contract.

CI/workflow assessment

The actual broad workflow adds pull_request and branch push '**', preserving workflow_dispatch and branch-only push selection. Two matrix projects/scripts, 45-minute job limit, fail-fast:false, contents:read, per-ref cancellation, artifact names/paths and14-day retention remain unchanged. No secret or privileged PR execution path is introduced; no pull_request_target trigger appears. PR and branch runs are separate refs, so the retained concurrency policy does not combine those two events.

The first commit updates setup-node7.0.0→7.1.0 and upload-artifact7.0.1→7.0.2 once. Inspected retained official release/action declarations support compatibility: node24 runtime retained, configured Node file/npm cache inputs remain supported, upload action interface retained. No reviewer network query was made. The second commit separately changes triggers and documents them. This makes broad results available before merge; it does not itself establish a passing broad run or branch-protection requirement.

Strict coverage

Actual JSON comparison confirms152 adopted/131 deferred, exactly nine additions/removals, original sourceRevisionabab859d94a3f364d2bb719fa09f00749fd69ef9 retained, compiler options and other tsconfig keys unchanged. All131 surviving deferral values, raw records and order are unchanged. The original baseline remains outside the changed pathset. All12 edited leaves are in the strict selection. Compilation cannot validate mocked role/envelope semantics, as R670-B1 demonstrates.

Architecture and scope conclusions

Ownership remains local: optional bulk intent in the existing form values, one serializer, existing UI controls and existing generated API adapters. There is no new transport, recovery framework, global abstraction, endpoint registry, provider/backend logic or runtime/paging change. Current captured guards/snapshots/no-replay contracts remain the owning boundaries.

The user requested observed broad repairs and premerge broad coverage. The delivered groups address those outcomes. Whole-leaf formatting accounts for substantial line churn; it does not establish another behavioral subsystem. Delivered workflow/fixture/strict/product milestones and bounded working-source verification support the current final-review phase. No scope expansion or history-only reason to delay this bounded review was found.

Complete history/consolidation conclusion

Actual full series, all single-parent ordinary descendants of integrated670:
1. 9fd6d575 — compatible broad workflow action refresh.
2. e615538c — PR/all-branch broad triggers and owning docs.
3. 96b02de8 — storage/DNS/export/focus/VPS fixture contracts and rollback reconciliation interaction.
4. e938939b — OS-template/node/outage/action-state fixtures; contains R670-B1.
5. 2e36503b — request approval/queue and WebAuthn fixtures.
6. e053e855 — nine whole-leaf strict adoptions.
7. ebfdc1e3 — explicit bulk-note intent, active tests/catalogs/contracts and evidence.

These are distinct reviewable purposes, not a superseded implementation/fixup chain. Adoption precedes the product documentation's152/131 statement. No obsolete unmerged alternatives or transitional framework remains. Preserve already integrated670 history. If R670-B1 is remedied, keep the original reviewed object/report and apply the lead's ordinary narrow-fix/history policy; this review does not authorize rewriting published/default history.

Explicit input-stream conclusion: no SDK/runtime/npm/flake/archive/frontend/BFF hash update in this follow-up. There is one compatible workflow action refresh stage, each selected action updated once, and a distinct trigger-policy stage. No repeated dependency or channel stream requires consolidation.

Explicit migration conclusion: no DB, schema or persisted-format migrations anywhere in the complete seven-commit range. The change alters whether existing optional note fields are omitted or explicitly cleared; it introduces no storage format. Backend guarded revision schema remains pre-existing provenance, not a migration in this branch.

Documentation, locales and compatibility limits

REQ055 and WORKFLOWS explain explicit selection, omission, trimming, clearing and cancellation semantics; dated work-log entries distinguish prepared source/quick results from pending review/browser/integration. CI docs describe the actual triggers. EN/CS keys/placeholders and wording follow the inspected own locka65 terminology; site942c has distinct source identity despite matching guide bytes. No new route/API inventory was required.

The retained canonical KBf977 assessment accurately identifies a legacy PHP/API942c contract with no registered React advisory control/page/capture binding. It cannot certify this React modal, unregistered live prose or existing bitmaps. No mapped KB update was established; actual EN/CS desktop/mobile synthetic captures remain required after review. This is a recorded coverage limit, not authorization for a KB publication campaign.

Generated client0.4/HaveAPI0.32 and guarded-backend822/equivalent requirements are unchanged. Expected_state remains optional non-null at the generated type boundary; application gates continue to choose supported states and capture revisions. Preview4ed/API610 is unchanged and insufficient to certify guarded writes. Source942c is not live-deployment evidence. A040 inherited CVE cursor completeness remains outside this repair.

A software revert restores the accidental-clear risk and cannot reconstruct notes already lost. Recover content only from known prior data through an explicit guarded correction or existing recovery source, never an automatic replay. No additional coordinated backend upgrade is introduced for already compatible guarded backends.

Verification and disposition

Read retained quick receipts/log bindings: combined native batch exit0/78.326s and focused3files31tests exit0/10.39s. They ran against working snapshot373f01af before the final ordinary commits. All final bindings match; these are valid exact-input records, not literal-ebfd execution claims. No reviewer tests, builds, evaluation, installs, browser/API/CI controls, network, Git/index/source mutation, claims or lifecycle actions occurred.

Still pending after finding disposition: affected native cases through later assertions, implemented EN/CS desktop/mobile captures, full configured broad BOTH projects, required final CI and exact-final Nix5. Historical670 core/Nix success and unchanged preview are not substitutes. Configurationb466 remains a retained earlier artifact; any later update must select the corrected verified integrated WebUI. No configuration/master or deployment authority follows.

All four lanes and complete seven-stage history assessed. One Important finding requires disposition; no other finding supported. Keep source/report provenance and the session open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-typescript-client-migration/
