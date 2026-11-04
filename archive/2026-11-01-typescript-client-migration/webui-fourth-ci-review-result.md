No Blocking, Important or Advisory findings in the completed fourth-CI affected review.

Please persist this full report as webui-fourth-ci-review-result.md.

Scope and reviewer
- Final affected range: 20aa0e9ea7568747f048242077f0cf15a325d990..b1b37ccf5dc5d000baed3d77d49fab6f5b84b663.
- Final tree: 29c88df362cb1d8e773ff6b141f39dbaa71d49cf.
- Complete branch: 63d484fc070dbee633d32624de545e834d483701..b1b37ccf5dc5d000baed3d77d49fab6f5b84b663, 34 commits; full diff 512 paths, +15268/-10136.
- Affected diff independently confirmed as exactly six leaf specs and two strict-membership JSON files, eight paths, +41/-59. Candidate HEAD/tree, clean worktree/index, all eight Git blobs, SHA256s and worktree bytes match the final inventory.
- reviewer0, retained gpt-6-astra/xhigh/read_only; live same-session roster revision61, ready review-purpose thread01a19801-c630-7971-b7b9-cc178b6ced88. dev-session current confirms the bound session; both environment identity variables are absent. No overrides, fallback or nested reviewer.
- Overall risk HIGH; all four affected lanes completed directly: general/history, architecture/repetition, scope/proportionality, risk/compatibility. Read current mandatory-change-review and all four references in full, current repository AGENTS and applicable workspace guidance; reused unchanged guidance and prior unaffected foundation/source/history/packaging/readiness conclusions.

General and correctness
The actual changes correct the fixtures at the boundary where the selected generated client and existing WebUI guards reject them. They do not relax those guards or change production behavior.

I inspected the selected99ee archive's emitted descriptors/declarations rather than substituting merged HaveAPI f29c. Its VPS Show declares dns_resolver as a nullable partial relation; the edited VPS actions require outputNamespace vps; Dataset Update requires dataset; Dataset/VPS Update output types are Record<string, never>. Existing src/lib/api/vps.ts:94 rejects a primitive resolver, the runtime requires the response namespace, and requireActionStateResult retains the separate receipt check.

- 1c9204df9049d9199b0717106829ad8d56ce040a: lifecycle, maintenance and power fixtures now use dns_resolver:null. Added vps:{} response frames preserve the same action-state IDs and mutation semantics. The single charAt(0) change gives the same label for the declared nonempty start/stop/restart union while satisfying strict indexed access. No timing or locking workaround was introduced.
- List feedback at e2e/specs/app/vps_list_action_failure_feedback.spec.ts:52 and :87 still returns the original409 first, then a canonical success frame with901/902. Confirmation/error/target assertions, explicit second submission and exact two-call assertions remain.
- 067b3bd93dac1cb0f8ea07c627aaa4e332a34699: private-IP rows81/82 explicitly declare network_interface:null at e2e/specs/app/vps_private_ip_availability.spec.ts:9 and :13. This matches the existing ipRouteAssignIntent requirement for a known-unassigned baseline; omission remains unknown. Both admin/member cases, location11/private_access/usable_for=vps query, exact network_interface:8 POST payload and availability-error/disabled-submit negative remain.
- b00877a6452bae53ff3fdadbfb2a3d2cbf146292: resource workspace replies use the declared empty dataset/VPS outputs at e2e/specs/app/vps_resource_workspace.spec.ts:29–37. Fixture state still changes in the same places and remains available through the separate GET handlers. This preserves independent disk/VPS drafts, actual payload/count assertions and subsequent readback. The new import is type-only.

Negative and role preservation
The important distinction between malformed framing and missing operation proof is preserved:
- Lifecycle migration missing-receipt now returns {vps:{}} without a receipt; the rejection branch is unchanged. Draft retention, no accepted toast and disabled retry remain.
- Lifecycle delete still lacks an action-state ID in its canonical vps frame. Its assertions require the explicit missing-task message, no accepted receipt, no progress modal and unchanged route.
- Resource workspace missing-task returns {dataset:{}} without metadata and without updating fixture state. The existing requireActionStateResult path therefore throws MissingActionStateError; the test still checks retained durable lock after reload and exactly one write.
- Allocation-error/explicit admin override, member/admin visibility, force/confirmation choices, task-context binding, delayed state reads, locale/geometry checks, fresh-read failures and busy/used-space protection remain.
I compared assertion and test-declaration lines across all six leaves and found them unchanged, then inspected the relevant surrounding negative/readback flows; this conclusion is not based on assertion counts alone.

Original-cause evidence
Read the16 selected retry0 trace/error-context members in memory from the retained local archives, verifying their mapped member hashes. Inspected their API network events and relevant original error contexts:
- Eleven lifecycle/maintenance/power originals returned namespaced VPS data with resolver 'inherit' and reached no mutation.
- Both list originals show409 followed by200 carrying only _meta action901/902.
- The disk-first original reached PUT datasets/10 and received only _meta action901.
- Both private-IP originals returned rows81/82 without network_interface and sent no assignment POST.
These support the corrections. Later same-leaf action-frame fixes are source-backed follow-on repairs, not evidence that those later actions executed in the original runs. No product or browser-engine fault is established.

Architecture/repetition
Ownership remains correct: generated descriptors and HaveAPI runtime own wire framing; the application owns relation validation, action receipts and uncertain-write locks; leaf fixtures now conform to those existing contracts. No provider behavior is copied downstream, no new shared helper/framework is introduced, and no production or harness normalization hides invalid input. Small explicit response frames in these scenario-specific handlers do not warrant another abstraction. The resource fixture's generated-derived satisfies annotations improve local contract alignment without changing execution.

Scope/proportionality
The eight-path repair is proportionate to the observed six-file failure boundary and the directly implicated later steps. The large complete branch diff is the retained migration, not new handwritten scope in this batch. There is no new runner, retry policy, CI cap, role coercion, timing accommodation, feature, visible copy or KB change. Commit rationale and the fourth-CI design record explain the fixture corrections. A later work-log append should report actual execution; no product-documentation rewrite is needed for these test-only changes.

Strict coverage
b1b37ccf5dc5d000baed3d77d49fab6f5b84b663 adds only list_action_failure_feedback, maintenance_mobile, power_stop_confirm and resource_workspace as complete files. Independently parsed old/new metadata: adopted136->140, deferred146->142; no adopted removals, no new deferrals, and all142 surviving records are identical. Only tsconfig.files changes; compiler options, support/ambient inputs and checker are unchanged. Baseline file SHA256 remains7bdc6a363a2706be14533e05712bda641aa709ce2413a4bd68ebe427ecec3317 and sourceRevision remainsabab859d94a3f364d2bb719fa09f00749fd69ef9. There is no hash-only refresh or compiler allowance.

Whole-history conclusion
Independently compared the actual complete ordered34-commit series against the inventory and its prior30-commit prefix. All30 through published20aa are literal unchanged objects. The four new ordinary commits have coherent purposes: known-unassigned IP fixtures; common VPS relation/action framing across four leaves; resource update framing; whole-file strict adoption. They repair newly observed inherited cases, not a superseded implementation introduced earlier in this batch. No new obsolete alternatives, fixup/replacement chain or published-history rewrite remains to reconcile. Retained original mapping/fold/direct-remedy conclusions continue to apply; no whole-source reaudit was necessary.

Repeated-input-stream conclusion
Actual package/lock/flake/vendor history still has only the established generated-client input change in167f8531; the other package.json-touching8b648c84 changes the test command, not a second dependency stream. The current four commits touch no input selection. Strict membership adoption is monotonic coverage expansion, not a repeated generated dependency artifact. No redundant pin stream or further consolidation is required.

Selected archive and provenance remain unchanged: client99ee/generator eea3/runtime0.32.0. I compared package.json, package-lock.json, flake.lock and vendor bytes with20aa; all match. Archive SHA256 remainsf3bb42d0392fb738f5c70fe1415cc8742ab943a31c2ed2a85af5ccbd385d831f. The separate HaveAPI/master integration does not adopt f29c into this WebUI or relabel existing archive evidence.

Migration conclusion
No DB, schema or persisted-format migrations occur in this affected range or the retained complete migration inventory. src/lib/api/migrations.ts and the MigrationPlan pages are existing VPS migration-plan consumers, not database migration lineage. No transitional schema versions or new merged/released/deployed/externally consumed state boundary is introduced. Existing API migration provenance remains unchanged historical input.

Verification evidence and residual limits
- Owner quick strict/lint/diff and metadata protection results are retained. Final combined strict receipt binds exactb1b and reports npm run typecheck:e2e:core exit0 in11.934742s,140 checked/142 deferred and zero diagnostics. I independently matched receipt SHA2568a2cf05822de50d7315e230125e9faea4a34984442c1e1cd0abad9305144362f and log SHA25630b792441aaef92e6046c245f7ad7a23ad03e67af90bc33a859b8595743b7670; I did not rerun checks.
- Inspected retained native list JSON:136 unique test IDs,68 Chromium+68 mobileChrome, exactly six affected paths, no errors. All20 mapped original observations resolve to listed current IDs with unchanged titles. Negative and later-step cases remain included. This is enumeration, not browser execution.
- No browser pass onb1b is established. The planned ordinary touched-case gate is still required, and can expose later inherited fixture defects after these earlier blockers.
- Original20aa core CI and WebKit274 passed/2 skipped retain their actual heads/scopes. Cancelled Chrome jobs provide no terminal complete-case totals; no new-head or cross-engine pass is inferred. Native full-matrix CI and exact-final-head packaging/readiness remain separate.
- Synthetic fixtures do not certify a real API, worker completion, deployment, OAuth or absence of historical API2 cleanup effects. Prior evidence and that cleanup uncertainty remain unchanged.
- Compatible released-client adoption remains pending under the user's separate release decision. This report supplies no WebUI/client default-merge, registry, deployment or lifecycle permission.

No finding blocks the parent's bounded native browser gate for this exact candidate. Parent owns acceptance, any direct remediation and launch. The review itself performed no source/file/index/Git mutation, checks/tests/builds/install, downloads, CI/browser/API/DB/server execution, release, merge, deployment or lifecycle action. Session remains open.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-typescript-client-migration/
